"""Validate every content entry against the schema, check cross-links, and
check that the body contains the sections the page type requires.

Usage:  python tools/validate.py            (exit 1 on any error)
"""
from __future__ import annotations

import re
import sys

from jsonschema import Draft202012Validator

from common import TYPES, load_all, load_schema

REQUIRED_SECTIONS = {
    "application": ["## Who needs it", "## Bottleneck", "## Computational problems", "## Verdict"],
    "problem": ["## Best classical", "## Best quantum", "## Verdict"],
    "method": ["## Preconditions", "## Known limits", "## Verdict"],
    "claim": ["## Claim", "## Refutation"],
    "question": ["## Why it matters", "## What would settle it"],
}


def main() -> int:
    entries = load_all()
    validator = Draft202012Validator(load_schema())
    ids = {t: set() for t in TYPES}
    for e in entries:
        for err in validator.iter_errors(e.meta):
            loc = "/".join(str(x) for x in err.path) or "<root>"
            e.errors.append(f"schema: {loc}: {err.message}")
        if e.type in ids:
            ids[e.type].add(e.id)
        for sec in REQUIRED_SECTIONS.get(e.type, []):
            if not re.search(r"^" + re.escape(sec) + r"\s*$", e.body, re.M):
                e.errors.append(f"missing section '{sec}'")
        if not e.meta.get("references") and e.type != "question":
            e.errors.append("no references")
    # cross-links
    for e in entries:
        rel = e.meta.get("related") or {}
        for kind, targets in rel.items():
            t = kind[:-1]
            for target in targets or []:
                if target not in ids.get(t, set()):
                    e.errors.append(f"related.{kind}: '{target}' does not exist")
    bad = [e for e in entries if e.errors]
    for e in bad:
        print(f"{e.path.relative_to(e.path.parents[2])}:")
        for err in e.errors:
            print(f"  - {err}")
    print(f"{len(entries)} entries, {len(bad)} with errors")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

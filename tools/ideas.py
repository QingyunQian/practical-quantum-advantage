"""Load and check lightweight candidate ideas, which carry no evidence verdict."""
from __future__ import annotations

import json
import re

from common import ROOT

IDEAS_PATH = ROOT / "data" / "ideas.json"


def load_ideas(entries):
    ideas = json.loads(IDEAS_PATH.read_text(encoding="utf-8"))
    errors = []
    if not isinstance(ideas, list):
        return [], ["data/ideas.json must be a list"]
    seen = set()
    existing = {(e.type, e.id) for e in entries}
    proposed_problems = {i.get("id") for i in ideas if isinstance(i, dict) and i.get("type") == "problem"}
    existing_problems = {e.id for e in entries if e.type == "problem"}
    linked_problems = set()
    for i in ideas:
        if not isinstance(i, dict):
            errors.append("idea must be an object")
            continue
        ident, kind = i.get("id"), i.get("type")
        if kind not in ("application", "problem") or not isinstance(ident, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", ident):
            errors.append(f"invalid idea type or id: {kind}/{ident}")
            continue
        if (kind, ident) in seen or (kind, ident) in existing:
            errors.append(f"duplicate idea or already catalogued: {kind}/{ident}")
        seen.add((kind, ident))
        for field in ("domain", "title", "title_zh", "question"):
            if not isinstance(i.get(field), str) or not i[field].strip():
                errors.append(f"{ident}: missing {field}")
        if any(k in i for k in ("verdict", "status", "resources", "dimensions")):
            errors.append(f"{ident}: idea must not carry an evidence verdict or resource claim")
        if kind == "application":
            pids = i.get("problem_ids")
            if not isinstance(pids, list) or not pids:
                errors.append(f"{ident}: application needs problem_ids")
                continue
            for pid in pids:
                linked_problems.add(pid)
                if pid not in proposed_problems and pid not in existing_problems:
                    errors.append(f"{ident}: unknown problem {pid}")
        elif "problem_ids" in i:
            errors.append(f"{ident}: only applications have problem_ids")
    for pid in proposed_problems - linked_problems:
        errors.append(f"unlinked proposed problem: {pid}")
    return ideas, errors

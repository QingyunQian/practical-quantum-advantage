"""Create a draft catalogue page for a human or agent to research.

Usage: python tools/new_entry.py application example-id --title "Example title"
"""
from __future__ import annotations

import argparse
import re
from datetime import date

import yaml

from common import DIRS, TYPES

SECTIONS = {
    "application": ["Who needs it", "Bottleneck", "Computational problems", "Verdict"],
    "problem": ["Best classical", "Best quantum", "Verdict"],
    "method": ["Preconditions", "Known limits", "Verdict"],
    "claim": ["Claim", "Refutation"],
    "question": ["Why it matters", "What would settle it"],
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("type", choices=TYPES)
    parser.add_argument("id", help="Permanent lowercase slug, such as battery-electrolytes")
    parser.add_argument("--title", required=True, help="Human-readable English title")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.id):
        parser.error("id must contain only lowercase letters, digits and hyphens")

    path = DIRS[args.type] / f"{args.id}.md"
    if path.exists():
        parser.error(f"page already exists: {path}")

    meta = {
        "type": args.type,
        "id": args.id,
        "title": args.title,
        "summary": "Replace with a concise, sourced description of this candidate.",
        "status": "seed",
    }
    if args.type in ("application", "problem", "method"):
        meta["verdict"] = "unassessed"
        meta["dimensions"] = {
            key: {"level": "unknown", "note": "Research needed"}
            for key in ("classical_hardness", "quantum_easiness", "willingness_to_pay")
        }
    elif args.type == "claim":
        meta["claim"] = {
            "claimant": "Identify the claimant",
            "date": date.today().strftime("%Y-%m"),
            "statement": "Replace with the precise published claim",
            "refuted": False,
        }
    else:
        meta["question"] = {
            "what_would_settle_it": "State a concrete result that would settle this question.",
            "difficulty": "month",
            "resolved": False,
        }
    meta["related"] = {}
    meta["references"] = []

    body = "\n\n".join(
        f"## {section}\n\nDescribe the evidence and cite primary sources."
        for section in SECTIONS[args.type]
    )
    path.write_text(
        "---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False)
        + "---\n\n" + body + "\n", encoding="utf-8",
    )
    print(f"Created {path}")
    print("Replace placeholders, add public references, then run validate.py and verify_refs.py.")


if __name__ == "__main__":
    main()

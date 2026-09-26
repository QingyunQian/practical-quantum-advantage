"""List pages that need source review or a fresh literature check.

Usage: python tools/review_queue.py [--markdown]
"""
from __future__ import annotations

import argparse
from datetime import date, timedelta

from common import load_all

MAX_AGE_DAYS = 180
SITE_URL = "https://yuchenguommm.github.io/practical-quantum-advantage/"


def classify(entries, today: date | None = None):
    today = today or date.today()
    cutoff = today - timedelta(days=MAX_AGE_DAYS)
    queue = {"disputed": [], "stale": [], "seed": []}
    for entry in entries:
        status = entry.meta.get("status", "seed")
        try:
            verified = date.fromisoformat(entry.meta["last_verified"])
        except (KeyError, ValueError):
            verified = None
        if status == "disputed":
            queue["disputed"].append(entry)
        elif verified is None or verified < cutoff:
            queue["stale"].append(entry)
        elif status == "seed":
            queue["seed"].append(entry)
    for group in queue.values():
        group.sort(key=lambda e: (e.meta.get("last_verified", ""), e.type, e.id))
    return queue


def markdown(queue, today: date) -> str:
    lines = [
        "# Catalogue review queue", "",
        f"Generated {today.isoformat()}. A page is stale when its `last_verified` date is more than {MAX_AGE_DAYS} days old.",
        "This is a reminder to check sources and claims; an old date does not make a conclusion false.", "",
    ]
    for key, title in (("disputed", "Disputed"), ("stale", "Stale"), ("seed", "Awaiting first review")):
        group = queue[key]
        lines.extend([f"## {title} ({len(group)})", ""])
        for entry in group:
            lines.append(f"- [{entry.meta['title']}]({SITE_URL}{entry.href}) (`{entry.type}/{entry.id}`, last checked {entry.meta.get('last_verified', 'unknown')})")
        if not group:
            lines.append("None.")
        lines.append("")
    lines.extend([
        "To review a page, check its primary sources, numerical claims, strongest classical comparison and quantum preconditions. Add or correct sources in a pull request, record what you checked in the PR, and update `last_verified` only after that check. A new paper alone does not justify marking a page `reviewed`.",
        "", f"[How to contribute]({SITE_URL}contribute.html)", "",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown", action="store_true", help="write a GitHub issue body")
    args = parser.parse_args()
    today = date.today()
    queue = classify(load_all(), today)
    if args.markdown:
        print(markdown(queue, today))
    else:
        for key, group in queue.items():
            print(f"{key}: {len(group)}")
            for entry in group:
                print(f"  {entry.type}/{entry.id}")


if __name__ == "__main__":
    main()

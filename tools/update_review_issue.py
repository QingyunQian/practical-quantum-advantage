"""Create or update one public GitHub issue for the monthly catalogue review.

Run with --dry-run locally. GitHub Actions supplies GITHUB_TOKEN and
GITHUB_REPOSITORY for the write operation.
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import date
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from common import load_all
from review_queue import classify, markdown

TITLE = "Catalogue review queue"


def request(method: str, path: str, data=None):
    repo = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GITHUB_TOKEN"]
    body = None if data is None else json.dumps(data).encode("utf-8")
    req = Request(
        f"https://api.github.com/repos/{repo}{path}", data=body, method=method,
        headers={"Accept": "application/vnd.github+json",
                 "Authorization": f"Bearer {token}",
                 "X-GitHub-Api-Version": "2022-11-28",
                 "Content-Type": "application/json"},
    )
    try:
        with urlopen(req, timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"GitHub API {method} {path}: HTTP {exc.code}") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    queue = classify(load_all())
    body = markdown(queue, date.today())
    if args.dry_run:
        print(body)
        return

    issue = None
    page = 1
    while True:
        batch = request("GET", f"/issues?state=open&per_page=100&page={page}")
        issue = next((item for item in batch if "pull_request" not in item and item["title"] == TITLE), None)
        if issue or len(batch) < 100:
            break
        page += 1

    if issue:
        request("PATCH", f"/issues/{issue['number']}", {"body": body})
        print(f"Updated issue #{issue['number']}")
    else:
        issue = request("POST", "/issues", {
            "title": TITLE, "body": body, "labels": ["evidence", "help wanted"],
        })
        print(f"Created issue #{issue['number']}")


if __name__ == "__main__":
    main()

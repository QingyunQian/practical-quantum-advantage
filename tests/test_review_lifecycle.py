"""Regression checks for new-page provenance and review queue routing."""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import new_entry  # noqa: E402
from common import Entry, load_schema, parse  # noqa: E402
from review_queue import classify  # noqa: E402


class ReviewLifecycleTest(unittest.TestCase):
    def test_generated_seed_has_no_unearned_verification_date(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "example.md"
            with patch.dict(new_entry.DIRS, {"application": target.parent}):
                with patch.object(sys, "argv", ["new_entry.py", "application", "example", "--title", "Example application"]):
                    new_entry.main()
            entry = parse(target)
            self.assertEqual(entry.meta["status"], "seed")
            self.assertNotIn("last_verified", entry.meta)
            self.assertFalse(list(Draft202012Validator(load_schema()).iter_errors(entry.meta)))
            queue = classify([entry])
            self.assertEqual(queue["seed"], [entry])
            self.assertFalse(queue["stale"])

    def test_reviewed_page_requires_verification_date(self):
        meta = {
            "type": "question", "id": "example", "title": "Example question",
            "summary": "A concrete and sufficiently long research question.",
            "status": "reviewed",
            "question": {"what_would_settle_it": "A matched comparison", "difficulty": "month"},
        }
        errors = list(Draft202012Validator(load_schema()).iter_errors(meta))
        self.assertTrue(any("last_verified" in error.message for error in errors))

    def test_unreviewed_page_remains_in_first_review_queue_even_when_old(self):
        entry = Entry(Path("example.md"), {"type": "question", "id": "example", "status": "seed", "last_verified": "2020-01-01"}, "")
        queue = classify([entry])
        self.assertEqual(queue["seed"], [entry])
        self.assertFalse(queue["stale"])


if __name__ == "__main__":
    unittest.main()

"""Protect the boundary between unassessed leads and evidence-graded pages."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from common import load_all  # noqa: E402
import ideas  # noqa: E402


class IdeaPoolTest(unittest.TestCase):
    def test_public_pool_has_valid_links_and_no_verdicts(self):
        pool, errors = ideas.load_ideas(load_all())
        self.assertEqual(errors, [])
        self.assertGreaterEqual(len(pool), 20)
        self.assertTrue(any(i["type"] == "application" for i in pool))
        self.assertTrue(any(i["type"] == "problem" for i in pool))

    def test_unknown_problem_and_prejudged_idea_are_rejected(self):
        item = {"id": "example-unassessed", "type": "application", "domain": "Test",
                "title": "Example", "title_zh": "示例", "question": "What is the task?",
                "problem_ids": ["nonexistent-problem"], "verdict": "promising"}
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "ideas.json"
            path.write_text(json.dumps([item]), encoding="utf-8")
            with patch.object(ideas, "IDEAS_PATH", path):
                _, errors = ideas.load_ideas(load_all())
        self.assertTrue(any("unknown problem" in e for e in errors))
        self.assertTrue(any("must not carry" in e for e in errors))


if __name__ == "__main__":
    unittest.main()

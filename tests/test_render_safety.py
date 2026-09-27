"""Published contributor Markdown must not become active script or unsafe links."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from build import render_md  # noqa: E402


class RenderSafetyTest(unittest.TestCase):
    def test_raw_html_and_unsafe_link_are_inert(self):
        html = render_md('<script>alert(1)</script> <img src=x onerror="alert(1)"> [open](javascript:alert(1))')
        self.assertNotIn("<script", html)
        self.assertNotIn("onerror", html)
        self.assertNotIn("javascript:", html)

    def test_tables_and_safe_links_survive(self):
        html = render_md("| A | B |\n|---|---|\n| 1 | [paper](https://arxiv.org/) |")
        self.assertIn("<table>", html)
        self.assertIn('href="https://arxiv.org/"', html)


if __name__ == "__main__":
    unittest.main()

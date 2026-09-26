"""Check generated HTML for missing local links and image assets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from common import ROOT


def main() -> int:
    site = (ROOT / "site").resolve()
    errors = []
    checked = 0

    class Links(HTMLParser):
        def __init__(self, page):
            super().__init__()
            self.page = page

        def handle_starttag(self, tag, attrs):
            nonlocal checked
            for key, value in attrs:
                if key not in ("href", "src") or not value:
                    continue
                url = urlsplit(value)
                if url.scheme or url.netloc or not url.path:
                    continue
                checked += 1
                target = (self.page.parent / unquote(url.path)).resolve()
                if not target.is_relative_to(site) or not target.exists():
                    errors.append(f"{self.page.relative_to(site)}: {value}")

    pages = list(site.rglob("*.html"))
    if not pages:
        errors.append("No built pages found; run tools/build.py first")
    for page in pages:
        Links(page).feed(page.read_text(encoding="utf-8"))
    for error in errors:
        print(error)
    print(f"{len(pages)} HTML pages, {checked} local links, {len(errors)} errors")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())

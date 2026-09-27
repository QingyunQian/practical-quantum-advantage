"""Check generated HTML for local targets, fragments, duplicate IDs and image alt text."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from common import ROOT


def main() -> int:
    site = (ROOT / "site").resolve()
    errors = []
    checked = 0

    class Page(HTMLParser):
        def __init__(self, page):
            super().__init__()
            self.page = page
            self.ids = set()
            self.links = []

        def handle_starttag(self, tag, attrs):
            attr = dict(attrs)
            if attr.get("id"):
                if attr["id"] in self.ids:
                    errors.append(f"{self.page.relative_to(site)}: duplicate id #{attr['id']}")
                self.ids.add(attr["id"])
            if tag == "img" and not attr.get("alt"):
                errors.append(f"{self.page.relative_to(site)}: image missing alt text: {attr.get('src')}")
            for key, value in attrs:
                if key not in ("href", "src") or not value:
                    continue
                self.links.append(value)

    pages = list(site.rglob("*.html"))
    if not pages:
        errors.append("No built pages found; run tools/build.py first")
    parsed = {}
    for page in pages:
        parser = Page(page)
        parser.feed(page.read_text(encoding="utf-8"))
        parsed[page.resolve()] = parser
    for page, parser in parsed.items():
        for value in parser.links:
            url = urlsplit(value)
            if url.scheme or url.netloc:
                continue
            checked += 1
            target = (page.parent / unquote(url.path)).resolve() if url.path else page
            if not target.is_relative_to(site) or not target.exists():
                errors.append(f"{page.relative_to(site)}: {value}")
            elif url.fragment and target.suffix == ".html" and target in parsed:
                anchor = unquote(url.fragment)
                if anchor not in parsed[target].ids:
                    errors.append(f"{page.relative_to(site)}: missing fragment {value}")
    for error in errors:
        print(error)
    print(f"{len(pages)} HTML pages, {checked} local links, {len(errors)} errors")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())

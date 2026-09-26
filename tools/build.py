"""Build the static site into ./site.

Usage:  python tools/build.py
"""
from __future__ import annotations

import json
import shutil
from collections import defaultdict
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

from common import ROOT, TYPES, VERDICT_LABEL, load_all

SITE = ROOT / "site"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
BASE_URL = "https://github.com/yuchenguommm/practical-quantum-advantage"

SECTION_TITLE = {
    "application": ("Applications", "应用"),
    "problem": ("Computational problems", "计算问题"),
    "method": ("Methods", "方法"),
    "claim": ("Advantage claims and refutations", "优势声明与打破记录"),
    "question": ("Open questions", "待研究"),
}

md = markdown.Markdown(extensions=["tables", "footnotes", "toc", "sane_lists", "attr_list", "fenced_code"])


def render_md(text: str) -> str:
    md.reset()
    return md.convert(text)


def main() -> None:
    entries = [e for e in load_all() if e.meta and e.meta.get("type") in TYPES and e.meta.get("id")]
    by_type = defaultdict(list)
    by_id = {}
    for e in entries:
        by_type[e.type].append(e)
        by_id[(e.type, e.id)] = e
    for t in by_type:
        by_type[t].sort(key=lambda e: e.meta["title"].lower())

    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape(["html"]))
    env.globals.update(
        VERDICT_LABEL=VERDICT_LABEL,
        SECTION_TITLE=SECTION_TITLE,
        TYPES=TYPES,
        BASE_URL=BASE_URL,
        by_type=by_type,
    )

    def resolve(kind: str, ids):
        t = kind[:-1]
        out = []
        for i in ids or []:
            e = by_id.get((t, i))
            if e:
                out.append(e)
        return out

    env.globals["resolve"] = resolve

    # Never publish stale pages after an incomplete OneDrive/Windows cleanup.
    if SITE.resolve() != ROOT.resolve() / "site":
        raise RuntimeError("Build output must remain inside the repository")
    if SITE.exists():
        # OneDrive may lock directories. Retain empty directories, but remove
        # every old file and fail if a file cannot be removed.
        for path in SITE.rglob("*"):
            if path.is_symlink() or not path.resolve().is_relative_to(SITE.resolve()):
                raise RuntimeError(f"Unexpected output link: {path}")
            if path.is_file():
                path.unlink()
    SITE.mkdir(exist_ok=True)
    shutil.copytree(STATIC, SITE / "static", dirs_exist_ok=True)
    if (ROOT / "numerics" / "figs").exists():
        shutil.copytree(ROOT / "numerics" / "figs", SITE / "figs", dirs_exist_ok=True)
    for t in TYPES:
        (SITE / (t + "s")).mkdir(exist_ok=True)

    # entry pages
    page_t = env.get_template("entry.html")
    for e in entries:
        html = page_t.render(e=e, body=render_md(e.body), depth="../")
        (SITE / e.href).write_text(html, encoding="utf-8")

    # index pages per type
    list_t = env.get_template("list.html")
    for t in TYPES:
        html = list_t.render(t=t, items=by_type[t], depth="../")
        (SITE / (t + "s") / "index.html").write_text(html, encoding="utf-8")

    # matrix: applications x problems
    apps = by_type["application"]
    probs = by_type["problem"]
    cells = {}
    for a in apps:
        for pid in (a.meta.get("related") or {}).get("problems") or []:
            p = by_id.get(("problem", pid))
            if p:
                cells[(a.id, pid)] = p.meta.get("verdict", "unassessed")
    used_probs = [p for p in probs if any((a.id, p.id) in cells for a in apps)]
    html = env.get_template("matrix.html").render(apps=apps, probs=used_probs, cells=cells, depth="")
    (SITE / "matrix.html").write_text(html, encoding="utf-8")

    # home
    claims = sorted(by_type["claim"], key=lambda e: e.meta["claim"]["date"], reverse=True)
    counts = {t: len(by_type[t]) for t in TYPES}
    verdict_counts = defaultdict(int)
    for t in ("application", "problem", "method"):
        for e in by_type[t]:
            verdict_counts[e.meta.get("verdict", "unassessed")] += 1
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = readme.replace("](AGENTS.md)", f"]({BASE_URL}/blob/main/AGENTS.md)")
    html = env.get_template("index.html").render(
        counts=counts, verdict_counts=verdict_counts, claims=claims[:8], depth="", readme=render_md(readme)
    )
    (SITE / "index.html").write_text(html, encoding="utf-8")

    # machine-readable exports
    export = []
    for e in entries:
        d = dict(e.meta)
        d["url"] = e.href
        d["body_markdown"] = e.body
        export.append(d)
    (SITE / "index.json").write_text(json.dumps(export, ensure_ascii=False, indent=1), encoding="utf-8")
    llms = ["# Practical Quantum Advantage", "", "A living catalogue of quantum-computing application candidates, each judged on three dimensions: classically hard, quantumly easy, someone pays.", "", "Full data: index.json (one object per entry, includes body_markdown).", ""]
    for t in TYPES:
        llms.append(f"## {SECTION_TITLE[t][0]}")
        for e in by_type[t]:
            v = e.meta.get("verdict")
            llms.append(f"- [{e.meta['title']}]({e.href})" + (f" — {v}" if v else "") + f": {e.meta['summary']}")
        llms.append("")
    (SITE / "llms.txt").write_text("\n".join(llms), encoding="utf-8")
    (SITE / ".nojekyll").write_text("")
    print(f"built {len(entries)} pages -> {SITE}")


if __name__ == "__main__":
    main()

"""Build the static site into ./site.

Usage:  python tools/build.py
"""
from __future__ import annotations

import json
import shutil
from collections import defaultdict
from datetime import date
from pathlib import Path

import markdown
import bleach
from jinja2 import Environment, FileSystemLoader, select_autoescape

from common import ROOT, TYPES, VERDICT_LABEL, load_all
from cases import load_cases
from ideas import load_ideas
from review_queue import MAX_AGE_DAYS, classify

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
SAFE_TAGS = {"a", "blockquote", "br", "code", "div", "em", "h1", "h2", "h3", "h4", "h5", "h6", "hr", "img", "li", "ol", "p", "pre", "span", "strong", "sup", "table", "tbody", "td", "th", "thead", "tr", "ul"}
SAFE_ATTRIBUTES = {"*": ["id", "class"], "a": ["href", "title"], "img": ["src", "alt", "title"]}


def sanitize_html(html: str) -> str:
    return bleach.clean(html, tags=SAFE_TAGS, attributes=SAFE_ATTRIBUTES,
                        protocols=["http", "https", "mailto"], strip=True)


def render_md(text: str) -> str:
    md.reset()
    return sanitize_html(md.convert(text))


def main() -> None:
    entries = [e for e in load_all() if e.meta and e.meta.get("type") in TYPES
               and e.meta.get("id") and e.meta.get("published", True)]
    ideas, idea_errors = load_ideas(entries)
    if idea_errors:
        raise ValueError("Invalid idea catalogue: " + "; ".join(idea_errors))
    cases, case_errors = load_cases(entries)
    if case_errors:
        raise ValueError("Invalid cases: " + "; ".join(case_errors))
    by_type = defaultdict(list)
    by_id = {}
    for e in entries:
        by_type[e.type].append(e)
        by_id[(e.type, e.id)] = e
    for t in by_type:
        by_type[t].sort(key=lambda e: e.meta["title"].lower())
    idea_apps = sorted((i for i in ideas if i["type"] == "application"), key=lambda i: (i["domain"], i["title"]))
    idea_problems = sorted((i for i in ideas if i["type"] == "problem"), key=lambda i: i["title"])
    problem_links = {p.id: {"title": p.meta["title"], "url": p.href} for p in by_type["problem"]}
    problem_links.update({p["id"]: {"title": p["title"], "url": "ideas.html#" + p["id"]} for p in idea_problems})
    idea_app_for_problem = {p["id"]: [a for a in idea_apps if p["id"] in a["problem_ids"]] for p in idea_problems}

    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape(["html"]))
    env.globals.update(
        VERDICT_LABEL=VERDICT_LABEL,
        SECTION_TITLE=SECTION_TITLE,
        TYPES=TYPES,
        BASE_URL=BASE_URL,
        by_type=by_type,
        STATUS_LABEL={"seed": "Awaiting review", "reviewed": "Reviewed", "disputed": "Disputed"},
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
        body = render_md(e.body)
        toc = sanitize_html(md.toc) if e.body.count("\n## ") >= 4 else ""
        html = page_t.render(e=e, body=body, toc=toc, depth="../")
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

    # Unassessed breadth pool, separate from evidence-graded entries.
    html = env.get_template("ideas.html").render(
        depth="", idea_apps=idea_apps, idea_problems=idea_problems,
        problem_links=problem_links, idea_app_for_problem=idea_app_for_problem,
    )
    (SITE / "ideas.html").write_text(html, encoding="utf-8")
    (SITE / "ideas.json").write_text(json.dumps(ideas, ensure_ascii=False, indent=1), encoding="utf-8")

    html = env.get_template("cases.html").render(cases=cases, depth="")
    (SITE / "cases.html").write_text(html, encoding="utf-8")
    (SITE / "cases.json").write_text(json.dumps(cases, ensure_ascii=False, indent=1), encoding="utf-8")

    # home
    claims = sorted(by_type["claim"], key=lambda e: e.meta["claim"]["date"], reverse=True)
    counts = {t: len(by_type[t]) for t in TYPES}
    verdict_counts = defaultdict(int)
    status_counts = defaultdict(int)
    for e in entries:
        status_counts[e.meta.get("status", "seed")] += 1
    for t in ("application", "problem", "method"):
        for e in by_type[t]:
            verdict_counts[e.meta.get("verdict", "unassessed")] += 1
    html = env.get_template("index.html").render(
        counts=counts, verdict_counts=verdict_counts, claims=claims[:8], depth="",
        idea_count=len(ideas), cases=cases, status_counts=status_counts,
        examples=[
            (by_id[("application", "battery-electrolyte-design")], "Reviewed application: a named benchmark and missing buyer target"),
            (by_id[("problem", "integer-factoring-hidden-subgroup")], "Foundational problem: proved quantum algorithm and explicit classical assumption"),
            (by_id[("claim", "ibm-sqd-2024")], "Reviewed claim: published result and later classical challenge"),
            (by_id[("question", "classical-output-fourier-crossover")], "Open question: a matched task and result that would settle it"),
        ],
    )
    (SITE / "index.html").write_text(html, encoding="utf-8")

    html = env.get_template("contribute.html").render(depth="", counts=counts)
    (SITE / "contribute.html").write_text(html, encoding="utf-8")

    review_queue = classify(entries)
    html = env.get_template("review_queue.html").render(
        depth="", queue=review_queue, max_age_days=MAX_AGE_DAYS,
    )
    (SITE / "review-queue.html").write_text(html, encoding="utf-8")
    (SITE / "review-queue.json").write_text(json.dumps({
        "generated": date.today().isoformat(), "max_age_days": MAX_AGE_DAYS,
        "groups": {key: [
            {"type": e.type, "id": e.id, "title": e.meta["title"],
             "url": e.href, "last_verified": e.meta.get("last_verified")}
            for e in group
        ] for key, group in review_queue.items()},
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    # machine-readable exports
    export = []
    for e in entries:
        d = dict(e.meta)
        if d.get("related"):
            d["related"] = {
                kind: [i for i in ids if (kind[:-1], i) in by_id]
                for kind, ids in d["related"].items()
            }
        d["url"] = e.href
        d["body_markdown"] = e.body
        export.append(d)
    (SITE / "index.json").write_text(json.dumps(export, ensure_ascii=False, indent=1), encoding="utf-8")
    llms = ["# Practical Quantum Advantage", "", "Evidence-graded catalogue: index.json. Unassessed idea pool: ideas.json. Fixed-input reproducible cases: cases.json. Ideas have no verdict and must not be cited as advantage evidence.", ""]
    for t in TYPES:
        llms.append(f"## {SECTION_TITLE[t][0]}")
        for e in by_type[t]:
            v = e.meta.get("verdict")
            llms.append(f"- [{e.meta['title']}]({e.href})" + (f" — {v}" if v else "") + f": {e.meta['summary']}")
        llms.append("")
    llms.extend(["## Unassessed ideas", "See ideas.json or ideas.html. Propose evidence through GitHub issues; ideas are not catalogue entries.", ""])
    llms.extend(["## Reproducible cases", "See cases.json or cases.html. A case is an evidence artifact, not an extra review tier.", ""])
    (SITE / "llms.txt").write_text("\n".join(llms), encoding="utf-8")
    (SITE / ".nojekyll").write_text("")
    print(f"built {len(entries)} pages -> {SITE}")


if __name__ == "__main__":
    main()

"""Shared helpers: load every content entry (YAML front matter + Markdown body)."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml


class Loader(yaml.SafeLoader):
    """SafeLoader that keeps dates as strings and only treats true/false as booleans
    (so a level of `no` stays the string "no")."""


Loader.yaml_implicit_resolvers = {
    k: [(tag, rx) for tag, rx in v if tag not in ("tag:yaml.org,2002:timestamp", "tag:yaml.org,2002:bool")]
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
Loader.add_implicit_resolver("tag:yaml.org,2002:bool", re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$"), list("tTfF"))

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SCHEMA = ROOT / "schema" / "entry.schema.json"
TYPES = ["application", "problem", "method", "claim", "question"]
DIRS = {t: CONTENT / (t + "s") for t in TYPES}

VERDICT_LABEL = {
    "no-go": ("No-go", "没戏"),
    "uneconomic": ("Uneconomic", "不划算"),
    "surviving": ("Surviving, unproven", "幸存待证"),
    "promising": ("Promising", "有戏"),
    "unassessed": ("Unassessed", "未评估"),
}

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.S)


@dataclass
class Entry:
    path: Path
    meta: dict
    body: str
    errors: list = field(default_factory=list)

    @property
    def type(self):
        return self.meta.get("type")

    @property
    def id(self):
        return self.meta.get("id")

    @property
    def href(self):
        return f"{self.type}s/{self.id}.html"


def parse(path: Path) -> Entry:
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        return Entry(path, {}, text, ["missing YAML front matter"])
    try:
        meta = yaml.load(m.group(1), Loader=Loader) or {}
    except yaml.YAMLError as e:  # pragma: no cover
        return Entry(path, {}, m.group(2), [f"YAML error: {e}"])
    return Entry(path, meta, m.group(2))


def load_all() -> list[Entry]:
    entries = []
    for t, d in DIRS.items():
        for p in sorted(d.glob("*.md")):
            e = parse(p)
            if e.meta and e.meta.get("type") != t:
                e.errors.append(f"type '{e.meta.get('type')}' does not match folder '{d.name}'")
            if e.meta and e.meta.get("id") != p.stem:
                e.errors.append(f"id '{e.meta.get('id')}' does not match filename '{p.stem}'")
            entries.append(e)
    return entries


def load_schema() -> dict:
    return json.loads(SCHEMA.read_text(encoding="utf-8"))

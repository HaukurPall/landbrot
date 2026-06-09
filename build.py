"""Static site generator for landbrot.is.

Renders every page in Icelandic (site root) and German (under ``de/``) from the shared
data in :mod:`data.horses` and :mod:`data.content`, then copies static assets into
``dist/``::

    uv run build.py
"""

from __future__ import annotations

import datetime
import hashlib
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from data import content, horses

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
BASE_URL = "https://landbrot.is"

TEMPLATE_BY_KEY = {
    "home": "index.html.j2",
    "about": "about.html.j2",
    "breeding": "breeding.html.j2",
    "young": "young.html.j2",
    "riding": "riding.html.j2",
    "contact": "contact.html.j2",
    "gallery": "gallery.html.j2",
}

# Old WordPress-era URLs -> new pages (meta-refresh stubs).
REDIRECTS = {
    "hestarnir.html": "reidhross.html",
    "myndband.html": "myndabanki.html",
}

REDIRECT_STUB = """<!DOCTYPE html>
<html lang="is">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="canonical" href="{base}/{target}">
  <title>Landbrot</title>
</head>
<body><a href="{target}">{target}</a></body>
</html>
"""


def score_filter(value: float) -> str:
    """Format a breeding score with a comma decimal separator: 8.0 -> '8,00'."""
    return f"{value:.2f}".replace(".", ",")


def build_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(("html", "html.j2")),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["score"] = score_filter
    return env


CSS_VERSION = hashlib.sha256((ROOT / "css" / "style.css").read_bytes()).hexdigest()[:10]


def page_context(page: dict, lang: str) -> dict:
    """Everything a template needs to render one page in one language."""
    asset = "" if lang == "is" else "../"
    other_prefix = "de/" if lang == "is" else "../"
    t = {key: value[lang] for key, value in content.LABELS.items()}
    sex_labels = {
        horses.Sex.MARE: t["sex_mare"],
        horses.Sex.STALLION: t["sex_stallion"],
        horses.Sex.GELDING: t["sex_gelding"],
    }
    return {
        "lang": lang,
        "asset": asset,
        "site_name": content.SITE_NAME,
        "tagline": content.TAGLINE[lang],
        "year": datetime.date.today().year,
        "css_version": CSS_VERSION,
        "page_title": page["title"][lang],
        "page_desc": page["desc"][lang],
        "page_h1": page["nav"][lang],
        "t": t,
        "sex_labels": sex_labels,
        "unnamed_markers": horses.UNNAMED_MARKERS,
        "nav": [
            {
                "file": item["file"],
                "label": item["nav"][lang],
                "active": item["key"] == page["key"],
            }
            for item in content.PAGES
        ],
        "lang_is_href": (asset if lang == "is" else other_prefix) + page["file"],
        "lang_de_href": (other_prefix if lang == "is" else "") + page["file"],
        "hreflang_links": [
            {"hreflang": "is", "href": f"{BASE_URL}/{page['file']}"},
            {"hreflang": "de", "href": f"{BASE_URL}/de/{page['file']}"},
            {"hreflang": "x-default", "href": f"{BASE_URL}/{page['file']}"},
        ],
        "prose": {key: value[lang] for key, value in content.PROSE.items()},
        "contact": content.CONTACT,
        "featured": horses.featured(),
        "breeding": horses.by_category(horses.Category.BREEDING_MARE),
        "young_mares": horses.by_category(horses.Category.YOUNG_MARE),
        "young_males": horses.by_category(horses.Category.YOUNG_MALE),
        "riding": horses.by_category(horses.Category.RIDING_HORSE),
        "gallery": range(1, horses.GALLERY_COUNT + 1),
    }


def main() -> None:
    env = build_env()
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "de").mkdir(parents=True)

    for page in content.PAGES:
        template = env.get_template(TEMPLATE_BY_KEY[page["key"]])
        for lang in content.LANGS:
            out_dir = DIST if lang == "is" else DIST / "de"
            html = template.render(page_context(page, lang))
            (out_dir / page["file"]).write_text(html, encoding="utf-8")
    print(f"Rendered {len(content.PAGES)} pages x {len(content.LANGS)} languages")

    for old, new in REDIRECTS.items():
        (DIST / old).write_text(REDIRECT_STUB.format(target=new, base=BASE_URL), encoding="utf-8")
    print(f"Wrote {len(REDIRECTS)} redirect stubs")

    shutil.copytree(ROOT / "css", DIST / "css")
    shutil.copytree(ROOT / "images", DIST / "images")
    shutil.copy(ROOT / "CNAME", DIST / "CNAME")
    print(f"Copied static assets -> {DIST}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Apply shared SEO meta invariants to every static HTML file."""

from __future__ import annotations

from pathlib import Path

from bs4 import BeautifulSoup, FeatureNotFound

from build_output import write_html_if_changed
from seo_meta import upsert_robots_image_preview

SITE_ROOT = Path(__file__).resolve().parents[2]

try:
    BeautifulSoup("", "lxml")
    HTML_PARSER = "lxml"
except FeatureNotFound:
    HTML_PARSER = "html.parser"


def apply_to_file(path: Path) -> bool:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), HTML_PARSER)
    changed = upsert_robots_image_preview(soup)
    return changed and write_html_if_changed(path, str(soup))


def main() -> int:
    html_files = sorted(
        path
        for path in SITE_ROOT.rglob("*.html")
        if ".git" not in path.parts
    )
    changed = [path for path in html_files if apply_to_file(path)]
    for path in changed:
        print(f"updated {path.relative_to(SITE_ROOT)}")
    print(f"SEO meta applied: {len(changed)} changed / {len(html_files)} checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

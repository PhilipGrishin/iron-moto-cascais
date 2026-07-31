#!/usr/bin/env python3
"""Apply shared SEO meta invariants to every static HTML file."""

from __future__ import annotations

from pathlib import Path
from typing import Set
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup, FeatureNotFound

from build_output import write_html_if_changed
from hero_images import ensure_lcp_image_delivery
from seo_meta import upsert_robots_image_preview

SITE_ROOT = Path(__file__).resolve().parents[2]

try:
    BeautifulSoup("", "lxml")
    HTML_PARSER = "lxml"
except FeatureNotFound:
    HTML_PARSER = "html.parser"


def sitemap_html_files() -> Set[Path]:
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    tree = ET.parse(SITE_ROOT / "sitemap.xml")
    paths = set()
    for loc in tree.findall(".//sm:loc", namespace):
        url_path = loc.text.split("ironcustommotors.com", 1)[-1].strip("/")
        paths.add(SITE_ROOT / url_path / "index.html" if url_path else SITE_ROOT / "index.html")
    return paths


def apply_to_file(path: Path, *, indexable: bool) -> bool:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), HTML_PARSER)
    changed = upsert_robots_image_preview(soup)
    if indexable:
        changed = ensure_lcp_image_delivery(soup, SITE_ROOT) or changed
    return changed and write_html_if_changed(path, str(soup))


def main() -> int:
    indexable_files = sitemap_html_files()
    html_files = sorted(
        path
        for path in SITE_ROOT.rglob("*.html")
        if ".git" not in path.parts
    )
    changed = [
        path
        for path in html_files
        if apply_to_file(path, indexable=path in indexable_files)
    ]
    for path in changed:
        print(f"updated {path.relative_to(SITE_ROOT)}")
    print(f"SEO meta applied: {len(changed)} changed / {len(html_files)} checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

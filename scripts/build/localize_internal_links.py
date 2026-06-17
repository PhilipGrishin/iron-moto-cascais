#!/usr/bin/env python3
"""Rewrite internal navigation links inside /ru/, /uk/, /pt/ pages
so they point to the correct localized version. Without this, clicking
"Услуги" on /ru/ takes users to /motorcycle-service/ (English)."""

import re
from pathlib import Path
from bs4 import BeautifulSoup, FeatureNotFound

SITE_ROOT = Path(__file__).resolve().parents[2]
TARGET_LANGS = ["ru", "uk", "pt"]

try:
    BeautifulSoup("", "lxml")
    HTML_PARSER = "lxml"
except FeatureNotFound:
    HTML_PARSER = "html.parser"

# All page paths that have localized versions (must match generator)
LOCALIZED_PATHS = {
    "/",
    "/motorcycle-service/",
    "/parts/",
    "/upgrades-tuning/",
    "/custom/",
    "/pre-purchase-inspection/",
    "/pricing/",
    "/services/",
    "/projects/",
    "/about/",
    "/community/",
    "/contact/",
    "/faq/",
    "/privacy/",
    "/cookies/",
    "/terms/",
    "/bmw-service/",
    "/harley-service/",
    "/ducati-service/",
    "/blog/",
    "/blog/revtech-110-oil-service-engine-gearbox-drive/",
    "/news/",
    "/news/ericeira-kustom-fest-2026/",
    "/news/opens-new-workshop-in-cascais/",
    "/news/lisbon-motorcycle-film-fest-2026-beckman/",
}
for proj in ["inspirium", "beckman", "unbreakable", "quanta-r",
             "burly", "sturmvogel", "geometric", "joker",
             "hellboy", "true-religion"]:
    LOCALIZED_PATHS.add(f"/projects/{proj}/")


def rewrite_href(href: str, lang: str) -> str:
    """If href points to a path that has a localized version, prepend /lang."""
    if not href:
        return href
    # Skip non-path links
    if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
        return href
    # Skip asset paths
    if href.startswith(("/photos/", "/assets/", "/worker/", "/pricing/files/")):
        return href
    # Already localized
    if re.match(r"^/(ru|uk|pt)(/|$)", href):
        return href
    # Try matching a known localized path. Strip fragment/query for comparison.
    base = re.split(r"[?#]", href, 1)[0]
    if base in LOCALIZED_PATHS:
        # Replace leading / with /lang/
        suffix = href[len(base):]  # keep fragment/query
        if base == "/":
            return f"/{lang}/{suffix}"
        return f"/{lang}{base}{suffix}"
    return href


def process_file(html_path: Path, lang: str) -> int:
    text = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(text, HTML_PARSER)
    changed = 0
    for a in soup.find_all("a", href=True):
        new = rewrite_href(a["href"], lang)
        if new != a["href"]:
            a["href"] = new
            changed += 1
    if changed:
        html_path.write_text(str(soup), encoding="utf-8")
    return changed


def main():
    total = 0
    for lang in TARGET_LANGS:
        lang_dir = SITE_ROOT / lang
        if not lang_dir.exists():
            continue
        for html in sorted(lang_dir.rglob("*.html")):
            changed = process_file(html, lang)
            if changed:
                rel = html.relative_to(SITE_ROOT)
                print(f"  {rel}: rewrote {changed} link(s)")
                total += changed
    print(f"\nDone: {total} internal links localized")


if __name__ == "__main__":
    main()

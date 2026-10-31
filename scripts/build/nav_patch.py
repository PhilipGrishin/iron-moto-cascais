#!/usr/bin/env python3
"""Apply the canonical navigation and managed footer to every sitemap page."""

from __future__ import annotations

from build_output import write_html_if_changed
from build_sitemap import LANGS, PAGES, html_file_for
from site_chrome import THANK_YOU_URLS, patch_footer_links, patch_navigation_footer


def patch_file(path, lang: str) -> bool:
    original = path.read_text(encoding="utf-8")
    rendered = patch_navigation_footer(original, lang)
    return write_html_if_changed(path, rendered)


def main() -> int:
    changed = 0
    total = 0
    missing = []
    for page_path, _, _ in PAGES:
        for lang in LANGS:
            total += 1
            path = html_file_for(lang, page_path)
            if not path.exists():
                missing.append(path)
                print(f"  missing: {path}")
                continue
            if patch_file(path, lang):
                changed += 1
                print(f"  patched: {path}")

    # Utility pages are excluded from PAGES but still share the managed footer.
    for lang in THANK_YOU_URLS:
        path = html_file_for(lang, "thank-you/")
        if not path.exists():
            missing.append(path)
            continue
        original = path.read_text(encoding="utf-8")
        write_html_if_changed(path, patch_footer_links(original, lang))

    print(f"\nDone. {changed}/{total} sitemap page(s) updated; utility footers synchronized.")
    if missing:
        print(f"Missing {len(missing)} sitemap page(s).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Generate sitemap.xml with all language versions and xhtml:link alternates."""

from datetime import date
from pathlib import Path

DOMAIN = "https://ironcustommotors.com"
SITE_ROOT = Path(__file__).resolve().parents[2]

# (path, changefreq, priority)
PAGES = [
    ("", "weekly", "1.0"),
    ("motorcycle-service/", "monthly", "0.9"),
    ("parts/", "monthly", "0.9"),
    ("upgrades-tuning/", "monthly", "0.85"),
    ("custom/", "monthly", "0.8"),
    ("pre-purchase-inspection/", "monthly", "0.85"),
    ("pricing/", "monthly", "0.9"),
    ("services/", "weekly", "0.95"),
    ("projects/", "monthly", "0.85"),
    ("about/", "monthly", "0.7"),
    ("community/", "monthly", "0.75"),
    ("contact/", "monthly", "0.8"),
    ("faq/", "monthly", "0.75"),
    ("privacy/", "yearly", "0.3"),
    ("cookies/", "yearly", "0.3"),
    ("terms/", "yearly", "0.3"),
    ("bmw-service/", "monthly", "0.9"),
    ("harley-service/", "monthly", "0.9"),
    ("ducati-service/", "monthly", "0.9"),
    ("motorcycle-tyre-service/", "monthly", "0.95"),
    ("blog/", "weekly", "0.85"),
    ("blog/revtech-110-oil-service-engine-gearbox-drive/", "monthly", "0.82"),
    ("blog/motorcycle-brake-pad-replacement-cascais/", "monthly", "0.82"),
    ("blog/front-fork-service-motorcycle-cascais/", "monthly", "0.82"),
    ("news/", "weekly", "0.9"),
    ("news/ericeira-kustom-fest-2026/", "yearly", "0.9"),
    ("news/opens-new-workshop-in-cascais/", "yearly", "0.8"),
    ("news/lisbon-motorcycle-film-fest-2026-beckman/", "yearly", "0.85"),
    ("projects/inspirium/", "yearly", "0.8"),
    ("projects/beckman/", "yearly", "0.8"),
    ("projects/unbreakable/", "yearly", "0.8"),
    ("projects/quanta-r/", "yearly", "0.75"),
    ("projects/burly/", "yearly", "0.75"),
    ("projects/sturmvogel/", "yearly", "0.7"),
    ("projects/geometric/", "yearly", "0.7"),
    ("projects/joker/", "yearly", "0.7"),
    ("projects/hellboy/", "yearly", "0.7"),
    ("projects/true-religion/", "yearly", "0.7"),
]

LANGS = ["en", "ru", "uk", "pt"]
TODAY = date.today().isoformat()
CUSTOM_LOCALIZED_PATHS = {
    "motorcycle-tyre-service/": {
        "en": "motorcycle-tyre-service/",
        "ru": "ru/shinomontazh-mototsiklov/",
        "uk": "uk/shynomontazh-mototsykliv/",
        "pt": "pt/montagem-de-pneus-mota/",
    }
}


def url_for(lang, path):
    if path in CUSTOM_LOCALIZED_PATHS:
        return f"{DOMAIN}/{CUSTOM_LOCALIZED_PATHS[path][lang]}"
    if lang == "en":
        return f"{DOMAIN}/{path}"
    return f"{DOMAIN}/{lang}/{path}"


def build_url_entry(lang, path, changefreq, priority):
    primary = url_for(lang, path)
    parts = [f"  <url>"]
    parts.append(f"    <loc>{primary}</loc>")
    parts.append(f"    <lastmod>{TODAY}</lastmod>")
    parts.append(f"    <changefreq>{changefreq}</changefreq>")
    parts.append(f"    <priority>{priority}</priority>")
    # Alternates pointing to all language versions, including self
    for alt in LANGS:
        parts.append(f'    <xhtml:link rel="alternate" hreflang="{alt}" href="{url_for(alt, path)}"/>')
    parts.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url_for("en", path)}"/>')
    parts.append(f"  </url>")
    return "\n".join(parts)


def main():
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for path, freq, pri in PAGES:
        for lang in LANGS:
            lines.append(build_url_entry(lang, path, freq, pri))
    lines.append("</urlset>")
    out = SITE_ROOT / "sitemap.xml"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out} ({len(PAGES)} pages × {len(LANGS)} langs = {len(PAGES) * len(LANGS)} URLs)")


if __name__ == "__main__":
    main()

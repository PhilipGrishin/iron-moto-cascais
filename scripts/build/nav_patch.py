#!/usr/bin/env python3
"""
Patch navigation (header + mobile drawer + footer) on every EN page of the
ICM site so that all anchor-based nav links are replaced with proper URLs.

New nav (everywhere):
  Services / Projects / Pricing / About / FAQ / Contact

Footer "Services" column:
  Motorcycle service & repair → /motorcycle-service/
  Parts & consumables         → /parts/
  Upgrades & tuning           → /upgrades-tuning/
  Custom & special projects   → /custom/
  Pre-purchase inspection     → /pre-purchase-inspection/
  Pricing                     → /pricing/

Footer "Company" column:
  About    → /about/
  Projects → /projects/
  Reviews  → /#reviews   (Reviews block is on home — dynamic widget)
  FAQ      → /faq/
  Contact  → /contact/

Run AFTER build_new_pages.py and BEFORE build_i18n.py.
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup

SITE_ROOT = Path(__file__).resolve().parents[2]

# All EN pages whose header + footer must be rewritten.
EN_PAGES = [
    "index.html",
    "motorcycle-service/index.html",
    "parts/index.html",
    "upgrades-tuning/index.html",
    "custom/index.html",
    "pre-purchase-inspection/index.html",
    "pricing/index.html",
    "services/index.html",
    "projects/index.html",
    "about/index.html",
    "community/index.html",
    "contact/index.html",
    "faq/index.html",
    # Project pages
    "projects/inspirium/index.html",
    "projects/beckman/index.html",
    "projects/unbreakable/index.html",
    "projects/quanta-r/index.html",
    "projects/burly/index.html",
    "projects/sturmvogel/index.html",
    "projects/geometric/index.html",
    "projects/joker/index.html",
    "projects/hellboy/index.html",
    "projects/true-religion/index.html",
    # Brand & news pages added 2026-05
    "bmw-service/index.html",
    "harley-service/index.html",
    "ducati-service/index.html",
    "blog/index.html",
    "news/index.html",
    "news/ericeira-kustom-fest-2026/index.html",
    "news/opens-new-workshop-in-cascais/index.html",
    "news/lisbon-motorcycle-film-fest-2026-beckman/index.html",
]


# Canonical primary nav (used as the source of truth)
PRIMARY_NAV_LINKS = [
    ("nav.services", "/services/",  "Services"),
    ("nav.projects", "/projects/",  "Projects"),
    ("nav.blog",     "/blog/",      "Blog"),
    ("nav.news",     "/news/",      "News"),
    ("nav.community", "/community/", "Community"),
    ("nav.pricing",  "/pricing/",   "Pricing"),
    ("nav.about",    "/about/",     "About"),
    ("nav.faq",      "/faq/",       "FAQ"),
    ("nav.contact",  "/contact/",   "Contact"),
]

FOOTER_SERVICES_LINKS = [
    ("services.s1.title", "/motorcycle-service/",      "Motorcycle service &amp; repair"),
    ("services.s2.title", "/parts/",                   "Parts &amp; consumables"),
    ("services.s3.title", "/upgrades-tuning/",         "Upgrades &amp; tuning"),
    ("services.s4.title", "/custom/",                  "Custom &amp; special projects"),
    ("nav.preInsp",       "/pre-purchase-inspection/", "Pre-purchase inspection"),
    ("nav.bmwServ",       "/bmw-service/",             "BMW Motorrad service"),
    ("nav.hdServ",        "/harley-service/",          "Harley-Davidson service"),
    ("nav.ducServ",       "/ducati-service/",          "Ducati service"),
    ("nav.pricing",       "/pricing/",                 "Pricing"),
]

FOOTER_COMPANY_LINKS = [
    ("nav.about",    "/about/",     "About"),
    ("nav.projects", "/projects/",  "Projects"),
    ("nav.blog",     "/blog/",      "Blog"),
    ("nav.news",     "/news/",      "News"),
    ("nav.community", "/community/", "Community"),
    ("nav.reviews",  "/#reviews",   "Reviews"),
    ("nav.faq",      "/faq/",       "FAQ"),
    ("nav.contact",  "/contact/",   "Contact"),
]


def render_primary_nav():
    parts = []
    for key, href, label in PRIMARY_NAV_LINKS:
        parts.append(f'<a data-i18n="{key}" href="{href}">{label}</a>')
    return "\n".join(parts)


def render_mobile_nav():
    return render_primary_nav()


def render_footer_services():
    items = []
    for key, href, label in FOOTER_SERVICES_LINKS:
        items.append(f'<li><a data-i18n="{key}" href="{href}">{label}</a></li>')
    return "\n".join(items)


def render_footer_company():
    items = []
    for key, href, label in FOOTER_COMPANY_LINKS:
        items.append(f'<li><a data-i18n="{key}" href="{href}">{label}</a></li>')
    return "\n".join(items)


def patch_file(path: Path):
    html = path.read_text(encoding="utf-8")
    orig = html
    soup = BeautifulSoup(html, "html.parser")

    # --- 1. Primary header nav ---
    primary = soup.find("nav", attrs={"aria-label": "Primary"})
    if primary:
        new = BeautifulSoup(f'<nav aria-label="Primary" class="nav">\n{render_primary_nav()}\n</nav>', "html.parser")
        primary.replace_with(new.nav)

    # --- 2. Mobile drawer nav ---
    mobile = soup.find("nav", class_="nav-mobile")
    if mobile:
        new = BeautifulSoup(f'<nav class="nav-mobile">\n{render_mobile_nav()}\n</nav>', "html.parser")
        mobile.replace_with(new.nav)

    # --- 3. Book-service buttons that pointed to #contact → /contact/ ---
    for a in soup.find_all("a"):
        if a.get("data-i18n") in ("cta.bookHeader", "cta.bookService") and a.get("href", "").endswith("#contact"):
            a["href"] = "/contact/"
    # sticky CTA in subpages also has data-i18n="cta.bookService" href="/#contact" — fix that too
    for a in soup.find_all("a", href=True):
        if a["href"] in ("#contact", "/#contact"):
            # If it's a CTA button or a header CTA, point to /contact/.
            # Form-anchor buttons inside /contact/ page itself keep #contact.
            page_id_for_contact = path.parent.name if path.parent != SITE_ROOT else ""
            if page_id_for_contact == "contact":
                # The "Open form" button on /contact/ stays as #contact (it triggers modal in main.js)
                continue
            classes = " ".join(a.get("class") or [])
            data_cta = a.get("data-cta") or ""
            if data_cta == "book" or "btn" in classes or "sticky" in classes:
                a["href"] = "/contact/"

    # --- 4. Footer columns ---
    # Find footer-col by their h5 data-i18n attribute
    for col in soup.find_all("div", class_="footer-col"):
        h5 = col.find("h5")
        if not h5:
            continue
        key = h5.get("data-i18n", "")
        if key == "footer.col1":
            ul = col.find("ul")
            if ul:
                new_ul = BeautifulSoup(f"<ul>\n{render_footer_services()}\n</ul>", "html.parser").ul
                ul.replace_with(new_ul)
        elif key == "footer.col2":
            ul = col.find("ul")
            if ul:
                new_ul = BeautifulSoup(f"<ul>\n{render_footer_company()}\n</ul>", "html.parser").ul
                ul.replace_with(new_ul)

    new_html = str(soup)
    if new_html != orig:
        path.write_text(new_html, encoding="utf-8")
        return True
    return False


def main():
    changed = 0
    for rel in EN_PAGES:
        p = SITE_ROOT / rel
        if not p.exists():
            print(f"  SKIP (missing): {rel}")
            continue
        if patch_file(p):
            changed += 1
            print(f"  patched: {rel}")
        else:
            print(f"  no change: {rel}")
    print(f"\nDone. {changed}/{len(EN_PAGES)} files updated.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Patch navigation (header + mobile drawer + footer) on every EN page of the
ICM site so that all anchor-based nav links are replaced with proper URLs.

New nav (everywhere):
  Services dropdown / Brands dropdown / Harley Hub dropdown / Authorized Dealer /
  Projects dropdown / About dropdown / Pricing / Contact

Footer "Services" column:
  Motorcycle service & repair → /motorcycle-service/
  Parts & consumables         → /parts/
  Upgrades & tuning           → /upgrades-tuning/
  Custom & special projects   → /custom/
  Pre-purchase inspection     → /pre-purchase-inspection/
  Authorized Dealer           → /authorized-dealer/
  For expats                  → /english-speaking-motorcycle-workshop/
  Pricing                     → /pricing/

Footer "Company" column:
  About    → /about/
  Projects → /projects/
  Reviews  → /#reviews   (Reviews block is on home — dynamic widget)
  FAQ      → /faq/
  Contact  → /contact/

Run after build_new_pages.py, then again after build_i18n.py so localized
project menus stay synchronized with the English source.
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup

from brand_pages_data import BRAND_NAME, BRAND_NAV_KEYS, BRAND_ORDER

SITE_ROOT = Path(__file__).resolve().parents[2]

# All EN pages whose header + footer must be rewritten.
EN_PAGES = [
    "index.html",
    "motorcycle-service/index.html",
    "motorcycle-tyre-service/index.html",
    "parts/index.html",
    "upgrades-tuning/index.html",
    "custom/index.html",
    "harley/index.html",
    "harley-tuning/index.html",
    "harley-custom/index.html",
    "pre-purchase-inspection/index.html",
    "english-speaking-motorcycle-workshop/index.html",
    "authorized-dealer/index.html",
    "pricing/index.html",
    "services/index.html",
    "projects/index.html",
    "about/index.html",
    "community/index.html",
    "contact/index.html",
    "faq/index.html",
    "privacy/index.html",
    "cookies/index.html",
    "terms/index.html",
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
    "projects/fighter/index.html",
    # Brand & news pages added 2026-05
    *[f"{slug}/index.html" for slug in BRAND_ORDER],
    "blog/index.html",
    "blog/revtech-110-oil-service-engine-gearbox-drive/index.html",
    "blog/motorcycle-brake-pad-replacement-cascais/index.html",
    "blog/front-fork-service-motorcycle-cascais/index.html",
    "blog/motorcycle-tyre-fitting-specialist-cascais/index.html",
    "blog/royal-enfield-bear-650-fork-oil-case-study/index.html",
    "blog/harley-davidson-full-service-done-right/index.html",
    "blog/royal-enfield-bear-650-scrambler-build/index.html",
    "news/index.html",
    "news/ericeira-kustom-fest-2026/index.html",
    "news/opens-new-workshop-in-cascais/index.html",
    "news/lisbon-motorcycle-film-fest-2026-beckman/index.html",
    "authorized-dealer/c-way/index.html",
]


# Canonical primary nav (used as the source of truth)
PRIMARY_NAV_LINKS = [
    ("nav.services", "/services/",  "Services"),
    ("nav.brands",   "/#brands",    "Brands"),
    ("nav.harleyHub", "/harley/",   "Harley Hub"),
    ("nav.authorizedDealer", "/authorized-dealer/", "Authorized Dealer"),
    ("nav.projects", "/projects/",  "Projects"),
    ("nav.about",    "/about/",     "About"),
    ("nav.pricing",  "/pricing/",   "Pricing"),
    ("nav.contact",  "/contact/",   "Contact"),
]

SERVICE_NAV_LINKS = [
    ("nav.allServices",     "/services/",                "All services"),
    ("services.s1.title",   "/motorcycle-service/",      "Motorcycle service &amp; repair"),
    ("services.s2.title",   "/parts/",                   "Parts &amp; consumables"),
    ("services.s3.title",   "/upgrades-tuning/",         "Upgrades &amp; tuning"),
    ("services.s4.title",   "/custom/",                  "Custom &amp; special projects"),
    ("nav.tyreServ",        "/motorcycle-tyre-service/", "Tyre fitting &amp; wheel balancing"),
    ("nav.preInsp",        "/pre-purchase-inspection/", "Pre-purchase inspection"),
]

BRAND_NAV_LINKS = [
    (BRAND_NAV_KEYS[slug], f"/{slug}/", BRAND_NAME[slug])
    for slug in BRAND_ORDER
]

HARLEY_NAV_LINKS = [
    ("nav.harleyHub", "/harley/", "Harley Hub"),
    ("nav.harleyService", "/harley-service/", "Service"),
    ("nav.harleyTuning", "/harley-tuning/", "Tuning"),
    ("nav.harleyCustom", "/harley-custom/", "Custom"),
]

PROJECT_NAV_LINKS = [
    ("nav.allProjects", "/projects/",                "All projects"),
    (None,              "/projects/inspirium/",       "Inspirium"),
    (None,              "/projects/beckman/",         "Beckman"),
    (None,              "/projects/unbreakable/",     "Unbreakable"),
    (None,              "/projects/quanta-r/",        "Quanta R"),
    (None,              "/projects/burly/",           "Burly"),
    (None,              "/projects/sturmvogel/",      "Sturmvogel"),
    (None,              "/projects/geometric/",       "Geometric"),
    (None,              "/projects/joker/",           "Joker"),
    (None,              "/projects/hellboy/",         "Hell Boy"),
    (None,              "/projects/true-religion/",   "True Religion"),
    (None,              "/projects/fighter/",         "Fighter"),
]

ABOUT_NAV_LINKS = [
    ("nav.aboutUs",   "/about/",     "About us"),
    ("nav.blog",      "/blog/",      "Blog"),
    ("nav.news",      "/news/",      "News"),
    ("nav.community", "/community/", "Community"),
    ("nav.faq",       "/faq/",       "FAQ"),
]

AUTHORIZED_DEALER_NAV_LINKS = [
    ("nav.authorizedDealerHub", "/authorized-dealer/", "Dealer hub"),
    ("nav.dealerCway", "/authorized-dealer/c-way/", "C-Way"),
]

DROPDOWN_NAV_LINKS = {
    "nav.services": SERVICE_NAV_LINKS,
    "nav.brands": BRAND_NAV_LINKS,
    "nav.harleyHub": HARLEY_NAV_LINKS,
    "nav.authorizedDealer": AUTHORIZED_DEALER_NAV_LINKS,
    "nav.projects": PROJECT_NAV_LINKS,
    "nav.about": ABOUT_NAV_LINKS,
}

FOOTER_SERVICES_LINKS = [
    ("services.s1.title", "/motorcycle-service/",      "Motorcycle service &amp; repair"),
    ("services.s2.title", "/parts/",                   "Parts &amp; consumables"),
    ("services.s3.title", "/upgrades-tuning/",         "Upgrades &amp; tuning"),
    ("services.s4.title", "/custom/",                  "Custom &amp; special projects"),
    ("nav.tyreServ",      "/motorcycle-tyre-service/", "Tyre fitting &amp; wheel balancing"),
    ("nav.preInsp",       "/pre-purchase-inspection/", "Pre-purchase inspection"),
    ("nav.authorizedDealer", "/authorized-dealer/",     "Authorized Dealer"),
    ("nav.expatWorkshop", "/english-speaking-motorcycle-workshop/", "For expats"),
    *BRAND_NAV_LINKS,
    ("nav.pricing",       "/pricing/",                 "Pricing"),
]

FOOTER_COMPANY_LINKS = [
    ("nav.about",    "/about/",     "About"),
    ("nav.harleyHub", "/harley/",   "Harley Hub"),
    ("nav.projects", "/projects/",  "Projects"),
    ("nav.blog",     "/blog/",      "Blog"),
    ("nav.news",     "/news/",      "News"),
    ("nav.community", "/community/", "Community"),
    ("nav.reviews",  "/#reviews",   "Reviews"),
    ("nav.faq",      "/faq/",       "FAQ"),
    ("nav.contact",  "/contact/",   "Contact"),
]


def render_nav_link(key, href, label):
    i18n = f' data-i18n="{key}"' if key else ""
    return f'<a{i18n} href="{href}">{label}</a>'


def render_dropdown(key, href, label, links):
    items = []
    for item_key, item_href, item_label in links:
        items.append(render_nav_link(item_key, item_href, item_label))
    menu_html = "\n".join(items)
    return f'''<div class="nav-dropdown">
<a aria-haspopup="true" class="nav-dropdown-trigger" data-i18n="{key}" href="{href}">{label}</a>
<div aria-label="{label}" class="nav-dropdown-menu">
{menu_html}
</div>
</div>'''


def render_primary_nav():
    parts = []
    for key, href, label in PRIMARY_NAV_LINKS:
        dropdown_links = DROPDOWN_NAV_LINKS.get(key)
        if dropdown_links:
            parts.append(render_dropdown(key, href, label, dropdown_links))
            continue
        parts.append(f'<a data-i18n="{key}" href="{href}">{label}</a>')
    return "\n".join(parts)


def render_mobile_group(key, label, links):
    items = []
    for item_key, href, item_label in links:
        items.append(render_nav_link(item_key, href, item_label))
    subnav_html = "\n".join(items)
    return f'''<details class="mobile-nav-group">
<summary class="mobile-nav-summary"><span data-i18n="{key}">{label}</span></summary>
<div class="mobile-subnav">
{subnav_html}
</div>
</details>'''


def render_mobile_nav():
    parts = []
    for key, href, label in PRIMARY_NAV_LINKS:
        dropdown_links = DROPDOWN_NAV_LINKS.get(key)
        if dropdown_links:
            parts.append(render_mobile_group(key, label, dropdown_links))
            continue
        parts.append(f'<a data-i18n="{key}" href="{href}">{label}</a>')
    return "\n".join(parts)


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


def localized_href(href: str, lang: str) -> str:
    if href == "/":
        return f"/{lang}/"
    return f"/{lang}{href}"


def unlocalize_href(href: str, lang: str) -> str:
    prefix = f"/{lang}"
    if href == f"{prefix}/":
        return "/"
    if href.startswith(f"{prefix}/"):
        return href[len(prefix):]
    return href


def patch_localized_project_links(path: Path, lang: str):
    """Replace localized project menus with one canonical, local link set."""
    html = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    changed = False

    desktop_menus = []
    for dropdown in soup.select(".nav-dropdown"):
        trigger = dropdown.select_one('.nav-dropdown-trigger[data-i18n="nav.projects"]')
        menu = dropdown.select_one(".nav-dropdown-menu")
        if trigger and menu:
            desktop_menus.append(menu)

    mobile_menus = []
    for group in soup.select(".mobile-nav-group"):
        summary = group.select_one('.mobile-nav-summary [data-i18n="nav.projects"]')
        menu = group.select_one(".mobile-subnav")
        if summary and menu:
            mobile_menus.append(menu)

    for menu in [*desktop_menus, *mobile_menus]:
        existing_labels = {}
        for anchor in menu.find_all("a", href=True):
            route = unlocalize_href(anchor["href"], lang)
            existing_labels.setdefault(route, anchor.get_text(strip=True))

        rendered = []
        for key, href, label in PROJECT_NAV_LINKS:
            target = localized_href(href, lang)
            anchor = soup.new_tag("a", href=target)
            if key:
                anchor["data-i18n"] = key
            anchor.string = existing_labels.get(href, label)
            rendered.append(anchor)

        current = [
            (anchor.get("href"), anchor.get("data-i18n"), anchor.get_text(strip=True))
            for anchor in menu.find_all("a", href=True)
        ]
        expected = [
            (anchor.get("href"), anchor.get("data-i18n"), anchor.get_text(strip=True))
            for anchor in rendered
        ]
        has_line_breaks = any("\n" in str(child) for child in menu.contents)
        if current != expected or not has_line_breaks:
            menu.clear()
            for anchor in rendered:
                menu.append("\n")
                menu.append(anchor)
            menu.append("\n")
            changed = True

    if changed:
        path.write_text(str(soup), encoding="utf-8")
    return changed


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

    localized_changed = 0
    localized_total = 0
    for lang in ("ru", "uk", "pt"):
        lang_root = SITE_ROOT / lang
        for path in sorted(lang_root.rglob("index.html")):
            localized_total += 1
            if patch_localized_project_links(path, lang):
                localized_changed += 1
                print(f"  patched localized projects menu: {path.relative_to(SITE_ROOT)}")

    print(
        f"\nDone. {changed}/{len(EN_PAGES)} EN files and "
        f"{localized_changed}/{localized_total} localized files updated."
    )


if __name__ == "__main__":
    main()

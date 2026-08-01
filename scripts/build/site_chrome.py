#!/usr/bin/env python3
"""Canonical navigation and managed footer rendering for every site page."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from bs4 import BeautifulSoup

from brand_pages_data import BRAND_NAME, BRAND_NAV_KEYS, BRAND_ORDER
from localize_internal_links import rewrite_href
from new_pages_data import PROJECT_TILES

SITE_ROOT = Path(__file__).resolve().parents[2]
BUILD_DIR = Path(__file__).resolve().parent
DOMAIN_HOSTS = {"ironcustommotors.com", "www.ironcustommotors.com"}

HTML_PARSER = "html.parser"

GLOBAL_I18N = json.loads((BUILD_DIR / "i18n.json").read_text(encoding="utf-8"))

PRIMARY_NAV_LINKS = [
    ("nav.services", "/services/", "Services"),
    ("nav.brands", "/#brands", "Brands"),
    ("nav.harleyHub", "/harley/", "Harley Hub"),
    ("nav.authorizedDealer", "/authorized-dealer/", "Authorized Dealer"),
    ("nav.projects", "/projects/", "Projects"),
    ("nav.about", "/about/", "About"),
    ("nav.pricing", "/pricing/", "Pricing"),
    ("nav.contact", "/contact/", "Contact"),
]

SERVICE_NAV_LINKS = [
    ("nav.allServices", "/services/", "All services"),
    ("services.s1.title", "/motorcycle-service/", "Motorcycle service &amp; repair"),
    ("services.s2.title", "/parts/", "Parts &amp; consumables"),
    ("services.s3.title", "/upgrades-tuning/", "Upgrades &amp; tuning"),
    ("services.s4.title", "/custom/", "Custom &amp; special projects"),
    ("nav.tyreServ", "/motorcycle-tyre-service/", "Tyre fitting &amp; wheel balancing"),
    ("nav.preInsp", "/pre-purchase-inspection/", "Pre-purchase inspection"),
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
    ("nav.allProjects", "/projects/", "All projects"),
    *[
        (None, f"/projects/{tile['slug']}/", tile["label"]["en"])
        for tile in PROJECT_TILES
    ],
]

ABOUT_NAV_LINKS = [
    ("nav.aboutUs", "/about/", "About us"),
    ("nav.blog", "/blog/", "Blog"),
    ("nav.news", "/news/", "News"),
    ("nav.community", "/community/", "Community"),
    ("nav.faq", "/faq/", "FAQ"),
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
    ("services.s1.title", "/motorcycle-service/", "Motorcycle service &amp; repair"),
    ("services.s2.title", "/parts/", "Parts &amp; consumables"),
    ("services.s3.title", "/upgrades-tuning/", "Upgrades &amp; tuning"),
    ("services.s4.title", "/custom/", "Custom &amp; special projects"),
    ("nav.tyreServ", "/motorcycle-tyre-service/", "Tyre fitting &amp; wheel balancing"),
    ("nav.preInsp", "/pre-purchase-inspection/", "Pre-purchase inspection"),
    ("nav.authorizedDealer", "/authorized-dealer/", "Authorized Dealer"),
    ("nav.expatWorkshop", "/english-speaking-motorcycle-workshop/", "For expats"),
    *BRAND_NAV_LINKS,
    ("nav.pricing", "/pricing/", "Pricing"),
]

FOOTER_COMPANY_LINKS = [
    ("nav.about", "/about/", "About"),
    ("nav.harleyHub", "/harley/", "Harley Hub"),
    ("nav.projects", "/projects/", "Projects"),
    ("nav.blog", "/blog/", "Blog"),
    ("nav.news", "/news/", "News"),
    ("nav.community", "/community/", "Community"),
    ("nav.reviews", "/#reviews", "Reviews"),
    ("nav.faq", "/faq/", "FAQ"),
    ("nav.contact", "/contact/", "Contact"),
]


def localized_href(href: str, lang: str) -> str:
    """Localize an internal site URL while preserving query and fragment."""
    if lang == "en" or not href:
        return href
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc:
        if parsed.netloc not in DOMAIN_HOSTS:
            return href
        localized_path = rewrite_href(parsed.path or "/", lang)
        return urlunsplit(
            (parsed.scheme, parsed.netloc, localized_path, parsed.query, parsed.fragment)
        )
    if not parsed.path.startswith("/"):
        return href
    base = urlunsplit(("", "", parsed.path, parsed.query, parsed.fragment))
    return rewrite_href(base, lang)


def label_for(key: str | None, lang: str, fallback: str) -> str:
    if not key:
        return fallback
    return (
        GLOBAL_I18N.get(lang, {}).get(key)
        or GLOBAL_I18N["en"].get(key)
        or fallback
    )


def render_nav_link(
    key: str | None,
    href: str,
    fallback: str,
    lang: str = "en",
) -> str:
    label = html.escape(label_for(key, lang, fallback), quote=False)
    i18n = f' data-i18n="{key}"' if key else ""
    return f'<a{i18n} href="{localized_href(href, lang)}">{label}</a>'


def render_dropdown(
    key: str,
    href: str,
    fallback: str,
    links: list[tuple[str | None, str, str]],
    lang: str = "en",
) -> str:
    label = html.escape(label_for(key, lang, fallback), quote=False)
    items = "\n".join(
        render_nav_link(item_key, item_href, item_fallback, lang)
        for item_key, item_href, item_fallback in links
    )
    return (
        '<div class="nav-dropdown">\n'
        f'<a aria-haspopup="true" class="nav-dropdown-trigger" '
        f'data-i18n="{key}" href="{localized_href(href, lang)}">{label}</a>\n'
        f'<div aria-label="{html.escape(label, quote=True)}" class="nav-dropdown-menu">\n'
        f"{items}\n"
        "</div>\n"
        "</div>"
    )


def render_primary_nav(lang: str = "en") -> str:
    items = []
    for key, href, fallback in PRIMARY_NAV_LINKS:
        dropdown = DROPDOWN_NAV_LINKS.get(key)
        if dropdown:
            items.append(render_dropdown(key, href, fallback, dropdown, lang))
        else:
            items.append(render_nav_link(key, href, fallback, lang))
    return '<nav aria-label="Primary" class="nav">\n' + "\n".join(items) + "\n</nav>"


def render_mobile_nav(lang: str = "en") -> str:
    items = []
    for key, href, fallback in PRIMARY_NAV_LINKS:
        dropdown = DROPDOWN_NAV_LINKS.get(key)
        if not dropdown:
            items.append(render_nav_link(key, href, fallback, lang))
            continue
        links = "\n".join(
            render_nav_link(item_key, item_href, item_fallback, lang)
            for item_key, item_href, item_fallback in dropdown
        )
        label = html.escape(label_for(key, lang, fallback), quote=False)
        items.append(
            '<details class="mobile-nav-group">\n'
            f'<summary class="mobile-nav-summary"><span data-i18n="{key}">'
            f"{label}</span></summary>\n"
            '<div class="mobile-subnav">\n'
            f"{links}\n"
            "</div>\n"
            "</details>"
        )
    return '<nav class="nav-mobile">\n' + "\n".join(items) + "\n</nav>"


def render_footer_links(
    links: list[tuple[str | None, str, str]],
    lang: str = "en",
) -> str:
    rows = "\n".join(
        f"<li>{render_nav_link(key, href, fallback, lang)}</li>"
        for key, href, fallback in links
    )
    return f"<ul>\n{rows}\n</ul>"


def render_footer_services(lang: str = "en") -> str:
    return render_footer_links(FOOTER_SERVICES_LINKS, lang)


def render_footer_company(lang: str = "en") -> str:
    return render_footer_links(FOOTER_COMPANY_LINKS, lang)


def footer_column(soup, key: str):
    heading = soup.find(attrs={"data-i18n": key})
    return heading.find_parent("div", class_="footer-col") if heading else None


def apply_navigation_footer(soup, lang: str) -> None:
    """Replace managed chrome regions and localize all links inside that chrome."""
    primary = soup.find("nav", attrs={"aria-label": "Primary"})
    if primary:
        primary.replace_with(
            BeautifulSoup(render_primary_nav(lang), HTML_PARSER).find("nav")
        )

    mobile = soup.find("nav", class_="nav-mobile")
    if mobile:
        mobile.replace_with(
            BeautifulSoup(render_mobile_nav(lang), HTML_PARSER).find("nav")
        )

    for key, renderer in (
        ("footer.col1", render_footer_services),
        ("footer.col2", render_footer_company),
    ):
        column = footer_column(soup, key)
        current_list = column.find("ul") if column else None
        if current_list:
            current_list.replace_with(
                BeautifulSoup(renderer(lang), HTML_PARSER).find("ul")
            )

    chrome_regions = [
        soup.select_one("#stickyCta"),
        soup.select_one("header.site-header"),
        soup.select_one("#mobileDrawer"),
        soup.select_one("footer.site-footer"),
    ]
    for region in chrome_regions:
        if not region:
            continue
        for anchor in region.find_all("a", href=True):
            anchor["href"] = localized_href(anchor["href"], lang)

    for button in soup.select("button[data-lang]"):
        if button.get("data-lang") == lang:
            button["aria-current"] = "true"
        else:
            button.attrs.pop("aria-current", None)
    current_lang = soup.select_one("#langCurrent")
    if current_lang:
        current_lang.string = lang.upper()


def patch_navigation_footer(html_text: str, lang: str) -> str:
    """Patch only managed chrome substrings, preserving every byte outside them."""
    replacements = (
        (
            r'<nav aria-label="Primary" class="nav">.*?</nav>',
            render_primary_nav(lang),
        ),
        (
            r'<nav class="nav-mobile">.*?</nav>',
            render_mobile_nav(lang),
        ),
        (
            r'(<h5 data-i18n="footer\.col1">[^<]*</h5>\s*)<ul>.*?</ul>',
            lambda match: match.group(1) + render_footer_services(lang),
        ),
        (
            r'(<h5 data-i18n="footer\.col2">[^<]*</h5>\s*)<ul>.*?</ul>',
            lambda match: match.group(1) + render_footer_company(lang),
        ),
    )
    patched = html_text
    for pattern, replacement in replacements:
        patched, count = re.subn(
            pattern,
            replacement,
            patched,
            count=1,
            flags=re.DOTALL,
        )
        if count != 1:
            raise ValueError(f"Expected one managed chrome match for {pattern!r}")

    def localize_region(match: re.Match[str]) -> str:
        return re.sub(
            r'href=(["\'])(.*?)\1',
            lambda href_match: (
                f'href={href_match.group(1)}'
                f'{localized_href(html.unescape(href_match.group(2)), lang)}'
                f'{href_match.group(1)}'
            ),
            match.group(0),
        )

    for pattern in (
        r'<header\b(?=[^>]*class="[^"]*\bsite-header\b[^"]*")[^>]*>.*?</header>',
        r'<div class="mobile-actions">.*?</div>',
        r'<footer\b(?=[^>]*class="[^"]*\bsite-footer\b[^"]*")[^>]*>.*?</footer>',
    ):
        patched, count = re.subn(
            pattern,
            localize_region,
            patched,
            count=1,
            flags=re.DOTALL,
        )
        if count != 1:
            raise ValueError(f"Expected one chrome region match for {pattern!r}")

    def set_language_button(match: re.Match[str]) -> str:
        opening_tag = re.sub(r'\s+aria-current="true"', "", match.group(0))
        if match.group(1) == lang:
            opening_tag = opening_tag[:-1] + ' aria-current="true">'
        return opening_tag

    patched = re.sub(
        r'<button\b(?=[^>]*data-lang="(en|pt|ru|uk)")[^>]*>',
        set_language_button,
        patched,
    )
    patched, count = re.subn(
        r'(<span id="langCurrent">).*?(</span>)',
        rf"\g<1>{lang.upper()}\g<2>",
        patched,
        count=1,
    )
    if count != 1:
        raise ValueError("Expected one current-language label")
    return patched


def apply_global_i18n(soup, lang: str) -> None:
    dictionary = GLOBAL_I18N.get(lang, GLOBAL_I18N["en"])
    for element in soup.select("[data-i18n]"):
        key = element.get("data-i18n")
        if key not in dictionary:
            continue
        element.clear()
        # I18N values are fragments. Document parsers such as lxml wrap a
        # plain label in <html><body><p>, which corrupts the target element.
        fragment = BeautifulSoup(dictionary[key], "html.parser")
        for child in list(fragment.contents):
            element.append(child)


def canonical_chrome_soup(lang: str):
    """Load the homepage chrome and apply the canonical localized navigation."""
    soup = BeautifulSoup(
        (SITE_ROOT / "index.html").read_text(encoding="utf-8"),
        HTML_PARSER,
    )
    apply_navigation_footer(soup, lang)
    apply_global_i18n(soup, lang)
    return soup


def render_pre_body_chrome(lang: str, include_loader: bool = False) -> str:
    soup = canonical_chrome_soup(lang)
    selectors = [
        "#cookieBanner",
        "#stickyCta",
        ".fab-wa",
        "header.site-header",
        "#mobileDrawer",
    ]
    if include_loader:
        selectors.insert(0, "#loader")
    return "\n".join(
        str(soup.select_one(selector))
        for selector in selectors
        if soup.select_one(selector)
    )


def render_site_footer(lang: str) -> str:
    soup = canonical_chrome_soup(lang)
    return str(soup.select_one("footer.site-footer"))


def render_contact_modal(lang: str) -> str:
    soup = canonical_chrome_soup(lang)
    return str(soup.select_one("#modal"))


def chrome_fragments(lang: str, cache_bust: str) -> tuple[str, str]:
    """Return shared pre-body and post-body chrome for standalone generators."""
    before = render_pre_body_chrome(lang, include_loader=True)
    after = "\n".join((render_site_footer(lang), render_contact_modal(lang)))
    after += f'\n<script defer="" src="/assets/main.js?v={cache_bust}"></script>'
    return before, after

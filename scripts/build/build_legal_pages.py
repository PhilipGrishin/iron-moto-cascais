#!/usr/bin/env python3
"""
Generate legal pages: /privacy/, /cookies/, /terms/ for all 4 languages.
Uses motorcycle-service/index.html as chrome template (header/footer/modal),
substitutes the body with legal-policy content.
"""

import json, re
from pathlib import Path
from bs4 import BeautifulSoup, FeatureNotFound

from legal_pages_data import LEGAL_PAGES, PRIVACY_HEAD, COOKIES_HEAD, TERMS_HEAD, LAST_UPDATED

SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
CACHE_BUST = "20260602b"

OG_LOCALES = {"en":"en_US","ru":"ru_RU","uk":"uk_UA","pt":"pt_PT"}
LANGS = ["en", "ru", "uk", "pt"]
TARGET_LANGS = ["ru", "uk", "pt"]

try:
    BeautifulSoup("", "lxml")
    HTML_PARSER = "lxml"
except FeatureNotFound:
    HTML_PARSER = "html.parser"


def parse_html(markup: str) -> BeautifulSoup:
    return BeautifulSoup(markup, HTML_PARSER)

# Inline CSS for legal pages
LEGAL_CSS = """.subpage.lg{padding:140px 0 60px;background:#0a0a0a;position:relative;overflow:hidden;isolation:isolate}
.subpage.lg::before{content:"";position:absolute;top:-30%;right:-15%;width:600px;height:600px;background:radial-gradient(circle,rgba(255,87,34,.18),transparent 60%);pointer-events:none;z-index:1}
.subpage.lg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.4),rgba(10,10,10,.95) 60%);z-index:0;pointer-events:none}
.subpage.lg .container{position:relative;z-index:1}
.crumb{display:flex;align-items:center;gap:10px;font-family:'Saira',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--text-mute);margin-bottom:24px}
.crumb a{color:var(--text-dim)}
.crumb a:hover{color:var(--accent)}
.crumb .sep{color:var(--accent)}
.subpage.lg h1{font-family:'Saira Condensed',sans-serif;font-weight:800;line-height:.95;letter-spacing:-.01em;text-transform:uppercase;font-size:clamp(40px,6.4vw,84px);color:#fff;margin-bottom:14px;max-width:18ch}
.subpage.lg .lead{max-width:62ch;color:var(--text-dim);font-size:clamp(15px,1.3vw,18px)}
.legal-body{padding:60px 0 80px;background:#0a0a0a;border-top:1px solid var(--border)}
.legal-body .container{max-width:840px}
.legal-body section{padding:24px 0;border-bottom:1px solid var(--border)}
.legal-body section:last-child{border-bottom:none}
.legal-body h2{font-family:'Saira Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:clamp(20px,1.8vw,26px);color:#fff;line-height:1.1;margin-bottom:14px}
.legal-body p{font-family:'Saira',sans-serif;font-weight:400;font-size:15px;line-height:1.65;color:var(--text-dim);max-width:72ch}
.legal-body .updated{margin-top:30px;font-family:'Saira',monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--text-mute)}
.legal-body .legal-nav{margin-top:40px;padding-top:30px;border-top:1px solid var(--border);display:flex;gap:18px;flex-wrap:wrap;font-family:'Saira',sans-serif;font-size:13px;letter-spacing:.06em;text-transform:uppercase}
.legal-body .legal-nav a{color:var(--text-dim)}
.legal-body .legal-nav a:hover{color:var(--accent)}
.legal-body .legal-nav a[aria-current="page"]{color:var(--accent)}"""

# Source for chrome (we read it and strip <main>)
CHROME_SOURCE = SITE_ROOT / "motorcycle-service" / "index.html"

I18N_LABELS = {
    "en": {"home":"Home","crumbHome":"Home","linkPrivacy":"Privacy","linkCookies":"Cookies","linkTerms":"Terms"},
    "ru": {"home":"Главная","crumbHome":"Главная","linkPrivacy":"Конфиденциальность","linkCookies":"Cookie","linkTerms":"Условия"},
    "uk": {"home":"Головна","crumbHome":"Головна","linkPrivacy":"Конфіденційність","linkCookies":"Cookie","linkTerms":"Умови"},
    "pt": {"home":"Início","crumbHome":"Início","linkPrivacy":"Privacidade","linkCookies":"Cookies","linkTerms":"Termos"},
}


def absolutize_paths(soup):
    """Convert relative head asset paths to absolute /."""
    for tag_name, attr in [("link","href"),("script","src"),("img","src")]:
        for el in soup.find_all(tag_name):
            v = el.get(attr)
            if v and v.startswith(("../","./")):
                stripped = re.sub(r"^(\.\./)+|^\./", "", v)
                el[attr] = "/" + stripped


def build_main(slug, lang, head_meta, body_data):
    """Build the <main> content for a legal page."""
    labels = I18N_LABELS[lang]
    sections_html = ""
    for h2, body in body_data["sections"]:
        sections_html += f'<section><h2>{h2}</h2><p>{body}</p></section>\n'

    legal_nav = []
    for s, key in [("privacy","linkPrivacy"), ("cookies","linkCookies"), ("terms","linkTerms")]:
        url = f"/{s}/" if lang=="en" else f"/{lang}/{s}/"
        current = ' aria-current="page"' if s == slug else ''
        legal_nav.append(f'<a href="{url}"{current}>{labels[key]}</a>')

    return f'''<main>
<section class="subpage lg">
<div class="container">
<div class="crumb"><a href="{"/" if lang=="en" else f"/{lang}/"}">{labels["crumbHome"]}</a><span class="sep">→</span><span>{body_data["h1"]}</span></div>
<h1>{body_data["h1"]}</h1>
<p class="lead">{body_data["intro"]}</p>
</div>
</section>
<section class="legal-body">
<div class="container">
{sections_html}
<div class="updated">{body_data["updated"]}</div>
<div class="legal-nav">
{chr(10).join(legal_nav)}
</div>
</div>
</section>
</main>'''


def build_page(slug, lang):
    """Generate a single legal page (slug × lang) and write to disk."""
    head_meta_dict, body_dict = LEGAL_PAGES[slug]
    head_meta = head_meta_dict[lang]
    body = body_dict[lang]

    # Start from motorcycle-service template
    chrome = parse_html(CHROME_SOURCE.read_text(encoding="utf-8"))

    # 1. html lang
    chrome.html["lang"] = lang
    chrome.html["data-lang"] = lang

    # 2. Replace <head> meta
    head = chrome.head

    # Title
    if chrome.title: chrome.title.string = head_meta["title"]

    def upsert_meta(name=None, prop=None, content=""):
        sel = {"name": name} if name else {"property": prop}
        el = head.find("meta", attrs=sel)
        if el is None:
            el = chrome.new_tag("meta")
            if name: el["name"] = name
            if prop: el["property"] = prop
            head.append(el)
        el["content"] = content

    upsert_meta(name="description", content=head_meta["description"])
    upsert_meta(prop="og:title", content=head_meta["title"])
    upsert_meta(prop="og:description", content=head_meta["description"])
    upsert_meta(prop="og:type", content="website")
    upsert_meta(prop="og:url", content=f"{DOMAIN}/{slug}/" if lang=="en" else f"{DOMAIN}/{lang}/{slug}/")
    upsert_meta(prop="og:locale", content=OG_LOCALES[lang])
    upsert_meta(name="twitter:title", content=head_meta["title"])
    upsert_meta(name="twitter:description", content=head_meta["description"])

    # Canonical
    can = head.find("link", attrs={"rel":"canonical"})
    if can is None:
        can = chrome.new_tag("link"); can["rel"]="canonical"; head.append(can)
    can["href"] = f"{DOMAIN}/{slug}/" if lang=="en" else f"{DOMAIN}/{lang}/{slug}/"

    # 3. Remove existing hreflang and add fresh
    for el in head.find_all("link", attrs={"rel":"alternate","hreflang":True}):
        el.decompose()
    for lg in LANGS:
        url = f"{DOMAIN}/{slug}/" if lg=="en" else f"{DOMAIN}/{lg}/{slug}/"
        t = chrome.new_tag("link"); t["rel"]="alternate"; t["hreflang"]=lg; t["href"]=url
        head.append(t)
    xd = chrome.new_tag("link"); xd["rel"]="alternate"; xd["hreflang"]="x-default"
    xd["href"] = f"{DOMAIN}/{slug}/"
    head.append(xd)

    # 4. Absolutize asset paths
    absolutize_paths(chrome)

    # 5. Drop the existing inline <style>, replace with legal CSS
    for st in head.find_all("style"):
        st.decompose()
    style = chrome.new_tag("style")
    style.string = LEGAL_CSS
    head.append(style)

    # 6. Remove existing JSON-LD (was Service schema for motorcycle-service)
    for s in head.find_all("script", attrs={"type":"application/ld+json"}):
        s.decompose()
    # Add fresh BreadcrumbList
    crumb = chrome.new_tag("script"); crumb["type"]="application/ld+json"
    crumb.string = json.dumps({
        "@context":"https://schema.org",
        "@type":"BreadcrumbList",
        "itemListElement":[
            {"@type":"ListItem","position":1,"name":I18N_LABELS[lang]["home"],"item":(f"{DOMAIN}/" if lang=="en" else f"{DOMAIN}/{lang}/")},
            {"@type":"ListItem","position":2,"name":body["h1"],"item":(f"{DOMAIN}/{slug}/" if lang=="en" else f"{DOMAIN}/{lang}/{slug}/")},
        ],
    }, ensure_ascii=False)
    head.append(crumb)

    # 7. Drop ICM_I18N_PAGE script (specific to motorcycle-service)
    for s in head.find_all("script"):
        txt = s.string or ""
        if "ICM_I18N_PAGE" in txt:
            s.decompose()

    # 8. Bump cache-bust on main.css and main.js
    for el in head.find_all(["link","script"]):
        for a in ("href","src"):
            v = el.get(a)
            if v and ("main.css" in v or "main.js" in v):
                el[a] = re.sub(r"\?v=[a-z0-9]+", f"?v={CACHE_BUST}", v)

    # 9. Replace <main>
    main_old = chrome.find("main")
    if main_old:
        new_main = parse_html(build_main(slug, lang, head_meta, body))
        main_old.replace_with(new_main.main)

    # 10. Update nav lang switcher current
    cur = chrome.find(id="langCurrent")
    if cur: cur.string = lang.upper()
    # Update primary nav so .lang-menu buttons' aria-current reflects current
    for b in chrome.select(".lang-menu button[data-lang]"):
        if b.get("data-lang") == lang:
            b["aria-current"] = "true"
        elif "aria-current" in b.attrs:
            del b["aria-current"]
    for b in chrome.select(".mobile-langs button[data-lang]"):
        if b.get("data-lang") == lang:
            b["aria-current"] = "true"
        elif "aria-current" in b.attrs:
            del b["aria-current"]

    # 11. Localize all data-i18n elements in chrome (nav, footer, etc.)
    # Read main I18N
    I18N = json.loads((Path(__file__).resolve().parent / "i18n.json").read_text(encoding="utf-8"))
    page_dict = I18N.get(lang, {})
    for el in chrome.find_all(attrs={"data-i18n": True}):
        key = el["data-i18n"]
        if key in page_dict:
            new_html = page_dict[key]
            new_soup = parse_html(new_html)
            container = new_soup.body or new_soup
            children = list(container.children)
            el.clear()
            for child in children:
                el.append(child)

    # 12. Internal-link localization for non-EN langs (e.g. /services/ → /ru/services/)
    if lang != "en":
        LOCALIZED_PATHS = {"/","/motorcycle-service/","/parts/","/upgrades-tuning/","/custom/",
                          "/pre-purchase-inspection/","/pricing/","/services/","/projects/",
                          "/about/","/contact/","/faq/","/privacy/","/cookies/","/terms/"}
        for proj in ["inspirium","beckman","unbreakable","quanta-r","burly","sturmvogel",
                    "geometric","joker","hellboy","true-religion"]:
            LOCALIZED_PATHS.add(f"/projects/{proj}/")
        for a in chrome.find_all("a", href=True):
            h = a["href"]
            if h.startswith(("http://","https://","mailto:","tel:","whatsapp:","#")): continue
            if h.startswith(("/photos/","/assets/","/pricing/files/","/worker/")): continue
            if re.match(r"^/(ru|uk|pt)/", h): continue
            base = re.split(r"[?#]", h, 1)[0]
            if base in LOCALIZED_PATHS:
                suffix = h[len(base):]
                if base == "/":
                    a["href"] = f"/{lang}/{suffix}"
                else:
                    a["href"] = f"/{lang}{base}{suffix}"

    # 13. Write
    out = SITE_ROOT / slug / "index.html" if lang == "en" else SITE_ROOT / lang / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(str(chrome), encoding="utf-8")
    return out


def main():
    total = 0
    for slug in LEGAL_PAGES:
        for lang in LANGS:
            out = build_page(slug, lang)
            total += 1
            print(f"  wrote {out.relative_to(SITE_ROOT)}")
    print(f"\nDone. {total} legal pages.")


if __name__ == "__main__":
    main()

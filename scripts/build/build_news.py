#!/usr/bin/env python3
"""
Generate the News section:
  /news/                                 — hub (CollectionPage / Blog schema)
  /news/<slug>/                          — individual article (NewsArticle schema)
+ EN sources. build_i18n.py picks up RU/UK/PT via inline ICM_I18N_PAGE.

Photos used by the first article live at:
  /photos/news/news-opening-{01..04}-1600.jpg  (+ -800.jpg)

Author for every article: Iron Custom Motors (per project policy).
"""

import json
from pathlib import Path

from hero_images import hero_background_css
from news_data import (
    NEWS_HUB_META, NEWS_HUB_BODY,
    NEWS_ARTICLES,
)
from site_chrome import (
    patch_navigation_footer,
    render_contact_modal,
    render_pre_body_chrome,
    render_site_footer,
)

SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
CACHE_BUST = "20260724a"
LANGS = ["en", "ru", "uk", "pt"]
OG_LOCALE = {"en":"en_US","ru":"ru_RU","uk":"uk_UA","pt":"pt_PT"}
BUSINESS_ID = f"{DOMAIN}/#business"
AUTHOR_URL = f"{DOMAIN}/about/"


def schema_datetime(value):
    """Return Article/BlogPosting dates as full ISO-8601 with Europe/Lisbon offset."""
    value = str(value).strip()
    if "T" in value:
        if len(value) >= 5 and value[-5] in ("+", "-") and value[-3] != ":":
            return f"{value[:-2]}:{value[-2:]}"
        return value
    # Default legacy date-only entries to a stable Lisbon local publication time.
    month = int(value[5:7])
    offset = "+01:00" if 4 <= month <= 10 else "+00:00"
    return f"{value}T10:00:00{offset}"


def schema_author():
    """Keep author tied to the canonical business entity while exposing author.url."""
    return {"@id": BUSINESS_ID, "url": AUTHOR_URL}

NEWS_RELATED_I18N = {
    "en": {
        "newsRel.eyebrow": "Related pages",
        "newsRel.title": "Keep exploring <em>Iron Custom Motors.</em>",
        "newsRel.lead": "News should connect back to the workshop: service, community, projects and the practical next step for your motorcycle.",
        "newsRel.serviceDesc": "Service, diagnostics, repair, parts and upgrades in Cascais and Greater Lisbon.",
        "newsRel.communityDesc": "Rider lounge, championship machines, coffee, local events and motorcycle culture.",
        "newsRel.projectsDesc": "The custom builds, records and competition projects behind the current workshop standard.",
    },
    "ru": {
        "newsRel.eyebrow": "Связанные страницы",
        "newsRel.title": "Продолжайте изучать <em>Iron Custom Motors.</em>",
        "newsRel.lead": "Новости должны вести обратно к мастерской: сервису, community, проектам и практическому следующему шагу для вашего мотоцикла.",
        "newsRel.serviceDesc": "Сервис, диагностика, ремонт, запчасти и апгрейды в Cascais и Greater Lisbon.",
        "newsRel.communityDesc": "Rider lounge, чемпионские мотоциклы, кофе, локальные события и мотокультура.",
        "newsRel.projectsDesc": "Кастом-сборки, рекорды и соревновательные проекты, на которых держится нынешний стандарт мастерской.",
    },
    "uk": {
        "newsRel.eyebrow": "Пов'язані сторінки",
        "newsRel.title": "Продовжуйте вивчати <em>Iron Custom Motors.</em>",
        "newsRel.lead": "Новини мають вести назад до майстерні: сервісу, community, проєктів і практичного наступного кроку для вашого мотоцикла.",
        "newsRel.serviceDesc": "Сервіс, діагностика, ремонт, запчастини й апґрейди у Cascais і Greater Lisbon.",
        "newsRel.communityDesc": "Rider lounge, чемпіонські мотоцикли, кава, локальні події і мотокультура.",
        "newsRel.projectsDesc": "Кастом-збірки, рекорди і змагальні проєкти, на яких тримається нинішній стандарт майстерні.",
    },
    "pt": {
        "newsRel.eyebrow": "Páginas relacionadas",
        "newsRel.title": "Continue a explorar a <em>Iron Custom Motors.</em>",
        "newsRel.lead": "As notícias devem voltar à oficina: serviço, comunidade, projetos e o próximo passo prático para a sua moto.",
        "newsRel.serviceDesc": "Serviço, diagnóstico, reparação, peças e upgrades em Cascais e Grande Lisboa.",
        "newsRel.communityDesc": "Rider lounge, máquinas campeãs, café, eventos locais e cultura motociclista.",
        "newsRel.projectsDesc": "Builds custom, recordes e projetos de competição por trás do padrão atual da oficina.",
    },
}

# --- shared chrome (same as other pages) ---

ARROW_SVG = '<svg fill="none" height="18" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24" width="18"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'

HEADER_HTML = render_pre_body_chrome("en")


FOOTER_HTML = render_site_footer("en")


MODAL_HTML = render_contact_modal("en")


def head(slug_for_url, lang, head_meta, body_data, json_ld_blocks, og_image=None):
    canonical = f"{DOMAIN}/{slug_for_url}/"
    og_img = og_image or f"{DOMAIN}/photos/og.jpg"
    hreflang_html = "".join(
        (f'<link rel="alternate" hreflang="{lg}" href="{DOMAIN}/{slug_for_url}/"/>' if lg == "en"
         else f'<link rel="alternate" hreflang="{lg}" href="{DOMAIN}/{lg}/{slug_for_url}/"/>')
        for lg in LANGS
    )
    hreflang_html += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{slug_for_url}/"/>'
    json_ld_html = "".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>'
        for b in json_ld_blocks
    )
    return f'''<!DOCTYPE html>
<html data-lang="{lang}" lang="{lang}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, viewport-fit=cover" name="viewport"/>
<meta content="#0a0a0a" name="theme-color"/>
<meta content="max-image-preview:large" name="robots"/>
<title>{head_meta["title"]}</title>
<meta content="{head_meta["description"]}" name="description"/>
<link href="{canonical}" rel="canonical"/>
<meta content="{head_meta["title"]}" property="og:title"/>
<meta content="{head_meta["description"]}" property="og:description"/>
<meta content="article" property="og:type"/>
<meta content="{canonical}" property="og:url"/>
<meta content="Iron Custom Motors" property="og:site_name"/>
<meta content="{og_img}" property="og:image"/>
<meta content="1200" property="og:image:width"/>
<meta content="630" property="og:image:height"/>
<meta content="{OG_LOCALE[lang]}" property="og:locale"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{head_meta["title"]}" name="twitter:title"/>
<meta content="{head_meta["description"]}" name="twitter:description"/>
<meta content="{og_img}" name="twitter:image"/>
<link href="/photos/favicon.ico" rel="icon" sizes="any"/>
<link href="/photos/favicon-32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/photos/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="/photos/site.webmanifest" rel="manifest"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Saira:wght@300;400;500;600;700;800;900&amp;family=Saira+Condensed:wght@400;600;700;800;900&amp;family=Roboto+Condensed:wght@400;500;600;700;800;900&amp;family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="/assets/main.css?v={CACHE_BUST}" rel="stylesheet"/>
<style>
{SHARED_STYLES}
{ARTICLE_CSS}
{HUB_CSS}
</style>
{json_ld_html}<script>window.ICM_I18N_PAGE = {{}};</script>
{hreflang_html}
</head>'''


# =================================================================
# Render /news/ hub
# =================================================================

def render_hub():
    en_head = NEWS_HUB_META["en"]
    en_body = NEWS_HUB_BODY["en"]

    # Build articles list (sorted by publish date DESC)
    articles_html = ""
    articles_sorted = sorted(
        NEWS_ARTICLES.items(),
        key=lambda x: x[1]["publishedISO"],
        reverse=True,
    )
    item_list = []
    for i, (slug, data) in enumerate(articles_sorted, start=1):
        ameta = data["meta"]["en"]
        abody = data["body"]["en"]
        hero_img = f"{data['imageBase']}-{data['imageHero']:02d}-1600.jpg"
        article_url = f"{DOMAIN}/news/{slug}/"
        item_list.append({
            "@type": "ListItem",
            "position": i,
            "url": article_url,
            "name": ameta["title"],
        })
        articles_html += f'''
<a class="news-card" href="/news/{slug}/">
<div class="img" style="{hero_background_css(hero_img, 768)}"></div>
<div class="body">
<div class="date">{abody["publishedLabel"]}</div>
<h3>{abody["h1Crumb"]}</h3>
<p>{ameta["excerpt"]}</p>
<span class="more">{en_body["readMore"]}</span>
</div>
</a>
'''

    # I18N: write inline ICM_I18N_PAGE with hub strings + per-article strings
    inline_i18n = {lang: {} for lang in LANGS}
    for lang in LANGS:
        body = NEWS_HUB_BODY[lang]
        inline_i18n[lang]["newsHub.eyebrow"] = body["eyebrow"]
        inline_i18n[lang]["newsHub.h1"] = body["h1"]
        inline_i18n[lang]["newsHub.sub"] = body["sub"]
        inline_i18n[lang]["newsHub.breadHome"] = body["breadHome"]
        inline_i18n[lang]["newsHub.h1Crumb"] = body["h1Crumb"]
        inline_i18n[lang]["newsHub.readMore"] = body["readMore"]
        # Per article translated bits
        for slug, data in NEWS_ARTICLES.items():
            ab = data["body"][lang]
            inline_i18n[lang][f"newsHub.{slug}.title"] = ab["h1Crumb"]
            inline_i18n[lang][f"newsHub.{slug}.excerpt"] = data["meta"][lang]["excerpt"]
            inline_i18n[lang][f"newsHub.{slug}.date"] = ab["publishedLabel"]

    json_ld_blocks = [
        {
            "@context": "https://schema.org",
            "@type": "Blog",
            "name": en_head["title"],
            "url": f"{DOMAIN}/news/",
            "publisher": {"@id": BUSINESS_ID},
            "isPartOf": {"@id": f"{DOMAIN}/#website"},
            "blogPost": [
                {"@type": "BlogPosting",
                 "headline": data["body"]["en"]["h1Crumb"],
                 "url": f"{DOMAIN}/news/{slug}/",
                 "datePublished": schema_datetime(data["publishedISO"])}
                for slug, data in articles_sorted
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
                {"@type": "ListItem", "position": 2, "name": "News", "item": f"{DOMAIN}/news/"},
            ],
        },
    ]

    head_html = head("news", "en", en_head, en_body, json_ld_blocks).replace(
        "window.ICM_I18N_PAGE = {};", f"window.ICM_I18N_PAGE = {json.dumps(inline_i18n, ensure_ascii=False)};"
    )

    # Body
    # Replace article items with i18n-aware versions
    articles_html_i18n = ""
    for i, (slug, data) in enumerate(articles_sorted, start=1):
        ameta = data["meta"]["en"]
        abody = data["body"]["en"]
        hero_img = f"{data['imageBase']}-{data['imageHero']:02d}-1600.jpg"
        articles_html_i18n += f'''
<a class="news-card" href="/news/{slug}/">
<div class="img" style="{hero_background_css(hero_img, 768)}"></div>
<div class="body">
<div class="date" data-i18n="newsHub.{slug}.date">{abody["publishedLabel"]}</div>
<h3 data-i18n="newsHub.{slug}.title">{abody["h1Crumb"]}</h3>
<p data-i18n="newsHub.{slug}.excerpt">{ameta["excerpt"]}</p>
<span class="more" data-i18n="newsHub.readMore">{en_body["readMore"]}</span>
</div>
</a>
'''

    body = f'''<main>
<section class="subpage news-hub">
<div aria-hidden="true" class="bg"></div>
<div class="container">
<div class="crumb"><a data-i18n="newsHub.breadHome" href="/">Home</a><span class="sep">→</span><span data-i18n="newsHub.h1Crumb">News</span></div>
<div class="h-eyebrow" data-i18n="newsHub.eyebrow" style="margin-bottom:18px">{en_body["eyebrow"]}</div>
<h1 data-i18n="newsHub.h1">{en_body["h1"]}</h1>
<p class="lead" data-i18n="newsHub.sub">{en_body["sub"]}</p>
</div>
</section>
<section style="padding:60px 0 80px;background:#0a0a0a;border-top:1px solid var(--border)">
<div class="container">
<div class="news-grid">
{articles_html_i18n}
</div>
</div>
</section>
</main>'''

    html = head_html + "\n<body>\n" + HEADER_HTML + body + FOOTER_HTML + MODAL_HTML + f'\n<script defer="" src="/assets/main.js?v={CACHE_BUST}"></script>\n</body>\n</html>'
    html = patch_navigation_footer(html, "en")

    out = SITE_ROOT / "news" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


# =================================================================
# Render individual article
# =================================================================

def render_article(slug, article):
    en_meta = article["meta"]["en"]
    en_body = article["body"]["en"]
    n_img = article["imageCount"]
    hero_img_path = f"{article['imageBase']}-{article['imageHero']:02d}-1600.jpg"
    hero_img_url = f"{DOMAIN}{hero_img_path}"

    page_url = f"{DOMAIN}/news/{slug}/"

    # JSON-LD: NewsArticle + BreadcrumbList
    images = [f"{DOMAIN}{article['imageBase']}-{i:02d}-1600.jpg" for i in range(1, n_img+1)]
    json_ld_blocks = [
        {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "headline": en_body["h1Crumb"],
            "description": en_meta["description"],
            "image": images,
            "datePublished": schema_datetime(article["publishedISO"]),
            "dateModified": schema_datetime(article.get("modifiedISO", article["publishedISO"])),
            "author": schema_author(),
            "publisher": {"@id": BUSINESS_ID},
            "mainEntityOfPage": {"@type": "WebPage", "@id": page_url},
            "url": page_url,
            "inLanguage": "en",
            "articleSection": "Workshop news",
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
                {"@type": "ListItem", "position": 2, "name": "News", "item": f"{DOMAIN}/news/"},
                {"@type": "ListItem", "position": 3, "name": en_body["h1Crumb"], "item": page_url},
            ],
        },
    ]

    # Inline I18N: flatten article body per language with a single prefix per slug
    pre = f"art_{slug.replace('-', '_')}"
    inline_i18n = {lang: {} for lang in LANGS}
    for lang in LANGS:
        ab = article["body"][lang]
        for k, v in ab.items():
            inline_i18n[lang][f"{pre}.{k}"] = v
        inline_i18n[lang][f"{pre}.related.readMore"] = NEWS_HUB_BODY[lang]["readMore"]
        for other_slug, other_data in NEWS_ARTICLES.items():
            if other_slug == slug:
                continue
            inline_i18n[lang][f"{pre}.related.{other_slug}.title"] = other_data["body"][lang]["h1Crumb"]
            inline_i18n[lang][f"{pre}.related.{other_slug}.excerpt"] = other_data["meta"][lang]["excerpt"]
        inline_i18n[lang].update(NEWS_RELATED_I18N[lang])

    # Compose head + override the ICM_I18N_PAGE
    head_html = head(f"news/{slug}", "en", en_meta, en_body, json_ld_blocks, og_image=hero_img_url).replace(
        "window.ICM_I18N_PAGE = {};", f"window.ICM_I18N_PAGE = {json.dumps(inline_i18n, ensure_ascii=False)};"
    )

    # Body: hero (full-bleed photo + title), then sections with inline figures.
    # Sections and image placement are driven by article data:
    #   sectionCount → number of sections (auto-detects paragraphs sX.p1, sX.p2, sX.p3 ...)
    #   imageMap     → list of (img_num, after_section_num) tuples, e.g. [(2, 2), (4, 3)]

    section_count = article.get("sectionCount", 7)
    image_map = article.get("imageMap", [])
    # Group images by which section they come after
    images_after = {}
    for img_num, after_sec in image_map:
        images_after.setdefault(after_sec, []).append(img_num)

    def render_section(sec_num):
        parts = [f'<section>',
                 f'<h2 data-i18n="{pre}.s{sec_num}.h2">{en_body[f"s{sec_num}.h2"]}</h2>']
        # Find all paragraphs sN.pK that exist in en_body
        for p_idx in range(1, 20):
            key = f"s{sec_num}.p{p_idx}"
            if key not in en_body:
                break
            parts.append(f'<p data-i18n="{pre}.{key}">{en_body[key]}</p>')
        parts.append("</section>")
        return "\n".join(parts)

    def render_figure(img_num):
        width, height = article.get("imageDims", {}).get(img_num, (1600, 1200))
        return f'''<figure class="article-fig">
<img alt="{en_body[f"img{img_num}.alt"]}" data-i18n-alt="{pre}.img{img_num}.alt" loading="lazy" src="{article['imageBase']}-{img_num:02d}-1600.jpg" width="{width}" height="{height}"/>
<figcaption data-i18n="{pre}.img{img_num}.cap">{en_body[f"img{img_num}.cap"]}</figcaption>
</figure>'''

    sections_html_parts = []
    for sec in range(1, section_count + 1):
        sections_html_parts.append(render_section(sec))
        if sec in images_after:
            for img_num in images_after[sec]:
                sections_html_parts.append(render_figure(img_num))

    sections_html = "\n\n".join(sections_html_parts)

    related_news_cards = ""
    related_articles = sorted(
        ((other_slug, other_data) for other_slug, other_data in NEWS_ARTICLES.items() if other_slug != slug),
        key=lambda x: x[1]["publishedISO"],
        reverse=True,
    )
    for other_slug, other_data in related_articles:
        related_news_cards += f'''
<article class="news-related-card">
<h3 data-i18n="{pre}.related.{other_slug}.title">{other_data["body"]["en"]["h1Crumb"]}</h3>
<p data-i18n="{pre}.related.{other_slug}.excerpt">{other_data["meta"]["en"]["excerpt"]}</p>
<a data-i18n="{pre}.related.readMore" href="/news/{other_slug}/">{NEWS_HUB_BODY["en"]["readMore"]}</a>
</article>
'''

    body = f'''<main>
<article>
<section class="subpage news-article">
<div aria-hidden="true" class="bg" style="{hero_background_css(article['imageBase'] + '-01-1600.jpg')}"></div>
<div aria-hidden="true" class="scrim"></div>
<div class="container">
<div class="crumb"><a data-i18n="{pre}.breadHome" href="/">Home</a><span class="sep">→</span><a data-i18n="{pre}.breadNews" href="/news/">News</a><span class="sep">→</span><span data-i18n="{pre}.h1Crumb">{en_body["h1Crumb"]}</span></div>
<div class="date" data-i18n="{pre}.eyebrow">{en_body["eyebrow"]}</div>
<h1 data-i18n="{pre}.h1">{en_body["h1"]}</h1>
<p class="lede" data-i18n="{pre}.lede">{en_body["lede"]}</p>
</div>
</section>
<section class="article-body">
<div class="container">

{sections_html}

<div class="article-author">
<span class="pill">Iron Custom Motors</span>
<span data-i18n="{pre}.publishedLabel">{en_body["publishedLabel"]}</span>
</div>

</div>
</section>

<section class="news-related">
<div class="container">
<div class="heading reveal">
<span class="h-eyebrow" data-i18n="newsRel.eyebrow">{NEWS_RELATED_I18N["en"]["newsRel.eyebrow"]}</span>
<div>
<h2 data-i18n="newsRel.title">{NEWS_RELATED_I18N["en"]["newsRel.title"]}</h2>
<p class="lead" data-i18n="newsRel.lead">{NEWS_RELATED_I18N["en"]["newsRel.lead"]}</p>
</div>
</div>
<div class="news-related-grid reveal-stagger">
{related_news_cards}
<article class="news-related-card">
<h3 data-i18n="nav.services">Services</h3>
<p data-i18n="newsRel.serviceDesc">{NEWS_RELATED_I18N["en"]["newsRel.serviceDesc"]}</p>
<a data-i18n="services.learn" href="/services/">Learn more</a>
</article>
<article class="news-related-card">
<h3 data-i18n="nav.community">Community</h3>
<p data-i18n="newsRel.communityDesc">{NEWS_RELATED_I18N["en"]["newsRel.communityDesc"]}</p>
<a data-i18n="services.learn" href="/community/">Learn more</a>
</article>
<article class="news-related-card">
<h3 data-i18n="nav.projects">Projects</h3>
<p data-i18n="newsRel.projectsDesc">{NEWS_RELATED_I18N["en"]["newsRel.projectsDesc"]}</p>
<a data-i18n="services.learn" href="/projects/">Learn more</a>
</article>
</div>
</div>
</section>

<section class="cta-back">
<div class="container">
<span class="h-eyebrow" data-i18n="{pre}.ctaEyebrow">{en_body["ctaEyebrow"]}</span>
<h2 data-i18n="{pre}.ctaTitle">{en_body["ctaTitle"]}</h2>
<p class="lead" data-i18n="{pre}.ctaText">{en_body["ctaText"]}</p>
<div class="btns">
<a class="btn btn-primary" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank"><span data-i18n="{pre}.btnWA">{en_body["btnWA"]}</span>{ARROW_SVG}</a>
<a class="btn btn-ghost" data-i18n="{pre}.btnBack" href="/news/">{en_body["btnBack"]}</a>
</div>
</div>
</section>

</article>
</main>'''

    html = head_html + "\n<body>\n" + HEADER_HTML + body + FOOTER_HTML + MODAL_HTML + f'\n<script defer="" src="/assets/main.js?v={CACHE_BUST}"></script>\n</body>\n</html>'
    html = patch_navigation_footer(html, "en")

    out = SITE_ROOT / "news" / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


def main():
    out = render_hub()
    print(f"  wrote {out.relative_to(SITE_ROOT)} ({out.stat().st_size:,} bytes)")
    for slug, article in NEWS_ARTICLES.items():
        out = render_article(slug, article)
        print(f"  wrote {out.relative_to(SITE_ROOT)} ({out.stat().st_size:,} bytes)")
    print(f"\nDone. {1 + len(NEWS_ARTICLES)} News pages written.")


if __name__ == "__main__":
    main()

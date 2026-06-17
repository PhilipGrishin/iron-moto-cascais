#!/usr/bin/env python3
"""
Generate the Blog section:
  /blog/                     — hub for practical workshop articles.

The first individual blog post will be added after the owner provides the
brief. This generator already keeps the hub data-driven and multilingual.
"""

import json
from pathlib import Path

from blog_data import BLOG_HUB_BODY, BLOG_HUB_META, BLOG_POSTS
from build_news import (
    ARROW_SVG,
    DOMAIN,
    FOOTER_HTML,
    HEADER_HTML,
    LANGS,
    MODAL_HTML,
    OG_LOCALE,
    SHARED_STYLES,
    SITE_ROOT,
    CACHE_BUST,
)


BLOG_CSS = """.subpage.blog-hub{padding:140px 0 74px}
.blog-hub .bg{position:absolute;inset:0;z-index:-1;background-size:cover;background-position:center;filter:saturate(.82) contrast(1.08) brightness(.46);background-image:url('/photos/lounge-1600.jpg')}
.blog-posts{padding:60px 0 20px;background:#0a0a0a;border-top:1px solid var(--border)}
.blog-grid{display:grid;grid-template-columns:1fr;gap:24px}
.blog-card{display:grid;grid-template-columns:1.2fr 1fr;gap:30px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;transition:border-color .25s var(--ease),transform .25s var(--ease)}
.blog-card:hover{border-color:var(--accent);transform:translateY(-2px)}
.blog-card .img{aspect-ratio:16/10;background-size:cover;background-position:center;background-color:#111}
.blog-card .body{padding:34px 30px;display:flex;flex-direction:column;gap:14px;justify-content:center}
.blog-card .date{font-family:'Saira',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.blog-card h3{font-family:'Saira Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:clamp(22px,2.2vw,32px);line-height:1.05;color:#fff}
.blog-card p{font-size:15px;color:var(--text-dim);max-width:50ch}
.blog-card .more{display:inline-flex;align-items:center;gap:8px;font-family:'Saira',sans-serif;font-weight:600;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);margin-top:auto}
.blog-empty{padding:46px 28px;text-align:center;color:var(--text-dim);font-size:16px;border:1px solid var(--border);background:var(--surface);border-radius:var(--radius-lg)}
.blog-topics{padding:80px 0;background:#0a0a0a;border-top:1px solid var(--border)}
.blog-topics .heading{margin-bottom:50px;display:grid;grid-template-columns:1fr 1.4fr;gap:60px;align-items:end;padding-bottom:30px;border-bottom:1px solid var(--border)}
.blog-topics .heading h2{margin:0;font-family:'Saira Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:clamp(30px,4.6vw,62px);line-height:.95;color:#fff}
.blog-topics .heading h2 em{color:var(--accent);font-style:italic}
.topic-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.topic-card{min-height:190px;padding:24px 20px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);display:flex;flex-direction:column;gap:14px}
.topic-card .num{font-family:'Saira',monospace;font-size:11px;letter-spacing:.16em;color:var(--accent)}
.topic-card h3{font-family:'Saira Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:24px;line-height:1;color:#fff}
.topic-card p{font-size:14px;line-height:1.55;color:var(--text-dim)}
@media (max-width:1100px){.topic-grid{grid-template-columns:repeat(2,1fr)}.blog-topics .heading{grid-template-columns:1fr;gap:24px}}
@media (max-width:760px){.blog-card{grid-template-columns:1fr}.blog-card .img{aspect-ratio:16/9}.topic-grid{grid-template-columns:1fr}}"""


def head(slug_for_url, lang, head_meta, json_ld_blocks, og_image=None):
    canonical = f"{DOMAIN}/{slug_for_url}/"
    og_img = og_image or f"{DOMAIN}/photos/og.jpg"
    hreflang_html = "".join(
        (
            f'<link rel="alternate" hreflang="{lg}" href="{DOMAIN}/{slug_for_url}/"/>'
            if lg == "en"
            else f'<link rel="alternate" hreflang="{lg}" href="{DOMAIN}/{lg}/{slug_for_url}/"/>'
        )
        for lg in LANGS
    )
    hreflang_html += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{slug_for_url}/"/>'
    json_ld_html = "".join(
        f'<script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>'
        for block in json_ld_blocks
    )
    return f'''<!DOCTYPE html>
<html data-lang="{lang}" lang="{lang}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, viewport-fit=cover" name="viewport"/>
<meta content="#0a0a0a" name="theme-color"/>
<title>{head_meta["title"]}</title>
<meta content="{head_meta["description"]}" name="description"/>
<link href="{canonical}" rel="canonical"/>
<meta content="{head_meta["title"]}" property="og:title"/>
<meta content="{head_meta["description"]}" property="og:description"/>
<meta content="website" property="og:type"/>
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
<link href="https://fonts.googleapis.com/css2?family=Saira:wght@300;400;500;600;700;800;900&amp;family=Saira+Condensed:wght@400;600;700;800;900&amp;family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="/assets/main.css?v={CACHE_BUST}" rel="stylesheet"/>
<style>
{SHARED_STYLES}
{BLOG_CSS}
</style>
{json_ld_html}<script>window.ICM_I18N_PAGE = {{}};</script>
{hreflang_html}
</head>'''


def render_hub():
    en_head = BLOG_HUB_META["en"]
    en_body = BLOG_HUB_BODY["en"]

    inline_i18n = {lang: {} for lang in LANGS}
    for lang in LANGS:
        body = BLOG_HUB_BODY[lang]
        for key, value in body.items():
            inline_i18n[lang][f"blogHub.{key}"] = value
        for slug, data in BLOG_POSTS.items():
            post_body = data["body"][lang]
            inline_i18n[lang][f"blogHub.{slug}.title"] = post_body["h1Crumb"]
            inline_i18n[lang][f"blogHub.{slug}.excerpt"] = data["meta"][lang]["excerpt"]
            inline_i18n[lang][f"blogHub.{slug}.date"] = post_body["publishedLabel"]

    posts_sorted = sorted(
        BLOG_POSTS.items(),
        key=lambda item: item[1]["publishedISO"],
        reverse=True,
    )

    if posts_sorted:
        posts_html = ""
        for slug, data in posts_sorted:
            meta = data["meta"]["en"]
            body = data["body"]["en"]
            hero_img = f"{data['imageBase']}-{data['imageHero']:02d}-1600.jpg"
            posts_html += f'''
<a class="blog-card" href="/blog/{slug}/">
<div class="img" style="background-image:url('{hero_img}')"></div>
<div class="body">
<div class="date" data-i18n="blogHub.{slug}.date">{body["publishedLabel"]}</div>
<h3 data-i18n="blogHub.{slug}.title">{body["h1Crumb"]}</h3>
<p data-i18n="blogHub.{slug}.excerpt">{meta["excerpt"]}</p>
<span class="more" data-i18n="blogHub.readMore">{en_body["readMore"]}</span>
</div>
</a>
'''
    else:
        posts_html = f'<div class="blog-empty" data-i18n="blogHub.noPosts">{en_body["noPosts"]}</div>'

    blog_schema = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": en_head["title"],
        "description": en_head["description"],
        "url": f"{DOMAIN}/blog/",
        "publisher": {"@id": f"{DOMAIN}/#business"},
        "isPartOf": {"@id": f"{DOMAIN}/#website"},
        "inLanguage": "en",
    }
    if posts_sorted:
        blog_schema["blogPost"] = [
            {
                "@type": "BlogPosting",
                "headline": data["body"]["en"]["h1Crumb"],
                "url": f"{DOMAIN}/blog/{slug}/",
                "datePublished": data["publishedISO"],
            }
            for slug, data in posts_sorted
        ]

    json_ld_blocks = [
        blog_schema,
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{DOMAIN}/blog/"},
            ],
        },
    ]

    head_html = head("blog", "en", en_head, json_ld_blocks, og_image=f"{DOMAIN}/photos/lounge-1600.jpg").replace(
        "window.ICM_I18N_PAGE = {};",
        f"window.ICM_I18N_PAGE = {json.dumps(inline_i18n, ensure_ascii=False)};",
    )

    topics_html = "\n".join(
        f'''<article class="topic-card">
<span class="num">{idx:02d}</span>
<h3 data-i18n="blogHub.topic{idx}Title">{en_body[f"topic{idx}Title"]}</h3>
<p data-i18n="blogHub.topic{idx}Text">{en_body[f"topic{idx}Text"]}</p>
</article>'''
        for idx in range(1, 6)
    )

    body = f'''<main>
<section class="subpage blog-hub">
<div aria-hidden="true" class="bg"></div>
<div class="container">
<div class="crumb"><a data-i18n="blogHub.breadHome" href="/">Home</a><span class="sep">→</span><span data-i18n="blogHub.h1Crumb">Blog</span></div>
<div class="h-eyebrow" data-i18n="blogHub.eyebrow" style="margin-bottom:18px">{en_body["eyebrow"]}</div>
<h1 data-i18n="blogHub.h1">{en_body["h1"]}</h1>
<p class="lead" data-i18n="blogHub.sub">{en_body["sub"]}</p>
</div>
</section>
<section class="blog-posts">
<div class="container">
<div class="blog-grid">
{posts_html}
</div>
</div>
</section>
<section class="blog-topics">
<div class="container">
<div class="heading reveal">
<span class="h-eyebrow" data-i18n="blogHub.topicsEyebrow">{en_body["topicsEyebrow"]}</span>
<div>
<h2 data-i18n="blogHub.topicsTitle">{en_body["topicsTitle"]}</h2>
<p class="lead" data-i18n="blogHub.topicsLead">{en_body["topicsLead"]}</p>
</div>
</div>
<div class="topic-grid reveal-stagger">
{topics_html}
</div>
</div>
</section>
<section class="cta-back">
<div class="container">
<span class="h-eyebrow" data-i18n="blogHub.ctaEyebrow">{en_body["ctaEyebrow"]}</span>
<h2 data-i18n="blogHub.ctaTitle">{en_body["ctaTitle"]}</h2>
<p class="lead" data-i18n="blogHub.ctaText">{en_body["ctaText"]}</p>
<div class="btns">
<a class="btn btn-primary" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank"><span data-i18n="blogHub.btnWA">{en_body["btnWA"]}</span>{ARROW_SVG}</a>
<a class="btn btn-ghost" data-i18n="blogHub.btnContact" href="/contact/">{en_body["btnContact"]}</a>
</div>
</div>
</section>
</main>'''

    html = (
        head_html
        + "\n<body>\n"
        + HEADER_HTML
        + body
        + FOOTER_HTML
        + MODAL_HTML
        + f'\n<script defer="" src="/assets/main.js?v={CACHE_BUST}"></script>\n</body>\n</html>'
    )

    out = SITE_ROOT / "blog" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


def main():
    out = render_hub()
    print(f"  wrote {out.relative_to(SITE_ROOT)} ({out.stat().st_size:,} bytes)")
    print(f"\nDone. {1 + len(BLOG_POSTS)} Blog page(s) written.")


if __name__ == "__main__":
    main()

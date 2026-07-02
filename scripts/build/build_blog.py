#!/usr/bin/env python3
"""
Generate the Blog section:
  /blog/                     — hub for practical workshop articles.
  /blog/<slug>/              — individual workshop guides.

EN sources are generated here. build_i18n.py creates RU/UK/PT variants from
the inline ICM_I18N_PAGE payload, keeping SEO and structured data localized.
"""

import json
from html import escape
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
from hero_images import hero_background_css, hero_preload_links, optimized_hero_url


BLOG_CSS = """.subpage.blog-hub{padding:126px 0 58px}
.blog-hub .bg{position:absolute;inset:0;z-index:-1;background-size:cover;background-position:center;filter:saturate(.82) contrast(1.08) brightness(.46);""" + hero_background_css('/photos/lounge-1600.jpg') + """}
.blog-posts{padding:44px 0 12px;background:#0a0a0a;border-top:1px solid var(--border)}
.blog-grid{display:grid;grid-template-columns:1fr;gap:24px}
.blog-card{display:grid;grid-template-columns:1.2fr 1fr;gap:24px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;transition:border-color .25s var(--ease),transform .25s var(--ease)}
.blog-card:hover{border-color:var(--accent);transform:translateY(-2px)}
.blog-card .img{aspect-ratio:16/9;background-size:contain;background-repeat:no-repeat;background-position:center;background-color:#050505}
.blog-card .body{padding:34px 30px;display:flex;flex-direction:column;gap:14px;justify-content:center}
.blog-card .date{font-family:var(--font-ui);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.blog-card h3{font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(22px,2.2vw,32px);line-height:1.05;color:#fff}
.blog-card p{font-size:15px;color:var(--text-dim);max-width:50ch}
.blog-card .more{display:inline-flex;align-items:center;gap:8px;font-family:var(--font-ui);font-weight:600;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);margin-top:auto}
.blog-empty{padding:46px 28px;text-align:center;color:var(--text-dim);font-size:16px;border:1px solid var(--border);background:var(--surface);border-radius:var(--radius-lg)}
.blog-topics{padding:56px 0;background:#0a0a0a;border-top:1px solid var(--border)}
.blog-topics .heading{margin-bottom:34px;display:grid;grid-template-columns:1fr 1.4fr;gap:40px;align-items:end;padding-bottom:24px;border-bottom:1px solid var(--border)}
.blog-topics .heading h2{margin:0;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(24px,3.2vw,44px);line-height:.95;color:#fff}
.blog-topics .heading h2 em{color:var(--accent);font-style:italic}
.topic-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.topic-card{min-height:170px;padding:22px 20px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);display:flex;flex-direction:column;gap:14px}
.topic-card .num{font-family:var(--font-ui);font-size:11px;letter-spacing:.16em;color:var(--accent)}
.topic-card h3{font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:24px;line-height:1;color:#fff}
.topic-card p{font-size:14px;line-height:1.55;color:var(--text-dim)}
@media (max-width:1100px){.topic-grid{grid-template-columns:repeat(2,1fr)}.blog-topics .heading{grid-template-columns:1fr;gap:24px}}
@media (max-width:760px){.blog-card{grid-template-columns:1fr}.blog-card .img{aspect-ratio:16/9}.topic-grid{grid-template-columns:1fr}}"""

ARTICLE_CSS = """.subpage.blog-article{padding:0;position:relative;overflow:hidden;isolation:isolate;background:#0a0a0a;min-height:92vh;display:flex;align-items:flex-end}
.blog-article::before,.blog-article::after{display:none}
.blog-article .bg{position:absolute;inset:0;z-index:0;background-size:cover;background-position:center;filter:saturate(.88) contrast(1.08) brightness(.55)}
.blog-article .hero-media{position:absolute;inset:0;z-index:0;display:block;overflow:hidden}
.blog-article .hero-media img{display:block;width:100%;height:100%;object-fit:cover;filter:saturate(.88) contrast(1.08) brightness(.55)}
.blog-article .scrim{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(10,10,10,.92) 0%,rgba(10,10,10,.7) 42%,rgba(10,10,10,.18) 74%),linear-gradient(180deg,rgba(10,10,10,.30) 0%,rgba(10,10,10,.42) 48%,rgba(10,10,10,.96) 100%);pointer-events:none}
.blog-article .container{position:relative;z-index:2;padding-top:140px;padding-bottom:64px;width:100%;min-width:0}
.blog-article .date{font-family:var(--font-ui);font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);margin-bottom:18px}
.blog-article .crumb,.blog-article h1,.blog-article .lede,.blog-article-body h2,.blog-article-body p,.blog-list li,.blog-faq-item summary{overflow-wrap:anywhere}
.blog-article h1{font-family:var(--font-display);font-weight:800;line-height:.92;letter-spacing:0;text-transform:uppercase;font-size:clamp(30px,4vw,52px);color:#fff;max-width:min(20ch,100%);margin-bottom:24px}
.blog-article h1 .accent{color:var(--accent)}
.blog-article .lede{font-family:var(--font-ui);font-size:clamp(17px,1.45vw,21px);color:var(--text);max-width:min(66ch,100%);line-height:1.55}
.blog-article-body{padding:56px 0;background:#0a0a0a;border-top:1px solid var(--border)}
.blog-article-body .container{max-width:820px;min-width:0}
.blog-article-body section{padding:0;margin-bottom:34px}
.blog-article-body section:last-child{margin-bottom:0}
.blog-article-body h2{font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(22px,2.1vw,30px);line-height:1.04;color:#fff;margin-bottom:22px}
.blog-article-body p{font-family:var(--font-ui);font-size:clamp(16px,1.25vw,19px);line-height:1.66;color:var(--text);margin-bottom:18px}
.blog-article-body p:last-child{margin-bottom:0}
.blog-article-body a{color:var(--accent);text-decoration:none;border-bottom:1px solid rgba(255,87,34,.45);transition:border-color .2s var(--ease),color .2s var(--ease)}
.blog-article-body a:hover{border-bottom-color:var(--accent);color:#fff}
.blog-article-body .btn{border-bottom:0}
.blog-article-body .btn:hover{border-bottom:0}
.blog-article-body .btn-primary,.blog-article-body .btn-primary span{color:#fff}
.blog-article-body .btn-primary:hover,.blog-article-body .btn-primary:hover span{color:#fff}
.blog-article-body .blog-article-lead{padding:34px 36px;border:1px solid var(--border);border-left:3px solid var(--accent);background:var(--surface);border-radius:var(--radius-lg)}
.blog-list{display:grid;gap:12px;margin:0;padding:0;list-style:none}
.blog-list li{position:relative;padding-left:28px;font-family:var(--font-ui);font-size:clamp(16px,1.2vw,18px);line-height:1.6;color:var(--text)}
.blog-list li::before{content:"";position:absolute;left:0;top:.72em;width:9px;height:9px;border:2px solid var(--accent);border-radius:50%}
.blog-list.blog-ordered-list{counter-reset:blog-step}
.blog-list.blog-ordered-list li{counter-increment:blog-step;padding-left:34px}
.blog-list.blog-ordered-list li::before{content:counter(blog-step);top:.18em;width:22px;height:22px;border:1px solid rgba(255,87,34,.65);border-radius:50%;display:grid;place-items:center;font-family:var(--font-ui);font-weight:800;font-size:11px;line-height:1;color:var(--accent)}
.blog-media{margin:34px 0;padding:18px;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--surface)}
.blog-media picture{display:block}
.blog-media img{display:block;width:100%;height:auto;border-radius:calc(var(--radius-lg) - 4px)}
.blog-media figcaption{padding:14px 2px 0;font-family:var(--font-ui);font-size:13px;color:var(--text-mute);font-style:italic}
.blog-article-body .blog-video{display:grid;grid-template-columns:minmax(0,1fr) minmax(260px,360px);gap:28px;align-items:center;padding:34px 36px;border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--surface)}
.blog-video .video-copy{display:grid;gap:14px}
.blog-video .video-eyebrow{font-family:var(--font-ui);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.blog-video .video-frame{position:relative;aspect-ratio:9/16;overflow:hidden;border-radius:var(--radius);border:1px solid var(--border);background:#111}
.blog-video iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.blog-video a{color:var(--accent);font-family:var(--font-ui);font-weight:700;font-size:13px;letter-spacing:.08em;text-transform:uppercase;text-decoration:none}
.blog-faq{display:grid;gap:12px}
.blog-faq-item{border:1px solid var(--border);border-radius:var(--radius);background:var(--surface);overflow:hidden}
.blog-faq-item summary{cursor:pointer;padding:18px 20px;font-family:var(--font-display);font-weight:800;text-transform:uppercase;font-size:clamp(19px,2vw,25px);line-height:1.1;color:#fff}
.blog-faq-item .a{padding:0 20px 20px}
.blog-article-body .blog-cta-box{padding:34px 36px;border:1px solid var(--border);border-radius:var(--radius-lg);background:linear-gradient(135deg,rgba(255,87,34,.14),rgba(255,255,255,.03));text-align:left}
.blog-cta-box .btns{display:flex;gap:14px;flex-wrap:wrap;margin-top:24px}
@media (max-width:900px){.blog-video{grid-template-columns:1fr}.blog-video .video-frame{max-width:320px;margin:0 auto;width:100%}}
@media (max-width:760px){.blog-article{min-height:84vh}.blog-article .container{padding-top:112px}.blog-article .crumb{line-height:1.5}.blog-article .crumb span:last-child{flex-basis:100%;min-width:0}.blog-article-body{padding:44px 0}.blog-article-body section{margin-bottom:30px}.blog-article-body .blog-article-lead{padding:26px 24px}.blog-media{margin:28px -20px;border-left:none;border-right:none;border-radius:0}.blog-media img{border-radius:0}.blog-article-body .blog-video{margin-left:-20px;margin-right:-20px;padding:28px 20px;border-left:none;border-right:none;border-radius:0}.blog-article-body .blog-cta-box{margin-left:-20px;margin-right:-20px;padding:28px 20px;border-left:none;border-right:none;border-radius:0}}"""


def h(value):
    """Escape plain text for HTML text nodes while allowing existing markup elsewhere."""
    return escape(str(value), quote=False)


def a(value):
    """Escape plain text for HTML attributes."""
    return escape(str(value), quote=True)


def trusted_html(value):
    """Render repo-owned article copy that may contain intentional inline links."""
    return str(value)


def article_prefix(slug):
    return f"blog_{slug.replace('-', '_')}"


def article_image(article, num, size=1600):
    return f"{article['imageBase']}-{num:02d}-{size}.jpg"


def article_hero_image(article):
    return article.get("heroImage") or article_image(article, article["imageHero"])


def article_hero_dims(article):
    return article.get("heroImageDims") or article["imageDims"][article["imageHero"]]


def optimized_srcset(source_url, ext):
    return ", ".join(
        f"{optimized_hero_url(source_url, width, ext)} {width}w"
        for width in (768, 1280, 1920)
    )


def render_picture(source_url, alt, alt_key, dims, *, sizes, loading="lazy", fetchpriority=None, class_name=None):
    width, height = dims
    loading_attr = "" if loading is None else f' loading="{loading}"'
    fetch_attr = "" if fetchpriority is None else f' fetchpriority="{fetchpriority}"'
    class_attr = "" if class_name is None else f' class="{class_name}"'
    return f'''<picture{class_attr}>
<source sizes="{sizes}" srcset="{optimized_srcset(source_url, "avif")}" type="image/avif"/>
<source sizes="{sizes}" srcset="{optimized_srcset(source_url, "webp")}" type="image/webp"/>
<img alt="{a(alt)}" data-i18n-alt="{alt_key}" decoding="async"{fetch_attr} height="{height}" sizes="{sizes}" src="{optimized_hero_url(source_url, 1280, "jpg")}" srcset="{optimized_srcset(source_url, "jpg")}" width="{width}"{loading_attr}/>
</picture>'''


def render_media_figure(article, image_num, alt, alt_key, caption=None, caption_key=None):
    image_path = article_image(article, image_num)
    image_html = render_picture(
        image_path,
        alt,
        alt_key,
        article["imageDims"][image_num],
        sizes="(max-width: 860px) 100vw, 820px",
    )
    caption_html = ""
    if caption:
        caption_attr = f' data-i18n="{caption_key}"' if caption_key else ""
        caption_html = f'\n<figcaption{caption_attr}>{h(caption)}</figcaption>'
    return f'''<figure class="blog-media">
{image_html}{caption_html}
</figure>'''


def head(slug_for_url, lang, head_meta, json_ld_blocks, og_image=None, og_type="website", preload_html=""):
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
<meta content="max-image-preview:large" name="robots"/>
<title>{h(head_meta["title"])}</title>
<meta content="{a(head_meta["description"])}" name="description"/>
<link href="{canonical}" rel="canonical"/>
<meta content="{a(head_meta["title"])}" property="og:title"/>
<meta content="{a(head_meta["description"])}" property="og:description"/>
<meta content="{og_type}" property="og:type"/>
<meta content="{canonical}" property="og:url"/>
<meta content="Iron Custom Motors" property="og:site_name"/>
<meta content="{og_img}" property="og:image"/>
<meta content="1200" property="og:image:width"/>
<meta content="630" property="og:image:height"/>
<meta content="{OG_LOCALE[lang]}" property="og:locale"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{a(head_meta["title"])}" name="twitter:title"/>
<meta content="{a(head_meta["description"])}" name="twitter:description"/>
<meta content="{og_img}" name="twitter:image"/>
<link href="/photos/favicon.ico" rel="icon" sizes="any"/>
<link href="/photos/favicon-32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/photos/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="/photos/site.webmanifest" rel="manifest"/>
{preload_html}
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Saira:wght@300;400;500;600;700;800;900&amp;family=Saira+Condensed:wght@400;600;700;800;900&amp;family=Roboto+Condensed:wght@400;500;600;700;800;900&amp;family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="/assets/main.css?v={CACHE_BUST}" rel="stylesheet"/>
<style>
{SHARED_STYLES}
{BLOG_CSS}
{ARTICLE_CSS}
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

    posts_sorted = [
        item
        for _, item in sorted(
            enumerate(BLOG_POSTS.items()),
            key=lambda entry: (entry[1][1]["publishedISO"], entry[0]),
            reverse=True,
        )
    ]

    if posts_sorted:
        posts_html = ""
        for slug, data in posts_sorted:
            meta = data["meta"]["en"]
            body = data["body"]["en"]
            hero_img = article_hero_image(data)
            posts_html += f'''
<a class="blog-card" href="/blog/{slug}/">
<div class="img" style="{hero_background_css(hero_img, 768)}"></div>
<div class="body">
<div class="date" data-i18n="blogHub.{slug}.date">{h(body["publishedLabel"])}</div>
<h3 data-i18n="blogHub.{slug}.title">{h(body["h1Crumb"])}</h3>
<p data-i18n="blogHub.{slug}.excerpt">{h(meta["excerpt"])}</p>
<span class="more" data-i18n="blogHub.readMore">{h(en_body["readMore"])}</span>
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


def render_article(slug, article):
    en_meta = article["meta"]["en"]
    en_body = article["body"]["en"]
    pre = article_prefix(slug)
    page_url = f"{DOMAIN}/blog/{slug}/"
    hero_img_path = article_hero_image(article)
    hero_img_url = f"{DOMAIN}{hero_img_path}"
    images = [hero_img_url]
    images.extend(
        f"{DOMAIN}{article_image(article, num)}"
        for num in range(1, article["imageCount"] + 1)
    )
    images = list(dict.fromkeys(images))

    inline_i18n = {lang: {} for lang in LANGS}
    for lang in LANGS:
        body = article["body"][lang]
        for key in [
            "eyebrow", "publishedLabel", "breadHome", "breadBlog", "introTitle",
            "videoEyebrow", "videoTitle", "videoText", "videoLink", "faqTitle",
            "ctaEyebrow", "ctaTitle", "btnWA", "btnBack", "imageAlt",
            "imageCaption", "h1", "h1Crumb", "lede", "ctaText", "heroAlt",
        ]:
            if key in body:
                inline_i18n[lang][f"{pre}.{key}"] = body[key]
        if "intro" in body:
            inline_i18n[lang][f"{pre}.intro.title"] = body["intro"]["title"]
            for idx, paragraph in enumerate(body["intro"]["paragraphs"], start=1):
                inline_i18n[lang][f"{pre}.intro.p{idx}"] = paragraph
        for idx, section in enumerate(body.get("sections", []), start=1):
            inline_i18n[lang][f"{pre}.section{idx}.title"] = section["title"]
            for p_idx, paragraph in enumerate(section.get("paragraphs", []), start=1):
                inline_i18n[lang][f"{pre}.section{idx}.p{p_idx}"] = paragraph
            for b_idx, bullet in enumerate(section.get("bullets", []), start=1):
                inline_i18n[lang][f"{pre}.section{idx}.b{b_idx}"] = bullet
        for s_idx, section in enumerate(body.get("contentSections", []), start=1):
            if section.get("title"):
                inline_i18n[lang][f"{pre}.content{s_idx}.title"] = section["title"]
            for b_idx, block in enumerate(section.get("blocks", []), start=1):
                block_key = f"{pre}.content{s_idx}.block{b_idx}"
                if block["type"] == "image":
                    inline_i18n[lang][f"{block_key}.alt"] = block["alt"]
                    if block.get("caption"):
                        inline_i18n[lang][f"{block_key}.caption"] = block["caption"]
                elif block["type"] in ("ul", "ol"):
                    for item_idx, item in enumerate(block["items"], start=1):
                        inline_i18n[lang][f"{block_key}.item{item_idx}"] = item
                else:
                    inline_i18n[lang][f"{block_key}.text"] = block["text"]
        for idx, faq in enumerate(body["faqs"], start=1):
            inline_i18n[lang][f"{pre}.faq{idx}.q"] = faq["q"]
            inline_i18n[lang][f"{pre}.faq{idx}.a"] = faq["a"]

    faq_entities = [
        {
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {"@type": "Answer", "text": faq["a"]},
        }
        for faq in en_body["faqs"]
    ]

    blog_posting_schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": en_body["h1Crumb"],
        "description": en_meta["description"],
        "image": images,
        "datePublished": article["publishedISO"],
        "dateModified": article["modifiedISO"],
        "author": {"@id": f"{DOMAIN}/#business"},
        "publisher": {"@id": f"{DOMAIN}/#business"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": page_url},
        "url": page_url,
        "inLanguage": "en",
        "articleSection": "Workshop guides",
    }
    if article.get("keywords", {}).get("en"):
        blog_posting_schema["keywords"] = ", ".join(article["keywords"]["en"])
    if article.get("youtubeEmbed") and article.get("youtubeUrl"):
        video_schema = {
            "@type": "VideoObject",
            "name": en_body["videoTitle"],
            "description": en_body["videoText"],
            "thumbnailUrl": hero_img_url,
            "embedUrl": article["youtubeEmbed"],
            "url": article["youtubeUrl"],
            "inLanguage": "en",
        }
        if article.get("youtubeUploadDate"):
            video_schema["uploadDate"] = article["youtubeUploadDate"]
        blog_posting_schema["video"] = video_schema

    json_ld_blocks = [
        blog_posting_schema,
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_entities,
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{DOMAIN}/blog/"},
                {"@type": "ListItem", "position": 3, "name": en_body["h1Crumb"], "item": page_url},
            ],
        },
    ]

    head_html = head(
        f"blog/{slug}",
        "en",
        en_meta,
        json_ld_blocks,
        og_image=hero_img_url,
        og_type="article",
        preload_html=hero_preload_links(hero_img_path),
    ).replace(
        "window.ICM_I18N_PAGE = {};",
        f"window.ICM_I18N_PAGE = {json.dumps(inline_i18n, ensure_ascii=False)};",
    )

    def render_content_block(s_idx, b_idx, block):
        block_key = f"{pre}.content{s_idx}.block{b_idx}"
        if block["type"] == "p":
            return f'<p data-i18n="{block_key}.text">{trusted_html(block["text"])}</p>'
        if block["type"] in ("ul", "ol"):
            items = "\n".join(
                f'<li data-i18n="{block_key}.item{item_idx}">{trusted_html(item)}</li>'
                for item_idx, item in enumerate(block["items"], start=1)
            )
            tag = "ol" if block["type"] == "ol" else "ul"
            class_name = "blog-list blog-ordered-list" if block["type"] == "ol" else "blog-list"
            return f'<{tag} class="{class_name}">\n{items}\n</{tag}>'
        if block["type"] == "image":
            return render_media_figure(
                article,
                block["image"],
                block["alt"],
                f"{block_key}.alt",
                caption=block.get("caption"),
                caption_key=f"{block_key}.caption",
            )
        raise ValueError(f"Unsupported blog content block type: {block['type']}")

    def render_content_sections(indexed_sections=None):
        if indexed_sections is None:
            indexed_sections = list(enumerate(en_body["contentSections"], start=1))
        section_parts = []
        for s_idx, section in indexed_sections:
            title = section.get("title")
            class_name = section.get("className", "")
            class_attr = f' class="{a(class_name)}"' if class_name else ""
            title_html = ""
            if title:
                title_html = f'<h2 data-i18n="{pre}.content{s_idx}.title">{h(title)}</h2>\n'
            block_html = "\n".join(
                render_content_block(s_idx, b_idx, block)
                for b_idx, block in enumerate(section.get("blocks", []), start=1)
            )
            section_parts.append(f'''<section{class_attr}>
{title_html}{block_html}
</section>''')
        return "\n\n".join(section_parts)

    if "contentSections" in en_body:
        indexed_content_sections = list(enumerate(en_body["contentSections"], start=1))
        article_cta_html = ""
        if indexed_content_sections and indexed_content_sections[-1][1].get("className") == "blog-cta-box":
            article_cta_html = render_content_sections([indexed_content_sections[-1]])
            indexed_content_sections = indexed_content_sections[:-1]
        article_body_main = render_content_sections(indexed_content_sections)
    else:
        intro_paragraphs = "\n".join(
            f'<p data-i18n="{pre}.intro.p{idx}">{trusted_html(paragraph)}</p>'
            for idx, paragraph in enumerate(en_body["intro"]["paragraphs"], start=1)
        )

        section_parts = []
        for idx, section in enumerate(en_body["sections"], start=1):
            paragraph_html = "\n".join(
                f'<p data-i18n="{pre}.section{idx}.p{p_idx}">{trusted_html(paragraph)}</p>'
                for p_idx, paragraph in enumerate(section.get("paragraphs", []), start=1)
            )
            if "bullets" in section:
                bullets = "\n".join(
                    f'<li data-i18n="{pre}.section{idx}.b{b_idx}">{trusted_html(bullet)}</li>'
                    for b_idx, bullet in enumerate(section["bullets"], start=1)
                )
                list_html = f'<ul class="blog-list">\n{bullets}\n</ul>'
                section_body = "\n".join(part for part in [paragraph_html, list_html] if part)
            else:
                section_body = paragraph_html
            section_parts.append(f'''<section>
<h2 data-i18n="{pre}.section{idx}.title">{h(section["title"])}</h2>
{section_body}
</section>''')
        sections_html = "\n\n".join(section_parts)

        media_html = render_media_figure(
            article,
            article["imageHero"],
            en_body["imageAlt"],
            f"{pre}.imageAlt",
            caption=en_body.get("imageCaption"),
            caption_key=f"{pre}.imageCaption",
        )

        video_html = ""
        if article.get("youtubeEmbed") and article.get("youtubeUrl"):
            video_html = f'''
<section class="blog-video">
<div class="video-copy">
<span class="video-eyebrow" data-i18n="{pre}.videoEyebrow">{h(en_body["videoEyebrow"])}</span>
<h2 data-i18n="{pre}.videoTitle">{h(en_body["videoTitle"])}</h2>
<p data-i18n="{pre}.videoText">{h(en_body["videoText"])}</p>
<a data-i18n="{pre}.videoLink" href="{article["youtubeUrl"]}" rel="noopener" target="_blank">{h(en_body["videoLink"])}</a>
</div>
<div class="video-frame">
<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" loading="lazy" src="{article["youtubeEmbed"]}" title="{a(en_body["videoTitle"])}" data-i18n-title="{pre}.videoTitle"></iframe>
</div>
</section>'''

        article_cta_html = f'''<section class="blog-cta-box">
<span class="h-eyebrow" data-i18n="{pre}.ctaEyebrow">{h(en_body["ctaEyebrow"])}</span>
<h2 data-i18n="{pre}.ctaTitle">{h(en_body["ctaTitle"])}</h2>
<p data-i18n="{pre}.ctaText">{trusted_html(en_body["ctaText"])}</p>
<div class="btns">
<a class="btn btn-primary" data-wa="" href="https://wa.me/351917961230" rel="noopener" target="_blank"><span data-i18n="{pre}.btnWA">{h(en_body["btnWA"])}</span>{ARROW_SVG}</a>
<a class="btn btn-ghost" data-i18n="{pre}.btnBack" href="/blog/">{h(en_body["btnBack"])}</a>
</div>
</section>'''

        article_body_main = f'''<section class="blog-article-lead">
<h2 data-i18n="{pre}.intro.title">{h(en_body["intro"]["title"])}</h2>
{intro_paragraphs}
</section>

{media_html}

{video_html}

{sections_html}'''

    faq_html = "\n".join(
        f'''<details class="blog-faq-item">
<summary class="q" data-i18n="{pre}.faq{idx}.q">{h(faq["q"])}</summary>
<div class="a"><p data-i18n="{pre}.faq{idx}.a">{h(faq["a"])}</p></div>
</details>'''
        for idx, faq in enumerate(en_body["faqs"], start=1)
    )
    hero_alt_text = en_body.get("heroAlt", en_body.get("imageAlt", en_body["h1Crumb"]))
    hero_alt_key = f"{pre}.heroAlt" if "heroAlt" in en_body else f"{pre}.imageAlt"

    body = f'''<main>
<article>
<section class="subpage blog-article">
{render_picture(hero_img_path, hero_alt_text, hero_alt_key, article_hero_dims(article), sizes="100vw", loading=None, fetchpriority="high", class_name="hero-media")}
<div aria-hidden="true" class="scrim"></div>
<div class="container">
<div class="crumb"><a data-i18n="{pre}.breadHome" href="/">Home</a><span class="sep">→</span><a data-i18n="{pre}.breadBlog" href="/blog/">Blog</a><span class="sep">→</span><span data-i18n="{pre}.h1Crumb">{h(en_body["h1Crumb"])}</span></div>
<div class="date" data-i18n="{pre}.eyebrow">{h(en_body["eyebrow"])}</div>
<h1 data-i18n="{pre}.h1">{en_body["h1"]}</h1>
<p class="lede" data-i18n="{pre}.lede">{trusted_html(en_body["lede"])}</p>
</div>
</section>

<section class="blog-article-body">
<div class="container">
{article_body_main}

<section>
<h2 data-i18n="{pre}.faqTitle">{h(en_body["faqTitle"])}</h2>
<div class="blog-faq">
{faq_html}
</div>
</section>

{article_cta_html}
</div>
</section>
</article>
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

    out = SITE_ROOT / "blog" / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


def main():
    outputs = [render_hub()]
    for slug, article in sorted(BLOG_POSTS.items()):
        outputs.append(render_article(slug, article))
    for out in outputs:
        print(f"  wrote {out.relative_to(SITE_ROOT)} ({out.stat().st_size:,} bytes)")
    print(f"\nDone. {len(outputs)} Blog page(s) written.")


if __name__ == "__main__":
    main()

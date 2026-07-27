#!/usr/bin/env python3
"""Build data-driven project pages in the existing project-page family."""

from __future__ import annotations

import json
from pathlib import Path

from bs4 import BeautifulSoup
from PIL import Image

from project_pages_data import PROJECT_CONFIGS, load_project


SITE_ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"
TEMPLATE_PATH = SITE_ROOT / "projects/joker/index.html"


def upsert_meta(soup: BeautifulSoup, *, name: str | None = None, prop: str | None = None, content: str):
    attrs = {"name": name} if name else {"property": prop}
    tag = soup.head.find("meta", attrs=attrs)
    if tag is None:
        tag = soup.new_tag("meta")
        tag.attrs.update(attrs)
        soup.head.append(tag)
    tag["content"] = content


def upsert_link(soup: BeautifulSoup, rel: str, href: str):
    tag = soup.head.find("link", attrs={"rel": rel})
    if tag is None:
        tag = soup.new_tag("link")
        tag["rel"] = rel
        soup.head.append(tag)
    tag["href"] = href
    return tag


def image_dimensions(path: str) -> tuple[int, int]:
    with Image.open(SITE_ROOT / path.lstrip("/")) as image:
        return image.size


def page_i18n(project: dict) -> dict:
    slug = project["slug"]
    payload = {}
    for lang in ["en", "ru", "uk", "pt"]:
        content = project["content"][lang]
        ui = project["ui"][lang]
        values = {
            f"proj.{slug}.name": content["h1"],
            f"proj.{slug}.subtitle": f"<em>{content['subtitle']}</em>",
            f"proj.{slug}.heroAlt": content["hero_alt"],
            f"proj.{slug}.body": content["body_html"],
            f"proj.{slug}.closing": content["closing_html"],
            f"proj.{slug}.badge": ui["badge"],
            f"proj.{slug}.cat": ui["category"],
            f"proj.{slug}.where": ui["where"],
            "proj.breadHome": ui["home"],
            "proj.breadProjects": ui["projects"],
            "proj.lblYear": ui["year_label"],
            "proj.lblCategory": ui["category_label"],
            "proj.lblWhere": ui["where_label"],
            "proj.lblGallery": ui["gallery"],
            f"proj.{slug}.galleryTitle": ui["gallery_title"],
        }
        for index, alt in enumerate(project["gallery_alts"][lang], start=1):
            values[f"proj.{slug}.galleryAlt{index}"] = alt
        payload[lang] = values
    return payload


def picture_html(base: str, widths: list[int], *, alt_key: str, alt: str, hero: bool = False) -> str:
    candidates = []
    for width in widths:
        dimensions = image_dimensions(f"{base}-{width}.webp")
        candidates.append((width, dimensions))
    largest_width, (largest_w, largest_h) = candidates[-1]
    srcset_avif = ", ".join(f"{base}-{width}.avif {width}w" for width, _ in candidates)
    srcset_webp = ", ".join(f"{base}-{width}.webp {width}w" for width, _ in candidates)
    sizes = "100vw" if hero else "(max-width:760px) 50vw, 25vw"
    picture_class = ' class="bg"' if hero else ""
    hero_attrs = ' decoding="async" fetchpriority="high"' if hero else ' decoding="async" loading="lazy"'
    return f'''<picture{picture_class}>
<source srcset="{srcset_avif}" sizes="{sizes}" type="image/avif"/>
<source srcset="{srcset_webp}" sizes="{sizes}" type="image/webp"/>
<img alt="{alt}" data-i18n-alt="{alt_key}"{hero_attrs} height="{largest_h}" sizes="{sizes}" src="{base}-{largest_width}.webp" srcset="{srcset_webp}" width="{largest_w}"/>
</picture>'''


def render_main(project: dict, i18n: dict) -> str:
    slug = project["slug"]
    en = project["content"]["en"]
    ui = project["ui"]["en"]
    hero = picture_html(
        project["hero_base"],
        [800, 1600, 2400],
        alt_key=f"proj.{slug}.heroAlt",
        alt=en["hero_alt"],
        hero=True,
    )
    gallery = []
    for index, alt in enumerate(project["gallery_alts"]["en"], start=1):
        image = picture_html(
            f"{project['gallery_base']}-{index:02d}",
            [800, 1600],
            alt_key=f"proj.{slug}.galleryAlt{index}",
            alt=alt,
        )
        gallery.append(f'<div class="gtile">{image}</div>')

    return f'''<main>
<section class="subpage">
{hero}
<div class="container">
<div class="crumb"><a data-i18n="proj.breadHome" href="/">{ui["home"]}</a><span class="sep">→</span><a data-i18n="proj.breadProjects" href="/projects/">{ui["projects"]}</a><span class="sep">→</span><span data-i18n="proj.{slug}.name">{en["h1"]}</span></div>
<span class="proj-badge" data-i18n="proj.{slug}.badge">{ui["badge"]}</span>
<h1 class="reveal" data-i18n="proj.{slug}.name">{en["h1"]}</h1>
<p class="tagline reveal" data-i18n-html="proj.{slug}.subtitle"><em>{en["subtitle"]}</em></p>
<div class="proj-meta">
<div class="item"><span class="label" data-i18n="proj.lblYear">{ui["year_label"]}</span><span class="val">{project["year"]}</span></div>
<div class="item"><span class="label" data-i18n="proj.lblCategory">{ui["category_label"]}</span><span class="val" data-i18n="proj.{slug}.cat">{ui["category"]}</span></div>
<div class="item"><span class="label" data-i18n="proj.lblWhere">{ui["where_label"]}</span><span class="val" data-i18n="proj.{slug}.where">{ui["where"]}</span></div>
</div>
</div>
</section>
<section class="sub-section">
<div class="container">
<article class="proj-story generated-project-story reveal" data-i18n-html="proj.{slug}.body">{en["body_html"]}</article>
</div>
</section>
<section class="sub-section">
<div class="container">
<div class="heading reveal">
<span class="h-eyebrow" data-i18n="proj.lblGallery">{ui["gallery"]}</span>
<div><h2 data-i18n-html="proj.{slug}.galleryTitle">{ui["gallery_title"]}</h2></div>
</div>
<div class="proj-gallery reveal-stagger">
{"".join(gallery)}
</div>
</div>
</section>
<section class="cta-back generated-project-closing">
<div class="container">
<div class="lead" data-i18n-html="proj.{slug}.closing">{en["closing_html"]}</div>
</div>
</section>
</main>'''


def schema_blocks(project: dict) -> list[dict]:
    slug = project["slug"]
    en = project["content"]["en"]
    page_url = f"{DOMAIN}/projects/{slug}/"
    hero_url = f"{DOMAIN}{project['hero_base']}-2400.webp"
    hero_width, hero_height = image_dimensions(f"{project['hero_base']}-2400.webp")
    return [
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "@id": f"{page_url}#article",
            "headline": en["h1"],
            "description": en["description"],
            "image": {
                "@type": "ImageObject",
                "url": hero_url,
                "width": hero_width,
                "height": hero_height,
            },
            "datePublished": project["published_iso"],
            "dateModified": project["published_iso"],
            "inLanguage": "en",
            "author": {
                "@type": "Organization",
                "name": "Iron Custom Motors",
                "url": f"{DOMAIN}/about/",
            },
            "publisher": {
                "@type": "LocalBusiness",
                "@id": f"{DOMAIN}/#business",
                "name": "Iron Custom Motors",
                "logo": {
                    "@type": "ImageObject",
                    "url": f"{DOMAIN}/photos/icon-512.png",
                    "width": 512,
                    "height": 512,
                },
            },
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": page_url,
                "name": en["h1"],
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": project["ui"]["en"]["home"],
                    "item": f"{DOMAIN}/",
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": project["ui"]["en"]["projects"],
                    "item": f"{DOMAIN}/projects/",
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": en["h1"],
                    "item": page_url,
                },
            ],
        },
    ]


def render_project(slug: str) -> Path:
    project = load_project(slug)
    if len(project["gallery_sources"]) != len(project["gallery_alts"]["en"]):
        raise ValueError(f"Gallery source/alt count mismatch for {slug}")

    soup = BeautifulSoup(TEMPLATE_PATH.read_text(encoding="utf-8"), "html.parser")
    en = project["content"]["en"]
    page_url = f"{DOMAIN}/projects/{slug}/"
    image_url = f"{DOMAIN}{project['hero_base']}-2400.webp"

    soup.title.string = en["title"]
    upsert_meta(soup, name="description", content=en["description"])
    upsert_meta(soup, prop="og:title", content=en["title"])
    upsert_meta(soup, prop="og:description", content=en["description"])
    upsert_meta(soup, prop="og:type", content="article")
    upsert_meta(soup, prop="og:url", content=page_url)
    upsert_meta(soup, prop="og:image", content=image_url)
    upsert_meta(soup, name="twitter:title", content=en["title"])
    upsert_meta(soup, name="twitter:description", content=en["description"])
    upsert_meta(soup, name="twitter:image", content=image_url)
    upsert_link(soup, "canonical", page_url)

    for preload in soup.head.find_all("link", attrs={"rel": "preload", "as": "image"}):
        preload.decompose()
    preload = soup.new_tag("link")
    preload["rel"] = "preload"
    preload["as"] = "image"
    preload["href"] = f"{project['hero_base']}-1600.avif"
    preload["type"] = "image/avif"
    preload["imagesrcset"] = ", ".join(
        f"{project['hero_base']}-{width}.avif {width}w" for width in [800, 1600, 2400]
    )
    preload["imagesizes"] = "100vw"
    preload["fetchpriority"] = "high"
    soup.head.append(preload)

    style = soup.head.find("style")
    style.string = (style.string or "") + """
.subpage picture.bg{position:absolute;inset:0;z-index:-1;display:block;filter:none;transform:none}
.subpage picture.bg img{width:100%;height:100%;object-fit:cover;object-position:center;filter:saturate(.85) contrast(1.05) brightness(.45)}
.generated-project-story{max-width:900px}
.generated-project-story h2{font-family:var(--font-display);font-size:clamp(26px,3vw,40px);font-weight:800;line-height:1.05;text-transform:uppercase;color:#fff;margin:44px 0 18px}
.generated-project-story h2:first-child{margin-top:0}
.generated-project-closing .lead{max-width:900px}
.generated-project-closing .lead p{margin:0;color:var(--text);font-size:clamp(17px,1.6vw,21px);line-height:1.65}
.generated-project-closing .lead a{color:var(--accent)}
.proj-gallery picture{display:block;width:100%;height:100%}
"""

    main = soup.find("main")
    new_main = BeautifulSoup(render_main(project, page_i18n(project)), "html.parser").main
    main.replace_with(new_main)

    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        script.decompose()
    for block in schema_blocks(project):
        script = soup.new_tag("script")
        script["type"] = "application/ld+json"
        script.string = json.dumps(block, ensure_ascii=False, separators=(",", ":"))
        soup.head.append(script)

    i18n_script = None
    for script in soup.find_all("script"):
        if "window.ICM_I18N_PAGE" in (script.string or ""):
            i18n_script = script
            break
    if i18n_script is None:
        i18n_script = soup.new_tag("script")
        soup.body.append(i18n_script)
    i18n_script.string = (
        "window.ICM_I18N_PAGE = "
        + json.dumps(page_i18n(project), ensure_ascii=False, separators=(",", ":"))
        + ";"
    )

    output = SITE_ROOT / "projects" / slug / "index.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(str(soup), encoding="utf-8")
    print(f"wrote {output.relative_to(SITE_ROOT)}")
    return output


def main():
    for slug in PROJECT_CONFIGS:
        render_project(slug)


if __name__ == "__main__":
    main()

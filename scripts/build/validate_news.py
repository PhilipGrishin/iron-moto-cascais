#!/usr/bin/env python3
"""Verify approved Markdown News copy, gallery delivery and related selections."""

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

from build_news import article_hero_path, format_gallery_alt, related_article_items
from hero_images import picture_hero_preload_alignment
from news_data import NEWS_ARTICLES

ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://ironcustommotors.com"


def text(value):
    return " ".join(BeautifulSoup(str(value), "html.parser").get_text(" ", strip=True).split())


def validate():
    errors = []
    pages = 0
    for slug, article in NEWS_ARTICLES.items():
        for lang in ("en", "pt", "ru", "uk"):
            prefix = "" if lang == "en" else f"{lang}/"
            path = ROOT / prefix / "news" / slug / "index.html"
            soup = BeautifulSoup(path.read_text(), "html.parser")

            def check(condition, message):
                if not condition:
                    errors.append(f"{path.relative_to(ROOT)}: {message}")

            expected_related = {
                f"/{prefix}news/{other}/" for other, _ in related_article_items(slug, article)
            }
            actual_related = {
                link["href"] for link in soup.select('.news-related-card a[href]')
                if "/news/" in link["href"]
            }
            check(actual_related == expected_related, "related News selection differs from registry")
            if not article.get("sourceBacked"):
                continue
            pages += 1
            body = article["body"][lang]
            meta = article["meta"][lang]
            check(len(soup.select("h1")) == 1, "expected one H1")
            check(text(soup.h1) == text(body["h1"]), "H1 differs from approved copy")
            check(soup.title.string == meta["title"], "SEO title differs from approved copy")
            check(soup.select_one('meta[name="description"]')["content"] == meta["description"], "meta description differs from approved copy")
            expected_units = [text(body["lede"])] + [
                text(value) for key, value in body.items() if re.fullmatch(r"s\d+\.(h2|p\d+)", key)
            ]
            actual_units = [text(soup.select_one(".lede"))] + [
                text(node) for node in soup.select(".article-body .container > section > h2, .article-body .container > section > p")
            ]
            check(actual_units == expected_units, "whole article copy or order differs from approved source")
            gallery = soup.select_one(".news-gallery-shell")
            preceding = gallery.find_previous_sibling("section")
            check(text(preceding.h2) == text(body["s2.h2"]), "gallery is not after section two")
            images = gallery.select("img")
            check([image.get("alt") for image in images] == [
                format_gallery_alt(body["gallery.altPattern"], number)
                for number in range(1, article["galleryCount"] + 1)
            ], "gallery ALT/order differs from approved pattern")
            check(all(image.get("loading") == "lazy" for image in images), "gallery must remain lazy")
            check(all(image.get("width") and image.get("height") for image in images), "gallery dimensions missing")
            canonical = f"{DOMAIN}/{prefix}news/{slug}/"
            check(soup.select_one('link[rel="canonical"]')["href"] == canonical, "canonical mismatch")
            check(len(soup.select("link[hreflang]")) == 5, "incomplete hreflang set")
            check(soup.select_one('meta[property="og:image"]')["content"] == DOMAIN + article_hero_path(article), "social image differs from hero")
            schemas = [json.loads(node.string) for node in soup.select('script[type="application/ld+json"]')]
            news = next(item for item in schemas if item.get("@type") == "NewsArticle")
            check(news["datePublished"] == article["publishedISO"], "publication date mismatch")
            check(news["dateModified"] == article["modifiedISO"], "modified date mismatch")
            check(len(news["image"]) == 1 + article["galleryCount"], "schema image inventory mismatch")
            if article.get("projectMedia"):
                picture, issues = picture_hero_preload_alignment(soup)
                check(picture is not None and not issues, f"responsive hero alignment: {issues}")
                check(len(soup.select('[fetchpriority="high"]')) == 1, "expected one high-priority hero")
                check(picture.img["alt"] == body["heroAlt"], "hero ALT differs from approved source")
                for number, image in enumerate(images, 1):
                    check(image["src"] == f"{article['galleryBase']}-{number:02d}-1600.jpg", "gallery no longer reuses project media")
    return pages, errors


if __name__ == "__main__":
    pages, errors = validate()
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(f"News validation passed: {pages} approved-source variants and all related selections.")

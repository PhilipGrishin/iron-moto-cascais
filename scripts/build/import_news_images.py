#!/usr/bin/env python3
"""Import registered News hero and gallery photos as responsive assets."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps

from news_data import NEWS_ARTICLES
from optimize_hero_images import optimize_source


SITE_ROOT = Path(__file__).resolve().parents[2]


def resize_to_width(image: Image.Image, width: int) -> Image.Image:
    if image.width <= width:
        return image.copy()
    height = round(image.height * width / image.width)
    return image.resize((width, height), Image.Resampling.LANCZOS)


def save_jpeg(image: Image.Image, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, "JPEG", quality=88, optimize=True, progressive=True)


def save_gallery_variants(image: Image.Image, base_path: Path) -> None:
    base_path.parent.mkdir(parents=True, exist_ok=True)
    for width in (800, 1600):
        resized = resize_to_width(image, width)
        outputs = {
            "avif": base_path.with_name(f"{base_path.name}-{width}.avif"),
            "webp": base_path.with_name(f"{base_path.name}-{width}.webp"),
            "jpg": base_path.with_name(f"{base_path.name}-{width}.jpg"),
        }
        resized.save(outputs["avif"], "AVIF", quality=68, speed=6)
        resized.save(outputs["webp"], "WEBP", quality=86, method=6)
        save_jpeg(resized, outputs["jpg"])
        names = ", ".join(str(path.relative_to(SITE_ROOT)) for path in outputs.values())
        print(f"wrote {names} ({resized.width}x{resized.height})")


def import_news_images(slug: str, source_dir: Path) -> None:
    article = NEWS_ARTICLES[slug]
    if not article.get("heroSource") or not article.get("gallerySources"):
        raise ValueError(f"News article has no registered media delivery: {slug}")

    hero_source = source_dir / article["heroSource"]
    if not hero_source.exists():
        raise FileNotFoundError(hero_source)
    with Image.open(hero_source) as raw:
        hero = ImageOps.exif_transpose(raw).convert("RGB")
        for width in (800, 1600):
            output = SITE_ROOT / f"{article['imageBase'].lstrip('/')}-01-{width}.jpg"
            resized = resize_to_width(hero, width)
            save_jpeg(resized, output)
            print(f"wrote {output.relative_to(SITE_ROOT)} ({resized.width}x{resized.height})")

    hero_messages = optimize_source(f"{article['imageBase'].lstrip('/')}-01-1600.jpg")
    for message in hero_messages:
        print(message)

    gallery_base = SITE_ROOT / article["galleryBase"].lstrip("/")
    for index, filename in enumerate(article["gallerySources"], start=1):
        source = source_dir / filename
        if not source.exists():
            raise FileNotFoundError(source)
        output_base = gallery_base.with_name(f"{gallery_base.name}-{index:02d}")
        with Image.open(source) as raw:
            image = ImageOps.exif_transpose(raw).convert("RGB")
            save_gallery_variants(image, output_base)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "slug",
        choices=sorted(
            slug for slug, article in NEWS_ARTICLES.items()
            if article.get("heroSource") and article.get("gallerySources")
        ),
    )
    parser.add_argument("source_dir", type=Path)
    args = parser.parse_args()
    import_news_images(args.slug, args.source_dir)


if __name__ == "__main__":
    main()

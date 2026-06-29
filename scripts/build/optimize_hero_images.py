#!/usr/bin/env python3
"""Generate responsive AVIF/WebP/JPEG hero background variants."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from brand_pages_data import BRAND_CONFIG
from hero_images import HERO_IMAGE_FORMATS, HERO_IMAGE_WIDTHS, hero_image_slug

SITE_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = SITE_ROOT / "photos" / "optimized"

DEFAULT_HERO_SOURCES = [
    "photos/hero.jpg",
    "photos/service-action.jpg",
    "photos/mechanic.jpg",
    "photos/parts-shelf.jpg",
    "photos/why-engine.jpg",
    "photos/lounge.jpg",
    "photos/team.jpg",
    "photos/exterior.jpg",
    "photos/services/english-speaking-motorcycle-workshop-main.jpg",
    "photos/projects/inspirium-hero-2400.jpg",
    "photos/news/news-opening-01-1600.jpg",
    "photos/news/news-lmff2026-01-1600.jpg",
    "photos/news/news-ericeira-kustom-fest-2026-01-1600.jpg",
    "photos/blog/blog-revtech-110-oil-service-01-1600.jpg",
    "photos/blog/blog-motorcycle-brake-pad-replacement-cascais-01-1600.jpg",
    "photos/blog/blog-front-fork-service-motorcycle-cascais-01-1600.jpg",
    "photos/blog/blog-motorcycle-tyre-fitting-specialist-cascais-01-1600.jpg",
]
HERO_SOURCES = list(
    dict.fromkeys(
        [
            *DEFAULT_HERO_SOURCES,
            *[config["hero"].lstrip("/") for config in BRAND_CONFIG.values()],
        ]
    )
)


try:
    from PIL import Image, ImageOps
except ImportError as exc:
    raise SystemExit(
        "Pillow is required. Use the bundled Codex Python runtime or install Pillow locally."
    ) from exc


def resized_rgb(source: Image.Image, target_width: int) -> Image.Image:
    image = ImageOps.exif_transpose(source).convert("RGB")
    if image.width <= target_width:
        return image.copy()
    target_height = round(image.height * target_width / image.width)
    return image.resize((target_width, target_height), Image.Resampling.LANCZOS)


def save_variant(image: Image.Image, output: Path, ext: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if ext == "avif":
        image.save(output, format="AVIF", quality=48, speed=6)
    elif ext == "webp":
        image.save(output, format="WEBP", quality=76, method=6)
    elif ext == "jpg":
        image.save(output, format="JPEG", quality=76, optimize=True, progressive=True)
    else:
        raise ValueError(f"Unsupported format: {ext}")


def optimize_source(relative_path: str) -> list[str]:
    source_path = SITE_ROOT / relative_path
    if not source_path.exists():
        return [f"missing source: {relative_path}"]

    slug = hero_image_slug(relative_path)
    messages = []
    with Image.open(source_path) as source:
        for width in HERO_IMAGE_WIDTHS:
            image = resized_rgb(source, width)
            for ext in HERO_IMAGE_FORMATS:
                output = OUTPUT_DIR / f"{slug}-{width}.{ext}"
                save_variant(image, output, ext)
            messages.append(f"{slug}-{width}: {image.width}x{image.height}")
    return messages


def requested_sources(values: list[str]) -> list[str]:
    if not values:
        return HERO_SOURCES

    sources: list[str] = []
    for value in values:
        if value in BRAND_CONFIG:
            sources.append(BRAND_CONFIG[value]["hero"].lstrip("/"))
        else:
            sources.append(value.lstrip("/"))
    return list(dict.fromkeys(sources))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate responsive AVIF/WebP/JPEG hero background variants."
    )
    parser.add_argument(
        "sources",
        nargs="*",
        help="Optional brand slug or source image path. Defaults to all configured hero images.",
    )
    args = parser.parse_args()

    all_messages: list[str] = []
    for relative_path in requested_sources(args.sources):
        all_messages.extend(optimize_source(relative_path))
    for message in all_messages:
        print(message)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Import project photos as responsive AVIF and WebP assets."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps

from project_pages_data import PROJECT_CONFIGS


SITE_ROOT = Path(__file__).resolve().parents[2]


def resize_to_width(image: Image.Image, width: int) -> Image.Image:
    height = round(image.height * width / image.width)
    return image.resize((width, height), Image.Resampling.LANCZOS)


def save_variants(image: Image.Image, base_path: Path, widths: list[int]):
    for width in widths:
        resized = resize_to_width(image, width)
        webp_path = base_path.with_name(f"{base_path.name}-{width}.webp")
        avif_path = base_path.with_name(f"{base_path.name}-{width}.avif")
        resized.save(webp_path, "WEBP", quality=86, method=6)
        resized.save(avif_path, "AVIF", quality=68, speed=6)
        print(
            f"wrote {webp_path.relative_to(SITE_ROOT)} and "
            f"{avif_path.relative_to(SITE_ROOT)} ({resized.width}x{resized.height})"
        )


def import_project(slug: str, source_dir: Path):
    config = PROJECT_CONFIGS[slug]
    hero_source = source_dir / config["hero_source"]
    if not hero_source.exists():
        raise FileNotFoundError(hero_source)

    hero_base = SITE_ROOT / config["hero_base"].lstrip("/")
    hero_base.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(hero_source) as raw:
        hero = ImageOps.exif_transpose(raw).convert("RGB")
        save_variants(hero, hero_base, [800, 1600, 2400])

    gallery_base = SITE_ROOT / config["gallery_base"].lstrip("/")
    gallery_base.parent.mkdir(parents=True, exist_ok=True)
    for index, filename in enumerate(config["gallery_sources"], start=1):
        source = source_dir / filename
        if not source.exists():
            raise FileNotFoundError(source)
        output_base = gallery_base.with_name(f"{gallery_base.name}-{index:02d}")
        with Image.open(source) as raw:
            image = ImageOps.exif_transpose(raw).convert("RGB")
            save_variants(image, output_base, [800, 1600])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", choices=sorted(PROJECT_CONFIGS))
    parser.add_argument("source_dir", type=Path)
    args = parser.parse_args()
    import_project(args.slug, args.source_dir)


if __name__ == "__main__":
    main()

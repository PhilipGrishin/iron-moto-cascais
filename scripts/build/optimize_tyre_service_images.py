#!/usr/bin/env python3
"""Generate responsive AVIF/WebP/JPEG variants for the tyre-service page."""

from __future__ import annotations

from pathlib import Path

from hero_images import HERO_IMAGE_FORMATS, HERO_IMAGE_WIDTHS, hero_image_slug

SITE_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = SITE_ROOT / "photos" / "optimized"

SOURCES = [
    "photos/services/motorcycle-tyre-service-workshop-cascais.jpg",
    "photos/services/motorcycle-specific-tyre-changer.jpg",
    "photos/services/wide-fat-motorcycle-tyre-400mm.jpg",
    "photos/services/spoked-wheel-tyre-fitting-cascais.jpg",
    "photos/services/motorcycle-wheel-balancing-fat-tyre.jpg",
    "photos/services/motorcycle-wheel-balancing-wide-tyre.jpg",
]

try:
    from PIL import Image, ImageOps
except ImportError as exc:
    raise SystemExit("Pillow is required to optimize tyre-service images.") from exc


def resized_rgb(source: Image.Image, target_width: int) -> Image.Image:
    image = ImageOps.exif_transpose(source).convert("RGB")
    if image.width <= target_width:
        return image.copy()
    target_height = round(image.height * target_width / image.width)
    return image.resize((target_width, target_height), Image.Resampling.LANCZOS)


def save_variant(image: Image.Image, output: Path, ext: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if ext == "avif":
        image.save(output, format="AVIF", quality=50, speed=6)
    elif ext == "webp":
        image.save(output, format="WEBP", quality=78, method=6)
    elif ext == "jpg":
        image.save(output, format="JPEG", quality=78, optimize=True, progressive=True)
    else:
        raise ValueError(f"Unsupported format: {ext}")


def optimize_source(relative_path: str) -> list[str]:
    source_path = SITE_ROOT / relative_path
    if not source_path.exists():
        return [f"missing source: {relative_path}"]

    messages: list[str] = []
    slug = hero_image_slug(relative_path)
    with Image.open(source_path) as source:
        for width in HERO_IMAGE_WIDTHS:
            image = resized_rgb(source, width)
            for ext in HERO_IMAGE_FORMATS:
                save_variant(image, OUTPUT_DIR / f"{slug}-{width}.{ext}", ext)
            messages.append(f"{slug}-{width}: {image.width}x{image.height}")
    return messages


def main() -> int:
    for relative_path in SOURCES:
        for message in optimize_source(relative_path):
            print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

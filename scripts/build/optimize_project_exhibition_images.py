#!/usr/bin/env python3
"""Create responsive exhibition-section media for registered project pages."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps

from import_project_images import save_variants
from project_pages_data import PROJECT_EXHIBITION_MEDIA


SITE_ROOT = Path(__file__).resolve().parents[2]


def optimize_exhibition_image(slug: str, source: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(source)
    media = PROJECT_EXHIBITION_MEDIA[slug]
    output_base = SITE_ROOT / media["base"].lstrip("/")
    output_base.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as raw:
        image = ImageOps.exif_transpose(raw).convert("RGB")
        save_variants(
            image,
            output_base,
            media["widths"],
            jpeg_fallback=True,
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", choices=sorted(PROJECT_EXHIBITION_MEDIA))
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    optimize_exhibition_image(args.slug, args.source)


if __name__ == "__main__":
    main()

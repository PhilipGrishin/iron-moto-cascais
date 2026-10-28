"""Dimensioned responsive pictures shared by project and News renderers."""

from __future__ import annotations

import html
from pathlib import Path

from PIL import Image

SITE_ROOT = Path(__file__).resolve().parents[2]


def image_dimensions(path: str) -> tuple[int, int]:
    with Image.open(SITE_ROOT / path.lstrip("/")) as image:
        return image.size


def picture_html(
    base: str,
    widths: list[int],
    *,
    alt: str,
    hero: bool = False,
    sizes: str | None = None,
) -> str:
    candidates = []
    for width in widths:
        dimensions = image_dimensions(f"{base}-{width}.webp")
        candidates.append((width, dimensions))
    largest_width, (largest_w, largest_h) = candidates[-1]
    srcset_avif = ", ".join(f"{base}-{width}.avif {width}w" for width, _ in candidates)
    srcset_webp = ", ".join(f"{base}-{width}.webp {width}w" for width, _ in candidates)
    has_jpeg_fallback = all(
        (SITE_ROOT / f"{base.lstrip('/')}-{width}.jpg").exists()
        for width, _ in candidates
    )
    fallback_extension = "jpg" if has_jpeg_fallback else "webp"
    fallback_srcset = ", ".join(
        f"{base}-{width}.{fallback_extension} {width}w" for width, _ in candidates
    )
    sizes = sizes or ("100vw" if hero else "(max-width:760px) 50vw, 25vw")
    picture_class = ' class="bg"' if hero else ""
    image_attrs = (
        ' decoding="async" fetchpriority="high"'
        if hero
        else ' decoding="async" loading="lazy"'
    )
    return f'''<picture{picture_class}>
<source srcset="{srcset_avif}" sizes="{sizes}" type="image/avif"/>
<source srcset="{srcset_webp}" sizes="{sizes}" type="image/webp"/>
<img alt="{html.escape(alt, quote=True)}"{image_attrs} height="{largest_h}" sizes="{sizes}" src="{base}-{largest_width}.{fallback_extension}" srcset="{fallback_srcset}" width="{largest_w}"/>
</picture>'''

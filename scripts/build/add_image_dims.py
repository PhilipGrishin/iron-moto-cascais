#!/usr/bin/env python3
"""Add width/height attributes to all <img> tags by reading actual image dimensions.
Eliminates Cumulative Layout Shift (CLS), one of Google's Core Web Vitals."""

import re
from pathlib import Path
from PIL import Image
from bs4 import BeautifulSoup

SITE_ROOT = Path(__file__).resolve().parents[2]

# Cache dimensions to avoid reading the same file twice
DIM_CACHE = {}

def get_dims(image_src: str, html_path: Path = None):
    """Resolve image src to (width, height). Handles absolute /foo.jpg and relative ./foo.jpg ../foo.jpg."""
    if not image_src:
        return None
    src = re.split(r"[?#]", image_src, 1)[0]
    # Resolve relative paths against the HTML file's directory
    if src.startswith("/"):
        candidate = SITE_ROOT / src.lstrip("/")
    elif html_path is not None:
        candidate = (html_path.parent / src).resolve()
    else:
        return None
    key = str(candidate)
    if key in DIM_CACHE:
        return DIM_CACHE[key]
    if not candidate.exists() or not candidate.is_file():
        DIM_CACHE[key] = None
        return None
    try:
        with Image.open(candidate) as img:
            dims = img.size
    except Exception:
        dims = None
    DIM_CACHE[key] = dims
    return dims


def process(html_path: Path):
    text = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(text, "lxml")
    changed = 0
    for img in soup.find_all("img"):
        if img.get("width") or img.get("height"):
            continue
        src = img.get("src", "")
        dims = get_dims(src, html_path)
        if dims is None:
            continue
        w, h = dims
        img["width"] = str(w)
        img["height"] = str(h)
        changed += 1
    if changed:
        html_path.write_text(str(soup), encoding="utf-8")
    return changed


def main():
    total_files = 0
    total_imgs = 0
    for html in sorted(SITE_ROOT.rglob("*.html")):
        # Skip .git, worker, build artifacts
        if ".git" in html.parts:
            continue
        if html.name == "404.html":
            continue  # no <img> tags
        changed = process(html)
        if changed:
            total_files += 1
            total_imgs += changed
            rel = html.relative_to(SITE_ROOT)
            print(f"  {rel}: +{changed} imgs")
    print(f"\nDone: {total_imgs} <img> tags got dimensions in {total_files} files")
    print(f"Unique images measured: {sum(1 for v in DIM_CACHE.values() if v)}")


if __name__ == "__main__":
    main()

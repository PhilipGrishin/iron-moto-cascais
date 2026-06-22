# Build scripts

Static site generators that produce the multilingual HTML files
in this repository. All scripts are path-portable: they resolve
`SITE_ROOT` from their own location (`scripts/build/` → `..`).

Run them with `python3 scripts/build/<name>.py` from the repo
root (works from any cwd because paths are absolute).

## Requirements

- Python 3.8+
- `beautifulsoup4` (HTML parsing/rewriting)
- `lxml` (recommended for stable HTML rewriting; scripts fall back to Python's built-in `html.parser`)
- `Pillow` (only for `add_image_dims.py`)
- `reportlab`, `pdfplumber`, `pypdf` (only for pricing PDF generation and PDF checks)
- Node.js 14+ (only for `extract_i18n.js`)

```
python3 -m pip install -r requirements.txt
```

If `pip3 install` fails with `externally-managed-environment`,
use a virtual environment:

```
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Files

### Generators (write HTML to repo)

| Script | Output |
|---|---|
| `build_new_pages.py` | `services/`, `projects/`, `about/`, `community/`, `contact/`, `faq/` |
| `build_brand_pages.py` | Registered brand service pages from `brand_pages_data.py` |
| `build_legal_pages.py` | `privacy/`, `cookies/`, `terms/` |
| `build_news.py` | `news/` hub + each `news/<slug>/` article |
| `build_blog.py` | `blog/` hub + `blog/<slug>/` articles |
| `build_pricing.py` | `pricing/` in all 4 languages |
| `build_pricing_pdfs.py` | `pricing/files/*.pdf` downloadable price lists in all 4 languages |
| `enhance_money_pages.py` | Adds reusable local SEO + related-page blocks to service and brand pages |
| `enhance_project_pages.py` | Adds reusable highlights + related-page blocks to project detail pages |
| `build_i18n.py` | `/ru/`, `/uk/`, `/pt/` copies of the EN main pages |
| `nav_patch.py` | Rewrites primary nav and footer on every EN page |
| `localize_internal_links.py` | Rewrites internal links in `/ru/`, `/uk/`, `/pt/` pages so they point inside the same language subtree |
| `add_image_dims.py` | Adds `width`/`height` attributes to every `<img>` based on the real image file |
| `apply_seo_meta.py` | Applies shared SEO meta invariants, including `max-image-preview:large`, to every HTML file |
| `build_sitemap.py` | Regenerates `sitemap.xml` with all 4 languages |
| `build_reviews_schema.py` | Pulls fresh Google reviews via the Cloudflare Worker, injects `AggregateRating` + `Review` JSON-LD into the home pages, and refreshes the static reviews HTML fallback |
| `extract_i18n.js` | Reads `assets/main.js` and writes `scripts/build/i18n.json` (consumed by `build_i18n.py`) |
| `validate_seo.py` | Validates sitemap files, title/meta/canonical/hreflang, JSON-LD, localized internal links, SEO robots meta and local assets |
| `validate_brand_pages.py` | Validates brand page registry, 4 language outputs, schema, sitemap, optimized hero assets, deploy workflow and reciprocal brand links |

### Data

| File | Used by |
|---|---|
| `page_meta.py` | `build_i18n.py` (per-page title / description / OG / Twitter, per language) |
| `new_pages_data.py` | `build_new_pages.py` (services / projects / about / contact / faq) |
| `brand_pages_data.py` | `build_brand_pages.py` and brand aggregators (brand registry, meta, hero image, related links, 4-language content) |
| `legal_pages_data.py` | `build_legal_pages.py` (Privacy / Cookies / Terms) |
| `news_data.py` | `build_news.py` (one entry per article slug, 4 languages) |
| `blog_data.py` | `build_blog.py` (blog hub and posts, 4 languages) |
| `pricing_data.py` | `build_pricing.py` and `build_pricing_pdfs.py` (LABELS + SECTIONS, 4 languages) |
| `i18n.json` | A snapshot of the runtime `I18N` object that lives inside `assets/main.js`. Regenerate with `node scripts/build/extract_i18n.js` after editing translations in `main.js`. |

## Typical sequences

### Full safe rebuild

Use this sequence after structural content changes, or before a
release when you want to verify the generated pages from source
data:

```
node scripts/build/extract_i18n.js
python3 scripts/build/build_new_pages.py
python3 scripts/build/build_brand_pages.py
python3 scripts/build/build_legal_pages.py
python3 scripts/build/build_news.py
python3 scripts/build/build_blog.py
python3 scripts/build/build_pricing.py
python3 scripts/build/build_pricing_pdfs.py
python3 scripts/build/nav_patch.py
python3 scripts/build/enhance_money_pages.py
python3 scripts/build/enhance_project_pages.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/add_image_dims.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_seo.py
```

Run `build_reviews_schema.py` separately only when a fresh Google
reviews snapshot is needed, because it calls the Cloudflare Worker.

### After editing translations in `assets/main.js`

```
node   scripts/build/extract_i18n.js
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
# bump cache-bust query in HTML
```

### After adding a new hub/landing page (services, etc.)

```
python3 scripts/build/build_new_pages.py
python3 scripts/build/nav_patch.py
python3 scripts/build/enhance_money_pages.py
python3 scripts/build/enhance_project_pages.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_seo.py
# bump cache-bust
```

### After adding a brand page

```
# 1. Add the brand to BRAND_CONFIG and BRAND_ORDER in brand_pages_data.py.
# 2. Add BRAND_HEAD and PAGE_I18N content for all 4 languages.
# 3. Add the nav label key to assets/main.js and regenerate i18n.json.
# 4. Add the hero source photo to photos/ and run optimize_hero_images.py for that brand.
node scripts/build/extract_i18n.js
python3 scripts/build/optimize_hero_images.py <new-brand-slug>
python3 scripts/build/build_brand_pages.py
python3 scripts/build/build_new_pages.py
python3 scripts/build/nav_patch.py
python3 scripts/build/enhance_money_pages.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_seo.py
python3 scripts/build/validate_brand_pages.py <new-brand-slug>
# bump cache-bust
```

### Brand page intake format

Future brand pages should arrive in the same format used for Suzuki:

- One Markdown file with 4 language blocks: English, Português, Русский, Українська.
- For each language: slug, SEO title, meta description, hero ALT, breadcrumb/eyebrow, H1, intro, section copy, cards, FAQ, related links, local area and CTA.
- One hero photo, named clearly enough to become `<brand>-service-main-1600.jpg`.
- Confirmed facts only: service prices, model names, diagnostic tools, contacts and opening hours.

The single source of truth for a new brand is `BRAND_CONFIG` in
`brand_pages_data.py`. Once a brand is registered there, these build helpers
consume it automatically:

- `build_brand_pages.py` for page rendering and reciprocal brand links.
- `nav_patch.py` for the Brands dropdown, mobile menu and footer.
- `build_new_pages.py` for the services hub brand list.
- `build_i18n.py`, `localize_internal_links.py`, `build_sitemap.py` and `validate_seo.py`.
- `optimize_hero_images.py` for AVIF/WebP/JPEG hero variants.
- `validate_brand_pages.py` for final brand-specific QA.

The GitHub Pages workflow is intentionally explicit. `validate_brand_pages.py`
checks that the new root-level brand folder is copied into the deploy artifact,
so a page cannot silently work locally but 404 on production.

### After adding a news article

```
# 1. Drop raw photos as JPEG into photos/news/NewsN/
# 2. Process them: a small Pillow loop produces -800 and -1600 variants:
python3 -c "
from pathlib import Path
from PIL import Image, ImageOps
SRC = Path('photos/news/NewsN')
OUT = Path('photos/news')
for i,f in enumerate(sorted(SRC.iterdir()), 1):
    im = ImageOps.exif_transpose(Image.open(f))
    w,h = im.size
    for size in (1600, 800):
        if max(w,h) > size:
            r = size/max(w,h); im2 = im.resize((round(w*r), round(h*r)), Image.LANCZOS)
        else:
            im2 = im
        im2.convert('RGB').save(OUT/f'news-<slug>-{i:02d}-{size}.jpg', 'JPEG', quality=82, optimize=True, progressive=True)
"
# 3. Add a new entry to news_data.py (NEWS_ARTICLES dict)
python3 scripts/build/build_news.py
# 4. Add the new slug to build_i18n.py MAIN_PAGES
# 5. Add it to build_sitemap.py PAGES
# 6. Add it to localize_internal_links.py LOCALIZED_PATHS
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_seo.py
# bump cache-bust
```

### After adding a blog post

```
# 1. Drop processed JPEG photos into photos/blog/ named
#    blog-<slug>-NN-1600.jpg and blog-<slug>-NN-800.jpg
# 2. Add the post content to blog_data.py (BLOG_POSTS dict)
# 3. Add the slug to build_i18n.py MAIN_PAGES
# 4. Add it to build_sitemap.py PAGES
# 5. Add it to localize_internal_links.py LOCALIZED_PATHS
# 6. Add it to nav_patch.py EN_PAGES if the post has standard nav/footer
python3 scripts/build/build_blog.py
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_seo.py
# bump cache-bust if assets/main.css or assets/main.js changed
```

### After editing pricing data

```
python3 scripts/build/build_pricing.py
python3 scripts/build/build_pricing_pdfs.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_seo.py
```

### After regenerating Google reviews snapshot

```
python3 scripts/build/build_reviews_schema.py
# This script reaches out to the Cloudflare Worker:
#   https://icm-reviews.vg-ab6.workers.dev/
# It must be run on a machine with outbound network access.
```

## Cache-bust convention

CSS and JS file references in every HTML page include a query
string of the form `?v=YYYYMMDDx`. When `assets/main.css` or
`assets/main.js` changes, bump this value across every HTML file
with a one-liner, e.g.:

```
python3 -c "
from pathlib import Path
OLD, NEW = '20260602b', '20260525a'
for f in Path('.').rglob('*.html'):
    if '.git' in f.parts: continue
    t = f.read_text(encoding='utf-8')
    if OLD in t: f.write_text(t.replace(OLD, NEW), encoding='utf-8')
print('done')
"
```

Build scripts that produce HTML carry their own `CACHE_BUST` constant
at the top — keep it in sync when bumping.

## Notes

- The HTML-rewriting Python scripts prefer `lxml`. If unavailable,
  they fall back to Python's built-in `html.parser`; whitespace and
  serialization can differ trivially.
- `extract_i18n.js` is fragile to formatting of the `I18N` literal
  in `main.js`. It walks brace depth starting from `const I18N = {`.
  Keep that marker intact.
- `add_image_dims.py` reads pixel sizes via Pillow. Images must be
  present at the resolved paths (root-relative).
- `nav_patch.py` rewrites the canonical primary nav and footer
  columns on every English page. The `PRIMARY_NAV_LINKS`,
  `FOOTER_SERVICES_LINKS`, `FOOTER_COMPANY_LINKS` lists at the top
  of the script define the source of truth.
- `localize_internal_links.py` skips asset paths (`/photos/`,
  `/assets/`, `/pricing/files/`, `/worker/`). The `LOCALIZED_PATHS`
  set at the top defines which page paths have localized
  counterparts.

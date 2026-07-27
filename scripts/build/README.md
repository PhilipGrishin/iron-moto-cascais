# Build scripts

Static site generators that produce the multilingual HTML files
in this repository. All scripts are path-portable: they resolve
`SITE_ROOT` from their own location (`scripts/build/` → `..`).

For compact project state and repeatable page-family ownership, read
`docs/PROJECT_STATE.md` and `docs/CONTENT_TYPES.md` before changing generators.
This file remains the source of truth for build command order.

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
| `build_authorized_dealer.py` | `authorized-dealer/` hub and direct partner subpages such as `authorized-dealer/c-way/` |
| `build_brand_pages.py` | Registered brand service pages from `brand_pages_data.py` |
| `build_legal_pages.py` | `privacy/`, `cookies/`, `terms/` |
| `build_news.py` | `news/` hub + each `news/<slug>/` article |
| `build_blog.py` | `blog/` hub + `blog/<slug>/` articles |
| `build_project_pages.py` | Data-driven `projects/<slug>/` detail pages registered in `project_pages_data.py` |
| `build_pre_purchase_inspection.py` | `pre-purchase-inspection/` in all 4 languages |
| `build_expat_hub.py` | `english-speaking-motorcycle-workshop/` in all 4 languages |
| `build_harley_hub.py` | `harley/`, `harley-tuning/` and `harley-custom/` in all 4 languages |
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
| `build_reviews_schema.py` | Pulls live Google rating/count via the Cloudflare Worker, reads curated visible reviews from `assets/reviews-curated.json`, injects `AggregateRating` + matching `Review` JSON-LD into the home pages, and refreshes the static reviews HTML fallback |
| `extract_i18n.js` | Reads `assets/main.js` and writes `scripts/build/i18n.json` (consumed by `build_i18n.py`) |
| `validate_seo.py` | Validates sitemap files, title/meta/canonical/hreflang, JSON-LD, localized internal links, SEO robots meta and local assets |
| `validate_brand_pages.py` | Validates brand page registry, 4 language outputs, schema, sitemap, optimized hero assets, deploy workflow and reciprocal brand links |
| `validate_harley_hub.py` | Validates the 12 Harley pages, exact source copy, LCP media, schema, same-language links, feed, portfolio and existing-page integrations |
| `validate_project_pages.py` | Validates one data-driven project page family across all 4 languages |

## Sitemap And Structured-Data Dates

Sitemap `<lastmod>` must reflect each page's real last-content-change date
from Git history of that page's source/served HTML, per language, in ISO-8601
with timezone. Never stamp all URLs with the build/deploy time. An unchanged
page must keep the same `lastmod` across deploys.

`build_sitemap.py` uses explicit publish/modified dates for blog and news
articles. Other pages use the last Git commit where the served HTML changed
semantically, ignoring serialization-only churn from shared build tools. If Git
cannot provide a reliable date, the generator falls back to the file's real
filesystem modification time, never the current build time.

Structured-data `datePublished` and `dateModified` follow the same principle:
use real content dates with timezone, not deploy time.

### Data

| File | Used by |
|---|---|
| `page_meta.py` | `build_i18n.py` (per-page title / description / OG / Twitter, per language) |
| `new_pages_data.py` | `build_new_pages.py` (services / projects / about / contact / faq) |
| `authorized_dealer_data.py` | `build_authorized_dealer.py` (Authorized Dealer hub copy, FAQ and future dealer-brand card registry) |
| `brand_pages_data.py` | `build_brand_pages.py` and brand aggregators (brand registry, meta, hero image, related links, 4-language content) |
| `legal_pages_data.py` | `build_legal_pages.py` (Privacy / Cookies / Terms) |
| `news_data.py` | `build_news.py` (one entry per article slug, 4 languages) |
| `blog_data.py` | `build_blog.py` (blog hub and posts, 4 languages) |
| `project_pages_data.py` | `build_project_pages.py` (project-page registry, reviewed Markdown parsing, media and localized UI data) |
| `content/projects/<slug>_4lang.md` | `project_pages_data.py` (approved 4-language project copy) |
| `content/pre_purchase_inspection_copy_4lang.md` | `build_pre_purchase_inspection.py` (4-language flagship service copy) |
| `content/expat_hub_copy_4lang.md` | `build_expat_hub.py` (4-language English-speaking expat hub copy) |
| `content/harley_hub_phase1_4lang.md` | `build_harley_hub.py` (exact 4-language copy for the Harley hub, tuning and custom pages) |
| `harley_hub_data.py` | `build_harley_hub.py` (page media, localized UI and project portfolio data) |
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
python3 scripts/build/build_authorized_dealer.py
python3 scripts/build/build_brand_pages.py
python3 scripts/build/build_legal_pages.py
python3 scripts/build/build_news.py
python3 scripts/build/build_blog.py
python3 scripts/build/build_pre_purchase_inspection.py
python3 scripts/build/build_pricing.py
python3 scripts/build/build_pricing_pdfs.py
python3 scripts/build/nav_patch.py
python3 scripts/build/enhance_money_pages.py
python3 scripts/build/enhance_project_pages.py
python3 scripts/build/build_i18n.py
python3 scripts/build/build_pre_purchase_inspection.py
python3 scripts/build/build_expat_hub.py
python3 scripts/build/build_harley_hub.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/add_image_dims.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_seo.py
python3 scripts/build/validate_harley_hub.py
```

Run `build_reviews_schema.py` separately only when a fresh Google
rating/count snapshot is needed, because it calls the Cloudflare Worker.
Visible review cards are controlled by `assets/reviews-curated.json`.

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

### After adding or updating the Authorized Dealer hub

The Authorized Dealer hub is a top-level category for official
parts/accessories dealer partners. Keep it separate from the
independent motorcycle-brand service pages unless the owner
provides explicit official partner copy.

```
# 1. Update scripts/build/authorized_dealer_data.py.
# 2. If the hero image changed, replace photos/authorized-dealer-main-1600.jpg.
python3 scripts/build/optimize_hero_images.py photos/authorized-dealer-main-1600.jpg
python3 scripts/build/build_authorized_dealer.py
python3 scripts/build/build_new_pages.py
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_seo.py
# bump cache-bust if assets/main.css or assets/main.js changed
```

Future dealer-brand cards should be appended to
`AUTHORIZED_DEALER_BRANDS` in `authorized_dealer_data.py`. Use
English-rooted URLs such as `/authorized-dealer/<brand>/`; the
localized pages will receive `/pt/`, `/ru/` and `/uk/` prefixes
through the normal localization pipeline. The current C-Way partner subpage is
generated directly by `build_authorized_dealer.py` from `CWAY_DEALER_I18N` and
must remain limited to the approved Honda Gold Wing luggage-system scope and
six priced Steel/Aluminium product configurations. Product media and numeric
prices live in `CWAY_MEDIA`; translated names and descriptions live in
`CWAY_DEALER_I18N`. Keep visible prices and Product/Offer schema in parity, and
do not add trailer/mototrailer content without a new explicit owner task.

### After editing pre-purchase inspection copy

```
# 1. Update scripts/build/content/pre_purchase_inspection_copy_4lang.md.
# 2. If the hero image changed, replace photos/services/pre-purchase-inspection-main.jpg.
python3 scripts/build/optimize_hero_images.py photos/services/pre-purchase-inspection-main.jpg
python3 scripts/build/build_pre_purchase_inspection.py
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/build_pre_purchase_inspection.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/add_image_dims.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_seo.py
# bump cache-bust if assets/main.css or assets/main.js changed
```

### After editing the English-speaking expat hub

The expat hub is a light funnel page for
`/english-speaking-motorcycle-workshop/`. It must remain footer-only and
contextual-link-only; do not add it to the header or Services dropdown.

```
# 1. Update scripts/build/content/expat_hub_copy_4lang.md.
# 2. If the hero image changed, replace photos/services/english-speaking-motorcycle-workshop-main.jpg.
python3 scripts/build/optimize_hero_images.py photos/services/english-speaking-motorcycle-workshop-main.jpg
node scripts/build/extract_i18n.js
python3 scripts/build/build_new_pages.py
python3 scripts/build/build_pre_purchase_inspection.py
python3 scripts/build/nav_patch.py
python3 scripts/build/enhance_money_pages.py
python3 scripts/build/build_i18n.py
python3 scripts/build/build_expat_hub.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/add_image_dims.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_seo.py
# bump cache-bust if assets/main.css or assets/main.js changed
```

### After editing the Harley Hub family

The source Markdown owns the approved four-language page copy. Portfolio
summaries and blog-topic behavior live in the adjacent Python data modules.

```
# 1. Update scripts/build/content/harley_hub_phase1_4lang.md.
# 2. Update scripts/build/harley_hub_data.py only for supplemental UI,
#    media or portfolio data.
node scripts/build/extract_i18n.js
python3 scripts/build/build_brand_pages.py
python3 scripts/build/build_blog.py
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/build_harley_hub.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_harley_hub.py
python3 scripts/build/validate_seo.py
python3 scripts/build/validate_brand_pages.py harley-service
# bump cache-bust if assets/main.css or assets/main.js changed
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

Also keep the homepage `#brands` strip synchronized with `BRAND_ORDER`.
Any registered brand with a live service page must be an active link in that
strip on EN/RU/UK/PT. `validate_brand_pages.py` checks this now, so a new brand
cannot silently remain plain text on the homepage after publication.

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
# 2. Add the post content to blog_data.py (BLOG_POSTS dict), or add a reviewed
#    4-language Markdown source under scripts/build/content/ and load it from
#    blog_data.py for long-form articles
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

### After adding a data-driven project page

```
# 1. Save the approved 4-language Markdown at:
#    content/projects/<slug>_4lang.md
# 2. Add the project to PROJECT_CONFIGS in project_pages_data.py
# 3. Import the hero and gallery photographs:
python3 scripts/build/import_project_images.py <slug> "/absolute/path/to/source/photos"
# 4. Register the page in page_meta.py, new_pages_data.py, nav_patch.py,
#    build_sitemap.py, localize_internal_links.py and validate_seo.py
python3 scripts/build/build_project_pages.py
python3 scripts/build/build_new_pages.py
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/nav_patch.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_project_pages.py <slug>
python3 scripts/build/validate_seo.py
```

### After editing pricing data

```
python3 scripts/build/build_pricing.py
python3 scripts/build/build_pricing_pdfs.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/validate_seo.py
```

### After editing curated reviews or regenerating Google reviews snapshot

```
python3 scripts/build/build_reviews_schema.py
# This script reaches out to the Cloudflare Worker:
#   https://icm-reviews.vg-ab6.workers.dev/
# It must be run on a machine with outbound network access.
```

The script writes the Worker response to `assets/reviews-snapshot.json`, reads
visible cards from `assets/reviews-curated.json`, and injects both the static
HTML fallback and the LocalBusiness `AggregateRating`/`Review` JSON-LD on the
four home pages. The `Review` JSON-LD items must match the visible curated cards
1:1. The aggregate `reviewCount` remains the real Google total, not the number
of curated cards.

A scheduled refresh is defined in `.github/workflows/reviews-refresh.yml`. It
runs every Monday at 06:17 UTC and also supports manual `workflow_dispatch`.

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

## Typography system

`assets/main.css` owns the site font stack through CSS variables:

- `--font-body` for long-form readable text.
- `--font-ui` for nav, buttons, labels and compact card text.
- `--font-display` for large uppercase headings.

Generated inline CSS must use these variables instead of hard-coding
Google font families. This keeps page families consistent when typography
changes and prevents new generators from reintroducing page-specific font
behavior.

Russian and Ukrainian pages use language-scoped Cyrillic tuning in
`assets/main.css`: `html[lang="ru"]` and `html[lang="uk"]` switch UI/display
type to `Roboto Condensed` and slightly reduce heading sizes and tracking.
When adding a new page family or generator, keep selectors compatible with
these language-level overrides, then visual-check at least one RU and one UK
page before release.

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

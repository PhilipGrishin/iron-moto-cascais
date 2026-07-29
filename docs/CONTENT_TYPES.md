# Content Types And Implementation Templates

This file maps repeatable site work to source data, generators, registration
points and verification. Use it to avoid one-off edits and to keep future pages
scalable.

## General Rules For All Page Families

- Keep public pages multilingual: EN, RU, UK, PT.
- Prefer source data and shared generators over hand-edited generated HTML.
- Add sitemap, canonical, hreflang and JSON-LD for every indexable page.
- Use absolute asset paths (`/photos/...`, `/assets/...`).
- Keep localized internal links inside the current language subtree.
- If `assets/main.css` or `assets/main.js` changes, bump cache-bust everywhere.
- Sitemap `<lastmod>` must reflect each page's real last-content-change date
  from Git history of that page's source/served HTML, per language, in
  ISO-8601 with timezone. Never stamp all URLs with the build/deploy time.
  An unchanged page must keep the same `lastmod` across deploys.
- Structured-data `datePublished` and `dateModified` must use real content
  dates with timezone, not deploy time.
- Language-specific FAQ counts are supported through `fq.qN` / `fq.aN` page
  translations. `build_i18n.py` expands the visible FAQ list before rebuilding
  `FAQPage`, so visible questions and schema remain identical per language.
- After push, verify the exact production URLs changed by the task.

## New Brand Service Page

Examples: Suzuki, Honda, Royal Enfield, Triumph.

Source of truth:

- `scripts/build/brand_pages_data.py`
- Hero images under `photos/`
- Optimized variants under `photos/optimized/`

Generator and helpers:

- `scripts/build/build_brand_pages.py`
- `scripts/build/build_new_pages.py`
- `scripts/build/nav_patch.py`
- `scripts/build/enhance_money_pages.py`
- `scripts/build/build_i18n.py`
- `scripts/build/localize_internal_links.py`
- `scripts/build/build_sitemap.py`
- `scripts/build/validate_brand_pages.py`

Required registrations:

- `BRAND_ORDER`
- `BRAND_CONFIG`
- `BRAND_HEAD`
- `PAGE_I18N`
- `assets/main.js` nav label if a new label key is needed
- GitHub Pages copy list in `.github/workflows/pages.yml` for the new root slug

Required page behavior:

- Independent workshop wording.
- Reciprocal "Other brands" links.
- Related workshop path cards.
- Brand visible in Brands dropdown, footer and services hub.
- Correct localized tyre-service links where present.

Verification:

```bash
node scripts/build/extract_i18n.js
python3 scripts/build/optimize_hero_images.py <new-brand-slug-or-photo>
python3 scripts/build/build_brand_pages.py
python3 scripts/build/build_new_pages.py
python3 scripts/build/nav_patch.py
python3 scripts/build/enhance_money_pages.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/build_llms.py
python3 scripts/build/validate_seo.py
python3 scripts/build/validate_brand_pages.py <brand-slug>
git diff --check
```

## Existing Brand Text Or Hero Refresh

Examples: humanized Harley-Davidson, BMW Motorrad, Ducati copy.

Preferred source:

- Existing `PAGE_I18N` and `BRAND_HEAD` blocks in
  `scripts/build/brand_pages_data.py`
- Existing hero path in `BRAND_CONFIG[slug]["hero"]`

Rules:

- Preserve section order and page structure unless explicitly requested.
- Update visible FAQ text and FAQPage JSON-LD together via source data.
- Keep the shared `money-related` section linked to every other registered
  brand service page in the same language; `validate_brand_pages.py` enforces
  the complete reciprocal link set.
- Keep model names, prices, contact details and technical terms exactly as
  approved by the owner-provided copy.

Verification:

```bash
python3 scripts/build/build_brand_pages.py
python3 scripts/build/build_new_pages.py
python3 scripts/build/nav_patch.py
python3 scripts/build/enhance_money_pages.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/build_llms.py
python3 scripts/build/validate_seo.py
python3 scripts/build/validate_brand_pages.py <brand-slug>
git diff --check
```

## New Service Page Or Service Hub Card

Examples: tyre service, pre-purchase inspection, services hub cards.

Source of truth varies by page:

- General hubs: `scripts/build/new_pages_data.py`
- Tyre service: `scripts/build/build_tyre_service.py` and its embedded/source
  copy conventions
- Pre-purchase inspection:
  `scripts/build/content/pre_purchase_inspection_copy_4lang.md` and
  `scripts/build/build_pre_purchase_inspection.py`
- English-speaking expat hub:
  `scripts/build/content/expat_hub_copy_4lang.md` and
  `scripts/build/build_expat_hub.py`

Required registrations:

- `scripts/build/build_i18n.py` `MAIN_PAGES`
- `scripts/build/build_sitemap.py` `PAGES`
- `scripts/build/localize_internal_links.py` `LOCALIZED_PATHS`
- `scripts/build/nav_patch.py` `EN_PAGES` where standard nav/footer applies
- `scripts/build/page_meta.py`
- `.github/workflows/pages.yml` if a new root-level folder is created

Schema:

- Usually `Service` + `FAQPage` + `BreadcrumbList`.
- For hubs, use the existing hub schema pattern.

Verification:

```bash
python3 scripts/build/build_new_pages.py
python3 scripts/build/build_pre_purchase_inspection.py
python3 scripts/build/build_tyre_service.py
python3 scripts/build/nav_patch.py
python3 scripts/build/enhance_money_pages.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/add_image_dims.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/build_llms.py
python3 scripts/build/validate_seo.py
git diff --check
```

Run only the relevant subset when the task is narrow.

## English-Speaking Expat Hub

Purpose:

- A light hub and funnel for English-speaking riders, expats and newcomers.
- Routes down to existing money pages instead of duplicating
  `/motorcycle-service/`.
- Footer Services column plus contextual inbound links only. Do not add this
  page to the header or Services dropdown.

Source of truth:

- `scripts/build/content/expat_hub_copy_4lang.md`
- `scripts/build/build_expat_hub.py`
- Hero source:
  `photos/services/english-speaking-motorcycle-workshop-main.jpg`

Required registrations:

- Footer label in `assets/main.js` as `nav.expatWorkshop`.
- Footer-only link in `scripts/build/nav_patch.py` `FOOTER_SERVICES_LINKS`.
- New path in `scripts/build/localize_internal_links.py`,
  `scripts/build/build_sitemap.py`, `scripts/build/validate_seo.py` and
  `.github/workflows/pages.yml`.
- Contextual inbound links from home, About, Motorcycle Service and
  Pre-purchase Inspection.

Schema:

- `CollectionPage` referencing the canonical `https://ironcustommotors.com/#business`
  by `@id`.
- `FAQPage` with exactly the six visible FAQ items per language.
- `BreadcrumbList`: Home -> English-speaking workshop.

Verification:

```bash
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
python3 scripts/build/build_llms.py
python3 scripts/build/validate_seo.py
git diff --check
```

## Harley Hub

Purpose:

- Route Harley-Davidson riders between service, tuning, custom work and parts.
- Keep the existing independent `/harley-service/` page as a focused service
  spoke rather than duplicating its copy.
- Surface future Harley blog posts automatically through topic metadata.

Source of truth:

- Exact four-language copy:
  `scripts/build/content/harley_hub_phase1_4lang.md`
- Supplemental page, UI and portfolio data:
  `scripts/build/harley_hub_data.py`
- Generator: `scripts/build/build_harley_hub.py`
- Validator: `scripts/build/validate_harley_hub.py`
- Hero source images: `photos/harley/`

Current URLs:

- `/harley/`
- `/harley-tuning/`
- `/harley-custom/`
- Matching `/pt/`, `/ru/` and `/uk/` variants.

Dynamic blog feed:

- Add `topics: ("harley",)` to a `BLOG_POSTS` entry in
  `scripts/build/blog_data.py`.
- `build_harley_hub.py` reads the blog registry and renders matching cards in
  descending publication order.

Custom portfolio:

- Portfolio order, existing project image paths and localized fact-based
  summaries live in `harley_hub_data.py`.
- Reuse project assets; do not create a separate image source for the same
  project cover.

Visual system:

- Keep Harley Hub pages on the established site scale: H1 up to `52px`, H2 up
  to `44px`, body copy up to `17px`, and section padding up to `48px`.
- Hero images use the same dark image filter and overlay treatment as brand
  service pages. Do not weaken the contrast behind hero copy.
- `validate_harley_hub.py` protects these typography, spacing and hero
  darkening tokens across all 12 generated pages.

Schema:

- Hub: `CollectionPage`/`WebPage` + `FAQPage` + `BreadcrumbList`.
- Tuning/custom: `WebPage` + `Service` + `FAQPage` + `BreadcrumbList`.
- Do not add `Product` or `Offer` until approved numeric pricing exists.

Verification:

```bash
node scripts/build/extract_i18n.js
python3 scripts/build/optimize_hero_images.py photos/harley/harley-hub-hero.jpg
python3 scripts/build/optimize_hero_images.py photos/harley/harley-tuning-hero.jpg
python3 scripts/build/optimize_hero_images.py photos/harley/harley-custom-hero.jpg
python3 scripts/build/build_brand_pages.py
python3 scripts/build/build_blog.py
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/build_harley_hub.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/build_llms.py
python3 scripts/build/validate_harley_hub.py
python3 scripts/build/validate_seo.py
python3 scripts/build/validate_brand_pages.py harley-service
git diff --check
```

## Authorized Dealer Hub

Purpose:

- Top-level official parts/accessories dealer partner category.
- Separate from independent motorcycle-brand service pages.

Source of truth:

- `scripts/build/authorized_dealer_data.py`
- `AUTHORIZED_DEALER_BRANDS` for future partner cards.
- `scripts/build/build_authorized_dealer.py`

Current URLs:

- `/authorized-dealer/`
- `/ru/authorized-dealer/`
- `/uk/authorized-dealer/`
- `/pt/authorized-dealer/`
- `/authorized-dealer/c-way/`
- `/ru/authorized-dealer/c-way/`
- `/uk/authorized-dealer/c-way/`
- `/pt/authorized-dealer/c-way/`

Schema:

- `CollectionPage`
- `FAQPage`
- `BreadcrumbList`

Required links:

- Top nav and footer label in `assets/main.js`.
- Reverse link from `/parts/` in all languages.
- Sitemap entry.

Verification:

```bash
python3 scripts/build/optimize_hero_images.py photos/authorized-dealer-main-1600.jpg
python3 scripts/build/build_authorized_dealer.py
python3 scripts/build/build_new_pages.py
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/build_llms.py
python3 scripts/build/validate_seo.py
git diff --check
```

Future partner subpages should follow `/authorized-dealer/<brand>/` with
localized prefixes for PT/RU/UK. Keep cards in `AUTHORIZED_DEALER_BRANDS`.
The C-Way subpage is generated directly by `build_authorized_dealer.py` from
`CWAY_DEALER_I18N` and must stay focused on C-Way Honda Gold Wing luggage
systems. The current catalog has six priced Steel/Aluminium configurations,
with media and numeric prices registered in `CWAY_MEDIA`; visible product data
and Product/Offer schema must remain in parity. Do not add
trailer/mototrailer content without a new explicit owner task.

## Blog Article

Source of truth:

- `scripts/build/blog_data.py`
- Long-form multilingual Markdown sources under `scripts/build/content/`
- Images under `photos/blog/`

Generator:

- `scripts/build/build_blog.py`

Required registrations:

- `BLOG_POSTS`
- `build_i18n.py` `MAIN_PAGES`
- `build_sitemap.py` `PAGES`
- `localize_internal_links.py` `LOCALIZED_PATHS`
- `nav_patch.py` `EN_PAGES` when standard nav/footer applies

Schema:

- `BlogPosting`
- `BreadcrumbList`
- Optional `VideoObject` when article embeds a video. Native self-hosted video
  slots use `nativeVideo` data and render as `<video>` without a YouTube iframe.
- `datePublished` and `dateModified` must be full ISO-8601 datetimes with a
  Europe/Lisbon timezone offset, not date-only strings.
- `author` must keep the canonical business `@id` and include `name` and `url`.
- `publisher` must keep the canonical business `@id`, include `name`, and expose
  the approved logo as an `ImageObject`.
- Native video dimensions and `duration` must be measured from the published
  media file. The rendered container must follow the real aspect ratio.

Verification:

```bash
python3 scripts/build/build_blog.py
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/build_llms.py
python3 scripts/build/validate_seo.py
git diff --check
```

## News Article

Source of truth:

- `scripts/build/news_data.py`
- Images under `photos/news/`

Generator:

- `scripts/build/build_news.py`

Required registrations:

- `NEWS_ARTICLES`
- `build_i18n.py` `MAIN_PAGES`
- `build_sitemap.py` `PAGES`
- `localize_internal_links.py` `LOCALIZED_PATHS`
- `nav_patch.py` `EN_PAGES`

Schema:

- `NewsArticle`
- `BreadcrumbList`
- `datePublished` and `dateModified` must be full ISO-8601 datetimes with a
  Europe/Lisbon timezone offset, not date-only strings.
- `author` must keep the canonical business `@id` and include `url`.

Verification:

```bash
python3 scripts/build/build_news.py
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/build_llms.py
python3 scripts/build/validate_seo.py
git diff --check
```

## Project Page

Current state:

- Project pages are mostly authored as static HTML with inline
  `window.ICM_I18N_PAGE` blocks.
- New project pages can use the shared data-driven flow in
  `scripts/build/project_pages_data.py` and
  `scripts/build/build_project_pages.py`.
- Approved long-form copy for data-driven pages lives in
  `content/projects/<slug>_4lang.md`; responsive media and localized gallery
  ALT text are registered in `PROJECT_CONFIGS`.

When editing:

- Preserve existing localized copy.
- Keep project pages in `/projects/<slug>/` and localized prefixes.
- Import new hero and gallery media with `import_project_images.py`.
- Register new slugs in the projects listing, global navigation, sitemap,
  localized-link registry and SEO validator.
- Run `enhance_project_pages.py` if shared project enhancement blocks need
  regeneration on legacy static project pages.

Verification:

```bash
python3 scripts/build/build_project_pages.py
python3 scripts/build/build_new_pages.py
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/nav_patch.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/build_llms.py
python3 scripts/build/validate_project_pages.py <slug>
python3 scripts/build/validate_seo.py
git diff --check
```

## Pricing

Source of truth:

- `scripts/build/pricing_data.py`

Generators:

- `scripts/build/build_pricing.py`
- `scripts/build/build_pricing_pdfs.py`

Verification:

```bash
python3 scripts/build/build_pricing.py
python3 scripts/build/build_pricing_pdfs.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/build_llms.py
python3 scripts/build/validate_seo.py
git diff --check
```

## Navigation And Footer

Source of truth:

- Desktop/mobile labels: `assets/main.js`
- English nav/footer structure: `scripts/build/nav_patch.py`
- Brand dropdown: generated from `BRAND_ORDER`

Rules:

- Do not hand-edit nav/footer across generated pages.
- Add nav labels to `assets/main.js`, run `extract_i18n.js`, then regenerate.
- If `assets/main.js` changes, bump cache-bust.

Verification:

```bash
node scripts/build/extract_i18n.js
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/apply_seo_meta.py
python3 scripts/build/build_sitemap.py
python3 scripts/build/build_llms.py
python3 scripts/build/validate_seo.py
git diff --check
```

## AI Discovery Index

Output:

- `llms.txt`

Canonical sources:

- `scripts/build/build_sitemap.py` `PAGES`
- `scripts/build/blog_data.py` `BLOG_POSTS`
- `scripts/build/news_data.py` `NEWS_ARTICLES`
- `scripts/build/new_pages_data.py` `PROJECT_TILES`
- `scripts/build/brand_pages_data.py` `BRAND_ORDER` and `BRAND_CONFIG`
- `scripts/build/legal_pages_data.py` `LEGAL_PAGES`
- `docs/BUSINESS_FACTS.md`
- published English H1 and meta descriptions

Generator:

- `scripts/build/build_llms.py`

Rules:

- Run the generator immediately after `build_sitemap.py`.
- Do not hand-edit `llms.txt`.
- Every English sitemap URL must appear as an internal page link.
- Keep business facts in `docs/BUSINESS_FACTS.md`; other documentation should
  link there rather than duplicate those values.
- Keep page descriptions in their existing page-family metadata source. The
  generator reads the published meta description instead of maintaining a
  second copy.
- `validate_seo.py` enforces sitemap coverage after generation.

Verification:

```bash
python3 scripts/build/build_sitemap.py
python3 scripts/build/build_llms.py
python3 scripts/build/validate_seo.py
git diff --check
```

## Reviews

Runtime source:

- Cloudflare Worker: `https://icm-reviews.vg-ab6.workers.dev/`

Static snapshot:

- `assets/reviews-snapshot.json`
- `assets/reviews-curated.json`
- `scripts/build/build_reviews_schema.py`

Rules:

- Do not expose Google Places API keys in client HTML/JS.
- The Worker owns Google Places calls.
- `assets/reviews-snapshot.json` stores the live Worker response and is the
  source for static rating/count fallback and `AggregateRating`.
- `assets/reviews-curated.json` is the editorial source for visible review
  cards and JSON-LD `review[]` items. Cards and `review[]` must match 1:1.
- Build-time review schema refresh requires network access.
- `.github/workflows/reviews-refresh.yml` runs the refresh weekly and can be
  dispatched manually.

Curated file structure:

```json
{
  "displayCount": 6,
  "preferPageLanguage": false,
  "reviews": [
    {
      "author": "Reviewer name",
      "rating": 5,
      "text": "Full review text.",
      "lang": "en",
      "publishedAt": "2026-05-31T15:11:38Z",
      "url": "https://www.google.com/maps/...",
      "avatar": ""
    }
  ]
}
```

Use exact Google review text and dates when adding records. If `avatar` is
empty, the site falls back to initials. `displayCount` controls how many cards
are rendered, capped by available curated records.

Verification:

```bash
python3 scripts/build/build_reviews_schema.py
python3 scripts/build/validate_seo.py
git diff --check
```

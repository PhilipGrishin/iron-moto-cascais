# P-COCKTAIL Delivery Report

Date: 2026-08-01

Status: **confirmed**

## Outcome

Cocktail is the twelfth registered project and is live in English, Portuguese,
Russian and Ukrainian. The project uses the existing shared project family;
the former Fighter-specific Markdown path was generalized into one reusable
Markdown project renderer for Cocktail and future approved projects.

Implementation commit: `e3ef595c` (`Add multilingual Cocktail project`).

GitHub Pages workflow: `30705942643` (`success`, 33 seconds).

Google Rich Results Test result: `FcQJIDL6po_NRWLDwce_1w`.

## Canonical Inputs And Dates

- Approved copy: `content/projects/cocktail_4lang.md`.
- The repository copy is byte-identical to the supplied file; SHA-256:
  `388ef7323f2d035b9edbc062b04230fa71db03a9d291a28308b30455755168b8`.
- Publication and modification time:
  `2026-08-01T14:55:25+01:00`, taken from the supplied source file creation
  time and used consistently in Article schema and the four new sitemap URLs.
- Project year: `2013`.
- Category: localized `Bagger · Full Custom`.
- Location: localized `Built in Kharkiv, Ukraine`.
- Hero: `Cocktail_HERO.jpg`; gallery: the ten approved remaining JPEG files in
  the supplied order.

## Architecture Decision

- `MARKDOWN_PROJECT_CONFIGS` is the single registration point for new
  Markdown-backed project details.
- `build_project_pages.py` renders every registered project; Cocktail has no
  project-specific template or generator.
- `import_project_images.py` creates the registered responsive formats and
  writes JPEG fallback files only when `jpeg_fallback` is enabled.
- Project sitemap and localized-path entries are derived from
  `PROJECT_CONFIGS`; listing membership remains in `PROJECT_TILES`; Harley
  portfolio membership remains in `PORTFOLIO_ORDER`.
- This separation keeps page generation reusable without making every future
  project a Harley project or forcing every project into every commercial hub.

## Changed File Manifest

Implementation commit `e3ef595c` contains 106 files:

- 4 new outputs:
  `projects/cocktail/index.html`, `pt/projects/cocktail/index.html`,
  `ru/projects/cocktail/index.html`, `uk/projects/cocktail/index.html`;
- 12 integration outputs: `/projects/`, `/custom/` and `/harley-custom/` in all
  four languages;
- 1 approved content file: `content/projects/cocktail_4lang.md`;
- 9 build/data/validation files:
  `build_new_pages.py`, `build_project_pages.py`, `build_sitemap.py`,
  `harley_hub_data.py`, `import_project_images.py`,
  `localize_internal_links.py`, `new_pages_data.py`,
  `project_pages_data.py`, `validate_project_pages.py`;
- `sitemap.xml` and `llms.txt`;
- 78 responsive media files: 9 project hero variants, 60 gallery variants and
  9 Harley portfolio variants across AVIF, WebP and JPEG.

No other HTML changed. `assets/main.css`, `assets/main.js`, their cache-bust
values and all existing project details remained unchanged.

## Copy And Localization Evidence

For EN/PT/RU/UK, the generated `.generated-project-story` and closing block are
semantically equal to the parsed canonical Markdown. Each page has its
localized hero ALT, ten localized gallery ALTs, canonical language chrome and
same-language internal links.

The generated whole-main visible-text SHA-256 values are:

| Language | SHA-256 |
|---|---|
| EN | `e43d1d9bb21e578daa812adf289f56aa4d8286ab1258d37235e5bf11d32423a0` |
| PT | `7b00141b6e913441b8e6a8d10315e1d40ed1d5f31fe767b2c9cae1d5c9af20a0` |
| RU | `6bd4cda40dbe3335d9173b3b5af8246e6eb51649f3c116a6c1e81109641442ee` |
| UK | `957939d4a665bd23d5d7aa4dbb31ffba4343034b6ee9be3c4b9e8479b0b81007` |

## Hero And Network Evidence

The hero AVIF source and preload have identical `srcset` and `sizes="100vw"`.
Therefore the preload and the rendered `<picture>` select the same candidate
for every required profile:

| Profile | Effective width | Selected candidate |
|---|---:|---|
| 390 CSS px / DPR 3 | 1170 px | `cocktail-1600.avif` |
| 390 CSS px / DPR 2 | 780 px | `cocktail-800.avif` |
| 768 CSS px / DPR 2 | 1536 px | `cocktail-1600.avif` |
| 1280 CSS px / DPR 1 | 1280 px | `cocktail-1600.avif` |

Production browser observation at 390 x 844 CSS pixels / DPR 2 with the
cache-bypass query `?p-cocktail=e3ef595c-browser`:

```text
currentSrc: https://ironcustommotors.com/photos/projects/cocktail-800.avif
observed Cocktail hero resources: 1
fetchpriority="high" elements: 1
fetchpriority="high" + loading="lazy": 0
gallery images: 10
```

The single observed asset was both the preload resource and the rendered
`srcset` resource; no second Cocktail hero candidate was requested.

## Structured Data Evidence

Google Rich Results Test fetched the cache-bypassed production URL on
2026-08-01 at 16:29:29 Europe/Lisbon and reported:

```text
4 valid items detected
Articles: 1 valid item detected
Breadcrumbs: 1 valid item detected
Local businesses: 1 valid item detected
Organization: 1 valid item detected
```

The Article detail contained the full ISO publication/modification timestamps,
the 2400 x 1600 primary image and the referenced complete Iron Custom Motors
publisher/author entity. No errors or warnings were reported.

## Sitemap And Discovery Evidence

- Before: 212 URLs; after: 216 URLs.
- Added exactly the four Cocktail URLs with
  `2026-08-01T14:55:25+01:00` lastmod.
- Changed lastmod exactly on the 12 integration URLs: `/projects/`, `/custom/`
  and `/harley-custom/` in all four languages.
- Removed URLs: none.
- All other lastmod values were byte-identical to the baseline.
- Final sitemap SHA-256:
  `76facd632b6938030a86f038ca9e333aeb5c91998f369a83b68aae01e0b16e01`.
- `llms.txt` contains the English Cocktail URL and reports 54 English paths / 216
  sitemap URLs.

## Acceptance Criteria

1. **PASS** — four production URLs return 200, use self-canonical and mutual
   EN/RU/UK/PT-PT plus x-default hreflang, and are present in the sitemap.
2. **PASS** — Cocktail and all other registered projects pass
   `validate_project_pages.py`; all four validator groups pass, including
   localized chrome parity.
3. **PASS** — Google Rich Results Test reports four valid items and no warnings.
4. **PASS** — one high-priority hero, no high/lazy conflict, responsive
   AVIF/WebP with JPEG fallback, and one observed production hero resource at
   390 CSS pixels.
5. **PASS** — project tile, Custom mention, Harley portfolio card and both
   outgoing Harley links are present in all four production languages.
6. **PASS** — generated `llms.txt` includes Cocktail; the SEO superset check
   passes.
7. **PASS** — existing HTML changes are limited to the 12 required integration
   pages; four project outputs, approved content/data/build files, sitemap,
   llms and media are the only additional implementation scope.
8. **PASS** — the documented Full Safe Rebuild on a clean clone of `e3ef595c`
   completed with empty `git status --short`.

## Validation Output

```text
SEO validation passed: 216 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
OK: cocktail project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
```

The project loop produced the same `OK` result for all 12 registered slugs.

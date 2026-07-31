# C7-FIX Report: CSS Hero Preload Alignment

Date: 2026-07-31

Implementation commit: `410809d1`

## Decision

The responsive-background option was implemented. CSS-background heroes now
render the 768px AVIF through 767px, the 1280px AVIF from 768px through 1279px,
and the 1920px AVIF from 1280px upward. These are the same media boundaries and
URLs used by the preload links. Existing background position, size, filter,
overlay and visible content remain unchanged.

The shared behavior lives in `scripts/build/hero_images.py` and is applied by
`scripts/build/apply_seo_meta.py`. `scripts/build/validate_seo.py` now computes
the effective first-section CSS background at media-query boundaries and
rejects a preload/rendered-resource mismatch.

## Scope

- Before: 104 CSS-background hero pages checked; 168 breakpoint mismatches on
  84 pages.
- After: all 104 CSS-background hero pages pass.
- Updated page families: Authorized Dealer hub; Blog hub; BMW, Ducati,
  Harley-Davidson, Honda, Royal Enfield, Suzuki and Triumph service; Community;
  Contact; FAQ; motorcycle tyre service; News hub and its three articles;
  pre-purchase inspection; Pricing; Projects hub; Services.
- Updated localized variants: EN, PT, RU and UK for every affected family.
- Project detail pages: 44 checked by SHA-256, zero changed.
- Changed HTML: 84 files. Removing the responsive style and marker from each
  produces the same normalized DOM as the pre-fix file.

## Browser Verification

Local browser checks used viewport widths 390, 900 and 1400px.

| Page / width | Active preload | Computed CSS background | Observed hero resources |
| --- | --- | --- | --- |
| `/bmw-service/` / 390 | `bmw-service-main-768.avif` | `bmw-service-main-768.avif` | only `bmw-service-main-768.avif` |
| `/bmw-service/` / 900 | `bmw-service-main-1280.avif` | `bmw-service-main-1280.avif` | matching candidate |
| `/bmw-service/` / 1400 | `bmw-service-main-1920.avif` | `bmw-service-main-1920.avif` | matching candidate |
| News article / 390 | article hero 768 AVIF | article hero 768 AVIF | only the article hero; no hub hero |
| Blog hub / 390 | `lounge-768.avif` | `lounge-768.avif` | hero preload is not a post-card image |

The BMW mobile screenshot retained its existing darkening, crop, copy layout
and CTA placement.

## Blog And News Findings

The Blog hub, News hub and News articles use CSS backgrounds and now inherit
the responsive alignment. The tested news article preloaded its own article
hero, not the reusable hub background or a card below the fold.

Blog article pages use responsive `<picture>` markup rather than CSS heroes.
Their preload points to the correct article hero. At 390px with device pixel
ratio 2, the tested article preloaded the 768px AVIF while `srcset` selected the
1280px AVIF of the same hero, so two width candidates were observed. This is a
separate high-DPR `<picture>` selection concern also shared by protected
project pages; it was not changed in this CSS-background block and is recorded
in `docs/OPEN_TASKS.md`.

## Reproducibility And Immutable State

- The complete documented build sequence was run twice. After committing the
  canonical generated output, the second complete rebuild left `git status`
  empty.
- `sitemap.xml`: 212 URL entries, 49 unique lastmod values, zero changed
  per-page lastmod values.
- Cache bust: unchanged. `assets/main.css` and `assets/main.js` were not
  modified; all existing asset stamps remain unchanged.
- `llms.txt` and `robots.txt`: unchanged.
- `git diff --check`: clean.

## SEO / GEO Scope Review

| Surface | Change required | Reason |
| --- | --- | --- |
| `sitemap.xml` and per-page lastmod | No | Technical delivery change; content and dates are unchanged |
| `llms.txt` | No | Link inventory and discovery text are unchanged |
| `robots.txt` | No | Crawl policy is unchanged |
| hreflang and self-canonical | No | URLs and language relationships are unchanged |
| JSON-LD | No | Structured data is unchanged |
| `MAIN_PAGES`, `PAGES`, `LOCALIZED_PATHS`, `EN_PAGES` | No | Page inventory is unchanged |
| `.github/workflows/pages.yml` | No | Deployment process is unchanged |
| Internal links | No | Navigation and body links are unchanged |
| Cache bust | No | No shared CSS or JavaScript asset changed |
| `docs/PROJECT_STATE.md` | Yes | Records the enforced CSS hero delivery invariant |
| `docs/CONTENT_TYPES.md` | Yes | Documents the repeatable page-family rule |
| `docs/CODEX_CHANGELOG.md` | Yes | Records the implementation and verification |
| `docs/OPEN_TASKS.md` | Yes | Records the separate high-DPR `<picture>` observation |

The exact before/after validator transcript is stored in
`docs/reports/C7_FIX_VALIDATION.txt`.

# Iron Custom Motors Website: Project State

Last updated: 2026-07-31

This is the only documentation file that owns current inventories, counts,
deployed public identifiers and cache-bust values. Operating rules live in
`AGENTS.md`; page ownership lives in `docs/CONTENT_TYPES.md`; commands live in
`scripts/build/README.md`.

## Status And Evidence

- Status: **confirmed**.
- Evidence date: 2026-07-31 (Europe/Lisbon).
- Repository evidence: tracked files at commit `a2daec42` before the FINAL
  documentation audit, plus a clean `main...origin/main` comparison.
- Inventory method: import the maintained Python registries, parse
  `sitemap.xml`, and enumerate tracked `*.html` files.
- Cache-bust method: scan asset references in every sitemap HTML file.
- Production evidence: cache-bypass requests to the public domain.
- Reproducibility evidence: the documented full rebuild and broad verification
  at documentation commit `d08a3297` left a clean clone with empty
  `git status --short`; verified 2026-07-31.

## Repository And Production

| Item | Current value |
|---|---|
| Production | `https://ironcustommotors.com/` |
| Repository | `https://github.com/dreamcarua/iron-moto-cascais` |
| Git remote | `https://github.com/dreamcarua/iron-moto-cascais.git` |
| Production branch | `main` |
| Hosting | GitHub Pages, checked-in static output |
| DNS/CDN | Cloudflare |
| Server-side framework | None |
| CMS | None |

Pushing `main` triggers `.github/workflows/pages.yml`. GitHub does not run the
site generators during deployment; the workflow packages checked-in output.

## Current Inventory

| Inventory | Current value | Canonical evidence |
|---|---:|---|
| Supported languages | 4 | `build_sitemap.py` `LANGS` |
| English path patterns | 53 | `build_sitemap.py` `PAGES` |
| Indexable sitemap URLs | 212 | parsed `sitemap.xml` `<url>` entries |
| Tracked HTML files | 215 | filesystem enumeration |
| Indexable HTML files | 212 | sitemap-to-file resolution |
| Non-indexed HTML files | 3 | `404.html` plus legacy redirect stubs |
| Sitemap lastmod tags | 212 | parsed `sitemap.xml` |
| Unique sitemap lastmod values | 49 | parsed `sitemap.xml` |
| Registered brand service pages | 7 | `BRAND_ORDER` / `BRAND_CONFIG` |
| Project detail pages | 11 | `PROJECT_TILES` |
| Data-driven project definitions | 1 | `PROJECT_CONFIGS` |
| Blog posts | 7 | `BLOG_POSTS` |
| News articles | 3 | `NEWS_ARTICLES` |
| Harley Hub English page patterns | 3 | `harley_hub_data.py` `PAGE_CONFIG` |
| Generated general hub English pages | 6 | `build_new_pages.py` / `new_pages_data.py` |
| Authorized Dealer English page patterns | 2 | `build_authorized_dealer.py` |
| Legal English page patterns | 3 | `LEGAL_PAGES` |

Language roots:

- English: `/`
- Portuguese: `/pt/`
- Russian: `/ru/`
- Ukrainian: `/uk/`

The tyre-service family intentionally uses localized slugs. Read them from
`build_sitemap.py` `LANG_PATHS`; do not infer them from the English slug.

Registry alignment on the evidence date:

| Registry | Entries | Relationship |
|---|---:|---|
| `build_sitemap.py` `PAGES` | 53 | canonical English indexable paths |
| `localize_internal_links.py` `LOCALIZED_PATHS` | 53 | matches `PAGES` after normalization |
| `build_i18n.py` `MAIN_PAGES` | 31 | English sources localized by the generic i18n flow |
| `build_i18n.py` `PROJECT_PAGES` | 11 | project detail sources localized by the generic i18n flow |

There is no active `EN_PAGES` registry. The canonical English page registry is
`build_sitemap.py` `PAGES`.

## Current Cache-Bust Values

| Assets | Value | Scope |
|---|---|---|
| `assets/main.css`, `assets/main.js` | `20260724a` | every sitemap page |
| `assets/projects.css`, `assets/projects.js` | `20260710b` | project detail pages |

Different asset families may legally use different values. Each individual
asset must use one value site-wide. Change a value only when that asset changes.

## Current Page Families

### General And Commercial Pages

`/`, `/services/`, `/motorcycle-service/`, `/parts/`,
`/upgrades-tuning/`, `/custom/`, `/pre-purchase-inspection/`,
`/motorcycle-tyre-service/`, `/pricing/`, `/projects/`, `/about/`,
`/community/`, `/contact/`, `/faq/`,
`/english-speaking-motorcycle-workshop/`, `/authorized-dealer/`,
`/blog/`, `/news/`, `/privacy/`, `/cookies/`, and `/terms/`.

The expat workshop page is intentionally footer-only and contextual-link-only;
it is not a top-navigation item.

### Harley Hub

- `/harley/`
- `/harley-tuning/`
- `/harley-custom/`

The existing `/harley-service/` page is the independent service spoke. Blog
feed membership comes from `BLOG_POSTS[*].topics`.

### Brand Service Pages

The current ordered inventory is the brands registered in `BRAND_ORDER`.
These are independent workshop pages, not authorized motorcycle-brand dealer
pages.

### Authorized Dealer

- `/authorized-dealer/`
- `/authorized-dealer/c-way/`

This is a separate official parts/accessories channel. The C-Way page currently
contains 6 visible priced configurations and 6 matching `Product`/`Offer`
entities, with no partial duplicate products.

### Projects

- `/projects/inspirium/`
- `/projects/beckman/`
- `/projects/unbreakable/`
- `/projects/quanta-r/`
- `/projects/burly/`
- `/projects/sturmvogel/`
- `/projects/geometric/`
- `/projects/joker/`
- `/projects/hellboy/`
- `/projects/true-religion/`
- `/projects/fighter/`

`Fighter` is data-driven. The other current project pages retain legacy static
copy while shared post-processors maintain common behavior.

Legacy noindex redirects:

- `/projects/nezlamniy/` -> `/projects/unbreakable/`
- `/projects/quanta/` -> `/projects/quanta-r/`

### Blog

- `/blog/revtech-110-oil-service-engine-gearbox-drive/`
- `/blog/motorcycle-brake-pad-replacement-cascais/`
- `/blog/front-fork-service-motorcycle-cascais/`
- `/blog/motorcycle-tyre-fitting-specialist-cascais/`
- `/blog/royal-enfield-bear-650-fork-oil-case-study/`
- `/blog/harley-davidson-full-service-done-right/`
- `/blog/royal-enfield-bear-650-scrambler-build/`

### News

- `/news/ericeira-kustom-fest-2026/`
- `/news/opens-new-workshop-in-cascais/`
- `/news/lisbon-motorcycle-film-fest-2026-beckman/`

## Current Delivery And Discovery State

- Every sitemap page has canonical, mutual hreflang and Schema.org JSON-LD with
  at least `BreadcrumbList`.
- Every sitemap page has an early hero discovery hint.
- CSS-background heroes use matching responsive preload/background candidates
  at the maintained viewport boundaries.
- Legacy project heroes use responsive AVIF/WebP/JPEG `<picture>` delivery.
- `llms.txt` is generated from the English page registry, maintained page-name
  sources, metadata and `docs/BUSINESS_FACTS.md`.
- `robots.txt` advertises both `sitemap.xml` and `llms.txt`.
- `sitemap.xml` uses stable, per-page content dates rather than deployment time.

Open performance caveats and external verification limits are in
`docs/OPEN_TASKS.md`.

## External Services And Public Identifiers

| Service | Current public identifier or endpoint |
|---|---|
| Reviews Worker | `https://icm-reviews.vg-ab6.workers.dev/` |
| Google Analytics | `G-D15BLYEKBN` |
| Meta Pixel | `1708697916976439` |
| FormSubmit inbox | `Ironcustom.office@gmail.com` |

The Google Places API key is a Cloudflare Worker secret and must never appear
in client files or documentation. Account-only risks and verification limits
live in `docs/OPEN_TASKS.md`; variable names live in `.env.example`.

## Current Build Ownership

The exhaustive script/input/output/validator inventory and every executable
command sequence live in `scripts/build/README.md`. Page-family ownership and
stable implementation rules live in `docs/CONTENT_TYPES.md`.

The full documented rebuild currently requires macOS because
`build_pricing_pdfs.py` uses macOS system Arial paths. This is an open
portability risk, not a cross-platform guarantee.

## Corrections Recorded By The FINAL Audit

- **Previous statement:** `HANDOFF.md` contained stale counts and should be
  treated as a current-state conflict.
  **Correction (2026-07-31):** C1 already converted `HANDOFF.md` into a thin
  historical entry point with no competing inventory. Evidence: file review.
- **Previous statement:** all build scripts were path-portable and Python 3.8+
  was sufficient.
  **Correction (2026-07-31):** source syntax requires Python 3.10+, and the PDF
  generator has macOS-only font paths. Evidence: source inspection and a clean
  environment build audit.
- **Previous statement:** one cache-bust value described the whole site.
  **Correction (2026-07-31):** main and project asset families have independent
  values, recorded above. Evidence: sitemap HTML asset scan.
- **Previous terminology:** `EN_PAGES` was treated as a current registry in a
  prior task report.
  **Correction (2026-07-31):** no such registry exists; `PAGES` is canonical.

## Recovery Answer

For a new session: this repository is the production static marketing site for
Iron Custom Motors. Its current inventory is above. There is no active
implementation task recorded; unresolved performance, portability, CDN and
external-account work is in `docs/OPEN_TASKS.md`. Read the affected family in
`docs/CONTENT_TYPES.md`, then use only `scripts/build/README.md` for commands.

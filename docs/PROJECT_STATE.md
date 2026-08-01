# Iron Custom Motors Website: Project State

Last updated: 2026-08-01

This is the only documentation file that owns current inventories, counts,
deployed public identifiers and cache-bust values. Operating rules live in
`AGENTS.md`; page ownership lives in `docs/CONTENT_TYPES.md`; commands live in
`scripts/build/README.md`.

## Status And Evidence

- Status: **confirmed**.
- Evidence date: 2026-08-01 (Europe/Lisbon).
- Repository evidence: CWAY-VAT size follow-up commit `8447160b`, CWAY-VAT
  implementation commit `560e3891`, EXPO-V2
  implementation commit `aa23075c`, NAV+EXPO
  implementation commit `6a2bdff7`, P-COCKTAIL implementation commit
  `e3ef595c`, the earlier C8 implementation commits `ce25a7c2` and `f42fb5d0`,
  and C8-FIX implementation commit `52316a26`.
- Inventory method: import the maintained Python registries, parse
  `sitemap.xml`, and enumerate tracked `*.html` files.
- Cache-bust method: scan asset references in every sitemap HTML file.
- Production evidence: CWAY-VAT size follow-up workflow `30716569527`,
  CWAY-VAT GitHub Pages workflow `30715488709`,
  cache-bypass checks on all four C-Way pages and the production sitemap,
  EXPO-V2 GitHub Pages workflow `30713880464`,
  cache-bypass checks on all 12 exhibition pages and four project listings,
  byte-identical production project CSS and sitemap, and Google Rich Results
  result `QtK8FJYbOvDZFu-k-TWBng` with four valid items, no errors and no
  warnings. Earlier evidence remains in the task reports and changelog.
- Reproducibility evidence: the documented full rebuild and all four validator
  groups at CWAY-VAT size follow-up commit `8447160b` left a clean clone with
  empty `git status --short`; verified 2026-08-01. The current `sitemap.xml`
  SHA-256 is
  `34ae75b4e6484387ee8eb2011523796dd7a83aa125bf39597efc6ffb666c2cd3`.
  The earlier repository audit baseline was documentation commit `d08a3297`.

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
| English path patterns | 54 | `build_sitemap.py` `PAGES` |
| Indexable sitemap URLs | 216 | parsed `sitemap.xml` `<url>` entries |
| Tracked HTML files | 225 | filesystem enumeration |
| Indexable HTML files | 216 | sitemap-to-file resolution |
| Non-indexed HTML files | 9 | `404.html` plus 8 localized project redirect stubs |
| Sitemap lastmod tags | 216 | parsed `sitemap.xml` |
| Unique sitemap lastmod values | 52 | parsed `sitemap.xml` |
| Registered brand service pages | 7 | `BRAND_ORDER` / `BRAND_CONFIG` |
| Project detail pages | 12 | `PROJECT_TILES` |
| Data-driven project definitions | 12 | `PROJECT_CONFIGS` |
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
| `build_sitemap.py` `PAGES` | 54 | canonical English indexable paths |
| `localize_internal_links.py` `LOCALIZED_PATHS` | 54 | matches `PAGES` after normalization |
| `build_i18n.py` `MAIN_PAGES` | 31 | English sources localized by the generic i18n flow |
| `project_pages_data.py` `PROJECT_CONFIGS` | 12 | project details rendered directly in four languages |

There is no active `EN_PAGES` registry. The canonical English page registry is
`build_sitemap.py` `PAGES`.

## Current Cache-Bust Values

| Assets | Value | Scope |
|---|---|---|
| `assets/main.css`, `assets/main.js` | `20260724a` | every sitemap page |
| `assets/projects.css` | `20260801a` | project detail pages |
| `assets/projects.js` | `20260710b` | project detail pages |

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
entities, with no partial duplicate products. Each visible configuration price
repeats the existing VAT-exclusion wording in the page language; the summary
price note and schema tax fields remain unchanged. The page-scoped suffix is
17 px in every language, approximately 31% larger than its original 13 px
release size.

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
- `/projects/cocktail/`

All 12 project details are data-driven and rendered through
`build_project_pages.py`. Fighter and Cocktail use approved Markdown; the 10
migrated projects use the versioned localized source at
`content/projects/legacy_projects_4lang.json`. Generated project HTML contains
no `window.ICM_I18N_PAGE` copy block.

Sturmvogel, Beckman and Hell Boy are confirmed in the permanent workshop
exhibition beside the rider lounge. Their four-language project pages use the
registered responsive exhibition split: photo on the left and text on the
right at desktop widths, then photo above text on mobile. The media uses
dimensioned lazy AVIF/WebP with JPEG fallback and localized approved ALT text.
The Hell Boy listing year is `2025` in every language.

Localized noindex redirects, intentionally excluded from the sitemap:

- `/projects/nezlamniy/` -> `/projects/unbreakable/`
- `/projects/quanta/` -> `/projects/quanta-r/`

The same redirect relationship exists under `/ru/`, `/uk/` and `/pt/`.

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
- Blog article `<picture>` heroes use one AVIF preload whose `imagesrcset` and
  `imagesizes` mirror the rendered AVIF source; the hero `<img>` is the only
  `fetchpriority="high"` element on those pages.
- News article heroes remain in the CSS-background family protected by the
  responsive CSS hero contract; they are not `<picture>` heroes.
- Project heroes retain responsive `<picture>` delivery. Migrated projects and
  Cocktail use AVIF/WebP sources with a JPEG fallback; Fighter retains its
  registered AVIF/WebP media set. Every project page has one responsive AVIF
  preload and exactly one `fetchpriority="high"` hero image.
- Registered project exhibition media is rendered through the common project
  generator from `PROJECT_EXHIBITION_MEDIA`; its picture stays lazy and never
  receives high fetch priority.
- Project detail chrome is pre-rendered from the same `GLOBAL_I18N` source as
  the matching language homepage. Sitemap-wide validation compares cookie,
  booking, WhatsApp, header/mobile and footer chrome strings against that
  same-language baseline.
- The desktop and mobile Projects menus derive from `PROJECT_TILES`, the same
  ordered registry as `/projects/`. Sitemap-wide validation protects all 12
  localized project links on every indexable page.
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

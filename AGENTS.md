# Project instructions for AI agents

This file is read by AI coding agents (Codex, Cursor, Cline,
Claude Code etc.) before doing work. Read it fully on every
session start.

For project facts (URLs, IDs, what is deployed where) read
`HANDOFF.md`. For commit history read `CHANGELOG.md`. For build
scripts read `scripts/build/README.md`.

## How to operate in this repo

- The repo is a static site (HTML, CSS, JS). There is no
  framework, no build step on the server side, no test suite.
  GitHub Pages serves files in `main` branch root as-is.
- Most editing tasks fall into one of three modes:
  1. Direct file edits (typo, copy tweak, style fix).
  2. Run a Python generator under `scripts/build/` to regenerate
     a family of pages from a data file.
  3. Both, in some order.
- After any change to `assets/main.css` or `assets/main.js`,
  bump the cache-bust query (`?v=...`) on every HTML file. The
  convention is `?v=YYYYMMDD<letter>`. The latest value at the
  time of writing is `20260603a`.
- When the project owner asks Codex to do implementation work,
  treat the request as an end-to-end delivery by default: make
  the change, run the relevant verification, commit, push, and
  verify the result after the push. Do not stop at a proposal or
  an unpushed working tree unless the owner explicitly says
  "no commit", "no push", "analysis only", "draft", or gives
  another limiting instruction.
- Verification does not stop at `git push`. After every push,
  automatically verify the exact work that was pushed. For site
  changes, check the public production URLs after deployment
  whenever possible, confirm the relevant pages/assets/schema are
  live, and report any external checks that cannot be performed
  without account access.

## File-by-file routing

- Site-wide copy → look first in `assets/main.js` (`I18N` object,
  keys like `nav.services`, `cta.bookHeader` etc.). If the copy
  appears in pre-rendered HTML, it must be updated in BOTH
  `main.js` AND every language's pre-rendered HTML — running
  `scripts/build/build_i18n.py` keeps them in sync.
- Per-page copy that is specific to one page (e.g. the
  `/bmw-service/` body text) lives in
  `scripts/build/<feature>_data.py`. Editing the data file and
  re-running the matching `build_*.py` script regenerates the
  HTML.
- Project pages (`/projects/<slug>/`) have their copy in inline
  `<script>window.ICM_I18N_PAGE = {...}</script>` blocks at the
  top of each project HTML. There is no separate generator for
  these — they were authored once.
- News articles live in `scripts/build/news_data.py`. To add
  one, add an entry to `NEWS_ARTICLES`, then run
  `build_news.py`.
- Brand service pages (BMW, HD, Ducati) are in
  `scripts/build/brand_pages_data.py`. Same flow: edit data, run
  `build_brand_pages.py`.
- Pricing tables are in `scripts/build/pricing_data.py`. Edit
  and re-run `build_pricing.py`.
- Legal pages (Privacy, Cookies, Terms) are in
  `scripts/build/legal_pages_data.py`.
- The 5 hub pages (`/services/`, `/projects/`, `/about/`,
  `/contact/`, `/faq/`) are in `scripts/build/new_pages_data.py`.

## Non-negotiables

- Multilingual parity. Every public page exists in 4 languages.
  Do not introduce a page that only exists in English.
- Internal link locality. A page under `/ru/` must link to other
  `/ru/` pages, not to the English root. `localize_internal_links.py`
  enforces this; run it after generating HTML.
- Absolute asset paths. Use `/photos/...` and `/assets/...`, not
  relative `../`. Relative paths break inside language subtrees.
- Schema.org JSON-LD on every indexable page. At minimum a
  `BreadcrumbList`. The site relies on this for both Google and
  AI engine citation.
- Cache-bust. Every change to `assets/main.css` or `assets/main.js`
  must come with a cache-bust bump across every HTML file.
- Sitemap and `hreflang` consistency. New pages go into
  `scripts/build/build_sitemap.py` PAGES list AND get hreflang
  alternates on every language variant. New page paths also go
  into `scripts/build/localize_internal_links.py` LOCALIZED_PATHS.

## Conventions

- Cache-bust query string format: `?v=YYYYMMDD<letter>`.
- Localized subtrees: `/ru/`, `/uk/`, `/pt/` (lowercase ISO 639-1).
- Default language is English at `/`.
- Tone of copy: premium, restrained, engineering-driven. No
  emojis in copy. Brand names of motorcycles are kept in their
  original spelling across all four languages (Beckman,
  Multistrada, Pan America, R nineT, Desmo).
- The project owner asked that the brand stay "independent" —
  do not call the workshop an authorized dealer of BMW / Harley
  / Ducati. The phrasing in current copy is "Independent BMW
  Motorrad workshop", "Independent Harley specialist",
  "Independent Ducati workshop". Maintain this phrasing.
- "Iron Custom Motors" is the brand name and stays untranslated.
- All Google review surfacing goes through the Cloudflare Worker
  at `https://icm-reviews.vg-ab6.workers.dev/`. Do not put the
  Google Places API key in the client-side site.

## Common task templates

### Add or edit a translation string

1. Edit the key in the `I18N` object inside `assets/main.js`.
2. `node scripts/build/extract_i18n.js` (writes
   `scripts/build/i18n.json`).
3. `python3 scripts/build/build_i18n.py` (regenerates `/ru/`,
   `/uk/`, `/pt/` pages from the EN sources).
4. `python3 scripts/build/localize_internal_links.py`.
5. Bump cache-bust in HTML files.

### Add a new service / hub page

1. Add content to `scripts/build/new_pages_data.py`.
2. Add a renderer to `scripts/build/build_new_pages.py` modelled
   on the existing ones.
3. Add a meta entry to `scripts/build/page_meta.py` (or rely on
   the auto-import that already exists).
4. Add the slug to `scripts/build/build_i18n.py` MAIN_PAGES.
5. Add the slug to `scripts/build/build_sitemap.py` PAGES.
6. Add the slug to `scripts/build/localize_internal_links.py`
   LOCALIZED_PATHS.
7. Add the slug to `scripts/build/nav_patch.py` EN_PAGES list (so
   the page itself gets the standard nav).
8. Run the pipeline in this order:
   - `build_new_pages.py`
   - `nav_patch.py`
   - `build_i18n.py`
   - `localize_internal_links.py`
   - `build_sitemap.py`
9. Bump cache-bust.

### Add a news article

1. Drop processed JPEG photos into `photos/news/` named
   `news-<slug>-NN-1600.jpg` and `news-<slug>-NN-800.jpg`
   (NN = 01, 02, …). See `scripts/build/README.md` for the
   Pillow snippet that resizes raw photos.
2. Add a new entry to `NEWS_ARTICLES` in `scripts/build/news_data.py`
   with translations for all 4 languages, an `imageBase`, an
   `imageCount`, an `imageHero` and an `imageMap` for figure
   placement.
3. Add the slug to `scripts/build/build_i18n.py` MAIN_PAGES.
4. Add the slug to `scripts/build/build_sitemap.py` PAGES.
5. Add the slug to `scripts/build/localize_internal_links.py`
   LOCALIZED_PATHS.
6. Add the slug to `scripts/build/nav_patch.py` EN_PAGES list.
7. Run:
   - `build_news.py`
   - `build_i18n.py`
   - `localize_internal_links.py`
   - `build_sitemap.py`
8. Bump cache-bust.

### Update Google reviews snapshot

This must be run on a machine with outbound network access.

```
python3 scripts/build/build_reviews_schema.py
```

The script fetches `https://icm-reviews.vg-ab6.workers.dev/`,
writes `assets/reviews-snapshot.json`, and injects
`AggregateRating` plus 8 `Review` items into the LocalBusiness
JSON-LD on the four home pages.

## What this site does NOT have (do not assume)

- No build step on GitHub side.
- No CMS.
- No test suite.
- No type checking.
- No backend other than FormSubmit and the Cloudflare Worker.
- No Google Tag Manager container (events go to `dataLayer`
  via `gtag` directly; no GTM loader).
- No admin UI.

If a task seems to require any of the above, stop and ask the
project owner before introducing one.

# P-FETISH Delivery Report

Date: 2026-08-03

Status: **confirmed**

## Outcome

Fetish is the thirteenth registered project and is live in English,
Portuguese, Russian and Ukrainian. It uses the shared Markdown-backed project
generator introduced for the reusable project family; no project-specific
renderer or manually maintained project HTML was added.

Implementation commit: `a0da49fd99d3bd1f5efd8e460bd84f376458d82e`.

GitHub Pages workflow: `30852768505` (`success`, 43 seconds).

## Canonical Inputs And Dates

- Approved copy: `content/projects/fetish_4lang.md`.
- The repository copy is byte-identical to the supplied file; SHA-256:
  `e7b75e9be859796c67aab8304f365487a1e3d773bc1055dd2859ddff8b1ac2ff`.
- Header-only `[VERIFY]` and integration notes are retained as source context
  and are not rendered on the public pages.
- Publication and modification time:
  `2026-08-03T21:43:44+01:00`.
- Project year: `2013`.
- Base: `Harley-Davidson Rocker C`.
- Category: localized `Chopper · Full Custom`.
- Location: localized `Built in Kharkiv, Ukraine`.
- Hero: `Fetish-Hero.jpg`; gallery: the thirteen other approved source JPEGs
  in the registered order.

The approved source does not establish the 2013 AMD result or current
whereabouts. The public copy deliberately states participation only and makes
no current-location claim; the open evidence boundary is recorded in
`docs/OPEN_TASKS.md`.

## Reusable Architecture

- `MARKDOWN_PROJECT_CONFIGS` remains the single registration point for new
  Markdown-backed project details.
- `build_project_pages.py` renders all thirteen registered projects in all four
  languages; Fetish has no separate generator.
- `PROJECT_TILES` owns project listing and shared desktop/mobile navigation
  order, so one registry entry added Fetish to every indexable page.
- `build_new_pages.py` now derives `/custom/` project mentions from
  `integrations.custom`; future registered Custom projects do not need manual
  output patches.
- Harley portfolio text and order remain explicit in `harley_hub_data.py`,
  because not every project is Harley-based.
- `reciprocal_projects` declares the Cocktail/Fetish relationship, and
  `validate_project_pages.py` now requires same-language links in both
  directions.

## Changed File Manifest

Implementation commit `a0da49fd` contains 325 files:

- 4 new project outputs:
  `projects/fetish/index.html`, `pt/projects/fetish/index.html`,
  `ru/projects/fetish/index.html`, `uk/projects/fetish/index.html`;
- 216 existing indexable HTML files with the new registry-derived project menu;
  200 changed only in shared chrome;
- 16 existing integration outputs whose `<main>` changed:
  `/projects/`, `/custom/`, `/harley-custom/` and `/projects/cocktail/` in all
  four languages. The first twelve gained visible Fetish integration content;
  Cocktail gained only the required contextual link around existing visible
  text;
- 2 maintained content files: the new Fetish source and the reciprocal-link
  update in `content/projects/cocktail_4lang.md`;
- 5 build/data/validation files: `build_new_pages.py`,
  `harley_hub_data.py`, `new_pages_data.py`, `project_pages_data.py` and
  `validate_project_pages.py`;
- `sitemap.xml` and generated `llms.txt`;
- 96 responsive media files: 9 detail-hero variants, 78 gallery variants and
  9 Harley portfolio variants across AVIF, WebP and JPEG.

The 8 localized redirect stubs, `404.html`, common CSS/JS, project CSS/JS and
all cache-bust values are unchanged.

## Copy And Localization Evidence

For EN/PT/RU/UK, title, meta description, H1, tagline, all body sections and
the closing block match the parsed canonical Markdown exactly. The header
notes are absent. Every gallery image has a localized ALT from the registered
language data, and PT/RU/UK pages use the same localized chrome source as their
language homepages.

The generated whole-main visible-text SHA-256 values are:

| Language | SHA-256 |
|---|---|
| EN | `ccc81f268049b436bf4cda774f97c8e0e72028de9b74632e1a892f5074325d1f` |
| PT | `28418597272c26dfce084d75c058a39927479cd000c181d6fb1e0fcac6c6fcc7` |
| RU | `d92f18f390620eb9735174e91f5a4e511ca72afb369c76c9bde7e8632e9edfb0` |
| UK | `bf59c4080b1586cf0bfe2ab78b4d4d54f77c2affa77a6f164b575baee6211358` |

Cocktail visible text remains identical before and after the reciprocal link;
the comma is inside the linked text so normalized text has no whitespace
change.

## Hero And Network Evidence

The hero AVIF preload and rendered AVIF source use identical `imagesrcset` and
`imagesizes="100vw"`. Static candidate resolution therefore selects the same
file for preload and paint:

| Profile | Selected candidate |
|---|---|
| 390 CSS px / DPR 3 | `fetish-1600.avif` |
| 390 CSS px / DPR 2 | `fetish-800.avif` |
| 768 CSS px / DPR 2 | `fetish-1600.avif` |
| 1280+ CSS px / DPR 1 | `fetish-1600.avif` |

Production browser observation at 390 x 844 CSS pixels / DPR 1 with a unique
cache-bypass query:

```text
currentSrc: https://ironcustommotors.com/photos/projects/fetish-800.avif
observed Fetish hero resources: 1
fetchpriority="high" elements: 1
fetchpriority="high" + loading="lazy": 0
horizontal overflow: 0 px
console errors and warnings: 0
```

Local browser checks at 390 x 844 and 1440 x 1000 observed the same one-resource
contract, selected the 800 and 1600 AVIF candidates respectively, and found no
horizontal overflow.

## Schema And Discovery Evidence

- Each page contains the common Article/WebPage/ImageObject/LocalBusiness and
  localized BreadcrumbList graph.
- `datePublished` and `dateModified` use the full maintained ISO timestamp.
- Article publisher/author resolve through `@id` to the complete
  LocalBusiness entity with maintained name and logo.
- Each page has a self-canonical and the mutual EN/PT-PT/RU/UK plus x-default
  hreflang set.
- Generated `llms.txt` contains the English Fetish URL.
- Local schema and family validation passed. Google Rich Results UI was not a
  P-FETISH acceptance requirement and was not run; no account-only result is
  claimed.

## Sitemap Evidence

- Before: 216 URLs; after: 220 URLs.
- Added exactly the four Fetish URLs with
  `2026-08-03T21:43:44+01:00` lastmod.
- Removed URLs: none.
- Changed existing lastmod exactly for these 12 visible integration pages:
  `/projects/`, `/custom/` and `/harley-custom/` under EN/PT/RU/UK.
- Cocktail lastmod did not move because its visible text did not change.
- All other existing lastmod values are byte-identical to baseline
  `844aa964`.
- Final sitemap SHA-256:
  `c675fb2d21f9918e53cb7e7dcd5fe9f17634258b0f900c07c33654dd711fbd21`.
- The cache-bypassed production sitemap has 220 `<loc>` entries, exactly four
  Fetish entries, and is byte-identical to the repository sitemap.

## Production Evidence

All four cache-bypassed project URLs returned HTTP 200. Their normalized
`<main>` text equals the deployed repository output, and every page has the
correct self-canonical, complete hreflang cluster and one high-priority hero.

For every language, production checks found Fetish twice in shared navigation
(desktop and mobile), in the `/projects/`, `/custom/` and `/harley-custom/`
main content, and as the target of the contextual link from Cocktail.

## Reproducibility And Validation

The documented Full Safe Rebuild was run on macOS in a clean clone of
`a0da49fd`, with the maintained `.venv` activated. It included pricing PDF
generation and all four validator groups. Final `git status --short` was empty.
The temporary clone was moved to Trash after verification and is recoverable
until the Trash is emptied.

Exact validator output:

```text
SEO validation passed: 220 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
OK: beckman project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: burly project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: cocktail project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: fetish project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: fighter project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: geometric project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: hellboy project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: inspirium project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: joker project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: quanta-r project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: sturmvogel project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: true-religion project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
OK: unbreakable project page passed multilingual copy, media, schema, cache-bust, redirect and integration checks
```

JavaScript syntax checks, Python compilation and `git diff --check` also
completed successfully and produced no output.

## Acceptance Criteria

1. **PASS** — four production URLs return 200 and exact approved copy is live.
2. **PASS** — all four validator groups pass, including project navigation and
   same-language chrome parity.
3. **PASS** — the Full Safe Rebuild leaves a clean clone.
4. **PASS** — changed scope is the four new pages, registry-driven chrome,
   exact integration pages, maintained data/generators, sitemap, llms and
   approved responsive media; common CSS/JS and cache-bust are unchanged.
5. **PASS** — preload and paint resolve to the same hero candidate for all
   required viewport/DPR profiles; one production hero resource was observed.
6. **PASS** — sitemap adds four URLs and moves only the twelve visible
   integration-page lastmods listed above.

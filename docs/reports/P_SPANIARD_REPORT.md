# P-SPANIARD delivery record

Date: 2026-10-28. Status: local acceptance passed; clean-clone and production checks pending.

## Scope and decisions

- Confirmed baseline / first implementation parent:
  `660c65b385beb62dd2b4176d1100aa80200183f1`.
- Publish the approved Spaniard project and news article in EN, PT, RU and UK.
  Register the project in the catalog, Custom hub, Harley Custom portfolio,
  shared navigation, discovery files and reciprocal project links.
- Preserve the approved source bytes and pin both SHA-256 values. Use the
  existing project importer for one shared photo set, including the supplied
  plate-cropped photo 06. Project gallery ALT text comes from the manifest;
  News gallery ALT text comes from its approved localized pattern.
- Confirmed by source/DOM inspection: the homepage has seven curated projects
  and no news feed. Harley Service has contextual links, not the shared Harley
  Custom portfolio. Neither main-content area changes.
- Confirmed: reciprocal project links are two-way. Add missing links from
  registry data without changing the existing approved Markdown prose.
- Confirmed: News related cards otherwise include every new article in all old
  articles. Pin the existing related selections to preserve their content and
  dates; the new article links to the existing stories.
- Shared navigation will change across the site, as required by the project
  registry. Navigation-only changes do not move content dates. Shared CSS/JS
  cache keys change only if those files actually change.

## Implementation and verification plan

1. Register the source data and shared media; extend the existing News parser
   and renderer for approved Markdown links and reusable project pictures.
2. Render all integrations, pin visible project text, and rebuild discovery.
3. Check exact copy, links, media metadata, dates and all release validators;
   inspect PT pages at 390/1440 and mobile DPR 2/3.
4. Commit, run Full Safe Rebuild in a clean full-history clone, push, verify
   production pages/assets and run both requested Google Rich Results tests.
5. Record deployment evidence, exact changed URL dates, image weights and any
   limitations here and update the canonical project handoff documents.

No changes to prices, existing prose, forms, Workers, secrets, analytics,
reviews or external business profiles are authorized by this task. Dyno work
remains deferred.

## Approved inputs and implementation

- Project source: `content/projects/spaniard_4lang.md`, SHA-256
  `a790f356917ad14509d339f2cf8dcb28e77fcb460d026baf4816c7a545c40408`.
- News source: `scripts/build/content/spaniard_news_4lang.md`, SHA-256
  `49aa8aeb58990720fbd3daf26014bcc6c579642f81bc15055d4959dad6053714`.
- Both files are byte-identical to the owner-approved deliveries. Independent
  one-byte mutation tests stopped each loader with a checksum error; original
  bytes were restored and rechecked.
- The media manifest is preserved at `content/projects/spaniard-media-manifest.md`.
  [Media evidence](P_SPANIARD_MEDIA.json) records source/output hashes, dimensions,
  file weights and EXIF checks. All six photo-06 outputs were independently
  reproduced byte-for-byte from the supplied 1934 × 2331 crop.
- The shared News parser now handles the approved standard Markdown links as
  well as the BBQ delivery tokens. It enforces a single H1/lead, four sections
  and the gallery after section two. A shared `validate_news.py` release gate
  compares complete approved copy, related selections and media contracts.
- `responsive_images.py` shares the existing project picture renderer with
  News and the new Harley portfolio item. No duplicate image set was created.
- Reciprocal links are two-way: Spaniard links to Cocktail, Fetish and The First;
  each links back through the registry. Existing contextual prose is unchanged.
- Homepage: its seven curated project tiles and absence of a news block were
  confirmed by source/DOM inspection. Main content and lastmod are unchanged.
  Harley Service has contextual links, not this portfolio; its main content and
  lastmod are also unchanged. Both receive the shared navigation entry.
- Shared CSS/JS, cache keys, reviews snapshot/curation, Workers, form actions and
  pricing/PDF outputs are unchanged. No external business-profile writes occurred.

## Local acceptance evidence

- Full Safe Rebuild passed, including PDFs and all existing validator families;
  all 15 project validators passed. The new News validator passed for both
  approved-source articles in all four languages and every related selection.
- Whole-page comparison: all 15 project body/heading/closing units and all 10
  News lead/heading/paragraph units match in each language. Project UI, metadata,
  hero ALT and all gallery ALTs also match their registered approved sources.
- Each new page has one H1, one high-priority hero, ten lazy gallery images,
  complete self-canonical/hreflang and the appropriate complete schema graph.
- Independent semantic comparison with baseline: exactly 28 existing main
  content pages changed. All other existing page-body/head semantics stayed
  unchanged. Navigation changed through the required registry-driven menus.
- Link audit: 45616 local asset/link destinations across
  all 261 HTML files, zero missing destinations.
- Playwright 1.64.1 with installed Chrome: PT project and PT News at 390 × 844
  / DPR 2, 390 × 844 / DPR 3 and 1440 × 1000 / DPR 1. All six profiles had zero
  horizontal overflow, zero JavaScript errors and zero failed HTTP responses.
  Project lightbox photo 06 and News horizontal gallery navigation were exercised.
- Initial hero requests: exactly one in every profile. Mobile DPR 2 selected
  `spaniard-800.avif` (36,684 bytes); DPR 3 and desktop selected
  `spaniard-1600.avif` (102,178 bytes). Gallery images retain native lazy loading:
  no project gallery images requested before scrolling; Chrome prefetched two
  desktop / three mobile News slides within its native lazy-loading distance.
  Remaining slides load as approached. This is observed browser behavior, not
  a promise that native lazy loading requests zero nearby offscreen images.
- Visual inspection covered mobile/desktop heroes, gallery framing and the
  cropped seat photo in the lightbox. Mixed-orientation News slides use
  `object-fit: contain`; the complete supplied images remain visible.

## Added media weight

| Format | Files | Bytes |
|---|---:|---:|
| AVIF | 23 | 4,595,084 |
| WebP | 23 | 5,948,984 |
| JPEG | 23 | 8,996,621 |
| Total | 69 | 19,540,689 |

The total is 18.64 MiB in the repository, not the page's initial transfer. Hero
widths are 800/1600/2400; gallery widths are 800/1600. All outputs are re-encoded
and carry no EXIF. Project, News and integrations reuse the same files.

## Content dates and URL accounting

Publication timestamp for the new project and News: `2026-10-28T21:43:06+00:00`
(Europe/Lisbon; winter offset +00:00). Existing listing dates derive from actual
content changes using the existing sitemap generator; chrome-only changes do
not advance dates. No URL was renamed or redirected.

Eight newly published URLs:

- https://ironcustommotors.com/news/spaniard-v-rod-2002-rebuild/
- https://ironcustommotors.com/projects/spaniard/
- https://ironcustommotors.com/pt/news/spaniard-v-rod-2002-rebuild/
- https://ironcustommotors.com/pt/projects/spaniard/
- https://ironcustommotors.com/ru/news/spaniard-v-rod-2002-rebuild/
- https://ironcustommotors.com/ru/projects/spaniard/
- https://ironcustommotors.com/uk/news/spaniard-v-rod-2002-rebuild/
- https://ironcustommotors.com/uk/projects/spaniard/

Exactly 28 existing URLs advance; the other 208 existing dates remain unchanged.

| URL | Reason | New lastmod |
|---|---|---|
| `/custom/` | Spaniard Custom link | `2026-10-28T21:33:44+00:00` |
| `/harley-custom/` | Spaniard Harley portfolio item | `2026-10-28T21:33:54+00:00` |
| `/news/` | Latest News card | `2026-10-28T21:43:06+00:00` |
| `/projects/` | Spaniard project tile | `2026-10-28T21:43:36+00:00` |
| `/projects/cocktail/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |
| `/projects/fetish/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |
| `/projects/the-first/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |
| `/pt/custom/` | Spaniard Custom link | `2026-10-28T21:33:45+00:00` |
| `/pt/harley-custom/` | Spaniard Harley portfolio item | `2026-10-28T21:33:54+00:00` |
| `/pt/news/` | Latest News card | `2026-10-28T21:43:06+00:00` |
| `/pt/projects/` | Spaniard project tile | `2026-10-28T21:43:39+00:00` |
| `/pt/projects/cocktail/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |
| `/pt/projects/fetish/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |
| `/pt/projects/the-first/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |
| `/ru/custom/` | Spaniard Custom link | `2026-10-28T21:33:44+00:00` |
| `/ru/harley-custom/` | Spaniard Harley portfolio item | `2026-10-28T21:33:54+00:00` |
| `/ru/news/` | Latest News card | `2026-10-28T21:43:06+00:00` |
| `/ru/projects/` | Spaniard project tile | `2026-10-28T21:43:43+00:00` |
| `/ru/projects/cocktail/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |
| `/ru/projects/fetish/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |
| `/ru/projects/the-first/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |
| `/uk/custom/` | Spaniard Custom link | `2026-10-28T21:33:44+00:00` |
| `/uk/harley-custom/` | Spaniard Harley portfolio item | `2026-10-28T21:33:54+00:00` |
| `/uk/news/` | Latest News card | `2026-10-28T21:43:06+00:00` |
| `/uk/projects/` | Spaniard project tile | `2026-10-28T21:43:48+00:00` |
| `/uk/projects/cocktail/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |
| `/uk/projects/fetish/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |
| `/uk/projects/the-first/` | Reciprocal Spaniard link | `2026-10-28T21:43:06+00:00` |

## Deviations and boundaries

- The task's "everything else changes by cache-bust only" wording conflicts
  with the required shared navigation addition. Other pages receive navigation
  only; no asset cache-bust is needed because shared CSS/JS bytes are unchanged.
- Existing News selections were explicitly pinned to avoid changing 16 older
  article pages and their dates outside the requested list.
- The requirement "project family 15, news family 2" is recorded as 15 registered
  projects and two Markdown-backed News deliveries; the complete News registry
  contains five articles. Current inventories belong in `PROJECT_STATE.md`.
- No new CMS, dependency for the public runtime, backend, price, service claim,
  owner identity or name-origin claim was introduced. Existing deferred risks
  remain in `OPEN_TASKS.md`.

## Deployment and external acceptance

Pending: implementation SHA, clean-clone rebuild, Pages run, production parity
and the two live Google Rich Results reports. These are not yet claimed passed.

Rollback: revert this task's implementation and evidence commits only; no
external service state needs rollback.

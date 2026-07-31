# Codex Compact Changelog

This is a high-signal memory log for Codex after context compaction. It does
not replace Git history. Add one short entry after each meaningful site task.

Format:

```md
## YYYY-MM-DD - Short task title

- Commit: `<hash>`
- Changed: ...
- Verified: ...
- Notes: ...
```

## 2026-07-31 - Sitemap-wide hero image delivery

- Commit: `3309b45b`
- Changed: Added early LCP image discovery to every sitemap page, responsive
  AVIF preloads for CSS heroes, and shared AVIF/WebP/JPEG `<picture>` delivery
  for legacy project heroes without changing their visual treatment.
- Verified: LCP coverage and image-attribute validation, semantic HTML
  invariants, desktop/mobile visual parity, unchanged sitemap lastmod and
  cache-bust values, focused validators, and `git diff --check`.
- Notes: The legacy project source registry remains `PROJECT_TILES`; binary
  hero optimization is explicit and remains outside the canonical full build.

## 2026-07-31 - Reproducible static-site builds

- Commit: `fc25c4a4`
- Changed: Made every maintained generator and post-processor idempotent,
  corrected localized pricing CTAs, centralized semantic output preservation,
  restored real historical hashes, and made the build README canonical.
- Verified: Every executable build tool individually, the complete documented
  rebuild on a clean worktree, all focused validators, immutable sitemap
  lastmod/cache-bust values, protected-file scope, and `git diff --check`.
- Notes: The obsolete root changelog was removed in favor of this maintained
  compact journal; the deferred pre-purchase discovery summary remains tracked
  in `docs/OPEN_TASKS.md` because C6 prohibited an `llms.txt` change.

## 2026-07-31 - Pre-purchase inspection fixed price

- Commit: `82bd35ef`
- Changed: Replaced starting-price wording with the fixed EUR 150 inspection
  price in all localized page copy, metadata and `Offer` schema; clarified the
  separately agreed on-site travel charge and added `WebPage.dateModified`.
- Verified: Exact multilingual copy, visible FAQ and `FAQPage` parity, one
  VAT-inclusive EUR 150 `Offer`, JSON-LD parsing, sitemap lastmod scope, all
  focused validators, and desktop/mobile browser layout checks.
- Notes: Travel remains a case-by-case charge agreed before booking; no rate,
  zone, radius or minimum is published.

## 2026-07-30 - Pricing breadcrumbs and cache validation

- Commit: `48009e44`
- Changed: Added standalone localized `BreadcrumbList` entities to generated
  pricing pages, centralized project-page asset versions in `CACHE_BUST`, and
  enforced breadcrumb and cache-bust invariants in `validate_seo.py`.
- Verified: Negative fixtures for all three new checks, full sitemap SEO
  validation, family validators, exact non-schema HTML preservation, unchanged
  cache-bust values and sitemap lastmod values, and `git diff --check`.
- Notes: Pricing lastmod values remain unchanged because this is a technical
  structured-data correction with no visible content change.

## 2026-07-30 - Shared site navigation and footer

- Commit: `f594df3b`
- Changed: Centralized desktop navigation, mobile navigation and footer
  rendering in `site_chrome.py`; connected standalone and page-family
  generators; made `nav_patch.py` sitemap-wide; and added same-language chrome
  parity and navigation-locality checks to `validate_seo.py`.
- Verified: Exact non-chrome byte preservation, sitemap and `llms.txt`
  immutability, generator inheritance, idempotency, focused validators,
  production-style desktop/mobile navigation checks and `git diff --check`.
- Notes: New sitemap pages inherit the same-language homepage menu and footer
  automatically, with brands sourced from `BRAND_ORDER` and `BRAND_CONFIG`.

## 2026-07-29 - AI discovery link labels

- Commit: `122dece4`
- Changed: Replaced marketing-heading anchors in generated `llms.txt` with
  stable page names sourced from navigation I18N and page-family registries;
  shortened news anchors to event names and reused the homepage meta
  description as the business introduction.
- Verified: Generator idempotency, exact sitemap-path coverage, missing-link
  rejection, focused validators, scope checks and `git diff --check`.
- Notes: The generator now fails when a sitemap path has no maintained source
  for its English page name instead of falling back to a published H1.

## 2026-07-29 - Generated AI discovery index

- Commit: `1842bb98`
- Changed: Added canonical business facts, generated `llms.txt` from maintained
  site registries and published metadata, declared it in `robots.txt`, and
  added complete sitemap coverage enforcement to SEO validation.
- Verified: Generator idempotency, business-fact and registry consistency,
  AI-index coverage, all focused validators, scope checks and
  `git diff --check`.
- Notes: `docs/BUSINESS_FACTS.md` is the canonical documentation source for
  NAP, identity, opening hours, origin, profiles, service languages and
  published key prices.

## 2026-07-29 - Repository documentation alignment

- Commit: `d13893a2`
- Changed: Removed the obsolete reviews script and legacy scripts README;
  aligned top-level agent documentation with the maintained project state,
  page-family ownership, review workflow and delivery rules.
- Verified: Documentation path searches, focused validators, broad SEO
  validation, scope checks and `git diff --check`.
- Notes: Current site quantities and the active cache-bust value belong only
  in `docs/PROJECT_STATE.md`; canonical workflows belong in
  `docs/CONTENT_TYPES.md` and `scripts/build/README.md`.

## 2026-07-27 - Fighter project page

- Commit: `6ea7118b`
- Changed: Added the Fighter project page in EN/PT/RU/UK from the approved
  Markdown source, responsive AVIF/WebP hero and 11-image gallery, project
  listing cards, global Projects menu links, structured data and sitemap URLs.
- Verified: Exact four-language source-copy checks; project-family and 212-URL
  SEO validation; schema, hreflang, canonical, localized-link and media checks;
  desktop and mobile browser layout checks.
- Notes: Fighter is the first page on the reusable data-driven project-page
  flow. It is intentionally absent from Harley Hub and Harley Custom content.

## 2026-07-27 - Homepage project selection

- Commit: `b6ec5921`
- Changed: Reduced the homepage project section on EN/PT/RU/UK to the featured
  Beckman project plus six standard cards in two desktop rows, and added a
  localized all-projects CTA.
- Verified: Four-language card order and link checks; 208-URL SEO validation;
  desktop and mobile browser layout checks; responsive overflow and console
  checks.
- Notes: Joker, Hell Boy and True Religion remain available in the complete
  projects catalogue and on their individual pages. Homepage project selection
  continues to be maintained directly in the four homepage files.

## 2026-07-24 - Homepage hero and Harley visual alignment

- Commit: `754c8256`
- Changed: Stopped the homepage hero heading from moving independently during
  scroll on EN/PT/RU/UK, and aligned the 12 Harley Hub pages with the approved
  site hero darkening, typography scale and compact vertical rhythm.
- Verified: Harley Hub, SEO and Harley brand validators; desktop and mobile
  browser checks; 24px homepage title/subtitle gap before and after scroll;
  responsive overflow checks on all 12 Harley URLs; clean browser console.
- Notes: `validate_harley_hub.py` now protects the approved H1/H2 limits,
  section spacing and hero darkening so regeneration cannot silently restore
  the oversized presentation.

## 2026-07-24 - Harley Hub phase 1

- Commit: `940427bb`
- Changed: Added the Harley Hub, Harley tuning and Harley custom page family in
  EN/PT/RU/UK from the approved Markdown source, three responsive LCP heroes, a
  tagged Harley blog feed, four-project custom portfolio, global dropdown,
  homepage/footer entry points and localized spoke backlinks.
- Verified: Exact source-copy checks; 12-page Harley validation; 208-URL SEO
  validation; Harley brand-page validation; JSON-LD, hreflang, canonical,
  sitemap and local-asset checks; desktop and mobile browser checks.
- Notes: Future Harley posts appear in the hub feed when their `BLOG_POSTS`
  entry includes the `harley` topic. The existing `/harley-service/` copy
  remains owned by the brand-page generator.

## 2026-07-24 - Sturmvogel photo refresh

- Commit: `52dfe1a8`
- Changed: Replaced the Sturmvogel hero under its existing stable image paths
  and added eight new responsive gallery photographs to all four language pages.
- Verified: Image decoding and dimensions; 16-item gallery parity across
  EN/PT/RU/UK; full SEO validation; desktop and mobile browser checks;
  production page and asset checks.
- Notes: The original eight gallery images remain in place. Project name, URL,
  localized copy, metadata, schema and layout remain unchanged.

## 2026-07-24 - Unbreakable photo refresh

- Commit: `d2ba2580`
- Changed: Replaced the Unbreakable hero under its existing stable image paths
  and added 12 new responsive gallery photographs to all four language pages.
- Verified: Image decoding and dimensions; 20-item gallery parity across
  EN/PT/RU/UK; full SEO validation; desktop and mobile browser checks;
  production page and asset checks.
- Notes: The original eight gallery images remain in place. Project name, URL,
  localized copy, metadata, schema and layout remain unchanged.

## 2026-07-24 - BMW Motorrad hero refresh

- Commit: `2b00fd3b`
- Changed: Replaced the BMW Motorrad service hero photograph and regenerated
  its existing responsive AVIF, WebP and JPEG variants under the same stable
  SEO-friendly filenames.
- Verified: Image decoding and dimensions; BMW brand-page validation; full SEO
  validation; desktop and mobile browser checks; production asset checks.
- Notes: Hero paths, localized ALT text, metadata, page copy, schema and layout
  remain unchanged.

## 2026-07-20 - Cross-project confirmation gate

- Commit: `04d5ac07`
- Changed: Added a mandatory owner-confirmation gate before inspecting,
  modifying, deploying, or otherwise acting on a task outside `ICM_Website`.
- Verified: Instruction scope review and clean Git diff validation.
- Notes: Non-site tasks must identify the intended project and receive explicit
  owner confirmation before any action is taken.

## 2026-07-20 - Bear 650 VideoObject naming

- Commit: `8192b4a5`
- Changed: Added localized schema-only VideoObject names for the Bear 650
  scrambler build article while preserving the visible video-section headings.
- Verified: Four-language schema-name and description checks; focused article
  SEO validation; sitemap lastmod checks; production Rich Results Test.
- Notes: No visible article copy or other structured-data entities changed.

## 2026-07-20 - Bear 650 scrambler build article

- Commit: `c6b2108a`
- Changed: Added the complete Royal Enfield Bear 650 scrambler build article in
  EN/PT/RU/UK from the reviewed Markdown source, responsive local hero media,
  a native landscape R2 video, localized blog cards, reciprocal Royal Enfield
  links, complete BlogPosting/VideoObject/FAQPage/BreadcrumbList schema and four
  sitemap URLs.
- Verified: Exact source-file parity; Python compile; 196-URL SEO validation;
  brand-page validation; focused four-language content, media, link, hreflang,
  canonical, FAQ/schema and sitemap checks; desktop/mobile browser checks; live
  MP4 playback at 1920x1080 with a measured duration of 403.285 seconds.
- Notes: The supplied R2 `poster.png` path returned 404. The available
  `bear650-scrambler-build-cover.png` asset is byte-identical to the approved
  cover and is used as the native video poster and VideoObject thumbnail.

## 2026-07-17 - Reciprocal brand service links

- Commit: `eed51847`
- Changed: Added a compact localized other-brand service link grid to all 28
  brand service pages through the shared renderer.
- Verified: Complete six-link same-language sets, brand validation, SEO and
  schema checks, responsive browser checks and production deployment.
- Notes: Future registered brands inherit anchor translations and reciprocal
  links from the shared generator. Sitemap builds preserve committed dates for
  semantically unchanged URLs while dating genuine working-tree changes.

## 2026-07-17 - Portuguese oficina SEO alignment

- Commit: `2b2d34d2`
- Changed: Added natural `oficina de motos` targeting to the PT homepage and
  motorcycle-service page, plus one PT-only conversational workshop FAQ with
  matching visible content and `FAQPage` schema.
- Verified: PT metadata, first-paragraph copy, FAQ/schema parity, unchanged
  EN/RU/UK rendered pages, brand-page workshop wording and focused SEO checks.
- Notes: Language-specific FAQ counts are expanded by `build_i18n.py`; the
  seven PT brand pages already contained natural `oficina` references.

## 2026-07-16 - C-Way Product graph deduplication

- Commit: `5a7a24be`
- Changed: Replaced the six partial Product nodes inside the C-Way Service
  OfferCatalog with `@id` references to the six complete priced Product nodes
  on all four language variants; updated their sitemap timestamps.
- Verified: Exactly six Product nodes per page, each with a complete Offer;
  Python compile, full SEO validation, production and Rich Results Test.
- Notes: C-Way catalog relationships must reference the canonical priced
  Product `@id` values and must not redeclare partial Product objects.

## 2026-07-15 - C-Way priced product catalog

- Commit: `1096835d`
- Changed: Replaced the three price-on-request C-Way positions with six priced
  Steel/Aluminium Canoe 2.0 configurations in EN/PT/RU/UK; added local lazy
  AVIF/WebP product media, in-stock states, gallery and fitment notes, and six
  matching Product/Offer entities without manufacturer links.
- Verified: Python compile; focused four-language content, media, canonical,
  hreflang and JSON-LD parity checks; full SEO validation; desktop/mobile
  browser checks; production and Rich Results Test after deploy. Google found
  17 valid rich-result items with no critical errors; optional Product review
  and Merchant shipping/return fields remain unset because no approved source
  data was supplied.
- Notes: C-Way product assets and numeric prices live in `CWAY_MEDIA`; visible
  copy lives in `CWAY_DEALER_I18N` and is rendered by the shared dealer build.

## 2026-07-10 - Harley service backlink and schema entities

- Commit: `2ce91fbb`
- Changed: Added one localized contextual link from each Harley-Davidson
  service page to the matching full-service article; expanded the article
  author and publisher references with names and an ImageObject publisher
  logo; updated the affected service and article sitemap timestamps.
- Verified: Python compile; focused EN/PT/RU/UK backlink, JSON-LD and sitemap
  checks; full SEO validation; production and Rich Results Test after deploy.
- Notes: The backlink lives in the scheduled-maintenance section and appears
  exactly once per localized service page.

## 2026-07-10 - Harley-Davidson full-service cornerstone article

- Commit: `03bbcdb4`
- Changed: Added the Harley-Davidson full-service cornerstone blog article in
  EN/PT/RU/UK from the reviewed Markdown source, responsive local AVIF/WebP/JPEG
  hero media, a portrait native R2 video, localized blog hub cards, reciprocal
  hreflang/canonical links, BlogPosting/VideoObject/FAQPage/BreadcrumbList
  schema and four sitemap URLs.
- Verified: Exact source-file parity; Python compile; SEO validation for 192
  sitemap URLs; focused four-language content, metadata, link, media, JSON-LD
  and blog-card checks; desktop/mobile browser checks including Cyrillic; R2
  responses; downloaded MP4 metadata confirmed AVC 1080x1920, AAC and 83.637 s.
- Notes: The optional separate YouTube mirror was not uploaded. The website
  intentionally embeds only the self-hosted R2 video and no YouTube iframe.

## 2026-07-10 - Homepage project hero captions

- Commit: `a55e015a`
- Changed: Restored the standard project caption layer on the full-width
  Beckman homepage card while keeping the image uncropped and without hover
  zoom; bumped the asset cache-bust to `20260710b`.
- Verified: Local SEO validation for 188 sitemap URLs; focused EN/RU/UK/PT
  homepage checks for Beckman labels, title, description, link and cache-bust;
  desktop and mobile browser checks confirmed visible meta/arrow, active
  gradient caption layer, `object-fit: contain` and no image transform.
- Notes: The Beckman card keeps the same label, title, description and arrow
  affordance as the other project cards.

## 2026-07-10 - Homepage project hero image

- Commit: `92e97738`
- Changed: Removed the inherited hero-section layout, overlay, filter and hover
  zoom from the full-width homepage project card so the Beckman image renders
  as a plain full image link; bumped the site asset cache-bust to
  `20260710a`.
- Verified: Local SEO validation for 188 sitemap URLs; focused EN/RU/UK/PT
  homepage hero-link check; desktop and mobile browser checks confirmed
  `object-fit: contain`, no transform/filter, no pseudo-overlay, no hidden
  hero padding/min-height, and the link still points to the Beckman project.
- Notes: Other project tiles keep their existing overlay and hover treatment.

## 2026-07-10 - Reviews refresh deploy recovery

- Commit: `a685f11d`
- Changed: Merged the scheduled Google reviews snapshot commit with the local
  homepage featured-project changes, deployed the combined `main`, and updated
  the GitHub Pages workflow so a successful `Refresh Google Reviews Snapshot`
  run also triggers a Pages deployment from the latest `main`.
- Verified: Local SEO validation for 188 sitemap URLs; focused EN/RU/UK/PT
  homepage checks for `reviewCount: 16`, Beckman-first project order and image
  sources; GitHub Pages run `29086000042`; production homepage and sitemap with
  `Last-Modified: Fri, 10 Jul 2026 10:20:34 GMT`.
- Notes: The scheduled review workflow had pushed commit `1d05bb0`, but the
  normal Pages deploy had not run afterward because the refresh used the
  GitHub Actions bot token.

## 2026-07-10 - Homepage featured projects

- Commit: `6c4ae46e`
- Changed: Promoted Beckman to the full-width featured position on all four
  homepages, using `beckman-06-800`; moved Inspirium into the standard project
  grid and changed the Unbreakable card image to `unbreakable-04-800`.
- Verified: Focused EN/RU/UK/PT card-order, link and image checks; unchanged
  head metadata and JSON-LD; `validate_seo.py` for 188 sitemap URLs; desktop
  browser layout check; `git diff --check`.
- Notes: Homepage project order and media are maintained directly in the four
  homepage HTML files; project copy remains in the existing I18N keys.

## 2026-07-04 - C-Way stock status and offer schema

- Commit: `7c16722e`
- Changed: Updated the C-Way dealer subpage in EN/RU/UK/PT so the three
  approved positions show an in-stock status with price-on-request copy,
  changed the OfferCatalog `itemOffered` entities from `Product` to `Service`,
  removed product-only schema fields, set Offer availability to `InStock`,
  updated the Portuguese Honda Gold Wing backlink anchor and refreshed sitemap
  `lastmod` values for C-Way and Honda service URLs.
- Verified: Python compile check for touched generators/data; Authorized
  Dealer rebuild; localized link/SEO pipeline; `validate_seo.py` for 188
  sitemap URLs; focused HTML/JSON-LD checks for all four C-Way pages and Honda
  anchors; `git diff --check`.
- Notes: C-Way page schema must not emit Product/ProductGroup while prices are
  "on request"; keep the three approved luggage-system positions as services
  in structured data.

## 2026-07-03 - C-Way dealer partner page

- Commit: `4ed79736`
- Changed: Added the C-Way official dealer subpage in EN/RU/UK/PT under
  `/authorized-dealer/c-way/`, registered the C-Way card on the Authorized
  Dealer hub, added optimized local C-Way imagery, native self-hosted video
  embeds, Service/VideoObject/FAQPage/BreadcrumbList schema and sitemap entries.
- Verified: Python compile check; Authorized Dealer rebuild; localization;
  SEO validation for 188 sitemap URLs; focused C-Way checks confirmed 3 product
  positions, 2 native videos, complete hreflang/self-canonical/noindex state,
  image dimensions/lazy loading and no trailer/mototrailer wording.
- Notes: C-Way scope is Honda Gold Wing luggage systems only unless the owner
  gives a new explicit task.

## 2026-07-02 - Stable sitemap lastmod dates

- Commit: `942477a7`
- Changed: Updated `build_sitemap.py` so sitemap `lastmod` values use real
  per-page content dates with timezone instead of the deploy/build date.
  Blog/news URLs use explicit article publish/modified dates; other pages use
  semantic Git history for the served HTML with a filesystem mtime fallback.
  Documented the rule in project instructions and build docs.
- Verified: Rebuilt sitemap twice with an identical SHA-256 hash; SEO
  validation passed for 184 sitemap URLs; production `sitemap.xml` returned
  200, matched the local hash, and exposed 19 unique timezone-qualified
  `lastmod` values.
- Notes: Keep sitemap dates and structured-data dates tied to real content
  changes, never deployment time.

## 2026-07-02 - Article schema recommended-field cleanup

- Commit: `d8da3afd`
- Changed: Updated BlogPosting/NewsArticle schema generation so article dates
  are emitted as full ISO-8601 datetimes with Europe/Lisbon offsets and authors
  keep the canonical business `@id` plus `url`; set the Bear 650 blog article
  publish/modified datetimes.
- Verified: Rebuilt blog/news pages and localized variants; SEO validation for
  184 sitemap URLs; focused Bear 650 JSON-LD checks across EN/PT/RU/UK;
  article schema datetime/author-url check across local blog/news files;
  Python compile check; `git diff --check`.
- Notes: Keep future blog/news article entries on the same datetime + author
  pattern to avoid Google Rich Results recommended-field warnings.

## 2026-07-02 - Project gallery award label parity

- Commit: `7f39aa5a`
- Changed: Updated `/projects/` gallery tile tags to mirror the homepage
  `projects.pN.label` award/category labels for all 10 projects in EN/RU/UK/PT;
  added build-time and runtime support for `data-i18n-proj-label` and
  `data-i18n-proj-tag`; bumped asset cache-bust to `20260702a`.
- Verified: Focused source/HTML parity check confirmed all 10 project tags on
  EN/RU/UK/PT `/projects/` match homepage labels; `node --check assets/main.js`;
  Python compile checks; SEO validation for 180 sitemap URLs; `git diff --check`.
- Notes: Keep future `/projects/` tile tags aligned with homepage
  `assets/main.js` labels unless the owner approves a different source of truth.

## 2026-06-29 - Full curated review schema parity

- Commit: `a3d5ad7e`
- Changed: Updated `build_reviews_schema.py` so curated JSON-LD `review[]`
  uses the full review text and original `publishedAt` value from
  `assets/reviews-curated.json`, matching the expandable visible cards.
- Verified: Rebuilt reviews from the live Worker total 15; SEO validation;
  focused EN/PT/RU/UK homepage checks confirmed 6 visible cards, 6 matching
  schema reviews, aggregate total 15 and read-more controls.
- Notes: This keeps the curated showcase and markup in exact parity while the
  aggregate rating/count remain sourced from the live Google snapshot.

## 2026-06-29 - English-speaking expat hub

- Commit: `38ba7331`
- Changed: Added `/english-speaking-motorcycle-workshop/` in EN/RU/UK/PT from
  `expat_hub_copy_4lang.md`, with optimized hero variants, footer-only service
  link, contextual inbound links from home/About/Motorcycle Service/Pre-purchase
  Inspection, sitemap entries and CollectionPage/FAQPage/BreadcrumbList schema.
- Verified: Optimized hero images; regenerated affected pages and localization;
  SEO validation for 180 sitemap URLs; focused acceptance check for copy parity,
  canonical/hreflang/noindex, footer-only navigation, inbound/funnel links,
  schema counts and hero AVIF/WebP/eager dimensions.
- Notes: The page is intentionally not in the top navigation or Services
  dropdown; keep future edits through `build_expat_hub.py` and the Markdown
  source file.

## 2026-06-29 - Six curated homepage reviews

- Commit: `5947d5b1`
- Changed: Replaced `assets/reviews-curated.json` with the six owner-approved
  Google reviews in the requested order and regenerated static homepage review
  cards plus matching LocalBusiness `review[]` JSON-LD on EN/PT/RU/UK.
- Verified: Curated JSON parse check; `build_reviews_schema.py` fetched live
  Worker rating 5 and total 15; local acceptance check confirmed 6 visible
  cards, matching schema reviews, aggregate total 15 and read-more controls on
  all 4 home pages; SEO validation passed.
- Notes: Eugene, Graeme, Yurii and Dmytro use the owner-provided seed dates and
  share URLs with initials avatars because the Worker top-5 response did not
  include them. Александр Рыбалко and Марія Легкун use exact Worker
  `publishedAt`, Google review URLs and avatars.

## 2026-06-29 - Curated reviews refresh pipeline

- Commit: `b8192062`
- Changed: Split reviews into live Worker rating/count and editorial curated
  visible cards from `assets/reviews-curated.json`; added read-more support for
  long reviews and weekly GitHub Actions refresh for static HTML/JSON-LD.
- Verified: Worker returned rating 5 and total 15; `build_reviews_schema.py`
  patched all 4 home pages; `node --check assets/main.js`; Python compile check;
  curated JSON parse check; focused home-page review/schema check; SEO validation;
  `git diff --check`.
- Notes: The initial curated file contains only confirmed local Google review
  records. Add more exact Google review records to reach the requested
  `displayCount` when available.

## 2026-06-28 - About page entity rework

- Commit: `554a9f21`
- Changed: Expanded About pages in 4 languages from `new_pages_data.py`,
  added the About hero image and Company FAQ, refreshed the story/timeline
  copy, and consolidated site identity around one canonical `#business` entity
  with sameAs, founder, awards and language metadata.
- Verified: Local rebuild, SEO validation and focused About
  canonical/hreflang/schema/hero/sitemap checks before deployment.
- Notes: About remains owned by `scripts/build/new_pages_data.py` and
  `scripts/build/build_new_pages.py`; canonical global schema IDs are shared by
  `build_i18n.py` and `validate_seo.py`.

## 2026-06-28 - Triumph brand service page

- Commit: `dd4abed2`
- Changed: Added Triumph brand service pages in 4 languages with hero photo,
  reciprocal brand links, navigation/footer/service hub integration and sitemap.
- Verified: Local brand rebuild, SEO validation and Triumph-specific brand
  validation before deployment.
- Notes: Triumph follows the shared `brand_pages_data.py` intake workflow.

## 2026-06-28 - Repository cache cleanup

- Commit: `ee4cbe5`
- Changed: Removed tracked Python bytecode files from `scripts/build/__pycache__`.
  The existing `.gitignore` already ignores `__pycache__/` and `*.pyc`, so
  regenerated cache files stay local and out of Git.
- Verified: Only `.pyc` deletions were staged; local ignored-file dry run was
  clean after cleanup.
- Notes: Do not commit Python cache files. Build scripts should remain source
  files plus documented generated HTML/assets only.

## 2026-06-28 - Project memory workflow

- Commit: `b92c695`
- Changed: Added repository-level context recovery documentation:
  `PROJECT_STATE`, `CONTENT_TYPES`, `CODEX_CHANGELOG`, `OPEN_TASKS` and
  `TASK_BRIEF_TEMPLATE`; updated `AGENTS.md`, `README.md`, `HANDOFF.md`,
  the then-present top-level historical journal and `scripts/build/README.md`
  to point future sessions to the active memory system.
- Verified: `git diff --check`; GitHub Pages deploy success; production home
  page returned 200 after deploy.
- Notes: After context compaction, read `AGENTS.md` first, then the active
  `docs/` files before relying on chat history.

## 2026-06-28 - Authorized Dealer hub

- Commit: `62e6053`
- Changed: Added `/authorized-dealer/` in EN/RU/UK/PT, top nav and footer
  labels, hero image, CollectionPage/FAQPage/BreadcrumbList schema, sitemap
  entries and reverse links from `/parts/`.
- Verified: GitHub Pages deploy success; four production URLs returned 200;
  production HTML contains localized H1, hero assets, hreflang, CollectionPage,
  FAQPage, BreadcrumbList and parts-page backlinks.
- Notes: Future partner cards live in
  `scripts/build/authorized_dealer_data.py` as `AUTHORIZED_DEALER_BRANDS`.

## 2026-06-27 - Tyre service media layout

- Commit: `21dfdcb`
- Changed: Aligned photo and YouTube video media on the tyre service page so
  they render as comparable horizontal media blocks across all languages.
- Verified: GitHub Pages deploy success and production visual/source checks.
- Notes: Keep future tyre-service media using the same shared layout classes.

## 2026-06-24 - Cyrillic typography system

- Commit: `e3f7d0c`
- Changed: Improved Russian/Ukrainian typography using language-scoped CSS,
  reducing oversized Cyrillic display/UI text while preserving EN/PT look.
- Verified: GitHub Pages deploy success; production checks on RU/UK pages.
- Notes: New generators must use `--font-body`, `--font-ui` and
  `--font-display` variables instead of hard-coded fonts.

## 2026-06-24 - Blog WhatsApp CTA text color

- Commit: `e3d7860`
- Changed: Fixed blog CTA WhatsApp button text so the label is visible in the
  inactive state, not only on hover.
- Verified: GitHub Pages deploy success and production page checks.
- Notes: Reuse shared button classes for future article CTAs.

## 2026-06-24 - Tyre fitting blog article

- Commit: `ea13d7e`
- Changed: Added motorcycle tyre fitting blog post in 4 languages with image,
  blog hub card, schema, sitemap and internal links to tyre service/pricing.
- Verified: Build, deploy and production URL checks.
- Notes: Blog source remains `scripts/build/blog_data.py`.

## 2026-06-24 - Pre-purchase service cards

- Commit: `0e7725a`
- Changed: Added pre-purchase inspection as a standard sixth service card on
  relevant service grids instead of a full-width stretched block.
- Verified: Build, deploy and production checks.
- Notes: Service-card layout should remain grid-based for future services.

## 2026-06-24 - Google reviews newest first

- Commit: `c55ea82`
- Changed: Sorted Google review display newest-first in the site widget.
- Verified: Deploy and production source/runtime checks.
- Notes: Reviews still flow through the Cloudflare Worker and static snapshot.

## 2026-06-22 - Royal Enfield service pages

- Commit: `a755ed8`
- Changed: Added Royal Enfield brand service pages in 4 languages, hero photo,
  brand dropdown/footer/service hub integration, reciprocal brand links and
  sitemap.
- Verified: Brand validation, deploy and production checks.
- Notes: Current brand page pattern should be used for future brands.

## 2026-06-22 - Pre-purchase inspection rebuild

- Commit: `91390e0`
- Changed: Rebuilt Pre-Purchase Inspection as a flagship service page in 4
  languages with hero, numbered sections, Service/Offer 150 EUR, FAQPage and
  BreadcrumbList schema.
- Verified: Build, deploy and production URL checks.
- Notes: Source copy lives in
  `scripts/build/content/pre_purchase_inspection_copy_4lang.md`.

## 2026-06-22 - Brand related link card design

- Commit: `ea1b786`
- Changed: Converted brand related paths and other-brand links into compact
  card/button grids and replaced MV Agusta with Royal Enfield on the home brand
  list.
- Verified: Build, deploy and visual checks.
- Notes: Future brand pages inherit this through shared brand generators.

## 2026-06-22 - Ducati service copy and hero

- Commit: `8bb6a6f`
- Changed: Humanized Ducati service copy in 4 languages and replaced hero
  image while preserving page structure and schema.
- Verified: Brand rebuild, deploy and production checks.
- Notes: Structure-preserving brand copy updates should continue through
  `brand_pages_data.py`.

## 2026-06-22 - Honda brand service page

- Commit: `41cafe4`
- Changed: Added Honda brand service pages in 4 languages with hero,
  reciprocal brand links, navigation/footer/service hub integration and sitemap.
- Verified: Brand validation, deploy and production checks.
- Notes: Honda followed the Suzuki-style intake workflow.

## 2026-06-22 - Brand page build tooling

- Commit: `62577ae2`
- Changed: Standardized brand-page intake and generator ownership so new brand
  pages can be added from a 4-language Markdown file plus one hero image.
- Verified: Subsequent Honda and Royal Enfield pages used the pattern.
- Notes: Keep expanding `brand_pages_data.py`; avoid brand-specific one-off
  generators.

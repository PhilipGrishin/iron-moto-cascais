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

## 2026-06-29 - Full curated review schema parity

- Commit: this commit
- Changed: Updated `build_reviews_schema.py` so curated JSON-LD `review[]`
  uses the full review text and original `publishedAt` value from
  `assets/reviews-curated.json`, matching the expandable visible cards.
- Verified: Rebuilt reviews from the live Worker total 15; SEO validation;
  focused EN/PT/RU/UK homepage checks confirmed 6 visible cards, 6 matching
  schema reviews, aggregate total 15 and read-more controls.
- Notes: This keeps the curated showcase and markup in exact parity while the
  aggregate rating/count remain sourced from the live Google snapshot.

## 2026-06-29 - English-speaking expat hub

- Commit: this commit
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

- Commit: this commit
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

- Commit: this commit
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

- Commit: this commit
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

- Commit: this commit
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
  `CHANGELOG.md` and `scripts/build/README.md` to point future sessions to the
  active memory system.
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

- Commit: see Git history before `41cafe4`
- Changed: Standardized brand-page intake and generator ownership so new brand
  pages can be added from a 4-language Markdown file plus one hero image.
- Verified: Subsequent Honda and Royal Enfield pages used the pattern.
- Notes: Keep expanding `brand_pages_data.py`; avoid brand-specific one-off
  generators.

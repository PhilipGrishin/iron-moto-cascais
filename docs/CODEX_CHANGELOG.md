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

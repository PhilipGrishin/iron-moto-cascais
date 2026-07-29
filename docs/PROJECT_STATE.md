# Iron Custom Motors Website - Project State

Last updated: 2026-07-29
Production: https://ironcustommotors.com/  
Repository: https://github.com/dreamcarua/iron-moto-cascais

This file is the fast recovery map for Codex context compaction. Read it after
`AGENTS.md` before doing site work. It preserves the current project context in
the repository instead of relying on chat history.

## Context Recovery Checklist

At the start of a new session or after context compaction:

1. Read `AGENTS.md`.
2. Read this file.
3. Read `docs/CONTENT_TYPES.md` for the page family you are about to edit.
4. Read `docs/OPEN_TASKS.md` for current risks and unresolved follow-ups.
5. Read `docs/TASK_BRIEF_TEMPLATE.md` when shaping a new large task.
6. Read `scripts/build/README.md` for the exact generator sequence.
7. Run `git status --short` before editing.
8. Inspect the relevant source data and generator before changing generated HTML.

## Business Purpose

The site is the production marketing and lead-generation website for Iron Custom
Motors, a premium motorcycle workshop in Cascais / Greater Lisbon. The business
goal is SEO, local search, AI-citation readiness and high-quality service leads.

## Current Technical State

- Static HTML/CSS/JavaScript site served from GitHub Pages.
- No server-side application framework.
- Four pre-rendered languages:
  - English at `/`
  - Russian at `/ru/`
  - Ukrainian at `/uk/`
  - Portuguese at `/pt/`
- Current sitemap: 53 indexable path patterns x 4 languages = 212 URLs.
- Current repo HTML count: 215 files, including `404.html` and 2 legacy noindex
  redirect stubs.
- Current cache-bust convention: `?v=20260724a`.
- `sitemap.xml` `lastmod` values are per-page real content dates with timezone,
  not deploy timestamps. Blog/news use their explicit article dates; other
  pages use semantic Git history for the served HTML.
- Production deploy is triggered by pushing `main`.
- Cloudflare fronts the domain and may cache recently deployed HTML/assets.

## Source Of Truth Order

Use sources in this order:

1. `AGENTS.md` - operating rules and non-negotiables.
2. `docs/PROJECT_STATE.md` - current compact project state.
3. `docs/BUSINESS_FACTS.md` - canonical NAP, hours, founder, origin,
   service languages, profiles and published key prices.
4. `docs/CONTENT_TYPES.md` - page-family source maps and task templates.
5. `docs/OPEN_TASKS.md` - temporary risks and unresolved follow-ups.
6. `docs/TASK_BRIEF_TEMPLATE.md` - compact intake format for large tasks.
7. `scripts/build/README.md` - build and verification command order.
8. `docs/CODEX_CHANGELOG.md` - compact implementation memory.
9. Actual source data and generators under `scripts/build/`.
10. Generated HTML only as output or for verification.

`HANDOFF.md` is historical and may contain stale counts from 2026-06-17. Use
this file for current state unless `HANDOFF.md` has been explicitly refreshed.

## Language And URL Rules

- Every public page must exist in all 4 languages.
- Default English URLs are root-level paths.
- Localized paths generally mirror English with `/ru/`, `/uk/`, `/pt/`.
- Custom localized slugs currently exist for tyre service:
  - EN `/motorcycle-tyre-service/`
  - PT `/pt/montagem-de-pneus-mota/`
  - RU `/ru/shinomontazh-mototsiklov/`
  - UK `/uk/shynomontazh-mototsykliv/`
- Internal localized pages must link within their own language subtree.
- Run `scripts/build/localize_internal_links.py` after generating localized
  pages.

## Current Page Families

### Top-Level And Hub Pages

- `/` home
- `/services/`
- `/projects/`
- `/about/`
- `/community/`
- `/contact/`
- `/faq/`
- `/pricing/`
- `/parts/`
- `/authorized-dealer/`
- `/authorized-dealer/c-way/`
- `/harley/`
- `/harley-tuning/`
- `/harley-custom/`
- `/english-speaking-motorcycle-workshop/`
- `/blog/`
- `/news/`
- `/privacy/`, `/cookies/`, `/terms/`

### Service Pages

- `/motorcycle-service/`
- `/parts/`
- `/upgrades-tuning/`
- `/custom/`
- `/pre-purchase-inspection/`
- `/motorcycle-tyre-service/`

### Light Funnel Hubs

- `/english-speaking-motorcycle-workshop/` targets English-speaking expats and
  newcomers, then routes down to the existing service, tyre, pre-purchase,
  brand, custom, pricing and contact pages. It is intentionally footer-only and
  contextual-link-only, not a top-navigation item.

Source:

- Copy: `scripts/build/content/expat_hub_copy_4lang.md`
- Generator: `scripts/build/build_expat_hub.py`
- Hero source: `/photos/services/english-speaking-motorcycle-workshop-main.jpg`

### Harley Hub

The Harley-specific content family routes riders between the existing
independent `/harley-service/` page and two focused service spokes:

- `/harley/` - collection hub and tagged Harley blog feed
- `/harley-tuning/` - stage, exhaust, suspension and braking work
- `/harley-custom/` - custom-build service and four-project portfolio

Source:

- Copy: `scripts/build/content/harley_hub_phase1_4lang.md`
- Supplemental data: `scripts/build/harley_hub_data.py`
- Generator: `scripts/build/build_harley_hub.py`
- Validator: `scripts/build/validate_harley_hub.py`
- Hero sources: `photos/harley/`

The workshop feed is generated from blog posts whose `topics` include
`harley`. Keep those tags accurate when adding future Harley articles.

### Brand Service Pages

Current brand order is defined in `scripts/build/brand_pages_data.py`:

1. `/harley-service/`
2. `/bmw-service/`
3. `/ducati-service/`
4. `/suzuki-service/`
5. `/honda-service/`
6. `/royal-enfield-service/`
7. `/triumph-service/`

The brand service pages are independent workshop pages. Do not describe Iron
Custom Motors as an authorized motorcycle-brand dealer for BMW, Harley-Davidson,
Ducati, Suzuki, Honda, Royal Enfield or Triumph unless the owner provides explicit
approved partner wording.

### Authorized Dealer

`/authorized-dealer/` is a separate top-level category for official
parts/accessories dealer partners. It is not the same as the independent
motorcycle-brand service pages.

Current hub source:

- Data: `scripts/build/authorized_dealer_data.py`
- Generator: `scripts/build/build_authorized_dealer.py`
- Future partner cards: `AUTHORIZED_DEALER_BRANDS`
- Hero source: `/photos/authorized-dealer-main-1600.jpg`

Current partner subpages:

- `/authorized-dealer/c-way/` in EN/RU/UK/PT. It is an official C-Way luggage
  systems page for Honda Gold Wing 2018–2026 with six priced Canoe 2.0
  configurations grouped into Steel and Aluminium. Product media is local
  AVIF/WebP, and each visible position has matching Product/Offer JSON-LD.
  Do not add trailer/mototrailer content to this page unless the owner gives a
  new explicit task.

### Projects

Current project pages:

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

New project pages can use the shared data-driven flow in
`scripts/build/project_pages_data.py` and `scripts/build/build_project_pages.py`.
Legacy project pages remain static HTML with inline localized copy.

Legacy redirect stubs:

- `/projects/nezlamniy/` -> `/projects/unbreakable/`
- `/projects/quanta/` -> `/projects/quanta-r/`

### Blog Posts

Current blog posts are registered in `scripts/build/blog_data.py`:

- `/blog/revtech-110-oil-service-engine-gearbox-drive/`
- `/blog/motorcycle-brake-pad-replacement-cascais/`
- `/blog/front-fork-service-motorcycle-cascais/`
- `/blog/motorcycle-tyre-fitting-specialist-cascais/`
- `/blog/royal-enfield-bear-650-fork-oil-case-study/`
- `/blog/harley-davidson-full-service-done-right/`
- `/blog/royal-enfield-bear-650-scrambler-build/`

### News Articles

Current news articles are registered in `scripts/build/news_data.py`:

- `/news/ericeira-kustom-fest-2026/`
- `/news/opens-new-workshop-in-cascais/`
- `/news/lisbon-motorcycle-film-fest-2026-beckman/`

## Core Build Files

- `assets/main.css` - site-wide design, typography, responsive behavior.
- `assets/main.js` - runtime behavior and shared `I18N` object.
- `scripts/build/build_new_pages.py` - hub pages.
- `scripts/build/build_brand_pages.py` - brand service pages.
- `scripts/build/build_authorized_dealer.py` - Authorized Dealer hub.
- `scripts/build/build_blog.py` - blog hub and articles.
- `scripts/build/build_news.py` - news hub and articles.
- `scripts/build/build_pre_purchase_inspection.py` - flagship inspection page.
- `scripts/build/build_expat_hub.py` - English-speaking expat funnel hub.
- `scripts/build/build_harley_hub.py` - Harley collection, tuning and custom
  pages.
- `scripts/build/build_tyre_service.py` - tyre service page.
- `scripts/build/build_pricing.py` - pricing pages.
- `scripts/build/nav_patch.py` - canonical nav and footer on English pages.
- `scripts/build/build_i18n.py` - localized copies and JSON-LD localization.
- `scripts/build/localize_internal_links.py` - localized internal link rewrites.
- `scripts/build/apply_seo_meta.py` - shared SEO meta invariants.
- `scripts/build/build_sitemap.py` - sitemap and hreflang alternates.
- `scripts/build/validate_seo.py` - broad SEO and asset validation.
- `scripts/build/validate_brand_pages.py` - brand-page QA.
- `scripts/build/validate_harley_hub.py` - Harley family content, schema,
  integrations and portfolio QA.

## Recent Project Context

Recent high-impact changes:

- Added the Authorized Dealer hub in 4 languages.
- Added and standardized brand pages for Suzuki, Honda, Royal Enfield and
  Triumph.
- Added the English-speaking expat funnel hub in 4 languages with footer-only
  navigation and contextual inbound links.
- Humanized Harley-Davidson, BMW Motorrad and Ducati pages.
- Rebuilt Pre-Purchase Inspection as a flagship service.
- Added Motorcycle Tyre Service and related blog content.
- Added top-navigation dropdowns for Services, Brands, Projects and About.
- Improved Cyrillic typography for Russian and Ukrainian pages.
- Split Google reviews into live rating/count from the Worker snapshot and
  editorial visible cards from `assets/reviews-curated.json`.
- Added YouTube social link and blog/video schema workflows.
- Added the multilingual Harley Hub family, global dropdown, workshop feed and
  custom portfolio.
- Documented and centralized scalable page-family patterns.

For compact commit memory, see `docs/CODEX_CHANGELOG.md`.

## External Services

- Hosting: GitHub Pages.
- CDN/DNS: Cloudflare.
- Reviews Worker: `https://icm-reviews.vg-ab6.workers.dev/`.
- Google Places API key is stored only as a Cloudflare Worker secret.
- Reviews refresh automation:
  `.github/workflows/reviews-refresh.yml` runs `build_reviews_schema.py`
  weekly and can be dispatched manually.
- GA4: `G-D15BLYEKBN`.
- Meta Pixel: `1708697916976439`.
- Form backend: FormSubmit to `Ironcustom.office@gmail.com`.
- Google Search Console requires account access for live manual inspection.

Never expose secrets in chat, docs, commits or logs.

## Verification Standard

After implementation:

1. Run the relevant generator pipeline from `scripts/build/README.md`.
2. Run focused validators (`validate_seo.py`, `validate_brand_pages.py`, schema
   checks, `git diff --check`).
3. Commit and push unless the owner explicitly says not to.
4. Wait for GitHub Pages deploy.
5. Verify production URLs with `curl -I` and focused HTML/source checks.
6. Report what was verified and what could not be externally verified.

For docs-only changes, at minimum run:

```bash
git diff --check
git status --short
```

## Documentation Maintenance Rule

When a task changes a repeatable workflow, update the documentation in the same
commit. Prefer updating:

- `docs/CONTENT_TYPES.md` for task templates and page-family ownership.
- `docs/PROJECT_STATE.md` for current structure and high-level facts.
- `docs/CODEX_CHANGELOG.md` for compact implementation memory.
- `docs/OPEN_TASKS.md` for unresolved risks or external follow-ups.
- `docs/TASK_BRIEF_TEMPLATE.md` for future large task intake.
- `scripts/build/README.md` for command sequences and generator details.

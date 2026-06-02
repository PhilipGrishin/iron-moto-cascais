# Changelog

Chronological log of changes. Each entry corresponds to a commit
on `main`. Dates are commit dates.

## 2026-06

### 2026-06-02
- `7ea6b1b` fix: harden multilingual SEO rendering
- `1f37f70` docs: full project handoff package

## 2026-05

### 2026-05-24
- `dc21b54` fix: remove mobile sticky-CTA, fix horizontal overflow on mobile
- `564cf95` news article — Lisbon Motorcycle Film Fest 2026 with Beckman
- `d09b138` news section + first article (opens new workshop in Cascais)

### 2026-05-23
- `1f87824` feat: 3 brand landing pages (BMW, Harley, Ducati) × 4 langs
- `0549c9a` feat: review schema (AggregateRating + Review JSON-LD) on home pages
- `068ad7c` check4

### 2026-05-22
- `b8d5fd7` check3
- `dad4b38` check2
- `3a0a770` check
- `335dc27` 5 new dedicated pages — kill anchor-only nav (adds /services/, /projects/, /about/, /contact/, /faq/)

### 2026-05-21
- `811a48c` fix: pricing layout on RU/UK/PT + add pricing teaser to home page

### 2026-05-20
- `27691e4` feat: add /pricing/ page in 4 languages (HTML + PDF download)
- `94330b2` fix: 5 content/translation issues + UK typo cleanup

### 2026-05-19
- `76f833c` feat: full GA4 event tracking + project context (CLAUDE.md)
- `6cf0b5d` Create CLAUDE.md
- `bf3620f` GA4
- `6c41abe` feat: full multilingual setup (RU/UK/PT pre-rendered), hreflang, image dims, sitemap, 404

### 2026-05-10
- `dd9bdc6` fix: Inspirium hero photo — cinematic shot at proper 21:9 ratio
- `3b1b6ff` fix: cache-bust all asset URLs (?v=20260510e)
- `35fab7b` fix: project pages render (header regex, null-safe handlers); homepage 3×3 grid
- `24dd52c` fix: project pages — header regex bug, null-safe handlers
- `65aed08` feat: complete projects rebuild — 10 projects, fresh photos

### 2026-05-05
- `013b000` fix: parallax — disable on mobile (was causing first-scroll jump on iOS bounce)
- `fa92e18` feat: clickable service cards — robust on touch
- `8ef9d5e` feat: clickable service cards (whole block triggers Learn more link)
- `5060d74` fix: reviews — use originalText (real author wording)
- `c1f66a2` fix: add canonical, fix hreflang URLs
- `4e9a439` fix: applyLang now handles data-i18n-html attribute
- `dcdaf6d` feat: project pages — lightbox, 3D tilt, parallax, KPI counter
- `571a4b0` feat: 7 dedicated project pages with full story + gallery (8 photos each), 4 langs
- `c690779` fix: project photos — regenerate from real source
- `86e1096` fix: project photos (gitignore), hours 10:00-18:00
- `a059696` feat: real project photos (7), updated i18n, Cloudflare Worker for Google Reviews
- `185d360` feat: complete site — 7 real projects, Google Reviews worker, all subpages i18n
- `f24091d` feat: add Nezlamniy/Unbreakable real photo — projects gallery complete
- `8433005` feat: replace Unsplash project placeholders with 6 real bikes
- `c13a747` feat: rewrite 4 subpages with new content
- `6809801` fix: logo (since 2010 visible everywhere), brands strip order
- `d1ca12c` feat(photos): hero=IMG_6884, team=IMG_6927, service-action=IMG_6951, parts=IMG_6908
- `e50c6ab` fix: exterior banner — 21:9 smart crop
- `f161492` feat: subpage hero photos, lounge-detail strip, exterior banner before footer
- `1feb1e7` feat: replace Unsplash with real Cascais workshop photos
- `3b62afd` feat: multipage SEO architecture, real GA4/Meta IDs, CNAME for ironcustommotors.com

### 2026-05-04
- `4a2e75d` feat(v1): community section + schema.org + maps + brands + cookies + sticky CTA + form backend + favicon/OG
- `b8c21fe` feat(v1): add Community / Lounge section with real photo + 4-lang i18n
- `c922998` fix: default language is now EN across V1/V2/V3
- `d19595a` fix(v1): remove cursor halo, marquee; widen logo + EST.2010 badge; align process line
- `9bd47ba` feat: alternative V3 — cyberpunk neon (later removed)
- `5b9ac9a` feat: alternative V2 — editorial racing concept (later removed)
- `0e1084a` feat: initial single-page MVP — EN/RU/UK/PT, real Cascais contacts

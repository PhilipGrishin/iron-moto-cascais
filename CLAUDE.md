# Iron Custom Motors — Project Context (for Claude / Cowork)

> Read this first before making any decisions on the site. Distilled from the
> official TZ (ICM_TZ_website_development_ru.docx) and updated 2026-05 after
> the migration from single-page landing to multi-page lead-gen site.

## What this project is

The marketing & lead-gen website for **Iron Custom Motors** — a premium
auto/moto service in **Cascais, Greater Lisbon**, run by a team with an
international custom-motorcycle pedigree:

- AMD World Championship (custom bike building)
- BMW Motorrad Customizing Championship 2023
- Bonneville Salt Flats world speed record 2017 (class 350APS-VG)

The brand existed long before Portugal — its credibility transfers to the
local service business.

## Concept (updated 2026-05)

**This is no longer a one-page landing.** It started as a long-scroll landing
with anchored sections; in May 2026 we restructured it into a proper
multi-page site so each commercial query has its own deep landing page that
Google and AI engines (ChatGPT, Perplexity, Google AI Overviews, Gemini) can
cite directly.

**The goal of the site is to be the answer when riders search or ask AI.**
Two distinct traffic sources, equal weight:

1. **Classic Google / Bing search** — for queries like "motorcycle service
   cascais", "pre purchase inspection portugal", "BMW service Lisbon".
   Strategy: one focused landing page per commercial query, with rich
   Schema.org markup, internal linking, and content depth.
2. **AI engine citation** — when someone asks "best motorcycle shop in
   Cascais" or "where can I get a BMW serviced near Lisbon", we want the
   answer to include Iron Custom Motors. Strategy: complete LocalBusiness +
   MotorcycleRepair + Service + FAQPage + BreadcrumbList JSON-LD on every
   page, in 4 languages, with consistent NAP (name/address/phone).

Conversion still happens through the same channels: WhatsApp (primary),
phone, contact form (FormSubmit). The site's job is to get them to those
channels with high intent.

## Non-negotiable principles

1. **The site sells service & trust, not brand story.** Brand history is a
   trust-builder, not the headline. Lead generation is the primary KPI.
2. **Path to contact must be short** — every page has a clear next step
   (Book service / WhatsApp / Get consultation). Sticky mobile CTA + floating
   WhatsApp button are required.
3. **Tone:** premium, human, confident, engineering-driven, **not arrogant**.
4. **Visuals:** premium industrial / performance / craftsmanship. Never
   "garage-y" or cheap-looking. Never over-artistic at the expense of
   readability or conversion.
5. **Mobile-first.** A big share of traffic comes from social, maps, messengers.
6. **No machine translation.** Each language version is human-written /
   editor-reviewed.

## Audience (in priority order)

| Segment | Lang | What they need | Implication for the site |
|---|---|---|---|
| Expats in Portugal (UK/US/EU) | EN | Clear English, trust signals, fast contact | Strong English version, reviews, WhatsApp |
| Russian-speaking expats | RU | Service in their language, human tone | Full RU, WhatsApp, clear pricing path |
| Ukrainian expats | UK | Communication in own language | Full UK at minimum on key landing pages |
| Local English-speaking riders | EN | Quality, kit, brands, reputation | Projects, services, FAQ, reviews |
| Portuguese clients | PT | Local feel, trust, clarity | Full PT site, local SEO, map, contacts |

## Service priorities (MVP)

Push these in order on home + ads:

1. **Motorcycle service / maintenance / repairs** — universal entry point
2. **Diagnostics** — broadest commercial demand
3. **Pre-purchase inspection** — the strongest hook for expats; high commercial intent
4. **Parts installation / upgrades** — easy-to-explain, high value
5. **Tuning consultation** — gateway to bigger jobs
6. Custom works — image builder + large tickets (secondary)

## Target SEO queries (from TZ)

- motorcycle service cascais / lisbon
- moto workshop portugal
- bmw motorcycle service lisbon
- harley service portugal
- **pre purchase inspection motorcycle portugal** ← biggest opportunity
- premium car service cascais
- custom motorcycle portugal

## Current site stack (what's actually built)

- Plain static **HTML + CSS + vanilla JS** in this repo. The checked-in
  HTML is what users see; Python/Node build scripts in `scripts/build/`
  regenerate the static pages from source data when content changes.
- Hosted on **GitHub Pages** with custom domain `ironcustommotors.com` (CNAME).
- Multi-language: pre-rendered static pages per language at `/`, `/ru/`,
  `/uk/`, `/pt/`. JS picks correct lang from URL and navigates between them
  on lang switcher click. Translations dict for runtime lives in
  `assets/main.js` (`I18N` object) — keep in sync if you change copy.
- 31 indexable page paths × 4 languages = **124 URLs** in `sitemap.xml`.
  The repo also contains `404.html` plus 2 noindex redirect stubs.
- Project pages have an inline `window.ICM_I18N_PAGE` with project-specific
  copy in 4 langs.
- Form: posts to `https://formsubmit.co/Ironcustom.office@gmail.com` and
  opens WhatsApp with a prefilled message — works without a backend.
- Reviews: pulled live from Google Maps via a **Cloudflare Worker** at
  `https://icm-reviews.vg-ab6.workers.dev/` (see `worker/`). 12h browser cache.
- Analytics: **GA4** `G-D15BLYEKBN` (owned by fg@abrisart.com) + **Meta Pixel**
  `1708697916976439` (legacy — still pointing to previous account; replace
  before running paid ads).
- Cookie consent: localStorage `icm-consent` gates analytics load
  (Consent-Mode-style — analytics only after Accept).

## SEO posture (what's in place)

✓ Schema.org JSON-LD on every main page: LocalBusiness + MotorcycleRepair,
  Organization, WebSite, BreadcrumbList, FAQPage, CollectionPage, Service,
  AboutPage, ContactPage, NewsArticle, Blog, AggregateRating and Review where
  relevant. **This is the asset that AI engines (ChatGPT, Perplexity,
  Google AI Overviews) read to cite the brand.**
✓ Unique title + meta description per page per language.
✓ OG + Twitter cards localized.
✓ Canonical + hreflang on every indexable page (en/ru/uk/pt + x-default).
✓ Sitemap with `<lastmod>` and `xhtml:link` alternates per URL.
✓ All `<img>` have `alt`, `width`, `height`, `loading="lazy"`.
✓ Branded 404 with language auto-detection.
✓ Cache-bust query `?v=YYYYMMDDx` on CSS/JS — bump when you change `assets/`.

## Site structure (as of 2026-06)

31 indexable URLs per language. Each is a real page with its own H1, meta,
JSON-LD, content depth and hreflang alternates — not an anchor on the home
page. Legacy `/projects/nezlamniy/` and `/projects/quanta/` are noindex
redirect stubs in English only.

**Hubs / landing pages (5 new in May 2026):**
- `/services/` — services hub (CollectionPage schema, links to all 5 service pages)
- `/projects/` — gallery hub (CollectionPage + ItemList, links to 10 project pages)
- `/about/` — brand story (AboutPage schema)
- `/contact/` — full contacts page (ContactPage schema, embed map, form trigger)
- `/faq/` — full FAQ (FAQPage schema — moved off home)

**Service landing pages (5):**
- `/motorcycle-service/` — primary service entry (Service schema)
- `/parts/` — parts & consumables
- `/upgrades-tuning/` — performance/touring upgrades
- `/custom/` — bespoke builds
- `/pre-purchase-inspection/` — strongest commercial-intent landing for expats

**Other:**
- `/` — overview / home (still has all sections, but main nav goes to deep pages)
- `/pricing/` — full price list with PDF downloads per language
- `/projects/<slug>/` — 10 individual custom build case studies
- `/news/` and `/news/<slug>/` — news hub and articles
- `/privacy/`, `/cookies/`, `/terms/` — legal pages

## Navigation philosophy (after May 2026 refactor)

- **Main nav (header + footer) uses real URLs only.** No `#anchors` for
  Services / Projects / About / FAQ / Contact / Pricing.
- The only anchors remaining are functional: `#contact` opens the form
  modal (JS-bound via `data-cta="book"`), `/#reviews` jumps to the dynamic
  Google Reviews widget on home (it's JS-rendered, no SEO value as standalone
  page).
- Pricing teaser on home page deep-links to `/pricing/`.
- All sub-pages have absolute-path nav so they work identically in
  `/ru/`, `/uk/`, `/pt/` subtrees.

## Known gaps (what's still missing, in priority order)

- ❌ **Blog / Insights section** — biggest remaining SEO opportunity.
  Long-tail queries like "what to check before buying a used motorcycle in
  Portugal", "BMW R nineT first service Lisbon", "winter prep Cascais" are
  easy ranking targets and feed AI engines. Suggested structure:
  `/blog/<slug>/` with `Article` schema, hub at `/blog/`.
- ❌ **Diagnostics** as a separate landing page (TZ flags it P1; currently
  folded into motorcycle-service).
- ❌ **Advanced lead form**: TZ asks for brand, model, year, urgency,
  preferred date, photo upload. Current form is the short version only.
- ❌ **Anti-spam** (reCAPTCHA v3 / honeypot / rate-limit). Form is exposed.
- ❌ **Thank-you / success state page** as a separate URL with its own
  analytics event.
- ⚠️ **GTM container** is not loaded by design. Events are sent directly to
  GA4 via `gtag` after consent and also queued in `dataLayer` for a future
  GTM migration.
- ⚠️ **Custom event tracking** is wired for `form_submit`, `click_whatsapp`,
  `click_phone`, `click_email`, `click_map`, `book_service`,
  `view_service_page`, and `lead_success`; real lead-delivery verification
  still depends on FormSubmit mailbox activation and a controlled test lead.
- ⚠️ **Schema gap**: no long-form `Article` content beyond news yet. Blog or
  insights pages are still the main content/SEO expansion path.
- ⚠️ Site is static HTML — **no CMS**. The TZ leaves the stack open; the
  current implementation trades CMS-convenience for speed + free hosting.
  Acceptable for MVP; revisit if non-tech team needs to edit content.

## Acceptance criteria from TZ (use as a checklist)

- Mobile + desktop both work correctly ✓
- All forms send leads and track as events — repo wiring ✓; real email
  delivery must be verified with FormSubmit activation/test lead
- All language versions linked properly ✓
- title/description/OG/canonical/hreflang correct ✓
- CTAs work from all key screens ✓
- Page-speed, a11y, SEO indexing checked — periodic audit needed
- Map / contacts / messengers / phones work ✓
- Admin can edit base content without a developer ✗ (no CMS)

## Working conventions (please follow)

- **All asset paths absolute** (`/photos/...`, `/assets/...`). Relative paths
  break inside `/ru/`, `/uk/`, `/pt/` subtrees.
- **Internal page links inside localized trees must include the lang prefix**
  (`/ru/motorcycle-service/`, not `/motorcycle-service/`). There's a helper
  script `localize_internal_links.py` in `scripts/build/`.
- **When editing translations**, update both `I18N` in `assets/main.js` AND
  the rendered text in each pre-rendered HTML file (or re-run
  `build_i18n.py` in `scripts/build/`).
- **When adding a new page**, add it to all 4 languages, to `sitemap.xml`,
  and add hreflang block.
- **Cache-bust query string** — bump `?v=...` everywhere when you change
  `main.css` / `main.js`. Use `?v=YYYYMMDDx` format.
- **No emojis in copy** — TZ explicitly calls for a premium, restrained tone.

## Useful commands / scripts (in `scripts/build/`)

- `build_new_pages.py` — generates the 5 hub pages from `new_pages_data.py`.
- `build_brand_pages.py` — generates BMW / Harley / Ducati service pages.
- `build_legal_pages.py` — generates privacy / cookies / terms pages.
- `build_news.py` — generates the news hub and article pages.
- `nav_patch.py` — rewrites primary nav + footer columns on all EN pages.
- `build_i18n.py` — regenerates `/ru/`, `/uk/`, `/pt/` pages from EN sources.
- `localize_internal_links.py` — rewrites internal links to localized URLs.
- `add_image_dims.py` — adds `width`/`height` to all `<img>` from real image files.
- `build_sitemap.py` — regenerates `sitemap.xml` for all 4 langs.
- `build_pricing.py` — generates `/pricing/` from `pricing_data.py` (own per-lang pipeline).

Typical sequence after content/translation changes:
```
node extract_i18n.js              # main.js → i18n.json
python3 build_new_pages.py        # 5 hubs
python3 build_brand_pages.py      # brand service pages
python3 build_legal_pages.py      # legal pages
python3 build_news.py             # news hub/articles
python3 build_pricing.py          # pricing 4 langs
python3 nav_patch.py              # consistent nav
python3 build_i18n.py             # RU/UK/PT
python3 localize_internal_links.py
python3 add_image_dims.py
python3 build_sitemap.py
# bump CACHE_BUST in HTML  (single search/replace across *.html)
```

## Contact / business facts

- Address: R. António José da Silva 100 B, 2785-253 São Domingos de Rana, Cascais
- Phone / WhatsApp: +351 917 961 230
- Email: Ironcustom.office@gmail.com
- Hours: Tue–Sat 10:00–18:00 (closed Sun & Mon)
- Founded: 2010
- Founder: Yaroslav Lutytskyi

## When in doubt

Reread the TZ. Anything in this file that conflicts with the original TZ:
**TZ wins.** Source: `/Users/philipgrishin/Library/Application Support/Claude/local-agent-mode-sessions/.../uploads/ICM_TZ_website_development_ru.docx`
(also archived in repo `.gitignore`'d list).

# Iron Custom Motors — Project Context (for Claude / Cowork)

> Read this first before making any decisions on the site. Distilled from the
> official TZ (ICM_TZ_website_development_ru.docx).

## What this project is

The marketing & lead-gen website for **Iron Custom Motors** — a premium
auto/moto service in **Cascais, Greater Lisbon**, run by a team with an
international custom-motorcycle pedigree:

- AMD World Championship (custom bike building)
- BMW Motorrad Customizing Championship 2023
- Bonneville Salt Flats world speed record 2017 (class 350APS-VG)

The brand existed long before Portugal — its credibility transfers to the
local service business.

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

- Plain static **HTML + CSS + vanilla JS** in this repo. No build step.
- Hosted on **GitHub Pages** with custom domain `ironcustommotors.com` (CNAME).
- Multi-language: pre-rendered static pages per language at `/`, `/ru/`,
  `/uk/`, `/pt/`. JS picks correct lang from URL and navigates between them
  on lang switcher click. Translations dict for runtime lives in
  `assets/main.js` (`I18N` object) — keep in sync if you change copy.
- 16 page paths × 4 languages = 64 main URLs (in `sitemap.xml`).
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
  Organization, WebSite, BreadcrumbList, FAQPage on home, CreativeWork on
  project pages. **This is the asset that AI engines (ChatGPT, Perplexity,
  Google AI Overviews) read to cite the brand.**
✓ Unique title + meta description per page per language.
✓ OG + Twitter cards localized.
✓ Canonical + hreflang on every indexable page (en/ru/uk/pt + x-default).
✓ Sitemap with `<lastmod>` and `xhtml:link` alternates per URL.
✓ All `<img>` have `alt`, `width`, `height`, `loading="lazy"`.
✓ Branded 404 with language auto-detection.
✓ Cache-bust query `?v=YYYYMMDDx` on CSS/JS — bump when you change `assets/`.

## Known gaps vs TZ (what's still missing)

- ❌ **Blog / Insights section** — TZ section 14 requires it for SEO and
  trust. Currently no `/blog/`. Big SEO opportunity — long-tail queries
  ("what to check before buying a used motorcycle in Portugal", "BMW service
  Cascais", "season prep") are easy ranking targets.
- ❌ **Diagnostics** as a separate landing page (TZ flags it P1; currently
  folded into motorcycle-service).
- ❌ **Legal pages**: Privacy Policy, Cookie Policy, Terms — required for
  GDPR compliance. Footer references them but pages don't exist.
- ❌ **Advanced lead form**: TZ asks for brand, model, year, urgency,
  preferred date, photo upload. Current form is the short version only.
- ❌ **Anti-spam** (reCAPTCHA v3 / honeypot / rate-limit). Form is exposed.
- ❌ **Thank-you / success state page** as a separate URL with its own
  analytics event.
- ❌ **GTM container** — events are pushed to `dataLayer` but no GTM is
  loaded, so they don't fire anywhere. Either add GTM or wire `gtag` events
  directly.
- ❌ **Custom event tracking** per TZ: `click_whatsapp`, `click_phone`,
  `click_email`, `click_map`, `book_service`, `view_service_page`,
  `lead_success`. Only `form_submit` is partially wired.
- ❌ **Schema gaps**: no `Article` (needs blog first), no `Review` markup
  (Google reviews come via JS — could be SSR'd into JSON-LD).
- ⚠️ Site is static HTML — **no CMS**. The TZ leaves the stack open; the
  current implementation trades CMS-convenience for speed + free hosting.
  Acceptable for MVP; revisit if non-tech team needs to edit content.

## Acceptance criteria from TZ (use as a checklist)

- Mobile + desktop both work correctly ✓
- All forms send leads and track as events — partially ✗
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
  script `localize_internal_links.py` in the outputs/build directory.
- **When editing translations**, update both `I18N` in `assets/main.js` AND
  the rendered text in each pre-rendered HTML file (or re-run
  `build_i18n.py` in outputs/build).
- **When adding a new page**, add it to all 4 languages, to `sitemap.xml`,
  and add hreflang block.
- **Cache-bust query string** — bump `?v=...` everywhere when you change
  `main.css` / `main.js`. Use `?v=YYYYMMDDx` format.
- **No emojis in copy** — TZ explicitly calls for a premium, restrained tone.

## Useful commands / scripts (in outputs/build)

- `build_i18n.py` — regenerates `/ru/`, `/uk/`, `/pt/` pages from EN sources.
- `localize_internal_links.py` — rewrites internal links to localized URLs.
- `add_image_dims.py` — adds `width`/`height` to all `<img>` from real image files.
- `build_sitemap.py` — regenerates `sitemap.xml` for all 4 langs.

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

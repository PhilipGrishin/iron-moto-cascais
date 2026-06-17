# Iron Custom Motors — project handoff

State of the repository as of 2026-06-17. This document is the
single entry point for anyone (human or AI agent) picking up the
project. It is factual and current; opinions, priorities and
roadmap recommendations are intentionally not included.

For day-to-day instructions read `AGENTS.md` (or `CLAUDE.md` —
they describe the same thing for different agents). For commit
history read `CHANGELOG.md`. For build scripts read
`scripts/build/README.md`. For credentials read `.env.example`.

---

## 1. What this is

The marketing and lead-generation website for **Iron Custom
Motors**, a motorcycle workshop in Cascais, Greater Lisbon
(Portugal). It is a static multi-page multilingual site,
deployed via GitHub Pages.

- Domain: `https://ironcustommotors.com`
- Hosting: GitHub Pages with a `CNAME` file (`ironcustommotors.com`)
- Repository: `https://github.com/dreamcarua/iron-moto-cascais`
- Languages: English (default at `/`), Russian (`/ru/`), Ukrainian (`/uk/`), Portuguese (`/pt/`)
- Total indexable URLs: 140 (35 path patterns × 4 languages)
- HTML files in repo: 143 (140 indexable + 404.html + 2 redirect stubs)

## 2. Tech stack

- Static HTML, CSS, JavaScript. No framework. No build step is
  strictly required to render — the HTML in the repo is what the
  user sees. Python build scripts in `scripts/build/` regenerate
  HTML from source data when content changes.
- Inline JSON-LD (`Schema.org`) on every page: `LocalBusiness`,
  `MotorcycleRepair`, `Organization`, `WebSite`, `BreadcrumbList`,
  `FAQPage`, `CollectionPage`, `Service`, `AboutPage`,
  `ContactPage`, `NewsArticle`, `Blog`, `BlogPosting`.
- Internationalization: each page is pre-rendered per language.
  Runtime language switch is via `assets/main.js` with the
  `I18N` object. Per-page translation deltas are stored as
  inline `<script>window.ICM_I18N_PAGE = …</script>`.
- Cookie consent: `localStorage` key `icm-consent`. Analytics
  load only after `Accept`.
- Analytics: Google Analytics 4 (`G-D15BLYEKBN`). Meta Pixel
  is wired in markup but kept inert until consent.
- Reviews widget: Cloudflare Worker proxies the Google Places
  API; reviews are also persisted to `assets/reviews-snapshot.json`
  via `scripts/build/build_reviews_schema.py` and embedded as
  JSON-LD on the home pages.
- Lead form: posts to FormSubmit
  (`https://formsubmit.co/Ironcustom.office@gmail.com`).

## 3. Repository layout

Top-level directories and their roles:

```
/                                  HTML files for English root pages
  CNAME                            GitHub Pages domain (ironcustommotors.com)
  CLAUDE.md                        Project context (for Claude Code / Cowork)
  AGENTS.md                        Project context (for Codex AI / OpenAI agents)
  HANDOFF.md                       This document
  CHANGELOG.md                     Chronological log of commits
  README.md                        Public-facing brief
  .env.example                     Names of secrets and where to obtain them
  .gitignore
  llms.txt                         Site map and citation guidance for LLMs
  robots.txt                       Allows all; points to sitemap.xml
  sitemap.xml                      140 URLs (35 paths × 4 langs)
  404.html                         Branded 404 with language auto-detect
  deploy.sh                        Legacy shell script (not used currently)

ru/, uk/, pt/                      Localized copies of all main pages
                                   (pre-rendered, not JS-only)

services/                          Hub page listing the 5 service pages
projects/                          Hub page listing the 10 project pages
about/, contact/, faq/             Single-page hubs added 2026-05
pricing/                           Pricing tables in 4 langs + PDF downloads
motorcycle-service/, parts/,
upgrades-tuning/, custom/,
pre-purchase-inspection/           Service landing pages
bmw-service/, harley-service/,
ducati-service/                    Brand-specific landing pages (2026-05-23)
blog/                              Practical workshop blog hub + articles (2026-06-17)
news/                              News hub + 3 articles
privacy/, cookies/, terms/         GDPR boilerplate pages (2026-05)

projects/<slug>/                   10 project pages (Inspirium, Beckman, …)

assets/main.css                    All styles, ~43 KB
assets/main.js                     All scripts and the I18N dict, ~110 KB
assets/reviews-snapshot.json       Snapshot of latest Google reviews

photos/                            Image assets
  hero-1600.jpg etc.               Top-level home/team/lounge photos
  projects/                        Photos per project
  news/                            Photos per news article (with -800 and -1600 sizes)
  blog/                            Photos per blog article (with -800 and -1600 sizes)
  brands/                          (empty as of writing — for future brand-specific hero images)

scripts/                           Locally-run helpers
  build/                           Page generators and pipeline (this is where Python lives)
  build_reviews_schema.py          Wrapper that calls the worker and updates JSON-LD
  README.md                        Notes for the local-only scripts

worker/                            Cloudflare Worker source (reviews proxy)
  reviews.js                       Worker code
  wrangler.toml                    Deploy config
  README.md                        Worker-specific notes
```

## 4. Build / deploy

- Local edits in this repo are pushed to GitHub via GitHub
  Desktop (the project owner does not use the `git` CLI).
- GitHub Pages serves from the `main` branch root. There is no
  build step on GitHub's side.
- Custom domain is configured by the `CNAME` file in the repo
  root plus DNS records at the domain registrar.
- For source-of-truth regeneration after content changes, run
  scripts under `scripts/build/`. See `scripts/build/README.md`
  for ordering.

## 5. URL inventory

140 URLs are listed in `sitemap.xml`. Path patterns:

```
/                                       (home)
/services/                              (services hub)
/motorcycle-service/                    (service detail)
/parts/                                 (service detail)
/upgrades-tuning/                       (service detail)
/custom/                                (service detail)
/pre-purchase-inspection/               (service detail)
/bmw-service/                           (brand service)
/harley-service/                        (brand service)
/ducati-service/                        (brand service)
/pricing/                               (pricing tables + PDF)
/projects/                              (projects hub)
/projects/inspirium/                    (project)
/projects/beckman/                      (project)
/projects/unbreakable/                  (project)
/projects/quanta-r/                     (project)
/projects/burly/                        (project)
/projects/sturmvogel/                   (project)
/projects/geometric/                    (project)
/projects/joker/                        (project)
/projects/hellboy/                      (project)
/projects/true-religion/                (project)
/about/                                 (about the workshop)
/community/                             (rider lounge and community)
/contact/                               (contacts + form + map)
/faq/                                   (10 Q/A, FAQPage schema)
/blog/                                  (blog hub)
/blog/revtech-110-oil-service-engine-gearbox-drive/  (blog article)
/news/                                  (news hub)
/news/ericeira-kustom-fest-2026/        (news article)
/news/opens-new-workshop-in-cascais/    (news article)
/news/lisbon-motorcycle-film-fest-2026-beckman/  (news article)
/privacy/                               (GDPR)
/cookies/                               (GDPR)
/terms/                                 (GDPR)
```

Each of the 35 path patterns has 4 language variants: `/path/`,
`/ru/path/`, `/uk/path/`, `/pt/path/`.

## 6. External services

| Service | Identifier | Used for | Access |
|---|---|---|---|
| Google Analytics 4 | `G-D15BLYEKBN` | Pageviews and events | GA4 owner email `fg@abrisart.com` |
| Meta Pixel | `1708697916976439` | Future ad campaigns | Meta Business owner |
| Cloudflare Worker | `https://icm-reviews.vg-ab6.workers.dev/` | Proxies Google Places API for reviews. 24h edge cache. | Cloudflare account that owns the Worker |
| Google Places API | (key stored as Worker secret) | Read reviews for `Place ID ChIJ-5VQL2bPHg0R-Oj5dD0Ojhk` | Google Cloud project owned by `fg@abrisart.com` |
| FormSubmit | `https://formsubmit.co/Ironcustom.office@gmail.com` | Delivers lead form submissions to email | Gmail account `Ironcustom.office@gmail.com` |
| Google Search Console | property = `https://ironcustommotors.com/` | SEO monitoring | account that verified the property |
| GitHub Pages | `dreamcarua/iron-moto-cascais` repo, `main` branch root | Hosting | repo collaborator access |
| Domain registrar | (the registrar that holds `ironcustommotors.com`) | DNS for the CNAME + email | account that owns the domain |

## 7. Contact and business facts

These appear in the site content and JSON-LD. Verify they are
still current before significant content changes.

- Address: R. António José da Silva 100 B, 2785-253 São Domingos de Rana, Cascais
- Phone / WhatsApp: +351 917 961 230
- Email: Ironcustom.office@gmail.com
- Hours: Tue–Sat 10:00–18:00 (closed Sun & Mon)
- Founded: 2010
- Founder: Yaroslav Lutytskyi
- Languages spoken: EN, RU, UK, PT

## 8. Pricing facts

These are embedded in the site copy and in `pricing_data.py`.

- Hourly rate: 50 €/h
- Pre-purchase inspection: 150 € flat
- Fault diagnostics: 50–350 € depending on depth
- Scheduled service: from 150 €
- Desmo service (Ducati): from 750 € (older Monsters) up to
  1 500 €+ (Panigale V4)
- Harley major service (25 000 km): from 400 €

## 9. Known incomplete / pending items

These are remaining planned items from the original TZ
(`ICM_TZ_website_development_ru.docx`, archived locally by the
project owner) and later scaling discussions as of 2026-06-17.

- Additional blog articles beyond the first workshop guide
- Separate `/diagnostics/` service landing page (TZ flags as P1;
  content currently included in `/motorcycle-service/`)
- Advanced lead form with brand, model, year, urgency, preferred
  date, photo upload
- Anti-spam on the form (reCAPTCHA v3 / honeypot / rate-limit)
- Thank-you / success state as a separate URL with its own
  analytics event
- Google Tag Manager container (events are dispatched to
  `dataLayer` but no GTM is loaded; `gtag` is wired directly)
- Server-side render of Google reviews into individual `Review`
  JSON-LD blocks for every review (currently 8 most-recent are
  embedded into the home pages via `build_reviews_schema.py`;
  the reviews widget fetches the full list via the worker at
  runtime)
- CMS — there is none. All content edits go through the repo
  and the build scripts. The TZ does not mandate a CMS.

## 10. Working conventions encoded in the codebase

These are enforced by the build scripts; the agent should follow
them when editing by hand.

- All asset paths are absolute (`/photos/...`, `/assets/...`).
  Relative paths break under `/ru/`, `/uk/`, `/pt/` subtrees.
- Internal page links inside a localized subtree include the
  language prefix. `localize_internal_links.py` enforces this.
- Translations live in two places that must stay in sync:
  (a) the `I18N` object inside `assets/main.js`, and
  (b) the pre-rendered HTML in the four language subtrees.
  Editing one without the other will produce inconsistent
  language switching.
- When a new page is added it must appear in all four languages,
  in `sitemap.xml`, in the page-meta lookup
  (`scripts/build/page_meta.py` and the corresponding
  `*_data.py`), and in the hreflang block at the top of each
  language's HTML.
- Cache-bust query string is bumped on every change to
  `assets/main.css` or `assets/main.js`. The convention is
  `?v=YYYYMMDD<letter>`. The current value at the time of this
  handoff is `20260602b`.
- All `<img>` elements have explicit `width` and `height`
  attributes plus `loading="lazy"`. `scripts/build/add_image_dims.py`
  reads pixel sizes from the actual image files.
- Site copy is restrained — the project owner asked that the
  tone stay premium and not garage-themed; emojis are not used
  in copy.

## 11. Resume point

For the latest commit on `main`, run:

```
git log -1 --oneline
```

Recent hardening work includes `7ea6b1b fix: harden multilingual SEO
rendering`, which removed an exposed sample Google API key from docs,
fixed localized JSON-LD URLs, fixed pre-rendering for `data-i18n-html`,
and regenerated the multilingual HTML. Detailed history is in
`CHANGELOG.md`.

The next stretches of work that were under discussion (as listed
in the TZ and tracked in the project owner's todo) include
blog rollout, anti-spam on the form, a separate `/diagnostics/`
landing page, and updates to brand-specific hero photos for
`/bmw-service/`, `/harley-service/`, `/ducati-service/`
(currently using default workshop photos). The owner has not
committed to ordering or scope for these.

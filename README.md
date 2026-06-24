# Iron Custom Motors - Website

Production marketing and lead-generation website for Iron Custom Motors, a
premium motorcycle workshop in Cascais, Greater Lisbon.

Production domain: https://ironcustommotors.com/

## Current State

- Static HTML, CSS, and vanilla JavaScript served by GitHub Pages.
- Four pre-rendered languages: English at `/`, Russian at `/ru/`, Ukrainian at `/uk/`, Portuguese at `/pt/`.
- 143 HTML files in the repository: 140 indexable pages, `404.html`, and 2 noindex redirect stubs.
- 140 sitemap URLs: 35 indexable path patterns times 4 languages.
- JSON-LD, canonical, Open Graph, Twitter metadata, and hreflang are generated per language.
- Reviews are proxied through a Cloudflare Worker and embedded into home-page JSON-LD from `assets/reviews-snapshot.json`.
- Lead form posts to FormSubmit and also opens a WhatsApp fallback path.

## Stack

- Static HTML/CSS/JS, no application framework.
- Python build scripts in `scripts/build/` regenerate pages and metadata.
- Node.js is used only to extract the runtime `I18N` object from `assets/main.js`.
- GitHub Pages serves the repo root.
- Cloudflare DNS fronts the production domain.
- Cloudflare Worker proxies Google Places reviews so no Google Places API key is exposed in client HTML/JS.

## Maintenance Principles

- Build for the next developer. Page families, navigation, SEO metadata,
  schema, typography, and repeated content patterns should be controlled
  by shared data files, shared renderers, or documented utilities.
- Avoid isolated one-off generators or page-only editing paths when an
  existing generic build path can be extended safely.
- When a repeatable pattern changes, update the relevant documentation so
  future work can find the source file, generator, rebuild command, and
  verification check quickly.
- Prefer small, stable, reusable changes over manual patches that future
  generated pages will not inherit.

## Key Paths

```
/                              Home
/services/                     Services hub
/motorcycle-service/           Service and repair landing
/parts/                        Parts and consumables landing
/upgrades-tuning/              Upgrades and tuning landing
/custom/                       Custom and special projects landing
/pre-purchase-inspection/      Pre-purchase inspection landing
/bmw-service/                  BMW Motorrad service landing
/harley-service/               Harley-Davidson service landing
/ducati-service/               Ducati service landing
/projects/                     Custom projects portfolio hub
/projects/<slug>/              Individual project pages
/pricing/                      Price list with PDF downloads
/about/                        Workshop and brand story
/contact/                      Contact details and map
/faq/                          Frequently asked questions
/blog/                         Practical workshop blog hub
/blog/<slug>/                  Workshop guide articles
/news/                         News hub
/news/<slug>/                  News articles
/privacy/                      Privacy policy
/cookies/                      Cookie policy
/terms/                        Terms and conditions
```

Legacy noindex redirect stubs:

```
/projects/nezlamniy/           Redirects to /projects/unbreakable/
/projects/quanta/              Redirects to /projects/quanta-r/
```

## Setup

```bash
python3 -m pip install -r requirements.txt
```

If macOS reports an externally managed Python environment, use a virtual
environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Local Preview

```bash
python3 -m http.server 8080
```

Open http://localhost:8080/ in a browser.

## Build Workflow

Detailed source-of-truth instructions live in `scripts/build/README.md`.

Full safe rebuild after content or page-structure changes:

```bash
node scripts/build/extract_i18n.js
python3 scripts/build/build_new_pages.py
python3 scripts/build/build_brand_pages.py
python3 scripts/build/build_legal_pages.py
python3 scripts/build/build_news.py
python3 scripts/build/build_blog.py
python3 scripts/build/build_pricing.py
python3 scripts/build/nav_patch.py
python3 scripts/build/build_i18n.py
python3 scripts/build/localize_internal_links.py
python3 scripts/build/add_image_dims.py
python3 scripts/build/build_sitemap.py
```

Run `scripts/build/build_reviews_schema.py` only when a fresh Google reviews
snapshot is needed. It calls the Cloudflare Worker and requires network
access.

When `assets/main.css` or `assets/main.js` changes, bump the cache-bust query
string across generated HTML and keep the `CACHE_BUST` constants in build
scripts in sync.

## Verification Checklist

Before publishing substantial work:

```bash
node --check assets/main.js
node --check assets/projects.js
node --check worker/reviews.js
python3 -m py_compile scripts/build/*.py
python3 scripts/build/build_sitemap.py
git diff --check
```

Also verify:

- sitemap URL count matches indexable HTML pages
- canonical and hreflang are correct for every language
- localized JSON-LD URLs match the localized page URL
- internal links in `/ru/`, `/uk/`, `/pt/` stay inside the same language subtree
- all local image, CSS, JS, and PDF references resolve
- no Google Places API key or other secret is present in repo text
- key desktop and mobile pages render without horizontal overflow

## External Services

- Domain: `ironcustommotors.com`
- Hosting: GitHub Pages
- DNS/CDN: Cloudflare
- Reviews Worker: `https://icm-reviews.vg-ab6.workers.dev/`
- Google Analytics 4: `G-D15BLYEKBN`
- Meta Pixel: `1708697916976439`
- Form backend: FormSubmit for `Ironcustom.office@gmail.com`

Secrets are documented by variable name in `.env.example`. Do not commit real
secret values.

## Deploy

```bash
git add .
git commit -m "..."
git push
```

GitHub Pages deploys from `main`. Cloudflare may keep cached HTML/assets for a
short time after a push unless the cache is purged.

## Scaling Priorities

The technical base is static, fast, and suitable for SEO content scaling. The
next content/product expansions are:

- More workshop blog articles for long-tail SEO and AI citations.
- Dedicated diagnostics landing page.
- Advanced lead form fields and anti-spam protection.
- Thank-you or lead-success page if paid acquisition needs cleaner conversion attribution.
- CMS or structured content pipeline only if non-developers must publish pages regularly.

# Iron Custom Motors — Website

Premium motorcycle service, parts, upgrades and custom expertise in Cascais.
Single-page marketing website. EN / RU / UK / PT.

## Two concepts in one repo

- `index.html` — **V1: Premium Industrial.** Dark charcoal + iron-orange accent, condensed display (Saira), magazine grid.
- `v2/index.html` — **V2: Editorial Racing.** Light bone background + racing crimson, serif display (Fraunces), magazine "Issue 001" framing, 3D tilt projects, custom-text cursor, accordion why-list.

When deployed via GitHub Pages they live side by side:
- `<user>.github.io/iron-moto-cascais/` — V1
- `<user>.github.io/iron-moto-cascais/v2/` — V2

## Stack

- Plain HTML + CSS + vanilla JS in a single `index.html`
- No build step, no dependencies
- Google Fonts (Saira, Saira Condensed, Inter) loaded via CDN
- Photo placeholders served from Unsplash CDN — to be replaced with brand photography

## Local preview

Just open `index.html` in any modern browser.

```bash
# or serve with any static server
python3 -m http.server 8080
# then http://localhost:8080
```

## Deploy

Static hosting only — drop `index.html` (and the `LOGO/` folder if used) on any of:

- GitHub Pages (push to `main`, enable Pages in Settings → Pages → branch `main`, root)
- Netlify (drag-and-drop the folder, or connect this repo)
- Vercel (import the repo, framework: Other)
- Cloudflare Pages (connect this repo, build command: empty, output: root)

Custom domain example: `ironcustom.pt`

## Languages

The four languages live in the `I18N` dictionary at the bottom of `index.html`.
Switch is instant (no reload), the choice is stored in `localStorage`.
Add or edit copy directly in that JS object.

## Real data

- Phone / WhatsApp: +351 917 961 230
- Email: Ironcustom.office@gmail.com
- Address: R. António José da Silva 100 B, 2785-253 São Domingos de Rana, Cascais
- Hours: Tue–Sat · 10:00–17:00 · Closed Sun & Mon

## Roadmap (next iteration)

- Replace Unsplash placeholder photos with real workshop / project photography
- Embed Google Maps for the workshop address (currently address-only block)
- Wire form `submit` to a CRM webhook or Google Sheets endpoint
- Optional Phase 2: extract sections into multipage structure with `/services`, `/parts`, `/projects` etc. for deeper SEO
- Add Open Graph image (`og.jpg`) and `favicon.ico`
- GA4 + Meta Pixel snippets

## Brand assets

The `LOGO/` folder is intentionally git-ignored (kept locally only). For deployed builds, the inline SVG inside `index.html` is what's actually rendered, so no external asset is required.

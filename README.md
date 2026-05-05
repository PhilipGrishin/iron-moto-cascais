# Iron Custom Motors — Website

Premium motorcycle service, parts, upgrades and custom expertise in Cascais.
Multipage marketing website with 4 languages (EN / RU / UK / PT).

## Domain

Production: **https://ironcustommotors.com/**

`CNAME` file in repo root tells GitHub Pages to serve the site on this custom domain.

## Site map

```
/                              — Homepage (long-scroll, all sections)
/motorcycle-service/           — Service & repair landing
/parts/                        — Parts & consumables landing
/upgrades-tuning/              — Upgrades & tuning landing
/custom/                       — Custom & special projects landing
/pre-purchase-inspection/      — Pre-purchase inspection landing (SEO target)
/v2/                           — Alternative concept (editorial racing)
/v3/                           — Alternative concept (cyberpunk neon)

/assets/main.css               — Shared styles
/assets/main.js                — Shared interactivity + i18n
/photos/                       — Brand assets (logo, OG image, lounge photo)
/sitemap.xml                   — Search engine sitemap
/robots.txt                    — Crawl directives
/CNAME                         — GitHub Pages custom domain
```

## Stack

- Plain HTML + CSS + vanilla JS in static files
- No build step, no dependencies
- Google Fonts (Saira, Saira Condensed, Inter) loaded via CDN
- Photos served from `/photos/` (replace placeholders with brand photos as ready)

## Languages

The four languages live in the `I18N` dictionary in `assets/main.js`.
Switch is instant (no reload), choice persists in `localStorage`.
Default is English.

## Real data integrated

- Phone / WhatsApp: +351 917 961 230
- Email: Ironcustom.office@gmail.com
- Address: R. António José da Silva 100 B, 2785-253 São Domingos de Rana, Cascais
- Hours: Tue–Sat · 10:00–18:00 · Closed Sun & Mon
- GA4: G-PJWZKP1CFW
- Meta Pixel: 1708697916976439
- Form backend: formsubmit.co/Ironcustom.office@gmail.com (needs first-time activation by clicking the verification email)

## Cloudflare DNS setup for ironcustommotors.com

After GitHub Pages is enabled and the repo is deployed:

1. In **Cloudflare DNS** for `ironcustommotors.com` add records:

   | Type  | Name | Target                                  | Proxy   |
   |-------|------|-----------------------------------------|---------|
   | CNAME | @    | `<your-github-username>.github.io`      | Proxied |
   | CNAME | www  | `<your-github-username>.github.io`      | Proxied |

   _GitHub Pages also accepts 4 A records pointing to GitHub IPs (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153) on the apex `@` if your DNS provider doesn't do CNAME flattening — Cloudflare does, so CNAME on `@` works._

2. In **GitHub repo Settings → Pages**:
   - Source: Deploy from a branch
   - Branch: `main` (root)
   - Custom domain: `ironcustommotors.com`
   - Enforce HTTPS: ✅

3. In **Cloudflare SSL/TLS**: set to **Full (strict)**.

4. **Cloudflare → Rules → Page Rules** (recommended):
   - `http://ironcustommotors.com/*` → Always Use HTTPS
   - `www.ironcustommotors.com/*` → Forwarding URL 301 → `https://ironcustommotors.com/$1`

## Local preview

```bash
# from project root
python3 -m http.server 8080
# open http://localhost:8080
```

## Deploy

```bash
git add . && git commit -m "..." && git push
```

GitHub Pages re-deploys within 30–60 seconds.

## Roadmap (next iteration)

- Replace Unsplash placeholder photos in homepage Hero/Projects/Why with real workshop / project photography
- Add real Google Reviews integration via Google Places API or static screenshots after first 10 reviews are collected
- Add pricing transparency block ("from €X") under each service page
- Add `/about/`, `/community/` standalone pages (currently sections on home)
- Phase 2: blog/insights for SEO content marketing

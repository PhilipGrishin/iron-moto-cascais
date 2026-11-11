# S-STAGE1 delivery record

Date: 2026-11-11. Status: **deployed and production-verified**.
Baseline: `8c760d835cf83c6aaceed5700965edf3714f9229`, clean `main` after a
fast-forward that preserved the two upstream review refresh commits.

## Approved scope and decisions

- **Confirmed:** attached S-STAGE1 brief takes precedence over the earlier
  prompt file. Protected pages may change shared chrome and cache references;
  their content, schema and content dates remain protected.
- **Confirmed owner decision, 2026-11-11:** S-STAGE1-NAV supersedes the ninth
  menu item plan. Stage replaces Authorized Dealer after Harley Hub. Dealer
  pages remain indexable and are reached through footer/contextual links.
  Shared spacing, typography and responsive breakpoint are preserved unless
  measured acceptance requires a documented correction.
- Approved source files and catalogue PDFs were checksum-verified at intake.
  Stage, integrations and News are stored byte-identically in `content/`;
  the DCF source is replaced by approved revision 2. Only the four authorized
  lines in each of Upgrades and Harley copy are replaced.
- **Confirmed:** hero source is 1504 × 1200. Existing encoder produces
  768/1280/1504 AVIF, WebP and JPEG, without upscaling or regrading.
  Official SVG downloaded to `photos/stage/dcf-performance-logo.svg`;
  SHA-256 matches `c0e98ee95454394fd05ab782aba04717bc2d66a2b1ef8a73132d986801069b34`.
- Static approved catalogues are copied from `_media/stage1/pdf/`, not the
  differently linked copies in its parent directory.

## Implementation

- Registry/parser/renderer/validator: `stage_pages_data.py`, `stage_copy.py`,
  `build_stage_pages.py`, `validate_stage_pages.py`; family CSS: `assets/stage.css`.
- Approved inputs: `content/stage1_copy_4lang.md`,
  `content/stage1_integrations_4lang.md`, `content/stage1_news_4lang.md` and revised
  `content/dcf_dealer_copy_4lang.md`. Current SHA pins are in the build README.
- Existing source owners changed: `pricing_data.py`, `news_data.py`,
  `authorized_dealer_data.py`, `w4_shared_data.py`; the two exact contextual
  replacements are in Upgrades/Harley Markdown. Builders, discovery registries,
  shared navigation, extraction, validators and Pages packaging consume these.
- Service PDFs keep their existing published filenames and now contain the
  three Stage rows and note. The four static catalogues match their supplied
  hashes. Hero widths are 768, 1280 and 1504; image provenance is recorded in
  `photos/stage/stage-1-media.json`. The official logo is
  `photos/stage/dcf-performance-logo.svg`.
- News `publishedISO` and `modifiedISO`: `2026-11-11T16:37:40+00:00` (Lisbon).
  Older articles keep their exact related selection, copy, schema and dates.
- No approved visible text was reworded. Source-only field labels/list syntax
  become semantic layout; price tokens are checked against the pricing registry
  before that registry emits them. Invalid source checksums and price drift
  were deliberately rejected, without changing originals.

## Header measurements

**Data-backed:** Chromium/Playwright, CSS pixels, device scale 1, height 1000,
loaded fonts, localhost, 2026-11-11. Full 24-case before/after measurements are
in [the measurement record](S_STAGE1_HEADER.json). `assets/main.css` is
byte-identical to baseline: no chrome spacing, type scale or breakpoint changes.

| Language | Before | After |
|---|---|---|
| EN | Services · Brands · Harley Hub · Authorized Dealer · Projects · About · Pricing · Contact | Services · Brands · Harley Hub · Stage · Projects · About · Pricing · Contact |
| PT | Serviços · Marcas · Harley Hub · Revendedor Oficial · Projetos · Sobre · Preços · Contacto | Serviços · Marcas · Harley Hub · Stage · Projetos · Sobre · Preços · Contacto |
| RU | Услуги · Бренды · Harley Hub · Официальный дилер · Проекты · О нас · Цены · Контакты | Услуги · Бренды · Harley Hub · Stage · Проекты · О нас · Цены · Контакты |
| UK | Послуги · Бренди · Harley Hub · Офіційний дилер · Проєкти · Про нас · Ціни · Контакти | Послуги · Бренди · Harley Hub · Stage · Проєкти · Про нас · Ціни · Контакти |

| Language | Viewport | Menu width before → after | Right edge of controls before → after |
|---|---:|---:|---:|
| EN | 1200 | 669.3 → 572.7 | 1148.8 → 1148.8 |
| EN | 1280 | 669.3 → 572.7 | 1228.8 → 1228.8 |
| PT | 1200 | 683.5 → 582.9 | 1183.6 → 1140.0 |
| PT | 1280 | 683.5 → 582.9 | 1220.0 → 1220.0 |
| RU | 1200 | 621.7 → 518.1 | 1140.0 → 1140.0 |
| RU | 1280 | 621.7 → 518.1 | 1220.0 → 1220.0 |
| UK | 1200 | 611.5 → 534.7 | 1140.0 → 1140.0 |
| UK | 1280 | 611.5 → 534.7 | 1220.0 → 1227.3 |

All final 1200/1280/1366/1440/1536/1920 cases have eight primary items, one
line per label, no overlapping logo/menu/actions and no viewport escape.
Dropdown hover and the mobile accordion reveal the registered Stage 1 item.
All 268 pages that have managed chrome, including four noindex thank-you pages,
share that menu/footer. The existing bare 404 and twelve immediate redirects
have no site menu and remain structurally unchanged. Full utility refresh also
corrected the previously stale Projects submenu (missing Spaniard); forms and
other utility content are preserved. No obsolete dealer dropdown registry or
navigation-only labels remain. Contextual dealer title keys are explicitly
named as related titles rather than navigation keys.

## Local acceptance

- Exact Stage source units and section counts pass in all languages; FAQ eight
  items match JSON-LD 1:1; Service emits only the two approved Offers with VAT.
- DCF revision 2 passes complete copy and six-item FAQ parity. Twelve dealer
  URLs remain in sitemap and llms, with footer/hub/contextual incoming links.
- Pricing has three rows, exactly two additional numeric Offers, two hero
  downloads, two section buttons and the approved descriptions. All four
  generated service PDFs contain the same names, prices, descriptions and note.
  The changed final pages were rendered and visually reviewed in every language.
- No new price occurs on protected brand pages: the brand renderer now emits
  only the related translations it displays and preserves historical unused
  entries. This prevents new registry values leaking into unrelated payloads.
- [Scope audit](S_STAGE1_SCOPE.json): 236 changed existing HTML files are
  semantically identical outside managed chrome/cache. Upgrades and Harley
  tuning each differ in visible main text by exactly the four authorized lines.
  The 24 old News variants retain copy/schema/dates and related selections.
- Sitemap: eight new URLs, 24 changed content dates, 232 previous dates preserved.
  Introduced currency amounts are limited to the authorized families/integrations;
  older pre-existing price occurrences remain untouched.
- [Responsive checks](S_STAGE1_BROWSER.json): four languages × 360/768/1280,
  viewport height 900. Zero horizontal overflow and JavaScript errors, all
  images decode, one responsive AVIF hero request per page, working dropdown/
  accordion and process scroll. Price plus exception footnote fit the initial
  viewport in every case (lowest footnote ends at approximately 826 CSS px).
  Smaller viewport heights naturally require scrolling; nothing is hidden in
  an accordion. WhatsApp prefill and language-specific PDF targets are checked.
- Page sections were visually inspected against the supplied catalogue. A
  temporary CSS class collision between a section and its inner grid was found
  during visual QA and corrected before release.

## Release evidence

- Implementation: `c7fbbb5c693092d397207e7b38a8a7755efcf9f5`.
- **Confirmed:** documented Full Safe Rebuild and `verify_site.sh` passed in a
  fresh non-shallow clone of that commit. All four service PDFs and generated
  output reproduced exactly; `git status --short` was empty.
- Local release validators, Worker tests and syntax checks passed.
- Published artifact: `4ddabb8b7b7b4baefd5242caa7595bf8a7fccb0d`, containing the
  implementation and acceptance documentation. [Pages run 43061911928](https://github.com/PhilipGrishin/iron-moto-cascais/actions/runs/43061911928)
  passed every validation/packaging/deployment step, completed 16:50:28 UTC.
- **Confirmed production, 2026-11-11:** all 264 sitemap URLs and four thank-you
  pages returned 200 and matched local main content, JSON-LD, title/description,
  canonical/hreflang, desktop/mobile navigation, footer and cache keys. All 26
  checked discovery/shared/media/PDF assets match repository bytes. These checks
  include the twelve dealer URLs and all eight downloadable PDFs.
  [Raw evidence](S_STAGE1_PRODUCTION.json).
- Initial comparison reported twelve email-bearing pages because Cloudflare's
  email-obfuscation wrapper split a text node. The comparison now decodes the
  known wrapper and merges adjacent text nodes on both sides; no site edit was
  needed. The complete rerun passed, with no remaining differences.
- **Data-backed production browser:** four languages at 360/768/1200/1280,
  height 900; sixteen cases, loaded fonts/images, no horizontal overflow or
  dealer header links. The eight desktop labels stay on one line with no
  logo/menu/control overlap. Price and footnote fit all initial viewports.
  Native in-app-browser measurements include its 10 px vertical scrollbar;
  local Chromium baseline measurements above remain the direct before/after
  comparison. [Compact production measurements](S_STAGE1_LIVE_BROWSER.json).
  PT desktop/mobile hero views were visually inspected. Mobile Stage expands
  to Stage 1, and the process link finishes at 69.875 px below the viewport top.
  No page errors were reported; no contact message or form was sent.
- **Confirmed Google Rich Results, mobile agent:** [PT Stage 1](https://search.google.com/test/rich-results/result?id=EQ1-gOf6KxdiCkxjOfbLEg)
  returned three valid supported items (Breadcrumb, Local business,
  Organization) at 16:50:44. [PT News](https://search.google.com/test/rich-results/result?id=4Gi_YwNazfHLQSuqX8TICg)
  returned four (Article plus those three) at 16:51:22. Neither summary showed
  errors or warnings. FAQ/Service Offer parity is protected by the local
  validator, independently of Google's supported rich-result types.
- All requested acceptance criteria are closed within the documented scope.
  The thirteen pre-existing bare utility documents have no chrome to replace;
  all four utility pages with chrome are included in the 268-page verification.
  No approved visible copy required rewording. Existing workflow runtime
  notices and macOS PDF portability remain separate maintenance risks, as
  recorded in `docs/OPEN_TASKS.md`.
- Final closeout is documentation-only and uses `[skip ci]`; it does not change
  this verified public artifact.

## Changed source and configuration inventory

Confirmed by `git diff --name-only 8c760d8 c7fbbb5c`; generated HTML, discovery
files, binary media/PDFs and documentation evidence are omitted from this source
list. The extracted `i18n.json` snapshot is included because builders consume it.

- `.gitattributes`
- `.github/workflows/pages.yml`
- `assets/main.js`
- `assets/stage.css`
- `scripts/build/authorized_dealer_data.py`
- `scripts/build/build_brand_pages.py`
- `scripts/build/build_harley_hub.py`
- `scripts/build/build_legal_pages.py`
- `scripts/build/build_llms.py`
- `scripts/build/build_new_pages.py`
- `scripts/build/build_news.py`
- `scripts/build/build_pricing.py`
- `scripts/build/build_pricing_pdfs.py`
- `scripts/build/build_project_pages.py`
- `scripts/build/build_service_custom_hubs.py`
- `scripts/build/build_sitemap.py`
- `scripts/build/build_stage_pages.py`
- `scripts/build/content/dcf_dealer_copy_4lang.md`
- `scripts/build/content/harley_hub_phase1_4lang.md`
- `scripts/build/content/stage1_copy_4lang.md`
- `scripts/build/content/stage1_integrations_4lang.md`
- `scripts/build/content/stage1_news_4lang.md`
- `scripts/build/content/upgrades_hub_copy_4lang.md`
- `scripts/build/dealer_copy.py`
- `scripts/build/extract_i18n.js`
- `scripts/build/i18n.json`
- `scripts/build/import_dealer_images.py`
- `scripts/build/localize_internal_links.py`
- `scripts/build/nav_patch.py`
- `scripts/build/news_data.py`
- `scripts/build/pricing_data.py`
- `scripts/build/site_chrome.py`
- `scripts/build/stage_copy.py`
- `scripts/build/stage_pages_data.py`
- `scripts/build/validate_authorized_dealer.py`
- `scripts/build/validate_seo.py`
- `scripts/build/validate_service_custom_hubs.py`
- `scripts/build/validate_stage_pages.py`
- `scripts/build/validate_w4_routing.py`
- `scripts/build/verify_site.sh`
- `scripts/build/w4_shared_data.py`

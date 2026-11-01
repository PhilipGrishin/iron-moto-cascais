# N-DCF delivery record

Date: 2026-11-01. Status: implementation in progress.

## Intake and decisions

- Confirmed clean baseline and fetched origin: `95eaf7a82b95af311218dec0a026e4cf4f84975b`.
- Approved copy is preserved byte-for-byte at
  `scripts/build/content/dcf_dealer_news_4lang.md`, SHA-256
  `1421651ee33ec8eb1f0664ca470235ec1b185ce44568bd4ef237ae8d174c5f94`.
  The existing checked News parser remains the only copy-rendering path.
- Make the gallery optional through the parser, renderer, importer and validator.
  A present gallery keeps the existing after-section-two contract; absence
  generates no gallery block, copy keys or images.
- Reuse the nine existing DCF dealer hero variants. The News picture container
  has centered cover behavior, not a required landscape source ratio; registered
  widths allow the same portrait file to serve the new article and hub card.
  New binary media weight: **0 bytes**. No photo edit or new crop is needed.
- Pin Spaniard's current related-News selection so the sixth registry entry
  does not change any previous article. Keep other selections as registered.
- Homepage inspection confirms only navigation/footer News links and no latest-
  news feed. Only the four News hubs gain a first card; all home pages remain
  unchanged. Shared runtime assets and cache stamps are unchanged.
- Register actual publication-day content timestamp `2026-11-01T21:29:06+00:00`,
  read from the UTC clock; Europe/Lisbon is UTC+0 on this date. Publication labels,
  NewsArticle dates and new sitemap dates derive from this stable value.
- Use the explicit author business reference introduced for Spaniard; author
  and publisher resolve to one complete business entity.
- Planned acceptance: exact approved copy and links, optional/no-gallery cases,
  checksum rejection, unchanged previous articles and protected files, precise
  sitemap scope, all validators, PT responsive checks, fresh full-history clone
  Full Safe Rebuild, publication verification and PT Google Rich Results Test.

## Local acceptance

- Full Safe Rebuild passed in the primary checkout, including all PDF outputs
  and every validator family; post-rebuild scope matches the narrow build.
  The common release gate also passed, including JS syntax and Leads Worker tests.
- The hero-only importer ran with the real optimizer in an isolated temporary
  directory, without gallery configuration. Eleven expected image files were
  created, no gallery appeared and no repository media was written. Evidence:
  [importer smoke check](N_DCF_IMPORTER_CHECK.json).

- Source SHA matches the owner file. A one-byte mutation caused the generator
  to fail before rendering; original bytes were restored. All four blocks
  parse without a gallery, and malformed gallery tokens are rejected.
  Evidence: [copy/parser checks](N_DCF_CHECKSUM.json).
- All 12 approved-source News variants pass complete copy, ordered sections,
  links, schema, dates, canonical/hreflang, media and related-selection checks.
  Every language hub contains six cards in descending publication order.
- [Scope audit](N_DCF_SCOPE.json): only four previous HTML files change (News
  hubs). The other 265 old files, including all 20 old article variants and
  all home/dealer/Upgrades/Fuel pages, are byte-identical. Hub navigation,
  footer and forms remain identical. All 156 previous form pages are preserved.
  Runtime assets, pricing/PDFs, Workers, reviews and photos have no changes.
- Checked 44,684 local URL/media references including responsive candidates,
  plus 600 real fragment destinations, with no broken target.
- [Browser checks](N_DCF_BROWSER_LOCAL.json): installed Chrome via Playwright,
  PT 390/DPR2 and 1440/DPR1. Zero overflow, JavaScript errors or HTTP failures;
  one hero request at each viewport (1280 AVIF / 1536 AVIF), no gallery, four
  body sections and two approved dealer links. Clicking the article link and
  first News-hub card reaches the correct Portuguese destination. Hero, body
  and hub screenshots were visually inspected. Lead events were intercepted;
  no contact form or WhatsApp message was submitted.

## Exact sitemap accounting

252 URLs become 256; 248 existing lastmod values remain unchanged. New article
and four hub dates use `2026-11-01T21:29:06+00:00`.

New approved announcement:

- `https://ironcustommotors.com/news/dcf-performance-dealer-portugal/`
- `https://ironcustommotors.com/ru/news/dcf-performance-dealer-portugal/`
- `https://ironcustommotors.com/uk/news/dcf-performance-dealer-portugal/`
- `https://ironcustommotors.com/pt/news/dcf-performance-dealer-portugal/`

Existing pages with a new first News card:

- `https://ironcustommotors.com/news/`
- `https://ironcustommotors.com/ru/news/`
- `https://ironcustommotors.com/uk/news/`
- `https://ironcustommotors.com/pt/news/`

The homepage has no latest-News block; its four files and content dates remain
unchanged. The new registry entry automatically feeds generic i18n, localized
links, sitemap and llms. Deployment already copies the complete News directory
and language roots. No manual deployment allowlist or route duplication is needed.

## Media and scope notes

- Reused `/photos/authorized-dealer/dcf-performance-hero-{768,1280,1536}` in
  AVIF/WebP/JPEG; existing EXIF-free files and dimensions are unchanged.
- Added media weight: **0 bytes**. Existing image weights/source hashes remain
  in `photos/authorized-dealer/dcf-performance-media.json`. Reuse saves storage,
  not the initial transfer of the selected hero candidate.
- `heroWidths` extends the existing picture path; no separate generator, CSS
  design or asset pipeline was added. The landscape-source crop condition does
  not apply because this container accepts portrait media with centered cover.
- `relatedSlugs` pins the existing Spaniard selection before adding the new
  story, preventing incidental old-article content or date changes.
- Shared JavaScript/CSS did not change, so no cache-bust bump is needed.
- The owner's approved equipment photograph retains its printed marks. No
  equipment-brand name is introduced in News copy, ALT text or asset filenames.

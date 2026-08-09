# B-TUBELESS Delivery Report

Date: 2026-08-09 (Europe/Lisbon)

## Outcome

The tubeless-conversion workshop video article is registered as the eighth
Blog post and rendered in EN/PT/RU/UK through the shared Blog pipeline. The
implementation commit is `fb4429e9`. Deployment and cache-bypass production
verification are pending.

Public paths:

- `/blog/tubeless-conversion-spoked-wheels/`
- `/pt/blog/tubeless-conversion-spoked-wheels/`
- `/ru/blog/tubeless-conversion-spoked-wheels/`
- `/uk/blog/tubeless-conversion-spoked-wheels/`

## Approved Copy And Generated Scope

The supplied four-language source was copied without rewriting to
`scripts/build/content/tubeless_conversion_blog_4lang.md`. The supplied file
and repository copy have the same SHA-256:

```text
c85b0cb625e2ecb8513445cadf9c0708a6f056c83e3c53733fd5f5ffd5b0b1f1
```

Service notes above the approved copy are not rendered. The common Markdown
video-post parser owns metadata, body sections, links, video placement and all
six FAQ items in every language.

The implementation commit contains 43 files:

- 4 new localized article HTML files.
- 4 regenerated Blog hubs, 4 tyre-service pages and 4 pricing pages.
- 4 regenerated price-list PDFs.
- The exact approved Markdown source and the maintained tyre-service source.
- One supplied hero source plus 9 optimized AVIF/WebP/JPEG candidates at the
  registered 768, 1280 and 1920 slots.
- Shared Blog, localization, sitemap, link-localization, tyre-service and
  pricing generators/data.
- Generated `sitemap.xml` and `llms.txt`.

No common CSS, JavaScript or cache-bust value changed.

## Video And Schema

The native 16:9 player uses these supplied media endpoints:

```text
https://media.ironcustommotors.com/tubeless-conversion-spoked-wheels.mp4
https://media.ironcustommotors.com/tubeless-conversion-spoked-wheels-poster.jpg
```

Both endpoints returned HTTP 200 before the implementation commit. The MP4 is
registered as `video/mp4`, 294,648,850 bytes and `PT5M37S`; the poster is
`image/jpeg`, 550,412 bytes. The page renders the poster with `preload="none"`,
keeps the MP4 URL in `data-src`, and moves it to `src` only on the first player
click. Local browser inspection before activation found an empty
`currentSrc` and no MP4 in the page-assets inventory.

Each localized graph contains `BlogPosting`, the localized `VideoObject`,
`FAQPage`, `BreadcrumbList` and the complete `LocalBusiness` entity. The
publisher resolves through `https://ironcustommotors.com/#business`; article
and video dates use full ISO-8601 values with the Lisbon offset. Every page has
a self-canonical and a mutual `en`, `pt-PT`, `ru`, `uk`, `x-default` hreflang
cluster.

## Responsive Hero Evidence

The supplied and repository hero sources have identical SHA-256:

```text
3498603f9c3374a16d403207706ab8f15f6f6eae3f0ae92192ddb790037dd683
```

The article uses the maintained C7-FIX2 Blog contract: one AVIF preload with
`imagesrcset` and `imagesizes` byte-identical to the rendered AVIF source, one
non-lazy `fetchpriority="high"` hero image, and no other high-priority element.
The focused validator passed the complete selection matrix:

```text
Picture hero preload validation passed: 32 picture hero page(s); 390px/DPR3, 390px/DPR2, 768px/DPR2, 1280px/DPR1, 1440px/DPR1
```

The in-app browser cannot expose the exact maintained DPR3 network profile and
has a known 10 px viewport-scrollbar discrepancy. Therefore the five-case
candidate result is reported from the repository validator, not misrepresented
as an unavailable exact DPR3 browser capture. At the available 390 x 844 and
1440 x 1000 layouts the new page had one high-priority element, no high/lazy
conflict, no horizontal overflow, an unrequested MP4, and a 16:9 player box.

## Price And Reciprocal Links

The fixed service is generated from one `additional_services` record in
`pricing_data.py`. All four pricing pages, all four `OfferCatalog` graphs and
all four PDFs expose a numeric EUR 100 offer with these visible labels:

```text
EN: Tubeless conversion of spoked wheels — €100 per wheel
PT: Conversão tubeless de rodas de raios — 100 € por roda
RU: Конверсия спицованного колеса в бескамерное — €100 за колесо
UK: Конверсія спицьованого колеса в безкамерне — €100 за колесо
```

PDF text extraction found the new service on page 5 in all four documents.
All four page-5 renders were inspected at 140 dpi; the row and price are clear,
aligned and unclipped.

The required same-language reciprocal article links and price mention are in
the maintained spoked-wheel paragraph on:

- `/motorcycle-tyre-service/`
- `/pt/montagem-de-pneus-mota/`
- `/ru/shinomontazh-mototsiklov/`
- `/uk/shynomontazh-mototsykliv/`

The article already links back to the matching tyre-service path in each
language. A separate crawl of all tracked HTML found zero broken internal
targets.

## Sitemap Discipline

The sitemap grew from 224 to 228 URLs. No URL was removed. The repository
`sitemap.xml` SHA-256 is:

```text
d46186c47b0978039fdb93d1345438f6c37235f87cfc660a63cebbf0b3d16048
```

Exactly 16 lastmod values were added or changed:

- 4 new article URLs: the EN path and its `/pt/`, `/ru/`, `/uk/` variants.
- 4 Blog hubs: `/blog/` and its `/pt/`, `/ru/`, `/uk/` variants.
- 4 pricing pages: `/pricing/` and its `/pt/`, `/ru/`, `/uk/` variants.
- 4 tyre-service pages: the English path and the three localized slugs listed
  above.

All other 212 pre-existing sitemap lastmod values are byte-identical to the
previous sitemap.

## Validator And Rebuild Evidence

Broad validator:

```text
SEO validation passed: 228 sitemap URL(s)
```

Brand validator:

```text
Brand page validation passed: 7 brand page set(s).
```

Harley Hub validator:

```text
Harley Hub validation passed: 12 pages and all required integrations
```

All 14 registered project validations passed their multilingual copy, media,
schema, cache-bust, redirect and integration checks. The clean-clone Full Safe
Rebuild and production checks are pending and must replace this sentence before
final delivery.

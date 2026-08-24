# N-BBQ Delivery Report

Date: 2026-08-24 (Europe/Lisbon)

Implementation commit: `f4d4dd071ecf463fc9359bbc0b27bf3aacc3f6e0`

Merged deployed state: `93b4f46089b7b8f76e86e2f9b9a5f4f1a8cbd2a0`

GitHub Pages workflow: `32704971695` (`success`, 44 seconds)

## Delivered URLs

- `https://ironcustommotors.com/news/workshop-bbq-party-august-2026/`
- `https://ironcustommotors.com/pt/news/workshop-bbq-party-august-2026/`
- `https://ironcustommotors.com/ru/news/workshop-bbq-party-august-2026/`
- `https://ironcustommotors.com/uk/news/workshop-bbq-party-august-2026/`

All four cache-bypass requests returned HTTP 200 after deployment.

## Approved Copy And Integration

The supplied source and the repository copy are byte-identical. Their
SHA-256 is:

```text
e6f7f3745c53b704832aad44e1a2bebbd1f9dc6c71f749360fb5df9cf6e76a16
```

The common source parser rendered the supplied title, metadata, H1, lede,
four section headings, seven paragraphs, link anchors, hero ALT, gallery label
and all ten numbered gallery ALT strings without rewriting them. Focused
comparisons passed in EN, PT, RU and UK. The placeholders became same-language
Community and Contact links plus the registered gallery; no source-only notes
appear on the public pages.

The card is first on all four `/news/` hubs. The same registered order also
adds the new story to the related-story area on each of the twelve existing
localized News articles. No homepage or other page family contained a News
feed requiring an update. Repository search found the new slug in exactly
these twenty HTML files.

## Media, Layout And Hero Selection

The News importer created:

- two source hero JPEG sizes and nine optimized AVIF/WebP/JPEG candidates at
  the maintained 768, 1280 and 1920 names;
- sixty gallery candidates: ten photographs, two widths (800 and 1600), and
  AVIF/WebP/JPEG at each width.

The gallery images are all 1600 x 1200 in their fallback markup, have explicit
dimensions, use `loading="lazy"` and `decoding="async"`, and have responsive
AVIF/WebP sources. There is no gallery script dependency. The gallery is a
contained horizontal `scroll-snap` region; a mobile swipe changed only the
gallery's `scrollLeft` while page scroll position and page width stayed fixed.

Cold local browser checks measured:

```text
390 x 844: page overflow 0; one 768 AVIF hero request;
           gallery client/scroll width 340/3466 px; x mandatory snap.
1440 x 900: page overflow 0; one 1920 AVIF hero request;
            gallery client/scroll width 665/6948 px; 680 px cards.
```

Production browser checks selected the 768 AVIF CSS image set at 390 x 844 and
the 1920 AVIF CSS image set at 1440 x 900, again with zero page overflow and
the same ten-item internal gallery geometry. Representative production 768
and 1920 hero AVIF files and gallery items 1 and 10 returned HTTP 200. The
common CSS and JavaScript files were not changed, so the cache-bust remains
`20260724a`.

## Structured Data And Metadata

Every localized article has:

- a self-canonical URL;
- mutual `en`, `pt-PT`, `ru`, `uk` and `x-default` alternates;
- `NewsArticle`, localized `BreadcrumbList` and a complete referenced
  `LocalBusiness` entity;
- `datePublished` and `dateModified` set to
  `2026-08-23T10:00:00+01:00`;
- a localized author URL and publisher `@id` resolving to the document's
  named `LocalBusiness` entity and logo.

Google Rich Results Test result `YVVmMMh-Ri99Utdpst9nbA` crawled the live EN
URL successfully and detected four valid items. Article, Breadcrumbs and Local
business each report one valid item with no errors. Organization is also
valid and carries a non-critical suggestion, not an error.

## Sitemap And Machine Discovery

The sitemap grew from 232 to 236 URLs. Its repository and production
SHA-256 is:

```text
4ef974f467c30c2e67efe7e276dbb6b03f93efd87959a3e72d7178673a9c31ae
```

Exactly twenty `lastmod` values were added or moved to
`2026-08-23T10:00:00+01:00`:

- the four new article URLs;
- `/news/`, `/pt/news/`, `/ru/news/`, `/uk/news/`;
- the EN/PT/RU/UK variants of `ericeira-kustom-fest-2026`,
  `opens-new-workshop-in-cascais`, and
  `lisbon-motorcycle-film-fest-2026-beckman`, whose visible related-story feed
  changed.

No other `lastmod` changed. Production `sitemap.xml` is byte-identical to the
repository artifact. Generated production `llms.txt` is also byte-identical,
contains the new English path, lists 59 English pages and has SHA-256:

```text
a8b748b20a7a3602b89e7ae2df1d3c629b6fca1e7c1dc913da88dd456c0696cd
```

## Verification

Focused source/render output:

```text
en OK h2=4 paragraphs=7 gallery=10 schema=resolved
pt OK h2=4 paragraphs=7 gallery=10 schema=resolved
ru OK h2=4 paragraphs=7 gallery=10 schema=resolved
uk OK h2=4 paragraphs=7 gallery=10 schema=resolved
```

Canonical validator output:

```text
SEO validation passed: 236 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
```

All fourteen registered project validators separately reported `OK` for their
multilingual copy, media, schema, cache-bust, redirect and integration checks.
`node --check`, Python compilation and `git diff --check` also passed.

The documented Full Safe Rebuild was run on a clean clone of merged deployment
state `93b4f460`. It regenerated the full site, passed all four validator
groups and left `git status --short` empty.

## Diff Scope

The implementation commit contains 104 files:

- twenty News HTML files: four new articles, four News hubs and twelve
  existing articles with a new visible related-story card;
- seventy-one new hero and gallery media files;
- the byte-identical approved Markdown source;
- News data, renderer, importer and shared registry/validation build files;
- generated `sitemap.xml` and `llms.txt`;
- News workflow and content-family documentation.

No homepage, Blog, project, service, pricing, legal or Authorized Dealer page
changed. Common CSS, JavaScript and cache-bust values did not change. The
automated Google Reviews refresh commit `1e2e9e6c` arrived independently while
the task was in progress, touched only the snapshot and four home pages, and
was merged without conflicts before the final clean-clone gate.

# B-TAPE Delivery Report

Date: 2026-08-15 (Europe/Lisbon)

Implementation commit: `6c24e8efc677130a5d116bf31232c155dd45ac5b`

GitHub Pages workflow: `31874899365` (`success`)

## Delivered URLs

- `https://ironcustommotors.com/blog/tubeless-sealing-tape-failure/`
- `https://ironcustommotors.com/pt/blog/tubeless-sealing-tape-failure/`
- `https://ironcustommotors.com/ru/blog/tubeless-sealing-tape-failure/`
- `https://ironcustommotors.com/uk/blog/tubeless-sealing-tape-failure/`

All four cache-bypass requests returned HTTP 200 after deployment.

## Approved Copy And Content

The supplied source and the repository copy are byte-identical. Their
SHA-256 is:

```text
7a2be15393fd5581b84ef337be47fe87d5ffb05ec51f8d8229071848e96b62b6
```

The common Markdown parser found and rendered all approved metadata, headings,
paragraphs and exactly five FAQ items in each language. Source-only service
notes are not present in the generated pages. Focused comparisons found no
missing approved content.

The four Blog hubs contain the new localized card. The maintained sister
article contains one same-language reciprocal link on each of these pages:

- `/blog/tubeless-conversion-spoked-wheels/`
- `/pt/blog/tubeless-conversion-spoked-wheels/`
- `/ru/blog/tubeless-conversion-spoked-wheels/`
- `/uk/blog/tubeless-conversion-spoked-wheels/`

The new article already links to the sister article and the localized
tyre-service page as supplied. A separate crawl checked 34,084 internal link
references across all 232 sitemap pages and found zero broken targets.

## Media, Layout And Network

The supplied hero was copied without modification; the source and repository
PNG share SHA-256:

```text
4df99bfb9290d9f80a04962fcff8f9f20cec18d85f6397502793f382c5756325
```

The image pipeline generated AVIF, WebP and JPEG candidates at the maintained
768, 1280 and 1920 candidate names without upscaling the 941 x 1672 source.
Every article has one high-priority hero, no high-plus-lazy conflict, and an
AVIF preload whose `imagesrcset` and `imagesizes` equal the rendered AVIF
source attributes.

The self-hosted media endpoints returned:

```text
MP4:    HTTP 200, video/mp4, 48,457,753 bytes, 1080 x 1920, PT1M33S
Poster: HTTP 200, image/jpeg, 512,905 bytes, 941 x 1672
```

The generated player has `preload="none"`; its source has no `src` before
interaction and retains the MP4 only in `data-src`. Production browser checks
confirmed `currentSrc` is empty and `readyState` is zero before activation.

At 390 x 844, the centered player measured 340 x 604.44 px at x=20 and the
document measured 380 px for both client and scroll width. The resource
inventory contained exactly the 768 AVIF hero and the poster, with zero video
resources.

At 1440 x 1000, the centered player measured 420 x 746.66 px at x=505 with
equal 142.41 px computed side margins; client and scroll widths were both
1430 px. The resource inventory contained exactly the 1920 AVIF hero and the
poster, with zero video resources. These measurements confirm the portrait
player and vertical card media do not create horizontal overflow.

## Structured Data And Metadata

Every localized article has:

- a self-canonical URL;
- mutual `en`, `pt-PT`, `ru`, `uk` and `x-default` alternates;
- `BlogPosting`, `VideoObject`, `FAQPage`, `BreadcrumbList` and the complete
  referenced `LocalBusiness` entity;
- five schema FAQ questions matching the visible FAQ;
- localized video `name` and `description`;
- `uploadDate`, `datePublished` and `dateModified` set to
  `2026-08-15T10:00:00+01:00`.

The SEO validator parsed this graph without errors. No external Rich Results
Test was required or represented as evidence.

## Sitemap And Machine Discovery

The sitemap grew from 228 to 232 URLs. Its repository and production SHA-256
is:

```text
d0c0d98dc180f44a3d13cadc859c7f1c355c8999557c2a232b84855d87d22b82
```

Exactly 12 lastmod values were added or moved to
`2026-08-15T10:00:00+01:00`:

- the four new article URLs;
- `/blog/`, `/pt/blog/`, `/ru/blog/`, `/uk/blog/`;
- the four localized tubeless-conversion article URLs listed above.

No other lastmod changed. Production `sitemap.xml` is byte-identical to the
repository artifact. Generated production `llms.txt` is also byte-identical
to the repository artifact, contains the English article path and has
SHA-256:

```text
9c63b8bef1f093fcff7f39d14e3fdc20e2d37a090e30407adcd26332c5c3dbc9
```

## Verification

Canonical validator output:

```text
SEO validation passed: 232 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
```

All 14 registered project validators separately reported `OK` for their
multilingual copy, media, schema, cache-bust, redirect and integration checks.
`node --check`, Python compilation and `git diff --check` also passed.

The documented Full Safe Rebuild was run on a clean clone of implementation
commit `6c24e8ef`. It regenerated the entire site and all four pricing PDFs,
passed the four validator groups and left `git status --short` empty.

## Diff Scope

The implementation commit contains 27 files:

- four new localized article HTML files;
- four existing Blog hubs;
- four existing localized tubeless-conversion articles;
- `scripts/build/blog_data.py`;
- the new approved Markdown source and the four-language sister source;
- the source hero and nine optimized image variants;
- generated `sitemap.xml` and `llms.txt`.

No tyre-service page, pricing page, PDF, project/news page, common CSS,
JavaScript or cache-bust value changed.

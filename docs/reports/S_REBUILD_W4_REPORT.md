# S-REBUILD-W4 Delivery Report

Date: 2026-09-07 (Europe/Lisbon)

Baseline commit: `87bbe1df47b318ca1ceaf1da7d5a5ebf24c9fb27`

Routing implementation commit: `e72c6827c646b0ec21d864e2f88b14484233e1fb`

Documentation commit: `8db59642d0d6e37101de62e0f310164696726200`

Rich Results schema closure commit: `34c3cf9449388958a37c180c538439815a61448f`

## Approved Source And Delivered Routing

`scripts/build/content/w4_routing_copy_4lang.md` is byte-identical to the
owner delivery and has SHA-256
`0fe5adbd58e585c1292768cd93bb39de9a4e494e04381a29f347aaee8e079438`.
`w4_shared_data.py` pins this value and parses only approved Parts A-D. Parts
E-G remain external to the repository and were not implemented.

The four homepage service cards now use four distinct intent anchors in each
language. The tyre, pre-purchase and Pricing CTAs use their approved specific
anchors, and only the year in `pricing.sub` moved from 2025 to 2026. The
existing `services.learn` values remain for News. Normalized DOM comparison
against the baseline, after replacing the eight approved homepage text nodes,
found no other homepage change. All four production home pages were also
checked against the generated visible text and internal-link sequence.

Wave 3's 17-target description registry and Wave 4's two additions now form a
single checked 19-target registry. `/projects/` and `/contact/` have localized
titles and descriptions and can be consumed by every shared related-card
renderer.

Every registered Blog post has exactly three mapped related-service targets.
The renderer places the localized section immediately after FAQ and before the
article CTA. The three previously orphaned literal posts have the approved
sentence as the final paragraph of their localized workshop-check section,
including the exact same-language link and approved price wording. The mapping
guard was break-tested by temporarily removing
`front-fork-service-motorcycle-cascais`; `build_blog.py` failed before writing
output with:

```text
ValueError: Wave 4 blog mapping must cover every BLOG_POSTS entry exactly once; missing=['front-fork-service-motorcycle-cascais'], extra=[]
```

The temporary mutation was removed and the passing source restored. For the
five Markdown-backed posts, `modifiedISO` is set by the common Wave 4 post-load
step after the loaders have populated `BLOG_POSTS`; this prevents the loader
defaults from overwriting the approved change date. All 36 rendered Blog
articles expose `Article.dateModified` as
`2026-09-07T10:00:00+01:00`.

The 10 legacy projects keep their frozen `main_html`. The common project
renderer replaces only the four generic `/projects/`, `/custom/`,
`/community/` and `/contact/` descriptions with the localized registry value.
Only the 40 maintained `visible_text_sha256` pins changed inside the frozen
JSON; comparison after removing those fields found zero other JSON changes.
All 14 project-family validators pass.

## Moved URLs And Honest Dates

The sitemap retains 236 URLs and the same membership. Exactly 80 entries moved
to `2026-09-07T10:00:00+01:00`:

- Home: `/`, `/pt/`, `/ru/`, `/uk/`.
- Blog: each language variant (`/`, `/pt/`, `/ru/`, `/uk/`) of
  `front-fork-service-motorcycle-cascais`,
  `motorcycle-brake-pad-replacement-cascais`,
  `revtech-110-oil-service-engine-gearbox-drive`,
  `harley-davidson-full-service-done-right`,
  `motorcycle-tyre-fitting-specialist-cascais`,
  `royal-enfield-bear-650-fork-oil-case-study`,
  `royal-enfield-bear-650-scrambler-build`,
  `tubeless-conversion-spoked-wheels` and
  `tubeless-sealing-tape-failure` — 36 URLs.
- Projects: each language variant of `inspirium`, `beckman`, `unbreakable`,
  `quanta-r`, `burly`, `sturmvogel`, `geometric`, `joker`, `hellboy` and
  `true-religion` — 40 URLs.

No Blog hub, News page, commercial/brand page or Markdown-backed project date
moved. Baseline sitemap SHA-256 was
`d8a1e6f48f55c699123fe4286f381f3326c6f6b604897457690e72299d5ad2e6`;
the deployed Wave 4 sitemap SHA-256 is
`d307cbc83053f44b22875d42362796d91d85c8a582fc9467c462574bf6c8d406`.
An independent sitemap comparison confirmed the exact 4 + 36 + 40 delta.

## Browser, Schema And Production Verification

Local and production browser checks covered the requested Portuguese legacy
article and the English Markdown-backed tape article at 390 x 844 and
1440 x 900. Both pages had one related section with three cards, immediately
after FAQ and before `.blog-cta-box`. At 390 pixels the three cards were a
single 340-pixel column; at 1440 pixels they were three approximately
225.6-pixel columns. `documentElement.scrollWidth` never exceeded the viewport.

The first live Rich Results run exposed an existing optional warning on the
legacy article: its author/publisher referenced `#business`, but that article
did not contain the resolving entity. The Blog post-load contract was therefore
closed for all nine posts: author and publisher use the canonical business ID,
and every generated article contains exactly one complete `LocalBusiness` node
with that ID. This is markup inside the already changed 36-page Blog scope and
does not alter visible copy or the 80-URL date boundary. The focused validator
now protects the resolution.

Final Google Rich Results Test runs are clean:

- PT legacy article: result
  [`ytzdF9NkdYzEEnOGOeDxzg`](https://search.google.com/test/rich-results/result?id=ytzdF9NkdYzEEnOGOeDxzg),
  five valid items and no warnings/errors: Article, Breadcrumb, Local business,
  Organization and Video.
- EN Markdown article: result
  [`12zZKdQMzlR8nJzSpDmEIg`](https://search.google.com/test/rich-results/result?id=12zZKdQMzlR8nJzSpDmEIg),
  the same five valid item families and no warnings/errors.

GitHub Pages workflow
[`34156212818`](https://github.com/PhilipGrishin/iron-moto-cascais/actions/runs/34156212818)
deployed `34c3cf9449388958a37c180c538439815a61448f` successfully. A final
cache-bypass crawl returned HTTP 200 for all 80 changed production URLs and
matched each page's visible `<main>` text and internal-link sequence to the
repository after normalizing Cloudflare's email protection. All 36 Blog URLs
also contained exactly one resolving `LocalBusiness` node. Production
`sitemap.xml` and `assets/main.js` are byte-identical to the repository, with
SHA-256 values
`d307cbc83053f44b22875d42362796d91d85c8a582fc9467c462574bf6c8d406`
and `94d69017a947e067cc143971fda5dd8c6285fb8fa34a9110fd004f23d5fd62c4`.
`llms.txt` membership is unchanged and its SHA-256 remains
`590d13f8acb21c4505deb0c358bc66b80c9bb99aa0ec79a8a13501979ca0b`.

## Rebuild, Validators And Diff Scope

A fresh clone from
`https://github.com/PhilipGrishin/iron-moto-cascais.git` at
`34c3cf9449388958a37c180c538439815a61448f` completed the documented Full
Safe Rebuild, including the pricing-PDF step. It passed `validate_seo`, all
seven brand sets, all 12 Harley Hub pages, all 16 commercial hubs and 52 trust
strips, the Wave 4 validator, and every one of the 14 project validators. The
resulting `git status --short` was empty. The sitemap-wide SEO gate also
confirmed zero broken internal links, complete canonical/hreflang clusters and
localized chrome parity.

Before this report, the cumulative baseline-to-schema-closure diff contained
264 files: all 240
tracked common-runtime HTML pages received the required `20260907b` cache key,
and 24 source/data/documentation files changed. Semantic HTML comparison
classifies exactly 80 pages as visible-content changes (4 home, 36 Blog,
40 legacy projects); the other 160 HTML files changed only by cache-bust or
generator serialization. The 28 Blog pages that previously lacked the
resolving business node also received the schema-only closure within that
36-page group. This report is the only additional path, making the final
cumulative path count 265.

No common CSS, media, forms, FormSubmit configuration, Workers, secrets, News
copy, Pricing data/PDFs, sitemap membership or external GBP assets changed.
There are no unverified in-repository acceptance items. Parts E-G of the owner
input remain deliberately outside the repository as required by the brief.

Rollback is the normal Git revert of the three Wave 4 implementation commits.
No external account, Worker, secret or infrastructure state was changed.

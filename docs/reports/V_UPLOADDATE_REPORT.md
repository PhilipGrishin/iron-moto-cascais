# V-UPLOADDATE Delivery Report

Date: 2026-08-14 (Europe/Lisbon)  
Status: **confirmed**  
Implementation commit: `39e44293`  
GitHub Pages workflow: `31781405314` (`success`)

## Requested Fix

The following three Blog articles previously emitted a `VideoObject` without
the required `uploadDate` in each of their four language variants:

- `/blog/revtech-110-oil-service-engine-gearbox-drive/`;
- `/blog/motorcycle-brake-pad-replacement-cascais/`;
- `/blog/front-fork-service-motorcycle-cascais/`.

The shared Blog data now declares these exact values:

| Article | `uploadDate` |
|---|---|
| RevTech 110 oil service | `2026-06-17T10:00:00+01:00` |
| Motorcycle brake pad replacement | `2026-06-17T10:00:00+01:00` |
| Front fork service | `2026-06-18T10:00:00+01:00` |

`build_blog.py` places the declared `youtubeUploadDate` in the generated
`VideoObject`. No generated HTML was edited manually.

## Regression Assertion

`validate_seo.py` now traverses every JSON-LD structure on every sitemap page
and requires a non-empty `uploadDate` on every `VideoObject`.

Before rebuilding the articles, the new assertion produced the intended red
result:

```text
SEO validation failed: 12 issue(s)
  - https://ironcustommotors.com/blog/revtech-110-oil-service-engine-gearbox-drive/: VideoObject 'Watch the RevTech 110 oil service' is missing required uploadDate
  - https://ironcustommotors.com/ru/blog/revtech-110-oil-service-engine-gearbox-drive/: VideoObject 'Смотрите масляный сервис RevTech 110' is missing required uploadDate
  - https://ironcustommotors.com/uk/blog/revtech-110-oil-service-engine-gearbox-drive/: VideoObject 'Дивіться сервіс оливи RevTech 110' is missing required uploadDate
  - https://ironcustommotors.com/pt/blog/revtech-110-oil-service-engine-gearbox-drive/: VideoObject 'Veja o serviço de óleo RevTech 110' is missing required uploadDate
  - https://ironcustommotors.com/blog/motorcycle-brake-pad-replacement-cascais/: VideoObject 'Watch the brake pad replacement' is missing required uploadDate
  - https://ironcustommotors.com/ru/blog/motorcycle-brake-pad-replacement-cascais/: VideoObject 'Смотрите замену тормозных колодок' is missing required uploadDate
  - https://ironcustommotors.com/uk/blog/motorcycle-brake-pad-replacement-cascais/: VideoObject 'Дивіться заміну гальмівних колодок' is missing required uploadDate
  - https://ironcustommotors.com/pt/blog/motorcycle-brake-pad-replacement-cascais/: VideoObject 'Veja a substituição das pastilhas de travão' is missing required uploadDate
  - https://ironcustommotors.com/blog/front-fork-service-motorcycle-cascais/: VideoObject 'Watch the front fork service' is missing required uploadDate
  - https://ironcustommotors.com/ru/blog/front-fork-service-motorcycle-cascais/: VideoObject 'Смотрите обслуживание передней вилки' is missing required uploadDate
  - https://ironcustommotors.com/uk/blog/front-fork-service-motorcycle-cascais/: VideoObject 'Дивіться обслуговування передньої вилки' is missing required uploadDate
  - https://ironcustommotors.com/pt/blog/front-fork-service-motorcycle-cascais/: VideoObject 'Veja o serviço da forquilha dianteira' is missing required uploadDate
exit_code=1
```

After the canonical Blog Workflow:

```text
SEO validation passed: 228 sitemap URL(s)
```

## Schema And Content Comparison

A structural before/after comparison parsed every affected JSON-LD block and
confirmed:

```text
Changed HTML files: 12
HTML scope exact: True
Affected schemas: 12/12 exact uploadDate additions only
Visible text: 12/12 byte-normalized render matches HEAD
VideoObject total: 40; missing uploadDate: 0
```

The 28 previously valid `VideoObject` entities live in HTML files that are
byte-identical to the parent commit. Each of the 12 changed entities is
identical to its previous form after removing the newly added `uploadDate`.

## Sitemap Discipline

The markup-only change did not move any `lastmod` value. The sitemap remained
byte-identical before and after the Blog Workflow:

```text
before  4ff1085cda49c0a631899e876f82ee4b81c93eb83ca4b8e9b8c9f2500a16e427
after   4ff1085cda49c0a631899e876f82ee4b81c93eb83ca4b8e9b8c9f2500a16e427
```

## Repository Validators

```text
SEO validation passed: 228 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
OK: all 14 registered project slugs passed multilingual copy, media, schema, cache-bust, redirect and integration checks
```

JavaScript syntax checks, Python compile checks and `git diff --check` also
passed.

## Reproducibility

The documented Full Safe Rebuild was run in a separate clean clone of
`39e44293`. It regenerated all maintained page families and pricing PDFs, ran
all four validator groups, and finished with:

```text
clean-clone status: clean
```

## Production Verification

GitHub Pages workflow `31781405314` completed successfully. Cache-bypass
requests using `?cb=39e44293` returned HTTP 200 for all 12 affected URLs. A
schema parser confirmed the expected timestamp on each page:

```text
revtech-110-oil-service-engine-gearbox-drive: 4/4 = 2026-06-17T10:00:00+01:00
motorcycle-brake-pad-replacement-cascais:     4/4 = 2026-06-17T10:00:00+01:00
front-fork-service-motorcycle-cascais:        4/4 = 2026-06-18T10:00:00+01:00
Schema parsing result: 0 VideoObject uploadDate errors across 12 production pages
```

The production sitemap also returned HTTP 200 and matched the repository
SHA-256 exactly. Local schema parsing is the accepted Rich Results check for
this task; the missing-field error is absent.

## Final Scope

Implementation output:

- `scripts/build/blog_data.py`;
- `scripts/build/validate_seo.py`;
- exactly 12 affected Blog `index.html` files.

Required durable documentation:

- `docs/PROJECT_STATE.md`;
- `docs/CONTENT_TYPES.md`;
- `docs/CODEX_CHANGELOG.md`;
- `docs/reports/V_UPLOADDATE_REPORT.md`.

No other HTML, CSS, JavaScript, media, cache-bust value, `llms.txt` or
`sitemap.xml` changed.

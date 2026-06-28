# Task Brief Template

Use this short template for large site tasks. It keeps chat context small while
still giving the developer or Codex enough structure to execute end-to-end.

Do not paste long 4-language copy into chat when it already exists as an
attached file. Reference the file path and let the agent read it locally.

## Template

```md
Task:
Type:
Source copy file:
Hero/media files:
Languages:
URLs:

Must update:
- source data:
- generator:
- nav/footer:
- sitemap:
- localized links:
- schema:
- reverse links:
- docs:

Do not change:
-

Verification:
- local build:
- validators:
- deploy:
- production URLs:
- external/manual checks:
```

## Example: New Brand Page

```md
Task: Add Yamaha service page
Type: brand service page
Source copy file: /Users/philipgrishin/Desktop/2026-07-01_yamaha-page_4lang.md
Hero/media files: /Users/philipgrishin/Desktop/Yamaha_Hero.jpg
Languages: EN, PT, RU, UK
URLs:
- /yamaha-service/
- /pt/yamaha-service/
- /ru/yamaha-service/
- /uk/yamaha-service/

Must update:
- source data: scripts/build/brand_pages_data.py
- generator: existing build_brand_pages.py only
- nav/footer: Brands dropdown and footer via shared registry
- sitemap: all 4 URLs
- localized links: same-language links
- schema: Service + FAQPage + BreadcrumbList
- reverse links: other brand pages
- docs: CODEX_CHANGELOG after implementation

Do not change:
- existing page structure outside shared brand blocks
- approved facts, prices, model names or contacts

Verification:
- local build: brand pipeline from docs/CONTENT_TYPES.md
- validators: validate_seo.py and validate_brand_pages.py yamaha-service
- deploy: GitHub Pages success
- production URLs: all 4 return 200 and contain correct H1/schema
- external/manual checks: mention if Google Rich Results UI was not run
```

## Example: Existing Copy Refresh

```md
Task: Refresh BMW text
Type: existing brand copy update
Source copy file: /Users/philipgrishin/Desktop/2026-07-01_bmw-refresh_4lang.md
Hero/media files: none, unless attached
Languages: EN, PT, RU, UK
URLs:
- /bmw-service/
- /pt/bmw-service/
- /ru/bmw-service/
- /uk/bmw-service/

Must update:
- source data: scripts/build/brand_pages_data.py
- schema: FAQPage text only if FAQ visible text changes
- docs: CODEX_CHANGELOG after implementation

Do not change:
- headings, section order, CTA, schema types or navigation
- prices, model names, technical terms unless the file explicitly says so

Verification:
- local build and brand validation
- deploy and production checks for all 4 URLs
```


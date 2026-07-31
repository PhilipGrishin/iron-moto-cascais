# C7-FIX2 Report: Blog Picture Hero Preload Alignment

Date: 2026-07-31

## Scope Correction

- Status: **confirmed** by source inspection and enumeration of tracked output.
- The task brief expected 28 Blog article variants and 12 News article variants
  to use `<picture>` heroes.
- The repository contains 28 Blog article variants with
  `.blog-article picture.hero-media` and zero responsive CSS-background markers.
- The repository contains zero News article `<picture>` heroes and 12 News
  article variants with `data-lcp-responsive-background`.
- The News family was already aligned by C7-FIX and was deliberately left
  unchanged. Converting or editing those CSS heroes would have violated the
  task's explicit protection for the closed C7-FIX scope.

## Before Evidence

The durable C7 measurement used Chromium at 390 x 844 CSS pixels, DPR 3,
1.6 Mbps / 170 ms latency and CPU throttling 4x. On
`/blog/front-fork-service-motorcycle-cascais/` it recorded:

| Resource | Encoded bytes | Role |
| --- | ---: | --- |
| `blog-blog-front-fork-service-motorcycle-cascais-01-768.avif` | 26,494 | viewport-media preload |
| `blog-blog-front-fork-service-motorcycle-cascais-01-1280.avif` | 50,467 | rendered `<picture>` candidate |

Both resources transferred although only the 1280px candidate was painted.
The historical post-C7-FIX LCP median was 1,388 ms from three runs under that
profile.

A fresh pre-change browser check on the current repository also observed the
768px preload and 1280px painted candidate together on the same Blog article.
The corresponding News article check observed one 768px CSS hero resource.

## Implementation

- `hero_images.py` owns a single responsive AVIF picture-preload renderer.
- `build_blog.py` uses that renderer only for Blog articles. Its preload
  `imagesrcset` and `imagesizes` are byte-identical to the first AVIF
  `<source>` in `picture.hero-media`.
- The preload does not duplicate `fetchpriority="high"`; the hero `<img>` is
  the only high-priority element and is not lazy.
- `validate_seo.py --check-picture-hero-preloads` protects all 28 variants and
  resolves both preload and rendered candidates for the required viewport/DPR
  matrix.
- Shared output helpers now treat hreflang/locale metadata ordering as
  semantically neutral and restore tracked canonical HTML bytes after the
  final SEO stage when the DOM is unchanged. This prevents a full rebuild from
  retaining parser-only serialization drift on unrelated pages.

## Candidate Matrix

The maintained `100vw` source size and 768w/1280w/1920w candidate set resolve
as follows. Because the preload and AVIF source use the same selection inputs,
they resolve to the same URL in every checked case.

| Viewport / DPR | Required source width | Selected candidate |
| --- | ---: | --- |
| 390px / DPR 3 | 1,170px | 1280w |
| 390px / DPR 2 | 780px | 1280w |
| 768px / DPR 2 | 1,536px | 1920w |
| 1280px / DPR 1 | 1,280px | 1280w |
| 1440px / DPR 1 | 1,440px | 1920w |

## Immutable Scope

- Changed served HTML: exactly 28 Blog article variants.
- Changed News HTML: zero.
- Changed project HTML: zero.
- Changed other tracked HTML: zero.
- `assets/main.css`: unchanged.
- `assets/main.js`: unchanged.
- Main cache-bust: unchanged at `20260724a`.
- `sitemap.xml` SHA-256 before and after:
  `4910de2803fdd535c37198cf27ed541c23e66be8bd53afe80466881261e54971`.
- All 212 `<lastmod>` tags are therefore byte-identical.

## Measurement Boundary

The available in-app browser can inspect local resources and rendered
`currentSrc`, but it does not expose the required DPR 3, network throttling or
CPU throttling controls. It also retains a 10px panel scrollbar in its narrow
viewport, so it is not the same laboratory profile as the historical
Playwright run. The exact throttled three-run after-LCP median is therefore
**not measured in this environment** and must not be invented. Structural
selection is protected by the validator; production delivery is checked after
deployment with a unique query string.

The expected transfer result under the documented 390px/DPR3 profile is one
50,467-byte 1280px AVIF instead of 26,494 + 50,467 bytes, a reduction of 26,494
encoded bytes. This is an algorithmic expectation from identical selection
inputs, not a substitute for a new throttled LCP measurement.

## Production Verification

GitHub Pages workflow `30662725617` deployed head `1431208a` successfully.
Cache-bypass requests with a unique query string confirmed:

- one Blog responsive preload whose `imagesrcset`/`imagesizes` exactly match
  the AVIF `<source>`;
- one Blog `fetchpriority="high"` element and zero high-priority lazy images;
- one observed 768px Blog hero resource at the available 390px/DPR1 browser
  profile;
- zero News `<picture>` heroes, one News CSS hero marker and one observed
  768px News hero resource at the same available profile;
- production `sitemap.xml` SHA-256
  `4910de2803fdd535c37198cf27ed541c23e66be8bd53afe80466881261e54971`.

The unchanged News C7 CSS contract contains three mutually exclusive
media-qualified preload links marked high priority. This does not create a
second transferred hero in the observed profile, but it means the brief's
literal “no more than one high-priority element per News page” condition is
incompatible with its instruction not to modify CSS-background heroes. No
News change is claimed.

## Verification

Implementation commit: `c177b67a`.

The complete Full Safe Rebuild from `scripts/build/README.md` was run in a
clean clone of that commit with `PYTHONDONTWRITEBYTECODE=1`. It ended with an
empty `git status --short` and the unchanged sitemap SHA-256
`4910de2803fdd535c37198cf27ed541c23e66be8bd53afe80466881261e54971`.

The four canonical validators returned:

```text
SEO validation passed: 212 sitemap URL(s)
Brand page validation passed: 7 brand page set(s).
Harley Hub validation passed: 12 pages and all required integrations
OK: fighter project page passed multilingual, media, schema and integration checks
```

The exact DPR3 network replay and throttled after-LCP median remain unmeasured
for the environment reason stated above; the task handoff must preserve that
boundary.

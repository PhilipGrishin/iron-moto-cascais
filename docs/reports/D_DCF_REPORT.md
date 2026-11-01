# D-DCF delivery record

Date: 2026-11-01. Status: deployed and production-verified.

## Intake and decisions

- Confirmed baseline: `457093b32cf4f5932ba5ed4ee0091045b7b33834`;
  local main and origin/main match and the worktree was clean.
- The task and pasted prompt differ only by a final newline. Approved page
  and integration source checksums match the requested values.
- Initial missing-hero dependency was resolved by the owner supplying
  `dcf_HERO.jpg` explicitly from their separate strategy workspace. Access is
  limited to this supplied file; no other project is inspected or copied.
- Use the supplied photo unchanged apart from orientation normalization,
  responsive resizing/encoding and metadata removal. Its printed equipment
  marks remain in the owner-approved photograph; no equipment-brand name is
  added to public copy, ALT text or filenames.
- Implement a checksum-checked labelled Markdown parser and a generic partner
  rendering path inside the existing Authorized Dealer generator. Reuse the
  C-Way styles; preserve its body, schema, prices and media.
- Add the approved second hub card, shared desktop/mobile dealer submenu,
  four Upgrades item-7 links, registry target and hub intro/metadata. Shared
  navigation/cache changes do not advance unrelated content dates.
- Main JavaScript changes only add the four menu labels. Advance its shared
  cache stamp, preserve forms, Workers, reviews, prices and page bodies outside
  the eight approved integration URLs.
- Verify source parity, checksum rejection, schema, local destinations,
  responsive hero requests/browser behavior, scope/date accounting, all release
  gates and a clean-clone Full Safe Rebuild; push and check production plus
  the requested PT Google Rich Results Test.
- Research dossier remains an input/reference, not public copy: its private
  GSC figures are not copied into the repository.

## Implementation identity

- Implementation/artifact commit: `5d01bd438090d39a01c66d35b120a3ccc893022a`.
- Actual first parent: `457093b32cf4f5932ba5ed4ee0091045b7b33834`, matching
  the requested baseline. Origin was fetched again before publication.
- Fresh full-history `--no-hardlinks` clone of the exact implementation commit:
  documented Full Safe Rebuild completed with exit 0 and empty Git status.
  All PDF outputs and validator families were included. The generated sitemap
  remained byte-identical. Evidence: [clean rebuild](D_DCF_REBUILD.json).

## Implementation and local acceptance

- Parsed, not transcribed: `dealer_copy.py` enforces SHA-256 before reading the
  labelled four-language contract. `COPY_DEALER_PAGES` registers the source,
  media and service schema; `build_authorized_dealer.py` owns both partner
  render paths and shared C-Way styles. No separate page generator was added.
- Page-source SHA-256:
  `3d3bd77bd92a71a3403ef6905025c8f3def1d30f08f1b63ca46098d9862e2aff`.
  The file is byte-identical to the attachment. Integrations were applied
  verbatim from their preserved input. Upgrades source changes exactly four
  lines; its new SHA is in the build README table.
- One-byte mutation of the real source caused the generator to fail at its
  checksum guard before rendering; original bytes were restored in `finally`.
  Evidence: [checksum check](D_DCF_CHECKSUM.json).
- Full Safe Rebuild passed, including all PDF outputs and validator families.
  The dedicated new Authorized Dealer validator is part of the common local/CI
  release gate and the documented Full Safe Rebuild sequence.
- Complete approved copy, 11 sections and all item counts pass in all languages.
  FAQ 6/6 matches JSON-LD; one H1, five hreflang entries, canonical, hero,
  per-language WhatsApp text, one partner outbound link and five internal links
  plus bike links all match. Only the approved diagnostics amount is present.
- [Scope evidence](D_DCF_SCOPE.json): only eight old main-content pages change.
  Existing schema changes only on the four dealer hubs. All existing headers
  and mobile drawers match after removing the new menu entry; footer, forms
  and modals remain unchanged. All 152 previous form pages are preserved.
  Pricing data/PDFs, shared CSS, C-Way media, review inputs and Workers match
  baseline bytes. Runtime JavaScript differs only by four approved nav labels.
- Checked 39,160 local URL/asset references and 592 real fragment destinations:
  no broken targets. Existing modal-action fragments retain their exception.
- [Browser evidence](D_DCF_BROWSER_LOCAL.json): installed Chrome through
  Playwright, PT at 390/DPR2 and 1440/DPR1. Exactly one hero image request at each
  profile; zero horizontal overflow, JavaScript errors or HTTP failures.
  WhatsApp prefill, smooth-scroll process button, FAQ expansion and both dealer
  menus work. Hero captures were visually inspected. Lead events were intercepted;
  no form submitted and no WhatsApp message sent.
- The initial browser assertion expected a URL hash after smooth scrolling;
  existing shared behavior intentionally prevents the default hash update.
  Acceptance now checks the actual target scroll position. Site behavior was
  not changed for the test.

## Exact sitemap accounting

248 existing URLs become 252. The following new URLs use their initial real
content timestamps, recorded by the existing sitemap workflow:

- `https://ironcustommotors.com/authorized-dealer/dcf-performance/`
- `https://ironcustommotors.com/ru/authorized-dealer/dcf-performance/`
- `https://ironcustommotors.com/uk/authorized-dealer/dcf-performance/`
- `https://ironcustommotors.com/pt/authorized-dealer/dcf-performance/`

Dealer hub card, first intro sentence and meta description change:

- `https://ironcustommotors.com/authorized-dealer/`
- `https://ironcustommotors.com/ru/authorized-dealer/`
- `https://ironcustommotors.com/uk/authorized-dealer/`
- `https://ironcustommotors.com/pt/authorized-dealer/`

Upgrades section 01 item 7 gains the approved contextual link:

- `https://ironcustommotors.com/upgrades-tuning/`
- `https://ironcustommotors.com/ru/upgrades-tuning/`
- `https://ironcustommotors.com/uk/upgrades-tuning/`
- `https://ironcustommotors.com/pt/upgrades-tuning/`

The other 240 existing lastmod values are unchanged. Shared menu/cache updates
never advance those dates. Exact timestamps/reasons are in the scope JSON.

## Media weights and import

The owner image is 4284 × 5712; responsive derivatives preserve its portrait
ratio and strip EXIF. `import_dealer_images.py` uses the existing project image
encoder. The original owner file remains outside Git and is unchanged. Source
and all output hashes are in `photos/authorized-dealer/dcf-performance-media.json`.

| Width | AVIF bytes | WebP bytes | JPEG bytes |
|---:|---:|---:|---:|
| 768 | 142,659 | 178,170 | 222,942 |
| 1280 | 403,554 | 501,692 | 614,776 |
| 1536 | 582,274 | 725,550 | 882,458 |

Nine files total 4,254,075 bytes; each browser profile requests one AVIF, not
all formats/sizes. The hub uses the 768 variant with explicit dimensions.

## Implementation differences and limits

- `assets/main.js` owns global translations; `extract_i18n.js` writes JSON,
  correcting the attachment's reversed arrow without changing approved labels.
- The deployment workflow already copies `authorized-dealer` recursively and
  each language root. No redundant per-child deploy-list entry is needed.
- The hub participates in generic i18n: the new card therefore uses a
  registry-derived description key. C-Way's existing card and page content stay
  unchanged. Utility headers receive only the partner-menu refresh, not a full
  shell replacement.
- Four approved WhatsApp-field lines end in a space. The narrowly scoped
  `.gitattributes` exception preserves the required source hash while keeping
  `git diff --check` meaningful for all other files.
- The public DCF dealer page was fetched on 2026-11-01: it names Iron Custom
  Motors and links to `https://ironcustommotors.com`. The official dealer index
  lists ICM under Portugal. Sources:
  [dealer profile](https://dcf-performance.com/dealers/iron-custom-motors),
  [dealer list](https://dcf-performance.com/dealers).
- Territorial exclusivity is not claimed. Existing dyno-availability work
  stays deferred; the approved page attributes dyno testing to DCF.
- Google no longer supports FAQ rich results; visible FAQ/schema parity is
  verified directly. The supported-item test passed as recorded below.

## Deployment and public acceptance

- Confirmed: [Pages run 41347446338](https://github.com/PhilipGrishin/iron-moto-cascais/actions/runs/41347446338)
  validated and published exact commit `5d01bd438090d39a01c66d35b120a3ccc893022a`;
  conclusion `success`, completed 2026-11-01T20:35:43Z.
- [Production comparison](D_DCF_PRODUCTION.json): 252 sitemap URLs plus four
  utility URLs returned successfully and matched local normalized main text,
  JSON-LD, title/description, canonical/hreflang, image references, asset cache
  keys and both DCF menu links. Cloudflare email obfuscation was normalized.
- All 22 checked files match local bytes: sitemap, llms, robots, four shared
  CSS/JS files, review snapshot, four PDFs and ten DCF media/manifest files.
  Sitemap SHA-256:
  `29547baa58527e788b80f3a0c68c1c1e66e6a73b47dc0aa2018bcddb1503fcf5`.
- [Live browser checks](D_DCF_BROWSER_PRODUCTION.json): PT 390/DPR2 and
  1440/DPR1 each request one AVIF hero; no overflow, JavaScript errors or HTTP
  failures. WhatsApp prefill, process scrolling, FAQ and respective mobile/
  desktop menu passed. Both live hero screenshots were visually inspected.
- [PT Google Rich Results Test](https://search.google.com/test/rich-results/result?id=zoA5ZcFluy9R9idHHXCt3Q)
  found three valid items (Breadcrumb, Local business, Organization), no errors
  and no displayed warnings. [Machine-readable record](D_DCF_RICH_RESULTS.json).
- Existing GitHub action-runtime/runner migration notices remain non-blocking
  and tracked in `docs/OPEN_TASKS.md`; this task did not alter CI configuration.
- No remaining D-DCF implementation dependency. Search-engine recrawl timing
  is external to deployment. The documentation-only closeout commit preserves
  the verified public artifact; its identity is available in Git history.

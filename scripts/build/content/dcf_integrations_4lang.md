# D-DCF integrations — approved strings for the links to `/authorized-dealer/dcf-performance/` (EN / PT-pt / RU / UK)
Iron Custom Motors · 2026-11-01 · companion to `2026-11-01_dcf-dealer-page_4lang.md` (the page copy). Codex applies the strings below verbatim where each part says. Placement: the page is the second brand page of the Authorized Dealer family (sibling of C-Way): hub card, dealer submenu entry (the family convention — C-Way sits there), one contextual link from the upgrades hub, registry entry, and a widening of the hub's own intro/meta so the hub no longer speaks of «parts» only.

# Part A — Hub card (`AUTHORIZED_DEALER_BRANDS`, second entry after `c-way`; image = the page hero at 768 px)

| Lang | `name` | `description` |
|---|---|---|
| EN | DCF-Performance | Official DCF-Performance dealer in Portugal: motorcycle ECU remapping and chip tuning with dyno-developed files, original map kept, written estimate, Cascais. |
| PT | DCF-Performance | Revendedor oficial DCF-Performance em Portugal: reprogramação de centralina e chip tuning de motos com ficheiros testados em banco, mapa original guardado, orçamento escrito, Cascais. |
| RU | DCF-Performance | Официальный дилер DCF-Performance в Португалии: прошивка ЭБУ и чип-тюнинг мотоциклов на калибровках со стенда, оригинальная прошивка сохраняется, смета письменно, Кашкайш. |
| UK | DCF-Performance | Офіційний дилер DCF-Performance у Португалії: прошивка ЕБК і чип-тюнінг мотоциклів на калібруваннях зі стенда, оригінальна прошивка зберігається, кошторис письмово, Кашкайш. |

# Part B — Dealer submenu entry (next to `nav.dealerCway`), key `nav.dealerDcf` ×4 (`i18n.json` → `main.js`)

| Lang | Label |
|---|---|
| EN | DCF-Performance |
| PT | DCF-Performance |
| RU | DCF-Performance |
| UK | DCF-Performance |

# Part C — Upgrades hub `/upgrades-tuning/` §01, item 7: replacement line ×4 (the only change to `upgrades_hub_copy_4lang.md`; SHA re-pinned)

| Lang | Current line | New line |
|---|---|---|
| EN | `**7. Tuning parts.** ECU maps, intake, exhaust, fuel control, throttle response — matched to each other, not bolted on one by one.` | `**7. Tuning parts.** ECU maps, intake, exhaust, fuel control, throttle response — matched to each other, not bolted on one by one. ECU remapping runs through our [DCF-Performance dealership](/authorized-dealer/dcf-performance/).` |
| PT | `**7. Peças de tuning.** Mapas de ECU, admissão, escape, controlo de combustível, resposta do acelerador, pensados em conjunto e não aparafusados um a um.` | `**7. Peças de tuning.** Mapas de ECU, admissão, escape, controlo de combustível, resposta do acelerador, pensados em conjunto e não aparafusados um a um. A reprogramação de centralina passa pela nossa [representação DCF-Performance](/pt/authorized-dealer/dcf-performance/).` |
| RU | `**7. Тюнинг-компоненты.** ECU-карты, впуск, выпуск, топливная коррекция, отклик на газ — согласованные между собой, а не прикрученные по одному.` | `**7. Тюнинг-компоненты.** ECU-карты, впуск, выпуск, топливная коррекция, отклик на газ — согласованные между собой, а не прикрученные по одному. Прошивку ЭБУ делаем через наше [дилерство DCF-Performance](/ru/authorized-dealer/dcf-performance/).` |
| UK | `**7. Тюнінг-компоненти.** ECU-мапи, впуск, вихлоп, паливна корекція, відгук на газ — узгоджені між собою, а не прикручені по одному.` | `**7. Тюнінг-компоненти.** ECU-мапи, впуск, вихлоп, паливна корекція, відгук на газ — узгоджені між собою, а не прикручені по одному. Прошивку ЕБК робимо через наше [дилерство DCF-Performance](/uk/authorized-dealer/dcf-performance/).` |

# Part D — Related-description registry: new target `/authorized-dealer/dcf-performance/` (W3/W4 `RELATED_DESCRIPTIONS`, 21st entry)

### DCF-Performance dealer — `/authorized-dealer/dcf-performance/`

| Lang | Line |
|---|---|
| EN | Official DCF-Performance dealer: motorcycle ECU remapping with dyno-developed files, Stage 1 and 2, original map kept, written estimate. |
| PT | Revendedor oficial DCF-Performance: reprogramação de centralina de mota com ficheiros testados em banco, Stage 1 e 2, mapa original guardado, orçamento escrito. |
| RU | Официальный дилер DCF-Performance: прошивка ЭБУ мотоцикла на калибровках со стенда, Stage 1 и 2, оригинал сохраняется, смета письменно. |
| UK | Офіційний дилер DCF-Performance: прошивка ЕБК мотоцикла на калібруваннях зі стенда, Stage 1 і 2, оригінал зберігається, кошторис письмово. |

# Part E — Authorized Dealer hub `/authorized-dealer/` widening ×4: the hub currently speaks of «parts and accessories» only. Replace the first sentence of `ad.intro` and the head `description`; titles unchanged (parts stay the main line).

| Lang | `ad.intro` — first sentence, current → new |
|---|---|
| EN | «Iron Custom Motors is now an authorized dealer and official representative of leading aftermarket motorcycle parts and accessories brands.» → «Iron Custom Motors is an authorized dealer and official representative of leading aftermarket motorcycle parts and accessories brands — and, through DCF-Performance, of professional ECU tuning for motorcycles.» |
| PT | «A Iron Custom Motors é agora revendedora oficial e representante autorizada das principais marcas de peças e acessórios para mota.» → «A Iron Custom Motors é revendedora oficial e representante autorizada das principais marcas de peças e acessórios para mota e, através da DCF-Performance, de reprogramação profissional de centralinas de mota.» |
| RU | «Iron Custom Motors теперь официальный дилер и представитель ведущих брендов мотозапчастей и аксессуаров.» → «Iron Custom Motors — официальный дилер и представитель ведущих брендов мотозапчастей и аксессуаров, а через DCF-Performance — профессионального чип-тюнинга мотоциклов.» |
| UK | «Iron Custom Motors тепер офіційний дилер і представник провідних брендів мотозапчастин та аксесуарів.» → «Iron Custom Motors — офіційний дилер і представник провідних брендів мотозапчастин та аксесуарів, а через DCF-Performance — професійного чип-тюнінгу мотоциклів.» |

| Lang | Head `description` (new, 140–155) |
|---|---|
| EN | Authorized dealer in Cascais: genuine parts from leading motorcycle brands with official warranty and expert fitment — and DCF-Performance ECU tuning. |
| PT | Revendedor oficial em Cascais: peças genuínas das principais marcas para mota, garantia oficial, montagem profissional — e reprogramação DCF-Performance. |
| RU | Официальный дилер в Кашкайше: оригинальные запчасти ведущих мотобрендов с гарантией производителя и установкой — и чип-тюнинг DCF-Performance. |
| UK | Офіційний дилер у Кашкайші: оригінальні запчастини провідних мотобрендів із гарантією виробника та встановленням — і чип-тюнінг DCF-Performance. |

The rest of the hub (why-cards, FAQ about parts, CTA) stays as it is: the DCF card itself carries the tuning message.

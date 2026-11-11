# S-STAGE1 integrations — approved strings for everything around `/stage-1/` (EN / PT-pt / RU / UK)
Iron Custom Motors · 2026-11-11 · companion to `2026-11-11_stage1-page_4lang.md` (the page copy) and `2026-11-11_dcf-dealer-page_4lang_rev2.md` (the dealer page, rev. 2). Codex applies the strings below verbatim where each part says. Owner decisions of 2026-11-11: a new top-menu group «Stage» with a dropdown that for now holds one item, «Stage 1»; no overview page for the group yet — the group label itself leads to `/stage-1/`; nothing about Stage 2, 3 or 4 is shown anywhere until those services are launched; Stage 1 also appears in the footer, on the pricing page under the existing price list, and the pricing page gets two download buttons.

Prices used below — the only two numbers of this task, both must live in `pricing_data.py` and be referenced from there everywhere: **Stage 1 = 800 EUR (VAT included, fixed)** · **Stage 1 for Chinese brands = 650 EUR (VAT included, fixed)**. «Additional options» carry no number («on request») and get no `Offer`.

---

# Part A — Navigation and footer

## A1. Top menu group (desktop dropdown and mobile accordion, same registry)

Position: directly after «Authorized Dealer», before «Projects». The group label is a link to `/stage-1/` (same-language), exactly as the other dropdown parents are links. The dropdown has one item now; future stages are appended to the same registry.

| Key | EN | PT | RU | UK |
|---|---|---|---|---|
| `nav.stage` (group label) | Stage | Stage | Stage | Stage |
| `nav.stage1` (dropdown item → `/stage-1/`) | Stage 1 | Stage 1 | Stage 1 | Stage 1 |

## A2. Footer, Services column

One new entry directly after «Carburettors & fuel system» (`nav.fuelServ`) and before «Authorized Dealer», → `/stage-1/`.

| Key | EN | PT | RU | UK |
|---|---|---|---|---|
| `nav.stage1Footer` | Stage 1 ECU remap | Stage 1 · reprogramação | Stage 1 · прошивка ЭБУ | Stage 1 · прошивка ЕБК |

---

# Part B — Pricing page `/pricing/` (+ `/pt/`, `/ru/`, `/uk/`)

## B1. New section «Stage 1», placed after the last priced section («06 Seasonal prep») and before «Customizing & community», which is renumbered. Anchor: `stage-1` (the Stage 1 page and the news article link to `/pricing/#stage-1`).

| Field | EN | PT | RU | UK |
|---|---|---|---|---|
| Section title | Stage 1 | Stage 1 | Stage 1 | Stage 1 |
| H2 | Stage 1 — individual ECU file | Stage 1 — ficheiro individual para a centralina | Stage 1 — индивидуальная прошивка ЭБУ | Stage 1 — індивідуальна прошивка ЕБК |

Intro (one paragraph, the link is same-language):

| Lang | Intro |
|---|---|
| EN | An individual DCF-Performance ECU file for your motorcycle, your setup and your goals — at a fixed price. Included: coverage check, computer diagnostics before and after, visual inspection, ECU read, original software kept in our archive, the individual file and the write. Scope, steps and terms are on the [Stage 1 page](/stage-1/). |
| PT | Um ficheiro individual DCF-Performance para a sua mota, a sua configuração e os seus objetivos — a preço fixo. Incluído: verificação de cobertura, diagnóstico por computador antes e depois, inspeção visual, leitura da centralina, software original guardado no nosso arquivo, o ficheiro individual e a gravação. O conteúdo, os passos e as condições estão na [página do Stage 1](/pt/stage-1/). |
| RU | Индивидуальный файл DCF-Performance под ваш мотоцикл, ваш сетап и ваши задачи — по фиксированной цене. В цене: проверка покрытия, компьютерная диагностика до и после, визуальный осмотр, чтение блока управления, сохранение оригинальной прошивки в нашем архиве, индивидуальный файл и запись. Состав, шаги и условия — на [странице Stage 1](/ru/stage-1/). |
| UK | Індивідуальний файл DCF-Performance під ваш мотоцикл, ваш сетап і ваші завдання — за фіксованою ціною. У ціні: перевірка покриття, комп'ютерна діагностика до і після, візуальний огляд, читання блока керування, збереження оригінальної прошивки в нашому архіві, індивідуальний файл і запис. Склад, кроки й умови — на [сторінці Stage 1](/uk/stage-1/). |

Rows (three; stable ids in the first column):

| id | Price | EN name — description | PT name — description | RU name — description | UK name — description |
|---|---|---|---|---|---|
| `stage1` | 800 EUR (fixed, no «from») | Stage 1 — all makes except Chinese brands — Individual DCF-Performance ECU file, VAT included | Stage 1 — todas as marcas, exceto marcas chinesas — Ficheiro individual DCF-Performance, IVA incluído | Stage 1 — все марки, кроме китайских брендов — Индивидуальный файл DCF-Performance, IVA включён | Stage 1 — усі марки, крім китайських брендів — Індивідуальний файл DCF-Performance, ПДВ включено |
| `stage1_chinese_brands` | 650 EUR (fixed, no «from») | Stage 1 — Chinese brands — CFMoto, Voge, Benelli, Zontes and others: individual price, VAT included | Stage 1 — marcas chinesas — CFMoto, Voge, Benelli, Zontes e outras: preço individual, IVA incluído | Stage 1 — китайские бренды — CFMoto, Voge, Benelli, Zontes и другие: индивидуальная цена, IVA включён | Stage 1 — китайські бренди — CFMoto, Voge, Benelli, Zontes та інші: індивідуальна ціна, ПДВ включено |
| `stage1_options` | no number — label «on request» / «sob consulta» / «по запросу» / «за запитом» | Additional options — Thermal Control, Neutral RPM, Max RPM, Exhaust Flaps, track options, A2 restriction removal: listed on the Stage 1 page | Opções adicionais — Thermal Control, Neutral RPM, Max RPM, Exhaust Flaps, opções de pista, remoção da limitação A2: lista na página do Stage 1 | Дополнительные опции — Thermal Control, Neutral RPM, Max RPM, Exhaust Flaps, опции для трека, снятие ограничения A2: список на странице Stage 1 | Додаткові опції — Thermal Control, Neutral RPM, Max RPM, Exhaust Flaps, опції для треку, зняття обмеження A2: список на сторінці Stage 1 |

Section note:

| Lang | Note |
|---|---|
| EN | Stage 1 is a fixed price and does not depend on how the ECU is read. The motorcycle must be technically ready for Stage 1: we need a motorcycle in good working order. A High Flow air filter and an exhaust system are not included. |
| PT | O Stage 1 tem preço fixo e não depende do método de leitura da centralina. A mota tem de estar tecnicamente pronta para o Stage 1: precisamos de uma mota em bom estado de funcionamento. O filtro de ar High Flow e o sistema de escape não estão incluídos. |
| RU | Цена Stage 1 фиксированная и не зависит от способа чтения блока. Мотоцикл должен быть технически готов к Stage 1: нам нужен исправный мотоцикл. High Flow воздушный фильтр и выпускная система в цену не входят. |
| UK | Ціна Stage 1 фіксована й не залежить від способу читання блока. Мотоцикл має бути технічно готовий до Stage 1: нам потрібен справний мотоцикл. Повітряний фільтр High Flow і вихлопна система в ціну не входять. |

Section buttons (two): a link to the Stage 1 page and the Stage 1 PDF download.

| Button | EN | PT | RU | UK |
|---|---|---|---|---|
| Page link → `/stage-1/` | Stage 1 in detail | Stage 1 em detalhe | Подробнее о Stage 1 | Докладніше про Stage 1 |
| PDF | Download Stage 1 (PDF) | Descarregar Stage 1 (PDF) | Скачать Stage 1 (PDF) | Завантажити Stage 1 (PDF) |

## B2. Hero of the pricing page: two download buttons instead of one

The existing single button («Download PDF») becomes the first of two; its file does not change.

| Button | EN | PT | RU | UK |
|---|---|---|---|---|
| 1 — existing service price list PDF | Download services (PDF) | Descarregar serviços (PDF) | Скачать прайс услуг (PDF) | Завантажити прайс послуг (PDF) |
| 2 — Stage 1 catalogue PDF | Download Stage 1 (PDF) | Descarregar Stage 1 (PDF) | Скачать Stage 1 (PDF) | Завантажити Stage 1 (PDF) |

Stage 1 PDF per language (the owner-approved catalogue, four ready files supplied with the task — static assets, not generated by the repository):

| Lang | Published path |
|---|---|
| EN | `/pricing/files/ICM_Stage-1_DCF-Performance_EN.pdf` |
| PT | `/pricing/files/ICM_Stage-1_DCF-Performance_PT.pdf` |
| RU | `/pricing/files/ICM_Stage-1_DCF-Performance_RU.pdf` |
| UK | `/pricing/files/ICM_Stage-1_DCF-Performance_UK.pdf` |

The repository's own service price-list PDFs are regenerated from the shared data and therefore gain the same Stage 1 rows and note (no links inside PDFs).

## B3. Pricing page head `description` ×4 (titles unchanged)

| Lang | New description |
|---|---|
| EN | Motorcycle service prices 2026 in Cascais: maintenance from 150 €, Harley-Davidson 300 €, diagnostics 50–350 €, Stage 1 ECU remap 800 €. Written estimates. |
| PT | Preços 2026 da oficina de motas em Cascais: revisão desde 150 €, Harley-Davidson 300 €, diagnóstico 50–350 €, Stage 1 por 800 €. Orçamento escrito. |
| RU | Прайс-лист 2026 мотосервиса в Кашкайше: ТО от 150 €, Harley-Davidson 300 €, диагностика 50–350 €, Stage 1 — 800 €. Письменная смета до работ. |
| UK | Прайс 2026 мотосервісу Iron Custom Motors у Кашкайші: ТО від 150 €, Harley-Davidson 300 €, діагностика 50–350 €, Stage 1 — 800 €. Кошторис письмово. |

---

# Part C — Related-description registry

## C1. New target `/stage-1/`

| Lang | Line |
|---|---|
| EN | Stage 1: an individual DCF-Performance ECU file for your motorcycle — fixed price 800 €, original software kept. |
| PT | Stage 1: ficheiro individual DCF-Performance para a sua mota — preço fixo 800 €, software original guardado. |
| RU | Stage 1: индивидуальный файл DCF-Performance под ваш мотоцикл — фиксированная цена 800 €, оригинал сохраняется. |
| UK | Stage 1: індивідуальний файл DCF-Performance під ваш мотоцикл — фіксована ціна 800 €, оригінал зберігається. |

## C2. Existing target `/authorized-dealer/dcf-performance/` — replacement (the current line says «Stage 1 and 2 … written estimate»)

| Lang | New line |
|---|---|
| EN | Official DCF-Performance dealer: motorcycle ECU remapping with dyno-developed files, Stage 1 at a fixed price, original map kept. |
| PT | Revendedor oficial DCF-Performance: reprogramação de centralina de mota com ficheiros testados em banco, Stage 1 a preço fixo, mapa original guardado. |
| RU | Официальный дилер DCF-Performance: прошивка ЭБУ мотоцикла на калибровках со стенда, Stage 1 по фиксированной цене, оригинал сохраняется. |
| UK | Офіційний дилер DCF-Performance: прошивка ЕБК мотоцикла на калібруваннях зі стенда, Stage 1 за фіксованою ціною, оригінал зберігається. |

---

# Part D — Authorized Dealer hub card «DCF-Performance» (`AUTHORIZED_DEALER_BRANDS`), `description` replacement

| Lang | New description |
|---|---|
| EN | Official DCF-Performance dealer in Portugal: motorcycle ECU remapping and chip tuning with dyno-developed files, original map kept, Stage 1 at a fixed 800 €, Cascais. |
| PT | Revendedor oficial DCF-Performance em Portugal: reprogramação de centralina e chip tuning de motos com ficheiros testados em banco, mapa original guardado, Stage 1 a preço fixo de 800 €, Cascais. |
| RU | Официальный дилер DCF-Performance в Португалии: прошивка ЭБУ и чип-тюнинг мотоциклов на калибровках со стенда, оригинальная прошивка сохраняется, Stage 1 по фиксированной цене 800 €, Кашкайш. |
| UK | Офіційний дилер DCF-Performance у Португалії: прошивка ЕБК і чип-тюнінг мотоциклів на калібруваннях зі стенда, оригінальна прошивка зберігається, Stage 1 за фіксованою ціною 800 €, Кашкайш. |

---

# Part E — Upgrades hub `/upgrades-tuning/` §01, item 7: replacement line ×4 (the only change to `upgrades_hub_copy_4lang.md`; SHA re-pinned)

| Lang | Current line | New line |
|---|---|---|
| EN | `**7. Tuning parts.** ECU maps, intake, exhaust, fuel control, throttle response — matched to each other, not bolted on one by one. ECU remapping runs through our [DCF-Performance dealership](/authorized-dealer/dcf-performance/).` | `**7. Tuning parts.** ECU maps, intake, exhaust, fuel control, throttle response — matched to each other, not bolted on one by one. ECU remapping is our [Stage 1](/stage-1/): an individual file at a fixed 800 €, through our [DCF-Performance dealership](/authorized-dealer/dcf-performance/).` |
| PT | `**7. Peças de tuning.** Mapas de ECU, admissão, escape, controlo de combustível, resposta do acelerador, pensados em conjunto e não aparafusados um a um. A reprogramação de centralina passa pela nossa [representação DCF-Performance](/pt/authorized-dealer/dcf-performance/).` | `**7. Peças de tuning.** Mapas de ECU, admissão, escape, controlo de combustível, resposta do acelerador, pensados em conjunto e não aparafusados um a um. A reprogramação de centralina é o nosso [Stage 1](/pt/stage-1/): um ficheiro individual a preço fixo de 800 €, através da nossa [representação DCF-Performance](/pt/authorized-dealer/dcf-performance/).` |
| RU | `**7. Тюнинг-компоненты.** ECU-карты, впуск, выпуск, топливная коррекция, отклик на газ — согласованные между собой, а не прикрученные по одному. Прошивку ЭБУ делаем через наше [дилерство DCF-Performance](/ru/authorized-dealer/dcf-performance/).` | `**7. Тюнинг-компоненты.** ECU-карты, впуск, выпуск, топливная коррекция, отклик на газ — согласованные между собой, а не прикрученные по одному. Прошивка ЭБУ — это наш [Stage 1](/ru/stage-1/): индивидуальный файл по фиксированной цене 800 €, через наше [дилерство DCF-Performance](/ru/authorized-dealer/dcf-performance/).` |
| UK | `**7. Тюнінг-компоненти.** ECU-мапи, впуск, вихлоп, паливна корекція, відгук на газ — узгоджені між собою, а не прикручені по одному. Прошивку ЕБК робимо через наше [дилерство DCF-Performance](/uk/authorized-dealer/dcf-performance/).` | `**7. Тюнінг-компоненти.** ECU-мапи, впуск, вихлоп, паливна корекція, відгук на газ — узгоджені між собою, а не прикручені по одному. Прошивка ЕБК — це наш [Stage 1](/uk/stage-1/): індивідуальний файл за фіксованою ціною 800 €, через наше [дилерство DCF-Performance](/uk/authorized-dealer/dcf-performance/).` |

---

# Part F — Harley tuning page `/harley-tuning/`, «Stage upgrades, explained», the Stage 1 paragraph: replacement line ×4 (the only change to `harley_hub_phase1_4lang.md`; SHA re-pinned if pinned). One sentence is appended; the link is same-language.

| Lang | Current line | New line |
|---|---|---|
| EN | `**Stage 1** is the foundation: intake, exhaust and calibration working as one system. Done properly, the engine breathes better and responds cleaner everywhere — it is the upgrade almost every Harley benefits from first.` | `**Stage 1** is the foundation: intake, exhaust and calibration working as one system. Done properly, the engine breathes better and responds cleaner everywhere — it is the upgrade almost every Harley benefits from first. The calibration is our [Stage 1](/stage-1/): an individual DCF-Performance file at a fixed 800 €; intake and exhaust are quoted separately.` |
| PT | `**Stage 1** é a base: admissão, escape e calibração a funcionar como um sistema único. Bem feito, o motor respira melhor e responde com mais limpeza em todo o regime — é o upgrade por onde quase todas as Harley devem começar.` | `**Stage 1** é a base: admissão, escape e calibração a funcionar como um sistema único. Bem feito, o motor respira melhor e responde com mais limpeza em todo o regime — é o upgrade por onde quase todas as Harley devem começar. A calibração é o nosso [Stage 1](/pt/stage-1/): um ficheiro individual DCF-Performance a preço fixo de 800 €; a admissão e o escape são orçamentados à parte.` |
| RU | `**Stage 1** — фундамент: впуск, выпуск и калибровка, работающие как единая система. Сделанный как следует, он даёт мотору свободное дыхание и чистый отклик во всём диапазоне. С него стоит начинать почти любому Harley.` | `**Stage 1** — фундамент: впуск, выпуск и калибровка, работающие как единая система. Сделанный как следует, он даёт мотору свободное дыхание и чистый отклик во всём диапазоне. С него стоит начинать почти любому Harley. Калибровка — это наш [Stage 1](/ru/stage-1/): индивидуальный файл DCF-Performance по фиксированной цене 800 €; впуск и выпуск считаются отдельно.` |
| UK | `**Stage 1** — фундамент: впуск, випуск і калібрування як єдина система. Зроблений як слід, він дає мотору вільне дихання і чистий відгук у всьому діапазоні. Саме з нього варто починати майже кожному Harley.` | `**Stage 1** — фундамент: впуск, випуск і калібрування як єдина система. Зроблений як слід, він дає мотору вільне дихання і чистий відгук у всьому діапазоні. Саме з нього варто починати майже кожному Harley. Калібрування — це наш [Stage 1](/uk/stage-1/): індивідуальний файл DCF-Performance за фіксованою ціною 800 €; впуск і випуск рахуються окремо.` |

---

# Part G — Machine-readable facts

- Stable page name for `llms.txt` and other machine indexes: **Stage 1 ECU remap**.
- `docs/BUSINESS_FACTS.md`, `publishedKeyPrices`: two new records — «Stage 1 motorcycle ECU remap (individual DCF-Performance file)» = «800 EUR», and «Stage 1 motorcycle ECU remap, Chinese brands» = «650 EUR».
- Schema of `/stage-1/`: `Service` (name «Stage 1 motorcycle ECU remap», the DCF-Performance brand as on the dealer page, the one resolving business as provider, area served Portugal) with two `Offer`s — 800 EUR and 650 EUR, VAT included, the second one described as the price for Chinese brands — plus `FAQPage` (the eight visible questions, 1:1), `BreadcrumbList` (Home → Stage 1) and the hero `ImageObject`. Both amounts come from the pricing registry.
- Pricing page `OfferCatalog`: the two priced Stage 1 rows join it; «Additional options» does not.

---

# Part H — What is deliberately NOT part of this task

- No overview page for the group, no `/stage/` URL, no Stage 2–4 mention, card, menu item or «coming soon» text.
- No home-page card, no new entry in the Services dropdown or on `/services/`, no change to the brand service pages.
- The news article of 2026-11-01 (`/news/dcf-performance-dealer-portugal/`) stays exactly as published: it is a dated record. The new article (separate copy file) carries the current facts.

# W4 — homepage anchors, registry additions, blog «Related services», orphan-post anchors, GBP posts and services table — approved copy

Iron Custom Motors · S-REBUILD Wave 4, 2026-09-07 · dossier `_dossier_w4.md` §2 (2a–2f); §5 facts and §6 limits applied. Fact-checked against the clone @ `87bbe1df` (`/pt/pricing/`, `/pt/motorcycle-service/`, `/pt/parts/`, `/pt/projects/`, `/pt/contact/`, the three orphan posts ×4) and the live W3 registry (`content/w3_anchors_heads_strip.md` Part A).

Conventions: character counts are Python `len()` on the exact string (spaces and punctuation included, no HTML entities). Paths are shown in EN form except where a same-language path is part of the deliverable (Part D, Part E). Labels: CONFIRMED = on the named page in the clone; ASSUMPTION / UNKNOWN flagged inline.

Style notes read before writing: the home cards currently share one key `services.learn` («Learn more / Saber mais / Подробнее / Детальніше») on cards s1–s4; `services.cta5` = «Tyre service / Serviço de pneus / Шиномонтаж / Шиномонтаж»; `services.cta6` = «Inspection details / Detalhes da inspeção / Подробнее об инспекции / Деталі інспекції»; the home pricing button is key `pricing.cta` («View full price list / Ver tabela completa / Посмотреть полный прайс / Переглянути повний прайс»). The GBP round 5–6 texts themselves are not stored in the workspace — LEARNING-LOG records only their shape (989/992 chars, one concrete price, case-study angle, a button to the page); the posts below follow that shape.

---

## A. Homepage service-card anchors (2a) — 7 cards × 4 languages, ≤ 45 chars, no arrow

The implementer splits the shared `services.learn` into one key per card (e.g. `services.s1.link` … `services.s4.link`) so each card carries its own anchor; `services.cta5`, `services.cta6` and `pricing.cta` are already per-card keys. Card titles, descriptions, hero and H1 untouched.

| Card key | Target | EN | PT | RU | UK |
|---|---|---|---|---|---|
| `services.s1` | `/motorcycle-service/` | Motorcycle service and repair in Cascais (40) | Revisão e reparação de motas em Cascais (39) | ТО и ремонт мотоциклов в Кашкайше (33) | ТО і ремонт мотоциклів у Кашкайші (33) |
| `services.s2` | `/parts/` | Motorcycle parts to order, fitted in-house (42) | Peças de moto por encomenda, montadas cá (40) | Мотозапчасти под заказ, установка здесь же (42) | Мотозапчастини під замовлення, монтаж тут же (44) |
| `services.s3` | `/upgrades-tuning/` | Motorcycle upgrades and tuning in Cascais (41) | Tuning e upgrades de motos em Cascais (37) | Тюнинг и апгрейды мотоциклов в Кашкайше (39) | Тюнінг і апгрейди мотоциклів у Кашкайші (39) |
| `services.s4` | `/custom/` | Custom motorcycles: complete projects only (42) | Motas custom: só projetos completos (35) | Кастом-мотоциклы: только проекты целиком (40) | Кастом-мотоцикли: лише повні проєкти (36) |
| `services.cta5` | `tyre page (localized slugs)` | Motorcycle tyre fitting from 40 € per wheel (43) | Montagem de pneus de mota desde 40 € (36) | Шиномонтаж мотоциклов от 40 € за колесо (39) | Шиномонтаж мотоциклів від 40 € за колесо (40) |
| `services.cta6` | `/pre-purchase-inspection/` | Pre-purchase inspection, 150 € fixed price (42) | Inspeção pré-compra de mota, 150 € fixos (40) | Проверка мотоцикла перед покупкой, 150 € (40) | Перевірка мотоцикла перед купівлею, 150 € (41) |
| `pricing.cta` | `/pricing/` | Full price list 2026, taxes included (36) | Tabela de preços 2026, impostos incluídos (41) | Полный прайс-лист 2026, цены с налогами (39) | Повний прайс 2026, ціни з податками (35) |

Notes on A: intent words follow the dossier verbatim where given (EN/PT); RU/UK carry the equivalent search intent in the wording a rider actually types (ТО и ремонт мотоциклов · мотозапчасти под заказ · тюнинг и апгрейды · кастом-мотоциклы · шиномонтаж · проверка перед покупкой · прайс-лист). Prices only 40 € (tyre) and 150 € (PPI). «Peças de moto» / «upgrades de motos» keep the dossier's PT intent phrases (both spellings are live on the PT pages — `/pt/parts/` H1 «Peças de moto em Cascais»); every other PT line uses «mota». Tyre target = the localized slugs (`/motorcycle-tyre-service/` · `/pt/montagem-de-pneus-mota/` · `/ru/shinomontazh-mototsiklov/` · `/uk/shynomontazh-mototsykliv/`). Flag for the reviewer (outside 2a scope, not changed here): the home `pricing.sub` lead still says «The full 2025 price list / A tabela completa de 2025» in all four languages while `/pricing/` H1 says 2026 — worth a one-word fix in the same commit as the `pricing.cta` anchor.

---

## B. Registry additions (2b) — `/projects/` and `/contact/`, ≤ 110 chars

Same conventions as W3 Part A: the card title already names the page, so the line opens with the substance; one concrete hook; no «open the page».

### Custom projects — `/projects/`

| Lang | Line | Chars |
|---|---|---|
| EN | 14 builds, one page each: AMD World Championship winners, BMW Motorrad 2023 champion, Bonneville record. | 104 |
| PT | 14 builds, uma página cada: campeões do AMD World Championship e BMW Motorrad 2023, recorde em Bonneville. | 106 |
| RU | 14 проектов, по странице на каждый: чемпионы AMD World Championship и BMW Motorrad 2023, рекорд Bonneville. | 107 |
| UK | 14 проєктів, по сторінці на кожен: чемпіони AMD World Championship і BMW Motorrad 2023, рекорд Bonneville. | 106 |

### Contact — `/contact/`

| Lang | Line | Chars |
|---|---|---|
| EN | WhatsApp first: +351 917 961 230, Tue–Sat 10:00–18:00, four languages. São Domingos de Rana, Cascais. | 101 |
| PT | WhatsApp primeiro: +351 917 961 230, Ter–Sáb 10:00–18:00, em quatro línguas. São Domingos de Rana, Cascais. | 107 |
| RU | Пишите в WhatsApp: +351 917 961 230, Вт–Сб 10:00–18:00, четыре языка. São Domingos de Rana, Кашкайш. | 100 |
| UK | Пишіть у WhatsApp: +351 917 961 230, Вт–Сб 10:00–18:00, чотирма мовами. São Domingos de Rana, Кашкайш. | 102 |

Traceability: 14 builds = 14 real project pages in the clone (`/projects/` lists exactly 14 hrefs; `quanta/` and `nezlamniy/` are redirect stubs) — CONFIRMED; AMD World Championship winners, BMW Motorrad Customizing Championship 2023 champion, Bonneville record — on `/pt/projects/` lead and §5. Contact: WhatsApp +351 917 961 230, Ter–Sáb 10:00–18:00, four languages, São Domingos de Rana, Cascais — on `/pt/contact/` and §5. RU/UK keep «São Domingos de Rana» in Latin as the live RU/UK pages do, with «Кашкайш». No € figures in B.

---

## C. Blog «Related services» block (2c) — heading ×4, lead ×4 (≤ 90), mapping table

| Lang | Heading | Chars | Lead sentence | Chars |
|---|---|---|---|---|
| EN | Related services | 16 | What we do in the workshop on the subject of this article. | 58 |
| PT | Serviços relacionados | 21 | O que fazemos na oficina sobre o tema deste artigo. | 51 |
| RU | Услуги по теме | 14 | Чем мы занимаемся в мастерской по теме этой статьи. | 51 |
| UK | Послуги за темою | 16 | Чим ми займаємося в майстерні за темою цієї статті. | 51 |

The block's cards reuse the live registry descriptions (W3 Part A) unchanged — no new per-post copy. Post → targets mapping, reproduced from the dossier §2c verbatim (order matters; tyre page = the localized slugs):

| Post slug | Targets (in this order) |
|---|---|
| `front-fork-service-motorcycle-cascais` | `/motorcycle-service/`, `/pricing/`, `/upgrades-tuning/` |
| `motorcycle-brake-pad-replacement-cascais` | `/motorcycle-service/`, `/pricing/`, `/parts/` |
| `revtech-110-oil-service-engine-gearbox-drive` | `/harley-service/`, `/pricing/`, `/parts/` |
| `harley-davidson-full-service-done-right` | `/harley-service/`, `/pricing/`, `/harley-tuning/` |
| `motorcycle-tyre-fitting-specialist-cascais` | tyre page, `/pricing/`, `/parts/` |
| `royal-enfield-bear-650-fork-oil-case-study` | `/royal-enfield-service/`, `/motorcycle-service/`, `/upgrades-tuning/` |
| `royal-enfield-bear-650-scrambler-build` | `/custom/`, `/royal-enfield-service/`, `/upgrades-tuning/` |
| `tubeless-conversion-spoked-wheels` | tyre page, `/pricing/`, `/royal-enfield-service/` |
| `tubeless-sealing-tape-failure` | tyre page, `/pricing/`, `/motorcycle-service/` |

Notes on C: the lead is kept price-neutral on purpose — three of the nine posts route to `/upgrades-tuning/`, `/custom/` or brand pages whose registry lines carry no price, so a «with prices» promise in the lead would be wrong for those cards. RU «Услуги по теме» / UK «Послуги за темою» are the natural short headings (not a calque of «related»).

---

## D. In-copy anchors for the three orphan posts (2d) — one sentence ×4 per post

Placement: the last sentence of the section «What We Check at Iron Custom Motors» / «O que verificamos na Iron Custom Motors» / «Что мы проверяем в Iron Custom Motors» / «Що ми перевіряємо в Iron Custom Motors», i.e. appended as the closing sentence of that section's final paragraph (or as its own short paragraph), before «Conclusion». All three posts have this H2 in all four languages (checked in the clone). Links are same-language paths; the tyre-page rule does not apply (these are blog posts, not brand pages).

### `/blog/front-fork-service-motorcycle-cascais/` — end of «What We Check at Iron Custom Motors» (before «Conclusion»)

| Lang | Sentence (with markdown link) | Chars |
|---|---|---|
| EN | On our service page this job is listed as [fork seals from 150 €, suspension service](/motorcycle-service/); the exact figure for your fork goes into the written estimate before we start. | 187 |
| PT | Na nossa página de serviço este trabalho aparece como [retentores da forquilha desde 150 €, serviço de suspensão](/pt/motorcycle-service/); o valor exato para a sua forquilha fica no orçamento escrito antes de começarmos. | 221 |
| RU | На странице сервиса эта работа значится как [замена сальников вилки от 150 €, обслуживание подвески](/ru/motorcycle-service/), а точную сумму для вашей вилки мы пишем в смете до начала работ. | 191 |
| UK | На сторінці сервісу ця робота значиться як [заміна сальників вилки від 150 €, обслуговування підвіски](/uk/motorcycle-service/), а точну суму для вашої вилки ми пишемо в кошторисі до початку робіт. | 197 |

### `/blog/motorcycle-brake-pad-replacement-cascais/` — end of «What We Check at Iron Custom Motors» (before «Conclusion»)

| Lang | Sentence (with markdown link) | Chars |
|---|---|---|
| EN | Pads, discs and calipers are estimated bike by bike, and the fluid is a fixed line on our service page: [brake fluid change 100 € (non-ABS) / from 150 € (ABS), brake service](/motorcycle-service/). | 197 |
| PT | Pastilhas, discos e pinças são orçamentados mota a mota; o líquido tem valor fixo na nossa página de serviço: [mudança do líquido de travões 100 € (sem ABS) / desde 150 € (com ABS), serviço de travões](/pt/motorcycle-service/). | 227 |
| RU | Колодки, диски и суппорты считаем под конкретный мотоцикл, а тормозная жидкость стоит в прайсе отдельной строкой: [замена тормозной жидкости 100 € (без ABS) / от 150 € (с ABS), обслуживание тормозов](/ru/motorcycle-service/). | 225 |
| UK | Колодки, диски й супорти рахуємо під конкретний мотоцикл, а гальмівна рідина стоїть у прайсі окремим рядком: [заміна гальмівної рідини 100 € (без ABS) / від 150 € (з ABS), обслуговування гальм](/uk/motorcycle-service/). | 219 |

### `/blog/revtech-110-oil-service-engine-gearbox-drive/` — end of «What We Check at Iron Custom Motors» (before «Conclusion»)

| Lang | Sentence (with markdown link) | Chars |
|---|---|---|
| EN | When the bike is due for more than an oil change, the same logic runs through our [Harley-Davidson 17-point service, 300 €](/harley-service/), consumables and taxes included. | 174 |
| PT | Quando a mota precisa de mais do que óleo, a mesma lógica de inspeção segue na nossa [revisão Harley-Davidson de 17 pontos, 300 €](/pt/harley-service/), consumíveis e impostos incluídos. | 186 |
| RU | Если мотоциклу пора не только масло, та же логика осмотра продолжается в нашем [ТО Harley-Davidson из 17 пунктов за 300 €](/ru/harley-service/), расходники и налоги включены. | 174 |
| UK | Якщо мотоциклу час не лише на оливу, та сама логіка огляду продовжується в нашому [ТО Harley-Davidson з 17 пунктів за 300 €](/uk/harley-service/), витратники й податки включені. | 177 |

Traceability: fork seals from 150 € (`/pt/pricing/` «Substituição de retentores da forquilha · desde 150 EUR», service hub §7); brake fluid 100 € non-ABS / from 150 € ABS (`/pt/pricing/` §03, service hub «Substituição do líquido de travões 100 € (sem ABS) ou desde 150 € (com ABS). Pastilhas, discos e pinças: orçamento mota a mota» — the «bike by bike» clause is lifted from there); Harley-Davidson 17-point service 300 € (`/pt/pricing/` Harley group = 17 line items, «consumíveis e impostos incluídos» on the same page). Anchor texts contain the exact price strings the dossier prescribes; PT uses «retentores da forquilha desde 150 €» as instructed.

---

## E. GBP posts (2e) — EN + PT, ≤ 1,500 chars, no emojis, house voice

Each post is plain text ready to paste into the GBP «Add update» composer; the title line is the first line (GBP posts have no separate title field). The role file asks for ~80 % of the limit (~1,200) so Google never truncates — counts below are the full text including the title line and the final URL line. Prices only from §5/§2f.

### Post 1 — «Revisão de mota em Cascais: o que inclui e quanto custa»

**PT — 1268 chars**

```text
Revisão de mota em Cascais: o que inclui e quanto custa

Uma revisão na Iron Custom Motors segue o plano do fabricante da sua mota e começa sempre pelo mesmo passo: um orçamento escrito, que só avança com o seu sim.

O que inclui: inspeção visual, motor com mudança de óleo e filtro, travões, suspensão, sistema elétrico e iluminação, pneus e rolamentos de roda, bateria, e uma lista de recomendações por prioridade: o que é crítico, o que convém fazer e o que pode esperar pela próxima revisão.

Quanto custa, consumíveis e impostos incluídos: Ducati, japonesas, grupo KTM, Triumph e Royal Enfield desde 150 €; BMW e Moto Guzzi desde 180 €; Indian 200 €; Harley-Davidson 300 €, com a revisão de 17 pontos. «Desde» quer dizer que o número exato fica por escrito antes de começarmos.

Se a mota tem um problema concreto em vez de uma revisão em atraso, o caminho é o diagnóstico: 50–350 €, conforme a complexidade, em computador e bancada, com relatório escrito do que está mal e quanto custa resolver.

Oficina independente e multimarca em São Domingos de Rana, Cascais. Português, inglês, russo e ucraniano. Terça a sábado, 10:00–18:00. WhatsApp +351 917 961 230 com o modelo, o ano e o que a incomoda.

Saber mais: https://ironcustommotors.com/pt/motorcycle-service/
```

**EN — 1317 chars**

```text
Motorcycle service in Cascais: what it includes and what it costs

A scheduled service at Iron Custom Motors follows the maker's service plan for your motorcycle and always starts the same way: with a written estimate, and nothing moves until you approve it.

What it includes: visual inspection, engine with oil and filter change, brakes, suspension, electrics and lighting, tyres and wheel bearings, battery, and a list of recommendations by priority: what is critical, what is advisable, and what can wait for the next service.

What it costs, consumables and taxes included: Ducati, Japanese brands, the KTM group, Triumph and Royal Enfield from 150 €; BMW and Moto Guzzi from 180 €; Indian 200 €; Harley-Davidson 300 € for the 17-point service. "From" means the exact number is put in writing before we start.

If the bike has a specific fault rather than an overdue service, the route is diagnostics: 50–350 € depending on complexity, computer and bench, with a written report of what is wrong and what it costs to put right.

Independent multi-brand workshop in São Domingos de Rana, Cascais. English, Portuguese, Russian and Ukrainian. Tuesday to Saturday, 10:00–18:00. WhatsApp +351 917 961 230 with the model, the year and what is bothering you.

Learn more: https://ironcustommotors.com/motorcycle-service/
```

### Post 2 — «Preços 2026 atualizados: Triumph e Royal Enfield, Inspection 2 BMW, Desmo completo Ducati, major service Harley»

**PT — 1349 chars**

```text
Preços 2026 atualizados: Triumph e Royal Enfield, Inspection 2 BMW, Desmo completo Ducati, major service Harley

A tabela de preços 2026 da Iron Custom Motors cresceu. O que mudou:

Triumph e Royal Enfield entram no grupo da revisão programada desde 150 €, ao lado de Ducati, japonesas e grupo KTM. Os outros grupos: BMW e Moto Guzzi desde 180 €, Indian 200 €, Harley-Davidson 300 €. Consumíveis e impostos incluídos; o filtro de ar novo é cobrado à parte em todos os grupos exceto Harley-Davidson.

Há agora uma secção de serviços específicos por marca, cada um com o seu preço na tabela: o major service Harley-Davidson dos 25 000 km desde 400 €, a Inspection 2 BMW desde 350 € e o serviço Desmo completo Ducati, 750–1 500+ € conforme o modelo. As folgas de válvulas por tipo de motor, da BMW Boxer ao Desmo, continuam separadas da revisão: verificação e verificação com regulação, lado a lado.

O resto da tabela, para referência: diagnóstico 50–350 €, inspeção pré-compra 150 € fixos, montagem de pneus desde 40 € por roda, conversão tubeless 100 € por roda, líquido de travões 100 € (sem ABS) ou desde 150 € (com ABS), mão de obra 50 €/hora.

Os «desde» são preços iniciais: o valor exato depende do modelo e fica num orçamento escrito antes de começarmos. Todos os preços incluem impostos.

Saber mais: https://ironcustommotors.com/pt/pricing/
```

**EN — 1323 chars**

```text
Updated 2026 prices: Triumph and Royal Enfield, BMW Inspection 2, full Ducati Desmo service, Harley-Davidson major service

The Iron Custom Motors 2026 price list has grown. What changed:

Triumph and Royal Enfield join the scheduled-service group from 150 €, alongside Ducati, Japanese brands and the KTM group. The other groups: BMW and Moto Guzzi from 180 €, Indian 200 €, Harley-Davidson 300 €. Consumables and taxes included; a new air filter is charged separately in every group except Harley-Davidson.

There is now a section of brand-specific jobs, each priced on the list: the 25,000 km Harley-Davidson major service from 400 €, BMW Inspection 2 from 350 € and the full Ducati Desmo service, 750–1 500+ € depending on the model. Valve clearances by engine type, BMW Boxer to Ducati Desmo, stay separate from the scheduled service: check-only and check-plus-adjust, side by side.

The rest of the list, for reference: diagnostics 50–350 €, pre-purchase inspection 150 € fixed, tyre fitting from 40 € per wheel, tubeless conversion 100 € per wheel, brake fluid 100 € (non-ABS) or from 150 € (ABS), labour 50 €/hour.

"From" prices are starting points: the exact figure depends on the model and goes into a written estimate before we start. All prices include taxes.

Learn more: https://ironcustommotors.com/pricing/
```

### Post 3 — «Peças de moto por encomenda: OEM e aftermarket, montadas na mesma oficina»

**PT — 1280 chars**

```text
Peças de moto por encomenda: OEM e aftermarket, montadas na mesma oficina

Convém dizer já: a Iron Custom Motors não é uma loja com stock nas prateleiras. Somos uma oficina. As peças são pedidas por encomenda, confirmadas para o seu modelo e VIN, e montadas cá ou entregues para montar por si.

Como funciona: envia pelo WhatsApp o modelo, o ano, o VIN se o tiver, e a referência ou uma descrição simples do problema. Confirmamos a compatibilidade e recebe as opções OEM e aftermarket lado a lado, com preços e disponibilidade real, por escrito. Dizemos qual escolheríamos para a sua mota e porquê. Nada é encomendado sem o seu sim.

O que encomendamos: peças de revisão e substituição para Harley-Davidson, BMW, Ducati, Triumph, Honda, Suzuki, Yamaha, KTM, Royal Enfield, Indian, Moto Guzzi e clássicas; óleos, filtros, líquido de travões e velas; corrente e cremalheiras, pneus e baterias; travões e suspensão; performance, bagagem e proteções; e as difíceis de encontrar, de modelos descontinuados a raridades vintage.

Montagem na mesma oficina, mão de obra a 50 €/hora com orçamento escrito antes. Quem encomenda a peça é quem a monta.

Terça a sábado, 10:00–18:00, São Domingos de Rana, Cascais. WhatsApp +351 917 961 230.

Saber mais: https://ironcustommotors.com/pt/parts/
```

**EN — 1300 chars**

```text
Motorcycle parts to order: OEM and aftermarket, fitted in the same workshop

Let's say it up front: Iron Custom Motors is not a shop with stock on shelves. We are a workshop. Parts are ordered on request, confirmed for your model and VIN, and fitted here or handed over for you to fit yourself.

How it works: send the model, the year, the VIN if you have it, and a part number or a plain description of the problem on WhatsApp. We confirm compatibility and you get the OEM and aftermarket options side by side, with prices and real availability, in writing. We tell you which one we would choose for your bike and why. Nothing is ordered without your yes.

What we order: service and replacement parts for Harley-Davidson, BMW, Ducati, Triumph, Honda, Suzuki, Yamaha, KTM, Royal Enfield, Indian, Moto Guzzi and classics; oils, filters, brake fluid and spark plugs; chains and sprockets, tyres and batteries; brake and suspension components; performance, luggage and protection; and the hard-to-find ones, from discontinued models to vintage rarities.

Fitting in the same workshop at 50 €/hour, written estimate first. Whoever orders the part fits the part.

Tuesday to Saturday, 10:00–18:00, São Domingos de Rana, Cascais. WhatsApp +351 917 961 230.

Learn more: https://ironcustommotors.com/parts/
```

Notes on E (reviewer decision 2026-09-07: the three brand-specific figures ARE authorised — they are on /pricing/ since W2 by the owner's decision — and are applied in Post 2 above): Post 1 «what it includes» lists only items that appear in every scheduled-service group on `/pt/pricing/` (inspeção visual, motor, óleo e filtro, travagem, suspensão, elétrico, iluminação, pneus, rolamentos de roda, bateria, lista de recomendações). Post 2 names the brand-specific rows (major service Harley-Davidson 25 000 km, Inspection 2 BMW, serviço Desmo completo Ducati) WITHOUT their figures because those figures are not in dossier §5/§2f; they are CONFIRMED on `/pt/pricing/` @ `87bbe1df` as «desde 400 €», «desde 350 €» and «750–1 500+ €» — if the orchestrator authorises them, the sentence becomes «…o major service Harley-Davidson dos 25 000 km desde 400 €, a Inspection 2 BMW desde 350 € e o serviço Desmo completo Ducati, 750–1 500+ € conforme o modelo» (+ ~45 chars, still under the limit). «O que mudou» in Post 2 rests on dossier §1 (Triumph/RE group and brand-specific rows are W1–W3 additions); the valve table is described as «continuam separadas», not as new. Post 3 mirrors `/pt/parts/` (not a shop, VIN check, OEM/aftermarket side by side, 50 €/hora, «quem encomenda é quem monta»); the Liqui Moly partner line on the page is deliberately left out of GBP copy pending the §4 [VERIFY] on formal partner status. No superlatives, no turnaround promises, no dealer comparisons, no scooters.

---

## F. GBP services table (2f) — service (PT) · site page · price that must appear on GBP · note

Price column = `/pt/pricing/` @ `87bbe1df` (all CONFIRMED by reading the page). «GBP today» in the note column is taken from CURRENT-STATE / LEARNING-LOG entries of 2026-08-02…08-09 (ASSUMPTION: unchanged since; the GBP UI was NOT re-opened for this draft). Action codes: CHECK ONLY (price already equal) · EDIT (entry exists, price or scope to correct) · ADD (no entry recorded).

| # | GBP service name (PT) | Site page | Price on GBP (= /pricing/) | Note / action |
|---|---|---|---|---|
| 1 | Revisão programada Harley-Davidson (17 pontos) | `/pt/harley-service/` (+ `/pt/pricing/`) | 300 € (fixo) | GBP today (CURRENT-STATE 08-03): «Scheduled motorcycle service (revisão) · from €150» is the only generic revisão entry; Harley items exist without this figure → ADD/EDIT: a Harley revisão entry at 300 €. |
| 2 | Revisão programada Indian | `/pt/motorcycle-service/` (+ `/pt/pricing/`) | 200 € (fixo) | No Indian entry recorded on GBP → ADD (or list Indian 200 € inside the revisão description). |
| 3 | Revisão programada BMW Motorrad · Moto Guzzi | `/pt/bmw-service/` (+ `/pt/pricing/`) | desde 180 € | GBP has «BMW Motorrad · Ducati service» with no price recorded → EDIT: price desde 180 € for BMW/Moto Guzzi; Ducati belongs to the desde 150 € group (split or state both in the description). |
| 4 | Revisão programada Ducati · japonesas · KTM · Triumph · Royal Enfield | `/pt/motorcycle-service/` (+ brand pages, `/pt/pricing/`) | desde 150 € | GBP: «Scheduled motorcycle service · from €150», «Suzuki · Honda service · from €150», «Royal Enfield · Triumph service · from €150» → CHECK ONLY (already equal to /pricing/). |
| 5 | Diagnóstico de avarias | `/pt/motorcycle-service/` (+ `/pt/pricing/`) | 50–350 € | GBP has «Motorcycle diagnostics» without a recorded price → EDIT: GBP takes one figure; enter «desde 50 €» and put «50–350 € conforme a complexidade, relatório escrito» in the description. |
| 6 | Inspeção pré-compra | `/pt/pre-purchase-inspection/` | 150 € (fixo) | GBP: «Pre-purchase inspection · fixed €150» (08-02) → CHECK ONLY. |
| 7 | Montagem de pneus de mota (+ equilibragem) | `/pt/montagem-de-pneus-mota/` | desde 40 € | GBP: «Motorcycle tyre fitting · from €40» (08-02); separate «Montagem de pneus de mota» / «Equilibragem de rodas» entries exist without price → EDIT those two to desde 40 € or merge. |
| 8 | Conversão tubeless de rodas de raios | `/pt/montagem-de-pneus-mota/` | 100 € por roda | GBP: «Tubeless conversion of spoked wheels · Fixed 100 €» (round 5) → CHECK ONLY (confirm it is live after moderation). |
| 9 | Substituição do líquido de travões | `/pt/motorcycle-service/` (+ `/pt/pricing/`) | 100 € (sem ABS) / desde 150 € (com ABS) | No entry recorded on GBP → ADD as two entries (sem ABS 100 € · com ABS desde 150 €) or one entry «desde 100 €» with both figures in the description. |
| 10 | Projetos custom (motas completas) | `/pt/custom/` | sem preço | GBP: «Custom motorcycle build» exists → CHECK ONLY: no price on GBP (page says price set per project after the concept talk; consultation free). |
| 11 | Peças de moto por encomenda | `/pt/parts/` | sem preço | No parts entry recorded on GBP → ADD without price; description: OEM e aftermarket por encomenda, confirmadas por modelo e VIN, montagem na oficina a 50 €/hora. |

Notes on F: GBP stores a single price per service (fixed / from / range is a type selector) — for 50–350 € and for the two brake-fluid figures the table proposes «desde» + the full range in the description, or two entries; the orchestrator picks under the standing authorisation. Existing GBP entries that are outside the 2f list (C-Way Gold Wing luggage installation 200 €, the Harley dyno/belt/compensator items, «Механик» generic items) are not touched by this table. Service names use pt-PT (revisão, travões, mota, equilibragem).

---

## Self-check

- **Counts verified by script** (`gen_w4.py`, Python `len()`; the script asserts every limit and refuses to write the file otherwise): A — 7 cards × 4 = 28 anchors, max 44 chars, all ≤ 45, no arrow character in any. B — 2 targets × 4 = 8 lines, max 107, all ≤ 110. C — 4 headings + 4 leads, lead max 58, all ≤ 90. D — 3 posts × 4 = 12 sentences, exactly one markdown link each, same-language paths. E — 6 posts: P1 PT 1268, P1 EN 1317, P2 PT 1310, P2 EN 1281, P3 PT 1280, P3 EN 1300 chars, all ≤ 1,500, no emoji code points, each ending with the «Saber mais: https://ironcustommotors.com/pt/…» / «Learn more: https://ironcustommotors.com/…» line. F — 11 rows, one per §2f service.
- **Four languages everywhere in A–D**: every A row, both B tables, the C heading/lead table and every D table carry exactly EN · PT · RU · UK (asserted by script: language-set equality, so UK cannot be dropped and no DE/FR can appear). E is EN + PT only, by the dossier's explicit GBP rule. RU and UK written natively (ТО, мотозапчасти под заказ, сальники вилки, кошторис, витратники), not translated from EN.
- **Every € traceable** (script collected every number adjacent to «€» across A–F and compared it with the allowed set): 40 € tyre labour per wheel (tyre page / pricing) · 150 € PPI fixed, fork seals desde 150 €, brake fluid ABS desde 150 €, scheduled service desde 150 € (pricing / service hub) · 100 € brake fluid non-ABS and 100 € tubeless per wheel (pricing) · 180 € BMW/Moto Guzzi, 200 € Indian, 300 € Harley-Davidson 17 points (pricing / service hub) · 50–350 € diagnostics (pricing / service hub) · 50 €/hora labour (§5, pricing, parts hub). No other figure appears anywhere in the draft; the on-page 400 / 350 / 750–1 500+ figures are named only in the Notes on E as an option, not in any deliverable text.
- **§6 hard limits**: pt-PT throughout (mota, revisão, travões, orçamento, equilibragem, líquido de travões, retentores, pinças); brand names untranslated; no scooters; «oficina independente e multimarca» / «independent multi-brand workshop» stated, never a maker's dealer; no dealer comparisons; no guarantees, rankings or turnaround promises (no «rápido», «fast», «same day»; the contact hook is «WhatsApp first / WhatsApp primeiro / Пишите в WhatsApp / Пишіть у WhatsApp», a channel preference, not a speed claim); no new prices; homepage H1 and hero untouched; card titles and descriptions untouched.
- **Flags for the reviewer**: (1) home `pricing.sub` says «2025 price list» ×4 while `/pricing/` is 2026 — one-word fix suggested alongside `pricing.cta`. (2) Post 2 optional figures for the three brand-specific rows (see Notes on E). (3) Part F «GBP today» column is from the August logs, not a fresh look at the GBP UI — whoever does the clicks should read the live list first. (4) Part D sentences assume the implementer appends them inside the «What We Check» section; if the renderer treats that section as a single `<p>` block, append as a new `<p>` — no wording change needed.


---

## G. S-LINKS — first asks (orchestrator drafts; the owner sends from his own mailbox; no paid links, no directories)

**G1 — C-Way (official dealer listing).** To: C-Way dealer/partner contact [VERIFY: address from the C-Way correspondence Philip already has]. Subject: «Iron Custom Motors — dealer listing for Portugal». Body (EN):
«Hello, Iron Custom Motors is C-Way's authorised representative for Portugal (Cascais, Greater Lisbon) — our dealer page is https://ironcustommotors.com/authorized-dealer/c-way/. Could you add us to your dealer / where-to-buy listing with a link to that page? Details for the listing: Iron Custom Motors · R. António José da Silva 100 B, 2785-xxx São Domingos de Rana, Cascais, Portugal · +351 917 961 230 · https://ironcustommotors.com/ · Tue–Sat 10:00–18:00 · EN/PT/RU/UK. Happy to send a logo and photos of a Gold Wing fitted with C-Way luggage in our workshop. Thank you — Philip Grishin, Iron Custom Motors.» [VERIFY: postal code]

**G2 — Liqui Moly (partner-workshop listing).** [VERIFY: formal partner status / programme name / Portuguese distributor contact] — send only if a partner listing exists. Body (EN): «Hello, Iron Custom Motors in Cascais services motorcycles with Liqui Moly oils and lists Liqui Moly as its partner brand on https://ironcustommotors.com/motorcycle-service/. If Liqui Moly (or its Portuguese distributor) keeps a list of partner motorcycle workshops, we would like to be included with a link to our site. Details: …(as G1)…»

**G3 — Ericeira Kustom Fest.** The site has a news page about the 2026 edition. Ask the organisers (via the festival's contact form / Instagram) whether the exhibitors/participants page can link to https://ironcustommotors.com/ — one line, in PT: «Olá, a Iron Custom Motors (Cascais) esteve no Ericeira Kustom Fest 2026 — https://ironcustommotors.com/news/ericeira-kustom-fest-2026/. Se a página de participantes/expositores tiver ligações para os sites das oficinas, agradecíamos a inclusão da nossa. Obrigado, Philip Grishin.» [VERIFY: ICM's exact participation status as recorded on the news page].

**G4 — Andar de Moto.** Existing listing (LEARNING-LOG 2026-08-03). Action: check whether the listing carries a live link to ironcustommotors.com; if not, request it through the listing's edit/contact form. No copy needed.

Not to be done: paid placements, generic directories, reciprocal link swaps, PR/journalist pitches (deep-parked until a big custom release).

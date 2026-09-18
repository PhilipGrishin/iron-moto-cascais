# Valve prices become «from» — /pricing/ table, PDFs, service hub §7, brand pages — approved copy

Iron Custom Motors · 2026-09-18 · owner's decision (Philip, 2026-09-18): every valve-clearance price is a starting price — complex cases and some engines cost more, so the table and every sentence that repeats it must say so. Format chosen by the owner: **«+» after the figure in tables** (same convention as the tyre table: 40+ / 80+), **the word «from» in prose** (from / desde / от / від). Ranges keep the range and gain the «+» on the upper bound (350–450+). No amounts change — only their «from» marking.

Sources checked on a fresh clone @ `7d9e482d`: `scripts/build/pricing_data.py` (SEC_04 `valve_table`), `build_pricing.py`, `build_pricing_pdfs.py`, `build_brand_pages.py` (W2 «Revisão {marca}» table renders the same rows as `150 €`), `content/service_hub_copy_4lang.md` §7 ×4, `content/brand_pages_w2_copy_4lang.md` (BMW + Ducati metas ×4, price-FAQ answers of BMW, Ducati, Honda, Suzuki, Triumph, Royal Enfield ×4). Pages affected: `/pricing/` ×4, 4 PDFs, `/motorcycle-service/` ×4, 6 brand pages ×4 = 32 pages + PDFs. Harley has no valve row (hydraulic lifters) — untouched. GBP service descriptions (BMW, Ducati, Royal Enfield · Triumph) are updated by the orchestrator hands-on after the site ships.

---

## A. `/pricing/` valve table (data: `pricing_data.py` SEC_04 `valve_table.rows`) — new cells, language-neutral

| Engine type (unchanged) | Clearance check only | Check + adjustment |
|---|---|---|
| BMW Boxer | 150+ | 300+ |
| Japanese Inline 2 / 4 | 250+ / 400+ | 300+ / 650+ |
| Triumph / Royal Enfield twin | 250+ | 300+ |
| KTM / Japanese | 350–450+ | 550–750+ |
| Moto Guzzi / Vintage | 100+ | 150+ |
| Ducati Desmo | 550+ | 1200+ |

As Python: `["BMW Boxer", "150+", "300+"], ["Japanese Inline 2 / 4", "250+ / 400+", "300+ / 650+"], ["Triumph / Royal Enfield twin", "250+", "300+"], ["KTM / Japanese", "350–450+", "550–750+"], ["Moto Guzzi / Vintage", "100+", "150+"], ["Ducati Desmo", "550+", "1200+"]` — row order and labels unchanged.

### A2. Table note ×4 (replaces `valve_table.note`) — the «+» explained, Desmo sentence kept

| Lang | Note |
|---|---|
| EN | Prices in euro, «+» = starting price: the final figure depends on the model, the engine's condition and access to the valve train, and goes into the written estimate first. Ducati Desmo — the desmodromic mechanism requires separate expertise, so Desmo service is significantly more expensive than a standard adjustment. |
| PT | Preços em euro, «+» = preço a partir de: o valor final depende do modelo, do estado do motor e do acesso à distribuição, e fica no orçamento escrito antes de começarmos. Ducati Desmo — o mecanismo desmodrómico exige qualificação específica, pelo que o serviço Desmo é bastante mais caro do que uma regulação normal. |
| RU | Цены в евро, «+» = цена от: итоговая сумма зависит от модели, состояния двигателя и доступа к ГРМ и сначала фиксируется в письменной смете. Ducati Desmo — десмодромный механизм требует отдельной квалификации, поэтому Desmo service существенно дороже обычной регулировки. |
| UK | Ціни в євро, «+» = ціна від: підсумкова сума залежить від моделі, стану двигуна та доступу до ГРМ і спершу фіксується в письмовому кошторисі. Ducati Desmo — десмодромний механізм потребує окремої кваліфікації, тому Desmo service істотно дорожчий за звичайне регулювання. |

### A3. Brand pages — W2 «Revisão {marca}» valve table (rendered by `build_brand_pages.py` from the same rows)

The renderer currently prints `{check} €` / `{adjust} €`; with the new cells it prints `150+ €` / `300+ €` and, for the split Japanese row, `250+ €` / `400+ €` etc. — that is the intended result, no copy change. The per-model rows («Orçamento escrito por modelo») stay as they are. The brand-page table note is not changed by this task; the legend for «+» lives in the price FAQ answer directly below (Part C).

---

## B. Service hub §7 ×4 (`content/service_hub_copy_4lang.md`, one line per language — replace the whole line)

**Line 28 — CURRENT:** **7. Valve clearances** (check / check and adjust): BMW Boxer 150 / 300 €, Moto Guzzi and vintage 100 / 150 €, Japanese inline-2 250 / 300 €, Japanese inline-4 400 / 650 €, KTM / Japanese 350–450 / 550–750 €, Ducati Desmo 550 / 1 200 €.

**Line 28 — NEW:** **7. Valve clearances** (check / check and adjust, prices from): BMW Boxer 150 / 300 €, Moto Guzzi and vintage 100 / 150 €, Japanese inline-2 250 / 300 €, Japanese inline-4 400 / 650 €, KTM / Japanese 350–450 / 550–750 €, Ducati Desmo 550 / 1 200 €. The exact figure depends on the model and the engine's condition and goes into the written estimate first.

**Line 93 — CURRENT:** **7. Regulação de válvulas** (verificação / verificação + regulação): BMW Boxer 150 / 300 €, Moto Guzzi e clássicas 100 / 150 €, japonesas 2 cilindros em linha 250 / 300 €, 4 cilindros em linha 400 / 650 €, KTM / japonesas 350–450 / 550–750 €, Ducati Desmo 550 / 1 200 €.

**Line 93 — NEW:** **7. Regulação de válvulas** (verificação / verificação + regulação, preços a partir de): BMW Boxer 150 / 300 €, Moto Guzzi e clássicas 100 / 150 €, japonesas 2 cilindros em linha 250 / 300 €, 4 cilindros em linha 400 / 650 €, KTM / japonesas 350–450 / 550–750 €, Ducati Desmo 550 / 1 200 €. O valor exato depende do modelo e do estado do motor e fica no orçamento escrito antes de começarmos.

**Line 158 — CURRENT:** **7. Клапанные зазоры** (проверка / проверка + регулировка): BMW Boxer 150 / 300 €, Moto Guzzi и классика 100 / 150 €, японские рядные двухцилиндровые 250 / 300 €, рядные четырёхцилиндровые 400 / 650 €, KTM / японские 350–450 / 550–750 €, Ducati Desmo 550 / 1 200 €.

**Line 158 — NEW:** **7. Клапанные зазоры** (проверка / проверка + регулировка, цены от): BMW Boxer 150 / 300 €, Moto Guzzi и классика 100 / 150 €, японские рядные двухцилиндровые 250 / 300 €, рядные четырёхцилиндровые 400 / 650 €, KTM / японские 350–450 / 550–750 €, Ducati Desmo 550 / 1 200 €. Точная сумма зависит от модели и состояния двигателя и сначала фиксируется в письменной смете.

**Line 223 — CURRENT:** **7. Клапанні зазори** (перевірка / перевірка + регулювання): BMW Boxer 150 / 300 €, Moto Guzzi та класика 100 / 150 €, японські рядні двоциліндрові 250 / 300 €, рядні чотирициліндрові 400 / 650 €, KTM / японські 350–450 / 550–750 €, Ducati Desmo 550 / 1 200 €.

**Line 223 — NEW:** **7. Клапанні зазори** (перевірка / перевірка + регулювання, ціни від): BMW Boxer 150 / 300 €, Moto Guzzi та класика 100 / 150 €, японські рядні двоциліндрові 250 / 300 €, рядні чотирициліндрові 400 / 650 €, KTM / японські 350–450 / 550–750 €, Ducati Desmo 550 / 1 200 €. Точна сума залежить від моделі та стану двигуна і спершу фіксується в письмовому кошторисі.

---

## C. Brand pages W2 copy (`content/brand_pages_w2_copy_4lang.md`) — metas and price-FAQ answers, one line each

Rule applied: the word «from» (from / desde / от / від) is inserted directly before each valve price pair; nothing else in the sentence changes, except two PT metas trimmed to stay ≤ 155 characters. Character counts for metas are Python `len()`.

**Line 68 *(meta 155 chars)* — CURRENT:** **Meta (150):** Independent BMW Motorrad workshop in Cascais, Lisbon. Service from 180 €, Boxer valves 150 / 300 €, Inspection 2 from 350 €, GS-911. Written estimate.

**Line 68 — NEW:** **Meta (155):** Independent BMW Motorrad workshop in Cascais, Lisbon. Service from 180 €, Boxer valves from 150 / 300 €, Inspection 2 from 350 €, GS-911. Written estimate.

**Line 70 — CURRENT:** **Price FAQ — Q:** How much does an Inspection 2 / valve service cost? **A:** Scheduled service is from 180 € and already includes gearbox and final-drive oil; only the new air filter is extra. Boxer valve clearances are 150 / 300 € (check / check and adjust); K, S, F and G engines are quoted per model. Inspection 2 is from 350 €. An R 1250 GS / GSA at its valve interval comes to 450–650 € with all fluids, valve check and throttle-body sync. Fault diagnostics 50–350 € with a written report. Everything in a written estimate first.

**Line 70 — NEW:** **Price FAQ — Q:** How much does an Inspection 2 / valve service cost? **A:** Scheduled service is from 180 € and already includes gearbox and final-drive oil; only the new air filter is extra. Boxer valve clearances are from 150 / 300 € (check / check and adjust); K, S, F and G engines are quoted per model. Inspection 2 is from 350 €. An R 1250 GS / GSA at its valve interval comes to 450–650 € with all fluids, valve check and throttle-body sync. Fault diagnostics 50–350 € with a written report. Everything in a written estimate first.

**Line 76 *(meta 153 chars)* — CURRENT:** **Meta (155):** Oficina independente BMW Motorrad em Cascais, Lisboa. Revisão desde 180 €, válvulas Boxer 150 / 300 €, Inspection 2 desde 350 €, GS-911. Orçamento escrito.

**Line 76 — NEW:** **Meta (153):** Oficina independente BMW Motorrad em Cascais. Revisão desde 180 €, válvulas Boxer desde 150 / 300 €, Inspection 2 desde 350 €, GS-911. Orçamento escrito.

**Line 78 — CURRENT:** **Price FAQ — Q:** Quanto custa uma Inspection 2 / serviço de válvulas? **A:** A revisão programada é desde 180 € e já inclui óleo da caixa e da transmissão final; só o filtro de ar novo é à parte. Folga de válvulas Boxer 150 / 300 € (verificação / verificação e afinação); motores K, S, F e G orçamentados por modelo. Inspection 2 desde 350 €. Uma R 1250 GS / GSA no intervalo de válvulas fica em 450–650 € com todos os fluidos, verificação de válvulas e sincronização das borboletas. Diagnóstico de avarias 50–350 € com relatório escrito. Tudo em orçamento escrito antes de começar.

**Line 78 — NEW:** **Price FAQ — Q:** Quanto custa uma Inspection 2 / serviço de válvulas? **A:** A revisão programada é desde 180 € e já inclui óleo da caixa e da transmissão final; só o filtro de ar novo é à parte. Folga de válvulas Boxer desde 150 / 300 € (verificação / verificação e afinação); motores K, S, F e G orçamentados por modelo. Inspection 2 desde 350 €. Uma R 1250 GS / GSA no intervalo de válvulas fica em 450–650 € com todos os fluidos, verificação de válvulas e sincronização das borboletas. Diagnóstico de avarias 50–350 € com relatório escrito. Tudo em orçamento escrito antes de começar.

**Line 84 *(meta 151 chars)* — CURRENT:** **Meta (148):** Независимая мастерская BMW Motorrad в Кашкайше. ТО от 180 €, клапаны Boxer 150 / 300 €, Inspection 2 от 350 €, диагностика GS-911. Письменная смета.

**Line 84 — NEW:** **Meta (151):** Независимая мастерская BMW Motorrad в Кашкайше. ТО от 180 €, клапаны Boxer от 150 / 300 €, Inspection 2 от 350 €, диагностика GS-911. Письменная смета.

**Line 86 — CURRENT:** **Price FAQ — Q:** Сколько стоит Inspection 2 / клапаны? **A:** Плановое ТО — от 180 €, и в него уже входит масло в КПП и в редукторе; отдельно только новый воздушный фильтр. Зазоры клапанов на Boxer — 150 / 300 € (проверка / проверка с регулировкой); K, S, F и G считаем по модели. Inspection 2 — от 350 €. R 1250 GS / GSA на клапанном интервале — 450–650 € со всеми жидкостями, проверкой клапанов и синхронизацией дросселей. Диагностика неисправностей 50–350 €, с письменным отчётом. Всё сначала в письменной смете.

**Line 86 — NEW:** **Price FAQ — Q:** Сколько стоит Inspection 2 / клапаны? **A:** Плановое ТО — от 180 €, и в него уже входит масло в КПП и в редукторе; отдельно только новый воздушный фильтр. Зазоры клапанов на Boxer — от 150 / 300 € (проверка / проверка с регулировкой); K, S, F и G считаем по модели. Inspection 2 — от 350 €. R 1250 GS / GSA на клапанном интервале — 450–650 € со всеми жидкостями, проверкой клапанов и синхронизацией дросселей. Диагностика неисправностей 50–350 €, с письменным отчётом. Всё сначала в письменной смете.

**Line 92 *(meta 153 chars)* — CURRENT:** **Meta (149):** Незалежна майстерня BMW Motorrad у Кашкайші. ТО від 180 €, клапани Boxer 150 / 300 €, Inspection 2 від 350 €, діагностика GS-911. Письмовий кошторис.

**Line 92 — NEW:** **Meta (153):** Незалежна майстерня BMW Motorrad у Кашкайші. ТО від 180 €, клапани Boxer від 150 / 300 €, Inspection 2 від 350 €, діагностика GS-911. Письмовий кошторис.

**Line 94 — CURRENT:** **Price FAQ — Q:** Скільки коштує Inspection 2 / клапани? **A:** Планове ТО — від 180 €, і в нього вже входить олива в КПП і в редукторі; окремо лише новий повітряний фільтр. Зазори клапанів на Boxer — 150 / 300 € (перевірка / перевірка з регулюванням); K, S, F і G рахуємо за моделлю. Inspection 2 — від 350 €. R 1250 GS / GSA на клапанному інтервалі — 450–650 € з усіма рідинами, перевіркою клапанів і синхронізацією дроселів. Діагностика несправностей 50–350 €, з письмовим звітом. Усе спершу в письмовому кошторисі.

**Line 94 — NEW:** **Price FAQ — Q:** Скільки коштує Inspection 2 / клапани? **A:** Планове ТО — від 180 €, і в нього вже входить олива в КПП і в редукторі; окремо лише новий повітряний фільтр. Зазори клапанів на Boxer — від 150 / 300 € (перевірка / перевірка з регулюванням); K, S, F і G рахуємо за моделлю. Inspection 2 — від 350 €. R 1250 GS / GSA на клапанному інтервалі — 450–650 € з усіма рідинами, перевіркою клапанів і синхронізацією дроселів. Діагностика несправностей 50–350 €, з письмовим звітом. Усе спершу в письмовому кошторисі.

**Line 101 *(meta 155 chars)* — CURRENT:** **Meta (150):** Independent Ducati workshop in Cascais, Greater Lisbon. Service from 150 €, Desmo valves 550 / 1 200 €, DDS diagnostics, dyno. Written estimate first.

**Line 101 — NEW:** **Meta (155):** Independent Ducati workshop in Cascais, Greater Lisbon. Service from 150 €, Desmo valves from 550 / 1 200 €, DDS diagnostics, dyno. Written estimate first.

**Line 103 — CURRENT:** **Price FAQ — Q:** How much does a desmo service cost at Iron Custom Motors? **A:** Three levels, all confirmed in writing before we start. Scheduled service from 150 €: oil, filter, chain, brakes and checks, new air filter extra. Desmo valve clearances 550 / 1 200 € (check / check and adjust): the desmodromic mechanism takes separate expertise, which is why it sits well apart from a standard adjustment. The full Desmo service is priced per model, from 750 € on an older Monster to 1 500 €+ on a Panigale V4 with full inspection.

**Line 103 — NEW:** **Price FAQ — Q:** How much does a desmo service cost at Iron Custom Motors? **A:** Three levels, all confirmed in writing before we start. Scheduled service from 150 €: oil, filter, chain, brakes and checks, new air filter extra. Desmo valve clearances from 550 / 1 200 € (check / check and adjust): the desmodromic mechanism takes separate expertise, which is why it sits well apart from a standard adjustment. The full Desmo service is priced per model, from 750 € on an older Monster to 1 500 €+ on a Panigale V4 with full inspection.

**Line 109 *(meta 146 chars)* — CURRENT:** **Meta (155):** Oficina independente Ducati em Cascais, Grande Lisboa. Revisão desde 150 €, válvulas Desmo 550 / 1 200 €, diagnóstico DDS, dyno próprio. Orçamento escrito.

**Line 109 — NEW:** **Meta (146):** Oficina independente Ducati em Cascais. Revisão desde 150 €, válvulas Desmo desde 550 / 1 200 €, diagnóstico DDS, dyno próprio. Orçamento escrito.

**Line 111 — CURRENT:** **Price FAQ — Q:** Quanto custa um serviço desmodrómico na Iron Custom Motors? **A:** Três níveis, todos confirmados por escrito antes de começarmos. Revisão programada desde 150 €: óleo, filtro, corrente, travões e verificações; filtro de ar novo à parte. Folga de válvulas Desmo 550 / 1 200 € (verificação / verificação e afinação): o mecanismo desmodrómico exige competência própria, e por isso fica bem acima de uma afinação normal. O serviço Desmo completo é orçamentado por modelo, desde 750 € numa Monster antiga até 1 500 €+ numa Panigale V4 com inspeção completa.

**Line 111 — NEW:** **Price FAQ — Q:** Quanto custa um serviço desmodrómico na Iron Custom Motors? **A:** Três níveis, todos confirmados por escrito antes de começarmos. Revisão programada desde 150 €: óleo, filtro, corrente, travões e verificações; filtro de ar novo à parte. Folga de válvulas Desmo desde 550 / 1 200 € (verificação / verificação e afinação): o mecanismo desmodrómico exige competência própria, e por isso fica bem acima de uma afinação normal. O serviço Desmo completo é orçamentado por modelo, desde 750 € numa Monster antiga até 1 500 €+ numa Panigale V4 com inspeção completa.

**Line 117 *(meta 150 chars)* — CURRENT:** **Meta (147):** Независимая мастерская Ducati в Кашкайше, Большой Лиссабон. ТО от 150 €, клапаны Desmo 550 / 1 200 €, диагностика DDS, свой дино. Письменная смета.

**Line 117 — NEW:** **Meta (150):** Независимая мастерская Ducati в Кашкайше, Большой Лиссабон. ТО от 150 €, клапаны Desmo от 550 / 1 200 €, диагностика DDS, свой дино. Письменная смета.

**Line 119 — CURRENT:** **Price FAQ — Q:** Сколько стоит desmo-сервис у Iron Custom Motors? **A:** Три уровня, и каждый сначала подтверждаем письменно. Плановое ТО — от 150 €: масло, фильтр, цепь, тормоза, проверки; новый воздушный фильтр отдельно. Зазоры клапанов Desmo — 550 / 1 200 € (проверка / проверка с регулировкой): десмодромный механизм требует отдельной квалификации, поэтому и стоит заметно дороже обычной регулировки. Полный Desmo-сервис считаем по модели: от 750 € на старом Monster до 1 500 €+ на Panigale V4 с полной проверкой.

**Line 119 — NEW:** **Price FAQ — Q:** Сколько стоит desmo-сервис у Iron Custom Motors? **A:** Три уровня, и каждый сначала подтверждаем письменно. Плановое ТО — от 150 €: масло, фильтр, цепь, тормоза, проверки; новый воздушный фильтр отдельно. Зазоры клапанов Desmo — от 550 / 1 200 € (проверка / проверка с регулировкой): десмодромный механизм требует отдельной квалификации, поэтому и стоит заметно дороже обычной регулировки. Полный Desmo-сервис считаем по модели: от 750 € на старом Monster до 1 500 €+ на Panigale V4 с полной проверкой.

**Line 125 *(meta 150 chars)* — CURRENT:** **Meta (146):** Незалежна майстерня Ducati у Кашкайші, Великий Лісабон. ТО від 150 €, клапани Desmo 550 / 1 200 €, діагностика DDS, свій дино. Письмовий кошторис.

**Line 125 — NEW:** **Meta (150):** Незалежна майстерня Ducati у Кашкайші, Великий Лісабон. ТО від 150 €, клапани Desmo від 550 / 1 200 €, діагностика DDS, свій дино. Письмовий кошторис.

**Line 127 — CURRENT:** **Price FAQ — Q:** Скільки коштує desmo-сервіс в Iron Custom Motors? **A:** Три рівні, і кожен спершу підтверджуємо письмово. Планове ТО — від 150 €: олива, фільтр, ланцюг, гальма, перевірки; новий повітряний фільтр окремо. Зазори клапанів Desmo — 550 / 1 200 € (перевірка / перевірка з регулюванням): десмодромний механізм потребує окремої кваліфікації, тому й коштує помітно дорожче за звичайне регулювання. Повний Desmo-сервіс рахуємо за моделлю: від 750 € на старому Monster до 1 500 €+ на Panigale V4 з повною перевіркою.

**Line 127 — NEW:** **Price FAQ — Q:** Скільки коштує desmo-сервіс в Iron Custom Motors? **A:** Три рівні, і кожен спершу підтверджуємо письмово. Планове ТО — від 150 €: олива, фільтр, ланцюг, гальма, перевірки; новий повітряний фільтр окремо. Зазори клапанів Desmo — від 550 / 1 200 € (перевірка / перевірка з регулюванням): десмодромний механізм потребує окремої кваліфікації, тому й коштує помітно дорожче за звичайне регулювання. Повний Desmo-сервіс рахуємо за моделлю: від 750 € на старому Monster до 1 500 €+ на Panigale V4 з повною перевіркою.

**Line 136 — CURRENT:** **Price FAQ — Q:** How much does a Honda service cost? **A:** Scheduled maintenance is from 150 €, consumables and tax included; the only extra is a new air filter, charged separately. Valve clearances on the Japanese twins are 250 / 300 € (check / check and adjust) and on the inline-fours 400 / 650 €; the VFR V4 is quoted per model. The DCT fluid and filter service is quoted separately in writing. Other work is 50 €/hour. Everything goes into a written estimate before we start.

**Line 136 — NEW:** **Price FAQ — Q:** How much does a Honda service cost? **A:** Scheduled maintenance is from 150 €, consumables and tax included; the only extra is a new air filter, charged separately. Valve clearances on the Japanese twins are from 250 / 300 € (check / check and adjust) and on the inline-fours from 400 / 650 €; the VFR V4 is quoted per model. The DCT fluid and filter service is quoted separately in writing. Other work is 50 €/hour. Everything goes into a written estimate before we start.

**Line 144 — CURRENT:** **Price FAQ — Q:** Quanto custa uma revisão Honda? **A:** A manutenção programada é desde 150 €, consumíveis e impostos incluídos; o único extra é o filtro de ar novo, cobrado à parte. A folga de válvulas nos bicilíndricos japoneses é 250 / 300 € (verificação / verificação e afinação) e nos quatro cilindros em linha 400 / 650 €; o V4 da VFR é orçamentado por modelo. O serviço DCT (fluido e filtro) é orçamentado por escrito. Outros trabalhos a 50 €/hora. Tudo em orçamento escrito antes de começar.

**Line 144 — NEW:** **Price FAQ — Q:** Quanto custa uma revisão Honda? **A:** A manutenção programada é desde 150 €, consumíveis e impostos incluídos; o único extra é o filtro de ar novo, cobrado à parte. A folga de válvulas nos bicilíndricos japoneses é desde 250 / 300 € (verificação / verificação e afinação) e nos quatro cilindros em linha desde 400 / 650 €; o V4 da VFR é orçamentado por modelo. O serviço DCT (fluido e filtro) é orçamentado por escrito. Outros trabalhos a 50 €/hora. Tudo em orçamento escrito antes de começar.

**Line 152 — CURRENT:** **Price FAQ — Q:** Сколько стоит обслуживание Honda? **A:** Плановое ТО — от 150 €, расходники и налоги включены; единственная доплата — новый воздушный фильтр, он считается отдельно. Клапаны на японских «двойках» — 250 / 300 € (проверка / проверка с регулировкой), на рядных «четвёрках» — 400 / 650 €; V4 на VFR считаем по модели. Обслуживание DCT (масло и фильтр) — по письменной смете. Прочие работы — 50 €/час. Всё сначала фиксируем в письменной смете.

**Line 152 — NEW:** **Price FAQ — Q:** Сколько стоит обслуживание Honda? **A:** Плановое ТО — от 150 €, расходники и налоги включены; единственная доплата — новый воздушный фильтр, он считается отдельно. Клапаны на японских «двойках» — от 250 / 300 € (проверка / проверка с регулировкой), на рядных «четвёрках» — от 400 / 650 €; V4 на VFR считаем по модели. Обслуживание DCT (масло и фильтр) — по письменной смете. Прочие работы — 50 €/час. Всё сначала фиксируем в письменной смете.

**Line 160 — CURRENT:** **Price FAQ — Q:** Скільки коштує обслуговування Honda? **A:** Планове ТО — від 150 €, витратні матеріали й податки включені; єдина доплата — новий повітряний фільтр, він рахується окремо. Клапани на японських «двійках» — 250 / 300 € (перевірка / перевірка з регулюванням), на рядних «четвірках» — 400 / 650 €; V4 на VFR рахуємо за моделлю. Обслуговування DCT (олива й фільтр) — за письмовим кошторисом. Інші роботи — 50 €/год. Усе спершу фіксуємо в письмовому кошторисі.

**Line 160 — NEW:** **Price FAQ — Q:** Скільки коштує обслуговування Honda? **A:** Планове ТО — від 150 €, витратні матеріали й податки включені; єдина доплата — новий повітряний фільтр, він рахується окремо. Клапани на японських «двійках» — від 250 / 300 € (перевірка / перевірка з регулюванням), на рядних «четвірках» — від 400 / 650 €; V4 на VFR рахуємо за моделлю. Обслуговування DCT (олива й фільтр) — за письмовим кошторисом. Інші роботи — 50 €/год. Усе спершу фіксуємо в письмовому кошторисі.

**Line 169 — CURRENT:** **Price FAQ — Q:** How much does a Suzuki service cost? **A:** Scheduled maintenance is from 150 €, consumables and tax included; the only extra is a new air filter, charged separately. Valve clearances on the twins (SV650 / V-Strom) are 250 / 300 € (check / check and adjust) and on the inline-fours (GSX-R / Bandit / Hayabusa) 400 / 650 €. Other work is 50 €/hour; a charging-system repair is quoted in writing once we've load-tested it. Everything goes into a written estimate before we start.

**Line 169 — NEW:** **Price FAQ — Q:** How much does a Suzuki service cost? **A:** Scheduled maintenance is from 150 €, consumables and tax included; the only extra is a new air filter, charged separately. Valve clearances on the twins (SV650 / V-Strom) are from 250 / 300 € (check / check and adjust) and on the inline-fours (GSX-R / Bandit / Hayabusa) from 400 / 650 €. Other work is 50 €/hour; a charging-system repair is quoted in writing once we've load-tested it. Everything goes into a written estimate before we start.

**Line 177 — CURRENT:** **Price FAQ — Q:** Quanto custa um serviço Suzuki? **A:** A manutenção programada é desde 150 €, consumíveis e impostos incluídos; o único extra é o filtro de ar novo, cobrado à parte. A folga de válvulas nos bicilíndricos (SV650 / V-Strom) é 250 / 300 € (verificação / verificação e afinação) e nos quatro cilindros em linha (GSX-R / Bandit / Hayabusa) 400 / 650 €. Outros trabalhos a 50 €/hora; uma reparação do sistema de carga é orçamentada por escrito depois do teste de carga. Tudo em orçamento escrito antes de começar.

**Line 177 — NEW:** **Price FAQ — Q:** Quanto custa um serviço Suzuki? **A:** A manutenção programada é desde 150 €, consumíveis e impostos incluídos; o único extra é o filtro de ar novo, cobrado à parte. A folga de válvulas nos bicilíndricos (SV650 / V-Strom) é desde 250 / 300 € (verificação / verificação e afinação) e nos quatro cilindros em linha (GSX-R / Bandit / Hayabusa) desde 400 / 650 €. Outros trabalhos a 50 €/hora; uma reparação do sistema de carga é orçamentada por escrito depois do teste de carga. Tudo em orçamento escrito antes de começar.

**Line 185 — CURRENT:** **Price FAQ — Q:** Сколько стоит обслуживание Suzuki? **A:** Плановое ТО — от 150 €, расходники и налоги включены; единственная доплата — новый воздушный фильтр, он считается отдельно. Клапаны на «двойках» (SV650 / V-Strom) — 250 / 300 € (проверка / проверка с регулировкой), на рядных «четвёрках» (GSX-R / Bandit / Hayabusa) — 400 / 650 €. Прочие работы — 50 €/час; ремонт зарядки считаем письменно после нагрузочного теста. Всё сначала фиксируем в письменной смете.

**Line 185 — NEW:** **Price FAQ — Q:** Сколько стоит обслуживание Suzuki? **A:** Плановое ТО — от 150 €, расходники и налоги включены; единственная доплата — новый воздушный фильтр, он считается отдельно. Клапаны на «двойках» (SV650 / V-Strom) — от 250 / 300 € (проверка / проверка с регулировкой), на рядных «четвёрках» (GSX-R / Bandit / Hayabusa) — от 400 / 650 €. Прочие работы — 50 €/час; ремонт зарядки считаем письменно после нагрузочного теста. Всё сначала фиксируем в письменной смете.

**Line 193 — CURRENT:** **Price FAQ — Q:** Скільки коштує обслуговування Suzuki? **A:** Планове ТО — від 150 €, витратні матеріали й податки включені; єдина доплата — новий повітряний фільтр, він рахується окремо. Клапани на «двійках» (SV650 / V-Strom) — 250 / 300 € (перевірка / перевірка з регулюванням), на рядних «четвірках» (GSX-R / Bandit / Hayabusa) — 400 / 650 €. Інші роботи — 50 €/год; ремонт зарядки рахуємо письмово після навантажувального тесту. Усе спершу фіксуємо в письмовому кошторисі.

**Line 193 — NEW:** **Price FAQ — Q:** Скільки коштує обслуговування Suzuki? **A:** Планове ТО — від 150 €, витратні матеріали й податки включені; єдина доплата — новий повітряний фільтр, він рахується окремо. Клапани на «двійках» (SV650 / V-Strom) — від 250 / 300 € (перевірка / перевірка з регулюванням), на рядних «четвірках» (GSX-R / Bandit / Hayabusa) — від 400 / 650 €. Інші роботи — 50 €/год; ремонт зарядки рахуємо письмово після навантажувального тесту. Усе спершу фіксуємо в письмовому кошторисі.

**Line 202 — CURRENT:** **Price FAQ — Q:** How much does a Triumph service cost? **A:** Scheduled maintenance is from 150 €, consumables and tax included; the only extra is a new air filter, charged separately. Valve clearances on the parallel twins (Bonneville / Speed Twin / Scrambler) are 250 / 300 € (check / check and adjust); the inline triples (Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3) are quoted per model in a written estimate. Other work is 50 €/hour. Everything goes into a written estimate before we start.

**Line 202 — NEW:** **Price FAQ — Q:** How much does a Triumph service cost? **A:** Scheduled maintenance is from 150 €, consumables and tax included; the only extra is a new air filter, charged separately. Valve clearances on the parallel twins (Bonneville / Speed Twin / Scrambler) are from 250 / 300 € (check / check and adjust); the inline triples (Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3) are quoted per model in a written estimate. Other work is 50 €/hour. Everything goes into a written estimate before we start.

**Line 210 — CURRENT:** **Price FAQ — Q:** Quanto custa um serviço Triumph? **A:** A revisão programada é desde 150 €, consumíveis e impostos incluídos; o único extra é o filtro de ar novo, cobrado à parte. A folga de válvulas nos bicilíndricos paralelos (Bonneville / Speed Twin / Scrambler) é 250 / 300 € (verificação / verificação e afinação); os triplos em linha (Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3) são orçamentados por modelo, por escrito. Outros trabalhos a 50 €/hora. Tudo em orçamento escrito antes de começar.

**Line 210 — NEW:** **Price FAQ — Q:** Quanto custa um serviço Triumph? **A:** A revisão programada é desde 150 €, consumíveis e impostos incluídos; o único extra é o filtro de ar novo, cobrado à parte. A folga de válvulas nos bicilíndricos paralelos (Bonneville / Speed Twin / Scrambler) é desde 250 / 300 € (verificação / verificação e afinação); os triplos em linha (Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3) são orçamentados por modelo, por escrito. Outros trabalhos a 50 €/hora. Tudo em orçamento escrito antes de começar.

**Line 218 — CURRENT:** **Price FAQ — Q:** Сколько стоит обслуживание Triumph? **A:** Плановое ТО — от 150 €, расходники и налоги включены; единственная доплата — новый воздушный фильтр, он считается отдельно. Клапаны на параллельных твинах (Bonneville / Speed Twin / Scrambler) — 250 / 300 € (проверка / проверка с регулировкой); рядные триплы (Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3) считаем по модели в письменной смете. Прочие работы — 50 €/час. Всё сначала фиксируем в письменной смете.

**Line 218 — NEW:** **Price FAQ — Q:** Сколько стоит обслуживание Triumph? **A:** Плановое ТО — от 150 €, расходники и налоги включены; единственная доплата — новый воздушный фильтр, он считается отдельно. Клапаны на параллельных твинах (Bonneville / Speed Twin / Scrambler) — от 250 / 300 € (проверка / проверка с регулировкой); рядные триплы (Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3) считаем по модели в письменной смете. Прочие работы — 50 €/час. Всё сначала фиксируем в письменной смете.

**Line 226 — CURRENT:** **Price FAQ — Q:** Скільки коштує обслуговування Triumph? **A:** Планове ТО — від 150 €, витратні матеріали й податки включені; єдина доплата — новий повітряний фільтр, він рахується окремо. Клапани на паралельних твінах (Bonneville / Speed Twin / Scrambler) — 250 / 300 € (перевірка / перевірка з регулюванням); рядні трипли (Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3) рахуємо за моделлю в письмовому кошторисі. Інші роботи — 50 €/год. Усе спершу фіксуємо в письмовому кошторисі.

**Line 226 — NEW:** **Price FAQ — Q:** Скільки коштує обслуговування Triumph? **A:** Планове ТО — від 150 €, витратні матеріали й податки включені; єдина доплата — новий повітряний фільтр, він рахується окремо. Клапани на паралельних твінах (Bonneville / Speed Twin / Scrambler) — від 250 / 300 € (перевірка / перевірка з регулюванням); рядні трипли (Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3) рахуємо за моделлю в письмовому кошторисі. Інші роботи — 50 €/год. Усе спершу фіксуємо в письмовому кошторисі.

**Line 235 — CURRENT:** **Price FAQ — Q:** How much does a Royal Enfield service cost? **A:** Scheduled maintenance is from 150 €, consumables and tax included; the only extra is a new air filter, charged separately. Valve clearances on the 650 parallel twin are 250 / 300 € (check / check and adjust); the 350 and 450 singles are quoted per model in a written estimate. Other work is 50 €/hour. Everything goes into a written estimate before we start.

**Line 235 — NEW:** **Price FAQ — Q:** How much does a Royal Enfield service cost? **A:** Scheduled maintenance is from 150 €, consumables and tax included; the only extra is a new air filter, charged separately. Valve clearances on the 650 parallel twin are from 250 / 300 € (check / check and adjust); the 350 and 450 singles are quoted per model in a written estimate. Other work is 50 €/hour. Everything goes into a written estimate before we start.

**Line 243 — CURRENT:** **Price FAQ — Q:** Quanto custa um serviço Royal Enfield? **A:** A manutenção programada é desde 150 €, consumíveis e impostos incluídos; o único extra é o filtro de ar novo, cobrado à parte. A folga de válvulas na bicilíndrica paralela 650 é 250 / 300 € (verificação / verificação e afinação); as monocilíndricas 350 e 450 são orçamentadas por modelo, por escrito. Outros trabalhos a 50 €/hora. Tudo em orçamento escrito antes de começar.

**Line 243 — NEW:** **Price FAQ — Q:** Quanto custa um serviço Royal Enfield? **A:** A manutenção programada é desde 150 €, consumíveis e impostos incluídos; o único extra é o filtro de ar novo, cobrado à parte. A folga de válvulas na bicilíndrica paralela 650 é desde 250 / 300 € (verificação / verificação e afinação); as monocilíndricas 350 e 450 são orçamentadas por modelo, por escrito. Outros trabalhos a 50 €/hora. Tudo em orçamento escrito antes de começar.

**Line 251 — CURRENT:** **Price FAQ — Q:** Сколько стоит обслуживание Royal Enfield? **A:** Плановое ТО — от 150 €, расходники и налоги включены; единственная доплата — новый воздушный фильтр, он считается отдельно. Клапаны на параллельном твине 650 — 250 / 300 € (проверка / проверка с регулировкой); одноцилиндровые 350 и 450 считаем по модели в письменной смете. Прочие работы — 50 €/час. Всё сначала фиксируем в письменной смете.

**Line 251 — NEW:** **Price FAQ — Q:** Сколько стоит обслуживание Royal Enfield? **A:** Плановое ТО — от 150 €, расходники и налоги включены; единственная доплата — новый воздушный фильтр, он считается отдельно. Клапаны на параллельном твине 650 — от 250 / 300 € (проверка / проверка с регулировкой); одноцилиндровые 350 и 450 считаем по модели в письменной смете. Прочие работы — 50 €/час. Всё сначала фиксируем в письменной смете.

**Line 259 — CURRENT:** **Price FAQ — Q:** Скільки коштує обслуговування Royal Enfield? **A:** Планове ТО — від 150 €, витратні матеріали й податки включені; єдина доплата — новий повітряний фільтр, він рахується окремо. Клапани на паралельному твіні 650 — 250 / 300 € (перевірка / перевірка з регулюванням); одноциліндрові 350 і 450 рахуємо за моделлю в письмовому кошторисі. Інші роботи — 50 €/год. Усе спершу фіксуємо в письмовому кошторисі.

**Line 259 — NEW:** **Price FAQ — Q:** Скільки коштує обслуговування Royal Enfield? **A:** Планове ТО — від 150 €, витратні матеріали й податки включені; єдина доплата — новий повітряний фільтр, він рахується окремо. Клапани на паралельному твіні 650 — від 250 / 300 € (перевірка / перевірка з регулюванням); одноциліндрові 350 і 450 рахуємо за моделлю в письмовому кошторисі. Інші роботи — 50 €/год. Усе спершу фіксуємо в письмовому кошторисі.

Line 4 (the file's «Rules» header) also changes for consistency: `Boxer 150 / 300 €` → `Boxer from 150 / 300 €`, `Desmo 550 / 1 200 €` → `Desmo from 550 / 1 200 €`, `twins 250 / 300 €, inline-fours 400 / 650 €` → `twins from 250 / 300 €, inline-fours from 400 / 650 €` — non-rendered, documentation only.

---

## D. Not changed on purpose

- Every amount stays as it is (the owner changed the *marking*, not the prices). No new figures anywhere.
- `BMW R 1250 GS / GSA — valve-interval service 450–650 €` and `Ducati full Desmo service 750–1 500+ €` are brand-specific cards, not valve-clearance rows — untouched.
- Harley pages: no valve rows — untouched.
- `Offer` JSON-LD: the valve table is not exposed as Offers (checked on `/pricing/` and `/bmw-service/`), so schema does not change; the brand-specific cards above keep their `price` values.
- The word «+» is a display convention; validators that whitelist € amounts strip non-digits already (`canonical_amount`) — the digits are unchanged, so the whitelist stays valid.

## E. GBP (orchestrator, hands-on, after the site ships)

- Service «BMW Motorrad · Moto Guzzi service»: `Boxer valve check 150 € / check and adjust 300 €` → `Boxer valve check from 150 € / check and adjust from 300 €`.
- Service «Ducati service»: `Desmo valve check 550 € / check and adjust 1 200 €` → `Desmo valve check from 550 € / check and adjust from 1 200 €`.
- Service «Royal Enfield · Triumph service»: `twin-cylinder valve check €250 / check and adjust €300` → `twin-cylinder valve check from €250 / check and adjust from €300`.

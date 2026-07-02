"""
Content and registry for brand-specific service landing pages.

Add future motorcycle brands here first. The build scripts import this registry
to keep the brand dropdown, footer links, service hub, sitemap, localized links,
SEO validation and page rendering in sync.

Used by build_brand_pages.py and the site-wide build helpers.
"""

LANGS = ("en", "ru", "uk", "pt")
BRAND_ORDER = ("harley-service", "bmw-service", "ducati-service", "suzuki-service", "honda-service", "royal-enfield-service", "triumph-service")

# ============================================================
# Per-brand registry
# ============================================================
BRAND_CONFIG = {
    "harley-service": {
        "prefix": "hd",
        "name": "Harley-Davidson",
        "nav_key": "nav.brandHarley",
        "hero": "/photos/harley-service-main-1600.jpg",
        "related_links": [
            ("services.s1.title", "/motorcycle-service/", "Motorcycle service &amp; repair"),
            ("services.s4.title", "/custom/", "Custom &amp; special projects"),
            ("nav.projects", "/projects/", "Projects"),
            ("nav.pricing", "/pricing/", "Pricing"),
        ],
    },
    "bmw-service": {
        "prefix": "bmw",
        "name": "BMW Motorrad",
        "nav_key": "nav.brandBmw",
        "hero": "/photos/bmw-service-main-1600.jpg",
        "related_links": [
            ("services.s1.title", "/motorcycle-service/", "Motorcycle service &amp; repair"),
            ("services.s2.title", "/parts/", "Parts &amp; consumables"),
            ("nav.pricing", "/pricing/", "Pricing"),
            ("nav.community", "/community/", "Community"),
        ],
    },
    "ducati-service": {
        "prefix": "duc",
        "name": "Ducati",
        "nav_key": "nav.brandDucati",
        "hero": "/photos/ducati-service-main-1600.jpg",
        "related_links": [
            ("services.s1.title", "/motorcycle-service/", "Motorcycle service &amp; repair"),
            ("services.s3.title", "/upgrades-tuning/", "Upgrades &amp; tuning"),
            ("services.s2.title", "/parts/", "Parts &amp; consumables"),
            ("nav.pricing", "/pricing/", "Pricing"),
        ],
    },
    "suzuki-service": {
        "prefix": "suz",
        "name": "Suzuki",
        "nav_key": "nav.brandSuzuki",
        "hero": "/photos/suzuki-service-main-1600.jpg",
        "related_links": [
            ("services.s1.title", "/motorcycle-service/", "Motorcycle service &amp; repair"),
            ("services.s3.title", "/upgrades-tuning/", "Upgrades &amp; tuning"),
            ("services.s2.title", "/parts/", "Parts &amp; consumables"),
            ("nav.pricing", "/pricing/", "Pricing"),
            ("services.s4.title", "/custom/", "Custom &amp; special projects"),
            ("nav.contact", "/contact/", "Contact"),
            ("nav.faq", "/faq/", "FAQ"),
        ],
    },
    "honda-service": {
        "prefix": "hon",
        "name": "Honda",
        "nav_key": "nav.brandHonda",
        "hero": "/photos/honda-service-main-1600.jpg",
        "related_links": [
            ("services.s1.title", "/motorcycle-service/", "Motorcycle service &amp; repair"),
            ("services.s3.title", "/upgrades-tuning/", "Upgrades &amp; tuning"),
            ("services.s2.title", "/parts/", "Parts &amp; consumables"),
            ("nav.pricing", "/pricing/", "Pricing"),
            ("services.s4.title", "/custom/", "Custom &amp; special projects"),
            ("nav.contact", "/contact/", "Contact"),
            ("nav.faq", "/faq/", "FAQ"),
        ],
    },
    "royal-enfield-service": {
        "prefix": "ren",
        "name": "Royal Enfield",
        "nav_key": "nav.brandRoyalEnfield",
        "hero": "/photos/royal-enfield-service-main-1600.jpg",
        "related_links": [
            ("services.s1.title", "/motorcycle-service/", "Motorcycle service &amp; repair"),
            ("services.s2.title", "/parts/", "Parts &amp; consumables"),
            ("services.s4.title", "/custom/", "Custom &amp; special projects"),
            ("nav.pricing", "/pricing/", "Pricing"),
            ("services.s3.title", "/upgrades-tuning/", "Upgrades &amp; tuning"),
            ("nav.contact", "/contact/", "Contact"),
            ("nav.faq", "/faq/", "FAQ"),
        ],
    },
    "triumph-service": {
        "prefix": "tri",
        "name": "Triumph",
        "nav_key": "nav.brandTriumph",
        "hero": "/photos/triumph-service-main-1600.jpg",
        "related_links": [
            ("services.s1.title", "/motorcycle-service/", "Motorcycle service &amp; repair"),
            ("services.s3.title", "/upgrades-tuning/", "Upgrades &amp; tuning"),
            ("services.s4.title", "/custom/", "Custom &amp; special projects"),
            ("services.s2.title", "/parts/", "Parts &amp; consumables"),
            ("nav.pricing", "/pricing/", "Pricing"),
            ("nav.contact", "/contact/", "Contact"),
            ("nav.faq", "/faq/", "FAQ"),
        ],
    },


}

BRAND_BG = {slug: config["hero"] for slug, config in BRAND_CONFIG.items()}
BRAND_PREFIX = {slug: config["prefix"] for slug, config in BRAND_CONFIG.items()}
BRAND_NAME = {slug: config["name"] for slug, config in BRAND_CONFIG.items()}
BRAND_NAV_KEYS = {slug: config["nav_key"] for slug, config in BRAND_CONFIG.items()}
COMMON_BRAND_RELATED_LINKS = (
    ("seo.relatedService", "/motorcycle-service/", "Service and repair"),
    ("seo.relatedUpgrades", "/upgrades-tuning/", "Upgrades and tuning"),
    ("seo.relatedParts", "/parts/", "Parts and consumables"),
    ("seo.relatedCustom", "/custom/", "Custom and special projects"),
    ("seo.relatedTyres", "/motorcycle-tyre-service/", "Tyre service"),
    ("seo.relatedPricing", "/pricing/", "Pricing"),
)
BRAND_RELATED_LINKS = {slug: COMMON_BRAND_RELATED_LINKS for slug in BRAND_CONFIG}

# ============================================================
# Per-brand head meta (title + description) per language
# ============================================================
BRAND_HEAD = {
    "bmw-service": {
        "en": {
            "title": "BMW Motorrad Service in Cascais & Lisbon | Iron Custom Motors",
            "description": "Independent BMW Motorrad workshop in Cascais. Diagnostics, scheduled service, valve clearance, final drive, ABS and tuning for R, K, S, F, G-series. BMW Customizing Champions 2023.",
        },
        "ru": {
            "title": "Сервис BMW Motorrad в Кашкайше и Лиссабоне | Iron Custom Motors",
            "description": "Независимая мастерская BMW Motorrad в Кашкайше. Диагностика, плановое ТО, клапаны, главная передача, ABS и тюнинг для R, K, S, F, G-серий. Чемпионы BMW Customizing 2023.",
        },
        "uk": {
            "title": "Сервіс BMW Motorrad у Кашкайші та Лісабоні | Iron Custom Motors",
            "description": "Незалежна майстерня BMW Motorrad у Кашкайші. Діагностика, планове ТО, клапани, головна передача, ABS і тюнінг для R, K, S, F, G-серій. Чемпіони BMW Customizing 2023.",
        },
        "pt": {
            "title": "Serviço BMW Motorrad em Cascais e Lisboa | Iron Custom Motors",
            "description": "Oficina independente BMW Motorrad em Cascais. Diagnóstico, manutenção programada, válvulas, transmissão final, ABS e tuning para R, K, S, F, G. Campeões BMW Customizing 2023.",
        },
    },
    "harley-service": {
        "en": {
            "title": "Harley-Davidson Service in Cascais & Lisbon | Iron Custom Motors",
            "description": "Independent Harley-Davidson specialist in Cascais. Sportster, Softail, Touring, Pan America. Stage I/II/IV upgrades, dyno tuning, custom. AMD World Championship project pedigree.",
        },
        "ru": {
            "title": "Сервис Harley-Davidson в Кашкайше и Лиссабоне | Iron Custom Motors",
            "description": "Независимый специалист по Harley-Davidson в Кашкайше. Sportster, Softail, Touring, Pan America. Stage I/II/IV, дино-тюнинг, кастом. Призёры AMD World Championship.",
        },
        "uk": {
            "title": "Сервіс Harley-Davidson у Кашкайші та Лісабоні | Iron Custom Motors",
            "description": "Незалежний спеціаліст з Harley-Davidson у Кашкайші. Sportster, Softail, Touring, Pan America. Stage I/II/IV, дино-тюнінг, кастом. Призери AMD World Championship.",
        },
        "pt": {
            "title": "Serviço Harley-Davidson em Cascais e Lisboa | Iron Custom Motors",
            "description": "Especialista independente em Harley-Davidson em Cascais. Sportster, Softail, Touring, Pan America. Upgrades Stage I/II/IV, dyno tuning, custom. Premiados AMD World Championship.",
        },
    },
    "ducati-service": {
        "en": {
            "title": "Ducati Service in Cascais & Lisbon — Desmo, Panigale, Multistrada | Iron Custom Motors",
            "description": "Independent Ducati workshop in Cascais. Desmodromic service, Panigale, Multistrada, Monster, Scrambler, Streetfighter. Transparent pricing, real specialist tooling, dyno-tuned exhausts.",
        },
        "ru": {
            "title": "Сервис Ducati в Кашкайше и Лиссабоне — Desmo, Panigale, Multistrada | Iron Custom Motors",
            "description": "Независимая мастерская Ducati в Кашкайше. Desmo-сервис, Panigale, Multistrada, Monster, Scrambler, Streetfighter. Прозрачные цены, специализированный инструмент, динo-тюнинг выхлопа.",
        },
        "uk": {
            "title": "Сервіс Ducati у Кашкайші та Лісабоні — Desmo, Panigale, Multistrada | Iron Custom Motors",
            "description": "Незалежна майстерня Ducati у Кашкайші. Desmo-сервіс, Panigale, Multistrada, Monster, Scrambler, Streetfighter. Прозорі ціни, спеціалізований інструмент, дино-тюнінг вихлопу.",
        },
        "pt": {
            "title": "Serviço Ducati em Cascais e Lisboa — Desmo, Panigale, Multistrada | Iron Custom Motors",
            "description": "Oficina independente Ducati em Cascais. Serviço desmodromico, Panigale, Multistrada, Monster, Scrambler, Streetfighter. Preços transparentes, ferramenta especialista, dyno-tuning.",
        },
    },
    "suzuki-service": {"en": {"title": "Suzuki Service in Cascais & Lisbon | Iron Custom Motors", "description": "Independent Suzuki workshop in Cascais. SDS diagnostics, scheduled service, valve clearance, charging and suspension for GSX-R, GSX-S, V-Strom, SV650, Hayabusa."}, "pt": {"title": "Serviço Suzuki em Cascais e Lisboa | Iron Custom Motors", "description": "Oficina Suzuki independente em Cascais. Diagnóstico SDS, manutenção, folga de válvulas, carga e suspensão para GSX-R, GSX-S, V-Strom, SV650 e Hayabusa."}, "ru": {"title": "Сервис Suzuki в Кашкайше и Лиссабоне | Iron Custom Motors", "description": "Независимый сервис Suzuki в Кашкайше. Диагностика SDS, ТО, регулировка клапанов, ремонт зарядки и подвески — GSX-R, GSX-S, V-Strom, SV650, Hayabusa."}, "uk": {"title": "Сервіс Suzuki у Кашкайші та Лісабоні | Iron Custom Motors", "description": "Незалежний сервіс Suzuki у Кашкайші. Діагностика SDS, ТО, регулювання клапанів, ремонт зарядки та підвіски — GSX-R, GSX-S, V-Strom, SV650, Hayabusa."}},
    "honda-service": {
        "en": {
            "title": "Honda Motorcycle Service in Cascais & Lisbon | Iron Custom",
            "description": "Independent Honda motorcycle workshop in Cascais. MCS diagnostics, scheduled service, DCT service, valve clearance, tuning for Africa Twin, CB, CBR, Gold Wing.",
        },
        "pt": {
            "title": "Serviço Honda Mota em Cascais e Lisboa | Iron Custom",
            "description": "Oficina Honda independente em Cascais. Diagnóstico MCS, manutenção, serviço DCT, folga de válvulas e afinação para Africa Twin, CB, CBR, Gold Wing.",
        },
        "ru": {
            "title": "Сервис мотоциклов Honda в Кашкайше и Лиссабоне | Iron Custom",
            "description": "Независимая мастерская Honda в Кашкайше. Диагностика MCS, регламентное ТО, обслуживание DCT, регулировка клапанов, тюнинг Africa Twin, CB, CBR, Gold Wing.",
        },
        "uk": {
            "title": "Сервіс мотоциклів Honda у Кашкайші та Лісабоні | Iron Custom",
            "description": "Незалежна майстерня Honda у Кашкайші. Діагностика MCS, регламентне ТО, обслуговування DCT, регулювання клапанів, тюнінг Africa Twin, CB, CBR, Gold Wing.",
        },
    },
}

# ============================================================
# Per-brand inline I18N content (data-i18n keys for the body)
# Prefix: bmw.*  hd.*  duc.*  suz.*  hon.*
# ============================================================

PAGE_I18N = {}

# ====================================================================================
# BMW Motorrad
# ====================================================================================
PAGE_I18N["bmw-service"] = {
    "en": {
        "bmw.eyebrow": "BMW Motorrad · Cascais / Greater Lisbon",
        "bmw.h1": "BMW Motorrad service<br/>in <span class=\"accent\">Cascais.</span>",
        "bmw.sub": "Independent BMW workshop for R-, K-, S-, F- and G-series. Diagnostics, scheduled service, repair and tuning by the team that won the BMW Motorrad Customizing Championship 2023.",
        "bmw.breadHome": "Home",
        "bmw.h1Crumb": "BMW Motorrad service",
        "bmw.btnWA": "WhatsApp us",
        "bmw.btnSend": "Send a request",
        "bmw.heroAlt": "BMW Motorrad motorcycle service at Iron Custom Motors workshop in Cascais",

        "bmw.introEyebrow": "Why bring your BMW to us",
        "bmw.introTitle": "BMW-first expertise, <em>independent rates.</em>",
        "bmw.introP1": "Iron Custom Motors is an independent BMW Motorrad workshop in Cascais, run by the same team that took the BMW Motorrad Customizing Championship 2023 — BMW's own recognition for engineering and build quality. The bikes we win trophies with and the bike you drop off for a service get the same pair of hands and the same standard.",
        "bmw.introP2": "We work across the whole BMW Motorrad range — the boxer R-series, the parallel-twin F-series, the single-cylinder G-series, the inline-four S-series and the inline-six K-series. Every platform has its own habits and weak spots, and we know them because we have these bikes in the workshop week in, week out. This is BMW-first expertise, not a general shop that happens to take BMWs.",
        "bmw.introP3": "Independent also means no dealer mark-up, the freedom to fit OEM or quality aftermarket parts as the job actually calls for, and a straight conversation throughout. You get an estimate before we start and a written report when we hand the bike back.",
        "bmw.toolsEyebrow": "Specialist tooling",
        "bmw.toolsTitle": "BMW-specific <em>diagnostic and tools.</em>",
        "bmw.toolsLead": "BMW Motorrad asks for tools most independent workshops simply don't own — so we bought them. That's the line between a real BMW shop and a workshop that occasionally takes one in.",
        "bmw.t1t": "GS-911 diagnostic interface",
        "bmw.t1d": "Reads and clears BMW-specific fault codes, runs adaptive resets, and shows live sensor data and service indicators.",
        "bmw.t2t": "BMW ISTA / dealer-level diagnostics",
        "bmw.t2d": "Where it's needed, we run dealer-equivalent diagnostic procedures to reach the deeper system menus a generic scanner never sees.",
        "bmw.t3t": "Paralever and Telelever tooling",
        "bmw.t3d": "The proper pre-load and alignment tools for BMW's front and rear suspension geometry — not improvised substitutes.",
        "bmw.t4t": "ESA suspension service kit",
        "bmw.t4d": "Spring compressor and the correct replacement procedure for Electronic Suspension Adjustment (ESA) dampers.",
        "bmw.servicesEyebrow": "What we do on BMW",
        "bmw.servicesTitle": "Service. Repair. <em>Tune.</em>",
        "bmw.servicesLead": "From an Inspection 1 to a full ground-up rebuild of a vintage airhead — all of it done with BMW-specific knowledge and the right tooling.",
        "bmw.s1t": "Scheduled service (Inspection 1 / 2)",
        "bmw.s1d": "BMW interval service — oil, filter, fluids, brake check, final-drive inspection, plus valve clearance when the interval calls for it.",
        "bmw.s2t": "Valve clearance — boxer / parallel-twin / single",
        "bmw.s2d": "Done properly with feeler gauges and shim selection where the engine needs it. R-series boxer, F-series, G-series.",
        "bmw.s3t": "Final drive service",
        "bmw.s3d": "Gear oil change, swingarm bearing inspection and a Paralever pre-load check — the work that keeps a GS, RT or R-series final drive alive for the long haul.",
        "bmw.s4t": "ABS Pro / Integral ABS bleed",
        "bmw.s4d": "A full bleed of BMW's integrated ABS. A standard brake bleed won't move the fluid where it needs to go here — it takes the proper BMW procedure.",
        "bmw.s5t": "Boxer engine tune-up",
        "bmw.s5d": "Throttle-body sync, idle stabilisation, air-mass meter calibration and spark plug service — the boxer running as smooth as it should.",
        "bmw.s6t": "Suspension service",
        "bmw.s6d": "ESA, Telelever and Paralever maintenance — fork seal replacement, oil change, sag setup, rebound and compression tuning. While the wheels are off, we can also handle <a href=\"/motorcycle-tyre-service/\">tyre fitting and balancing</a> for wide BMW rubber and spoked GS rims, including tubeless-spoked and custom wheel setups.",
        "bmw.s7t": "Electrical diagnostics",
        "bmw.s7d": "Full fault-code reading and live data with the GS-911. Battery, charging, CAN-bus and accessory wiring repair.",
        "bmw.s8t": "Tuning and upgrades",
        "bmw.s8d": "Exhaust fitment with the matching ECU re-flash (Akrapovič, Wilbers, Öhlins), suspension upgrades, ergonomics, protection and touring kit.",
        "bmw.issuesEyebrow": "Typical issues we know",
        "bmw.issuesTitle": "BMW failure patterns, <em>solved before they bite.</em>",
        "bmw.issuesLead": "Years on these bikes mean we know their weak points by heart. We check the high-risk items up front, not after they let go on a tour.",
        "bmw.i1t": "Boxer valve clearance drift",
        "bmw.i1d": "Common on the R 1200 and earlier — we know when the clearances genuinely need measuring versus when the dealer is just ticking a box.",
        "bmw.i2t": "Final drive bearing wear",
        "bmw.i2d": "Early symptoms on the R 1200/1250 GS and RT — caught with a proper play check before the bevel box gives up.",
        "bmw.i3t": "ABS / brake assist faults",
        "bmw.i3d": "Servo-motor and pump faults on older R-series. We diagnose and repair them where a dealer would swap the whole module.",
        "bmw.i4t": "Final-drive splines & paralever joints",
        "bmw.i4d": "We strip, clean, regrease and renew where worn — the service interval most dealers quietly skip.",
        "bmw.i5t": "Battery / charging on K1600 and R 1250",
        "bmw.i5d": "Alternator-regulator faults and low-charge symptoms — we read the full battery management with BMW-grade diagnostics.",
        "bmw.modelsEyebrow": "Models we service",
        "bmw.modelsTitle": "Across the BMW Motorrad <em>lineup.</em>",
        "bmw.modelsLead": "Current production, the recent past, vintage classics — if it wears the roundel, bring it in.",
        "bmw.m1t": "R-series (boxer)",
        "bmw.m1d": "R 1200 / 1250 / 1300 GS, GSA, RT, R, RS, the R nineT family and the R 18 family.",
        "bmw.m2t": "F-series (parallel twin)",
        "bmw.m2d": "F 750 GS, F 800 GS / R / GT, F 850 GS / Adventure, F 900 GS / GS Adventure / R / XR.",
        "bmw.m3t": "G-series (single)",
        "bmw.m3d": "G 310 GS, G 310 R, plus the vintage G 450 X — legacy projects are welcome too.",
        "bmw.m4t": "S-series (inline-4)",
        "bmw.m4d": "S 1000 R, S 1000 RR, S 1000 XR, M 1000 RR — track prep and dyno tuning available.",
        "bmw.m5t": "K-series (inline-6 and earlier inline-4)",
        "bmw.m5d": "K 1600 GT, GTL, B, Grand America; the K 1200/1300 family; and the legacy K airhead.",
        "bmw.m6t": "Classic / airhead",
        "bmw.m6d": "Vintage R 80/100, R 90 S, K-bricks. Restoration and ongoing service both welcome.",
        "bmw.partsEyebrow": "Parts and accessories",
        "bmw.partsTitle": "Catalog access for <em>major BMW parts.</em>",
        "bmw.partsLead": "We source through the international BMW Motorrad accessory, OEM and aftermarket catalog networks. Whatever your bike needs — OEM, performance, touring or protection — we order it directly through suppliers we trust.",
        "bmw.partsList": "<strong>Catalogs we work with:</strong> Wunderlich · Touratech · Hepco &amp; Becker · SW-Motech · Akrapovič · Wilbers · Öhlins · Brembo · AltRider · Rizoma · Mitas · Avon · OEM BMW Motorrad parts via our distributor network. Order ahead even if you're not booking service yet.",
        "bmw.faqEyebrow": "FAQ",
        "bmw.faqTitle": "Common questions.",
        "bmw.q1": "Are you an authorized BMW dealer?",
        "bmw.a1": "No — Iron Custom Motors is an independent BMW Motorrad workshop. The upside is no dealer mark-up and the freedom to fit OEM or quality aftermarket parts. Recall and warranty work has to be done at an authorized BMW dealer, but everything else — scheduled service, repair, modifications — we handle at independent-workshop rates and with deeper, BMW-first attention.",
        "bmw.q2": "Do you have proper BMW diagnostic equipment?",
        "bmw.a2": "Yes. We run the GS-911 (BMW's own diagnostic interface) and BMW ISTA / dealer-equivalent procedures where they apply. We read codes, run adaptive resets, watch live sensor data and write up what we find. Diagnostic fee 50–350€ depending on depth, with a written report.",
        "bmw.q3": "How much does an Inspection 2 / valve service cost?",
        "bmw.a3": "From €350, depending on the platform and what your bike actually needs. For an R 1250 GS / GSA at its valve interval, expect €450–€650 including all fluids, valve check and throttle-body sync. You get a written estimate before we lift a wrench.",
        "bmw.q4": "Can you do track-day prep for S 1000 RR?",
        "bmw.a4": "Yes — suspension setup, brake line and pad upgrade, slick fitment, ride-height and ECU map tuning for the circuit. We have the dyno and the suspension-setup tools to dial it in properly.",
        "bmw.q5": "Can you source OEM BMW parts not stocked locally?",
        "bmw.a5": "Yes — we have catalog access to OEM BMW Motorrad parts through our distributor network plus all the major aftermarket catalogs. If a part exists for your model, we can source it.",
        "seo.localLead": "Iron Custom Motors is based in São Domingos de Rana, Cascais. We work with riders from Cascais, Estoril, Oeiras, Sintra, Lisbon and across Greater Lisbon.",
        "seo.area1d": "A real workshop and client lounge, not a remote parts counter. Book a service, drop the bike off, or come by to talk a project through.",
        "seo.area2d": "English, Russian, Ukrainian and Portuguese — with written estimates and clear next steps.",
        "seo.area3d": "Diagnostics, parts sourcing, installation, upgrades and follow-up all happen under one workshop's standard.",
        "bmw.ctaEyebrow": "Ready when you are",
        "bmw.ctaTitle": "Bring your BMW in.",
        "bmw.ctaText": "Send the model, year and a short description over WhatsApp. We'll come back with the nearest available slot and a written estimate before any work starts.",
        "bmw.btnBack": "Back to home",
    },
    "ru": {
        "bmw.eyebrow": "BMW Motorrad · Кашкайш / Большой Лиссабон",
        "bmw.h1": "Сервис BMW Motorrad<br/>в <span class=\"accent\">Кашкайше.</span>",
        "bmw.sub": "Независимая мастерская BMW для R-, K-, S-, F- и G-серий. Диагностика, плановое ТО, ремонт и тюнинг от команды, которая выиграла BMW Motorrad Customizing Championship 2023.",
        "bmw.breadHome": "Главная",
        "bmw.h1Crumb": "Сервис BMW Motorrad",
        "bmw.btnWA": "WhatsApp",
        "bmw.btnSend": "Отправить заявку",
        "bmw.heroAlt": "Сервис мотоциклов BMW Motorrad в мастерской Iron Custom Motors, Кашкайш",

        "bmw.introEyebrow": "Почему BMW — к нам",
        "bmw.introTitle": "Глубокая BMW-экспертиза, <em>независимые цены.</em>",
        "bmw.introP1": "Iron Custom Motors — независимая мастерская BMW Motorrad в Кашкайше. За ней стоит та же команда, что взяла BMW Motorrad Customizing Championship 2023 — официальное признание BMW за инженерию и качество сборки. Мотоцикл, с которым мы берём награды, и ваш мотоцикл, который вы оставляете на ТО, проходят через одни руки и один и тот же стандарт.",
        "bmw.introP2": "Мы работаем со всей линейкой BMW Motorrad — оппозит R-серии, parallel-twin F-серии, одноцилиндровые G, рядные четвёрки S и рядные шестёрки K. У каждой платформы свой характер и свои слабые места, и мы их знаем — потому что эти мотоциклы стоят у нас в цеху из недели в неделю. Это специализация именно по BMW, а не «универсальный сервис, который заодно берёт и BMW».",
        "bmw.introP3": "Независимая мастерская — это ещё и отсутствие дилерской наценки, возможность ставить оригинал или качественный aftermarket по ситуации, и прямой разговор от начала до конца. Смета до работ, письменный отчёт при выдаче.",
        "bmw.toolsEyebrow": "Специализированный инструмент",
        "bmw.toolsTitle": "Диагностика и инструмент <em>под BMW.</em>",
        "bmw.toolsLead": "BMW Motorrad требует инструмент, которого у большинства независимых мастерских попросту нет, — мы его купили. Это и есть разница между настоящим BMW-сервисом и мастерской, которая «иногда берёт BMW».",
        "bmw.t1t": "Диагностический сканер GS-911",
        "bmw.t1d": "Читает и сбрасывает специфичные для BMW коды ошибок, выполняет адаптивные сбросы, показывает данные датчиков в реальном времени и сервисные индикаторы.",
        "bmw.t2t": "BMW ISTA / диагностика дилерского уровня",
        "bmw.t2d": "Где нужно, запускаем процедуры уровня дилера, чтобы добраться до глубоких системных меню, которые обычному сканеру недоступны.",
        "bmw.t3t": "Инструмент Paralever / Telelever",
        "bmw.t3d": "Правильные приспособления для преднатяга и регулировки геометрии передней и задней подвески BMW — без кустарных замен.",
        "bmw.t4t": "Сервисный комплект ESA",
        "bmw.t4d": "Пружинная стяжка и корректная процедура замены для амортизаторов Electronic Suspension Adjustment (ESA).",
        "bmw.servicesEyebrow": "Что делаем на BMW",
        "bmw.servicesTitle": "Сервис. Ремонт. <em>Тюнинг.</em>",
        "bmw.servicesLead": "От Inspection 1 до полной реставрации винтажного airhead — всё со знанием специфики BMW и правильным инструментом.",
        "bmw.s1t": "Плановое ТО (Inspection 1 / 2)",
        "bmw.s1d": "ТО по регламенту BMW — масло, фильтр, жидкости, проверка тормозов, осмотр final drive (кардана), плюс зазоры клапанов, когда подходит интервал.",
        "bmw.s2t": "Клапаны — boxer / parallel twin / single",
        "bmw.s2d": "Делаем как надо — щупами, с подбором регулировочных шайб там, где двигатель этого требует. Boxer R-серии, F-серия, G-серия.",
        "bmw.s3t": "Главная передача (кардан)",
        "bmw.s3d": "Замена масла в редукторе, проверка подшипников маятника, контроль преднатяга Paralever — та работа, что держит кардан GS, RT и R-серии в строю вдолгую.",
        "bmw.s4t": "Прокачка ABS Pro / Integral ABS",
        "bmw.s4d": "Полная прокачка интегрированной системы ABS от BMW. Обычная прокачка тормозов здесь жидкость как надо не прогонит — нужна именно BMW-процедура.",
        "bmw.s5t": "Настройка boxer-двигателя",
        "bmw.s5d": "Синхронизация дросселей, стабилизация холостого хода, калибровка датчика массового расхода воздуха (MAF), замена свечей — чтобы boxer работал ровно, как и должен.",
        "bmw.s6t": "Подвеска",
        "bmw.s6d": "Обслуживание ESA, Telelever, Paralever — замена сальников вилки, масла, настройка сэга, отбоя и сжатия. Пока колесо снято, заодно сделаем <a href=\"/ru/shinomontazh-mototsiklov/\">шиномонтаж и балансировку</a> под широкую резину BMW и спицованные диски GS, включая tubeless-spoked и кастомные колёса.",
        "bmw.s7t": "Электроника",
        "bmw.s7d": "Полное чтение кодов и данных в реальном времени через GS-911. Аккумулятор, зарядка, CAN-bus, ремонт проводки и аксессуарных линий.",
        "bmw.s8t": "Тюнинг и апгрейды",
        "bmw.s8d": "Установка выхлопа с соответствующей перепрошивкой ECU (Akrapovič, Wilbers, Öhlins), апгрейды подвески, эргономика, защита, тур-обвес.",
        "bmw.issuesEyebrow": "Типичные болезни BMW",
        "bmw.issuesTitle": "Слабые места BMW, <em>находим до того, как ударят.</em>",
        "bmw.issuesLead": "Годы на этих мотоциклах — и слабые места мы знаем наизусть. Рисковые узлы проверяем заранее, а не после того, как они подведут в дороге.",
        "bmw.i1t": "Уход клапанов boxer",
        "bmw.i1d": "Частое явление на R 1200 и более ранних — мы знаем, когда зазоры действительно надо мерить, а когда дилер просто ставит галочку.",
        "bmw.i2t": "Износ подшипников главной передачи",
        "bmw.i2d": "Ранние симптомы на R 1200/1250 GS и RT — ловим проверкой люфта до того, как редуктор умрёт.",
        "bmw.i3t": "Сбои ABS / brake assist",
        "bmw.i3d": "Неисправности серво и насоса на старых R-серии. Мы диагностируем и ремонтируем там, где дилер меняет модуль целиком.",
        "bmw.i4t": "Шлицы кардана и paralever-сочленения",
        "bmw.i4d": "Разбираем, чистим, перенабиваем смазкой, меняем при износе — тот интервал обслуживания, который большинство дилеров тихо пропускает.",
        "bmw.i5t": "АКБ и зарядка на K 1600 и R 1250",
        "bmw.i5d": "Сбои регулятора генератора, симптомы низкого заряда — считываем полный battery management диагностикой BMW-уровня.",
        "bmw.modelsEyebrow": "Модели на которых работаем",
        "bmw.modelsTitle": "Вся линейка <em>BMW Motorrad.</em>",
        "bmw.modelsLead": "Текущее производство, недавнее прошлое, винтажная классика — если на баке логотип «пропеллера», везите к нам.",
        "bmw.m1t": "R-серия (boxer)",
        "bmw.m1d": "R 1200 / 1250 / 1300 GS, GSA, RT, R, RS, семейство R nineT, семейство R 18.",
        "bmw.m2t": "F-серия (parallel twin)",
        "bmw.m2d": "F 750 GS, F 800 GS / R / GT, F 850 GS / Adventure, F 900 GS / GS Adventure / R / XR.",
        "bmw.m3t": "G-серия (single)",
        "bmw.m3d": "G 310 GS, G 310 R, плюс винтажный G 450 X — legacy-проекты тоже берём.",
        "bmw.m4t": "S-серия (рядная четвёрка)",
        "bmw.m4d": "S 1000 R, S 1000 RR, S 1000 XR, M 1000 RR — track-prep и dyno-тюнинг доступны.",
        "bmw.m5t": "K-серия (рядная шестёрка и предыдущие)",
        "bmw.m5d": "K 1600 GT, GTL, B, Grand America; семейство K 1200/1300; и legacy K airhead.",
        "bmw.m6t": "Классика / airhead",
        "bmw.m6d": "Винтажные R 80/100, R 90 S, K-bricks. Реставрация и текущий сервис — и то, и другое.",
        "bmw.partsEyebrow": "Запчасти и аксессуары",
        "bmw.partsTitle": "Доступ к <em>крупным каталогам BMW.</em>",
        "bmw.partsLead": "Заказываем через международные сети каталогов аксессуаров, OEM-запчастей и aftermarket BMW Motorrad. Что бы вашему мотоциклу ни понадобилось — оригинал, производительность, туринг, защита — заказываем напрямую у проверенных поставщиков.",
        "bmw.partsList": "<strong>Каталоги:</strong> Wunderlich · Touratech · Hepco &amp; Becker · SW-Motech · Akrapovič · Wilbers · Öhlins · Brembo · AltRider · Rizoma · Mitas · Avon · оригинальные запчасти BMW Motorrad через дистрибьюторскую сеть. Заказать можно и без записи на сервис.",
        "bmw.faqEyebrow": "FAQ",
        "bmw.faqTitle": "Частые вопросы.",
        "bmw.q1": "Вы официальный дилер BMW?",
        "bmw.a1": "Нет — Iron Custom Motors независимая мастерская BMW Motorrad. Плюс в том, что нет дилерской наценки и можно ставить оригинал или качественный aftermarket по ситуации. Гарантийные и отзывные работы должны выполняться у авторизованного дилера BMW, а всё остальное — плановое ТО, ремонт, модификации — делаем по ценам независимой мастерской и с более глубоким, BMW-первым вниманием.",
        "bmw.q2": "У вас есть нормальная диагностика BMW?",
        "bmw.a2": "Да. Работаем с GS-911 (собственным диагностическим интерфейсом BMW) и с BMW ISTA / процедурами дилерского уровня там, где они применимы. Читаем коды, делаем адаптивные сбросы, следим за данными в реальном времени и пишем заключение. Диагностика 50–350€ в зависимости от глубины, с письменным отчётом.",
        "bmw.q3": "Сколько стоит Inspection 2 / клапаны?",
        "bmw.a3": "От €350 — зависит от платформы и того, что мотоциклу реально нужно. Для R 1250 GS / GSA на клапанном интервале — ориентируйтесь на €450–€650 с учётом всех жидкостей, проверки клапанов и синхронизации дросселей. Письменная смета до того, как возьмёмся за ключи.",
        "bmw.q4": "Делаете трек-преп для S 1000 RR?",
        "bmw.a4": "Да — настройка подвески, апгрейд тормозных линий и колодок, установка сликов, регулировка ride-height и доводка карты ECU под трассу. Есть и dyno, и инструмент для настройки подвески, чтобы всё выставить как надо.",
        "bmw.q5": "Можете заказать редкие оригинальные запчасти BMW?",
        "bmw.a5": "Да — у нас каталожный доступ к оригинальным запчастям BMW Motorrad через дистрибьюторскую сеть плюс ко всем крупным aftermarket-каталогам. Если деталь существует для вашей модели — закажем.",
        "seo.localLead": "Iron Custom Motors находится в São Domingos de Rana, Cascais. Мы работаем с райдерами из Cascais, Estoril, Oeiras, Sintra, Lisbon и всего Greater Lisbon.",
        "seo.area1d": "Настоящая мастерская с клиентским lounge, а не удалённая стойка выдачи запчастей. Можно записаться на сервис, оставить мотоцикл или заехать обсудить проект.",
        "seo.area2d": "Английский, русский, украинский и португальский — с письменными сметами и понятными следующими шагами.",
        "seo.area3d": "Диагностика, подбор запчастей, установка, апгрейды и сопровождение идут по одному стандарту мастерской.",
        "bmw.ctaEyebrow": "Когда готовы — мы готовы",
        "bmw.ctaTitle": "Привозите ваш BMW.",
        "bmw.ctaText": "Напишите модель, год и коротко суть в WhatsApp. Сориентируем по ближайшему слоту и пришлём письменную смету до начала работ.",
        "bmw.btnBack": "На главную",
    },
    "uk": {
        "bmw.eyebrow": "BMW Motorrad · Кашкайш / Великий Лісабон",
        "bmw.h1": "Сервіс BMW Motorrad<br/>у <span class=\"accent\">Кашкайші.</span>",
        "bmw.sub": "Незалежна майстерня BMW для R-, K-, S-, F- і G-серій. Діагностика, планове ТО, ремонт і тюнінг від команди, що стала чемпіоном BMW Motorrad Customizing Championship 2023.",
        "bmw.breadHome": "Головна",
        "bmw.h1Crumb": "Сервіс BMW Motorrad",
        "bmw.btnWA": "WhatsApp",
        "bmw.btnSend": "Надіслати заявку",
        "bmw.heroAlt": "Сервіс мотоциклів BMW Motorrad у майстерні Iron Custom Motors, Кашкайш",

        "bmw.introEyebrow": "Чому BMW — до нас",
        "bmw.introTitle": "Глибока BMW-експертиза, <em>незалежні ціни.</em>",
        "bmw.introP1": "Iron Custom Motors — незалежна майстерня BMW Motorrad у Кашкайші. За нею стоїть та сама команда, що взяла BMW Motorrad Customizing Championship 2023 — офіційне визнання BMW за інженерію та якість збірки. Мотоцикл, з яким ми беремо нагороди, і ваш мотоцикл, який ви залишаєте на ТО, проходять через одні руки й один стандарт.",
        "bmw.introP2": "Ми працюємо з усією лінійкою BMW Motorrad — опозит R-серії, parallel-twin F-серії, одноциліндрові G, рядні четвірки S і рядні шестірки K. Кожна платформа має свій характер і свої слабкі місця, і ми їх знаємо — бо ці мотоцикли стоять у нас у цеху тиждень за тижнем. Це спеціалізація саме на BMW, а не «універсальний сервіс, який заодно бере й BMW».",
        "bmw.introP3": "Незалежна майстерня — це ще й відсутність дилерської націнки, можливість ставити оригінал або якісний aftermarket за ситуацією, і прямий діалог від початку до кінця. Кошторис до робіт, письмовий звіт при видачі.",
        "bmw.toolsEyebrow": "Спеціалізований інструмент",
        "bmw.toolsTitle": "Діагностика й інструмент <em>під BMW.</em>",
        "bmw.toolsLead": "BMW Motorrad вимагає інструмент, якого у більшості незалежних майстерень просто немає, — ми його придбали. Це й є різниця між справжнім BMW-сервісом і майстернею, яка «іноді бере BMW».",
        "bmw.t1t": "Діагностичний сканер GS-911",
        "bmw.t1d": "Читає та скидає специфічні для BMW коди помилок, виконує адаптивні скидання, показує дані датчиків у реальному часі й сервісні індикатори.",
        "bmw.t2t": "BMW ISTA / діагностика дилерського рівня",
        "bmw.t2d": "Де потрібно, запускаємо процедури рівня дилера, щоб дістатися до глибоких системних меню, недоступних звичайному сканеру.",
        "bmw.t3t": "Інструмент Paralever / Telelever",
        "bmw.t3d": "Правильні пристосування для переднатягу й регулювання геометрії передньої та задньої підвіски BMW — без кустарних замін.",
        "bmw.t4t": "Сервісний комплект ESA",
        "bmw.t4d": "Пружинна стяжка і коректна процедура заміни для амортизаторів Electronic Suspension Adjustment (ESA).",
        "bmw.servicesEyebrow": "Що робимо на BMW",
        "bmw.servicesTitle": "Сервіс. Ремонт. <em>Тюнінг.</em>",
        "bmw.servicesLead": "Від Inspection 1 до повної реставрації вінтажного airhead — усе зі знанням специфіки BMW і правильним інструментом.",
        "bmw.s1t": "Планове ТО (Inspection 1 / 2)",
        "bmw.s1d": "ТО за регламентом BMW — олива, фільтр, рідини, перевірка гальм, огляд final drive (кардана), плюс зазори клапанів, коли підходить інтервал.",
        "bmw.s2t": "Клапани — boxer / parallel twin / single",
        "bmw.s2d": "Робимо як належить — щупами, з підбором регулювальних шайб там, де двигун цього вимагає. Boxer R-серії, F-серія, G-серія.",
        "bmw.s3t": "Головна передача (кардан)",
        "bmw.s3d": "Заміна оливи в редукторі, перевірка підшипників маятника, контроль переднатягу Paralever — та робота, що тримає кардан GS, RT і R-серії у строю надовго.",
        "bmw.s4t": "Прокачка ABS Pro / Integral ABS",
        "bmw.s4d": "Повна прокачка інтегрованої системи ABS від BMW. Звичайна прокачка гальм тут рідину як слід не прожене — потрібна саме BMW-процедура.",
        "bmw.s5t": "Налаштування boxer-двигуна",
        "bmw.s5d": "Синхронізація дроселів, стабілізація холостого ходу, калібрування датчика масової витрати повітря (MAF), заміна свічок — щоб boxer працював рівно, як і має.",
        "bmw.s6t": "Підвіска",
        "bmw.s6d": "Обслуговування ESA, Telelever, Paralever — заміна сальників вилки, оливи, налаштування сегу, відбою і стиснення. Поки колесо зняте, заодно зробимо <a href=\"/uk/shynomontazh-mototsykliv/\">шиномонтаж і балансування</a> під широку гуму BMW і спицьовані диски GS, включно з tubeless-spoked і кастомними колесами.",
        "bmw.s7t": "Електроніка",
        "bmw.s7d": "Повне читання кодів і даних у реальному часі через GS-911. Акумулятор, зарядка, CAN-bus, ремонт проводки та аксесуарних ліній.",
        "bmw.s8t": "Тюнінг і апґрейди",
        "bmw.s8d": "Встановлення вихлопу з відповідною перепрошивкою ECU (Akrapovič, Wilbers, Öhlins), апґрейди підвіски, ергономіка, захист, тур-обвіс.",
        "bmw.issuesEyebrow": "Типові болячки BMW",
        "bmw.issuesTitle": "Слабкі місця BMW, <em>знаходимо до того, як вдарять.</em>",
        "bmw.issuesLead": "Роки на цих мотоциклах — і слабкі місця ми знаємо напам'ять. Ризикові вузли перевіряємо заздалегідь, а не після того, як вони підведуть у дорозі.",
        "bmw.i1t": "Дрейф клапанів boxer",
        "bmw.i1d": "Часте явище на R 1200 і ранніших — ми знаємо, коли зазори справді треба міряти, а коли дилер просто ставить галочку.",
        "bmw.i2t": "Знос підшипників головної передачі",
        "bmw.i2d": "Ранні симптоми на R 1200/1250 GS і RT — ловимо перевіркою люфту до того, як редуктор помре.",
        "bmw.i3t": "Збої ABS / brake assist",
        "bmw.i3d": "Несправності серво й помпи на старих R-серії. Ми діагностуємо й ремонтуємо там, де дилер міняє модуль цілком.",
        "bmw.i4t": "Шліци кардана й paralever-з'єднання",
        "bmw.i4d": "Розбираємо, чистимо, перенабиваємо мастилом, міняємо за зносу — той інтервал обслуговування, який більшість дилерів тихо пропускає.",
        "bmw.i5t": "АКБ і зарядка на K 1600 і R 1250",
        "bmw.i5d": "Збої регулятора генератора, симптоми низького заряду — зчитуємо повний battery management діагностикою BMW-рівня.",
        "bmw.modelsEyebrow": "Моделі, на яких працюємо",
        "bmw.modelsTitle": "Уся лінійка <em>BMW Motorrad.</em>",
        "bmw.modelsLead": "Сучасне виробництво, недавнє минуле, вінтажна класика — якщо на баку логотип «пропелера», везіть до нас.",
        "bmw.m1t": "R-серія (boxer)",
        "bmw.m1d": "R 1200 / 1250 / 1300 GS, GSA, RT, R, RS, родина R nineT, родина R 18.",
        "bmw.m2t": "F-серія (parallel twin)",
        "bmw.m2d": "F 750 GS, F 800 GS / R / GT, F 850 GS / Adventure, F 900 GS / GS Adventure / R / XR.",
        "bmw.m3t": "G-серія (single)",
        "bmw.m3d": "G 310 GS, G 310 R, плюс вінтажний G 450 X — legacy-проєкти теж беремо.",
        "bmw.m4t": "S-серія (рядна четвірка)",
        "bmw.m4d": "S 1000 R, S 1000 RR, S 1000 XR, M 1000 RR — track-prep і dyno-тюнінг доступні.",
        "bmw.m5t": "K-серія (рядна шестірка і попередні)",
        "bmw.m5d": "K 1600 GT, GTL, B, Grand America; родина K 1200/1300; і legacy K airhead.",
        "bmw.m6t": "Класика / airhead",
        "bmw.m6d": "Вінтажні R 80/100, R 90 S, K-bricks. Реставрація і поточний сервіс — і те, й інше.",
        "bmw.partsEyebrow": "Запчастини й аксесуари",
        "bmw.partsTitle": "Доступ до <em>великих каталогів BMW.</em>",
        "bmw.partsLead": "Замовляємо через міжнародні мережі каталогів аксесуарів, OEM-запчастин і aftermarket BMW Motorrad. Що б вашому мотоциклу не знадобилось — оригінал, продуктивність, туринг, захист — замовляємо напряму у перевірених постачальників.",
        "bmw.partsList": "<strong>Каталоги:</strong> Wunderlich · Touratech · Hepco &amp; Becker · SW-Motech · Akrapovič · Wilbers · Öhlins · Brembo · AltRider · Rizoma · Mitas · Avon · оригінальні запчастини BMW Motorrad через дистриб'юторську мережу. Замовити можна і без запису на сервіс.",
        "bmw.faqEyebrow": "FAQ",
        "bmw.faqTitle": "Часті питання.",
        "bmw.q1": "Ви офіційний дилер BMW?",
        "bmw.a1": "Ні — Iron Custom Motors незалежна майстерня BMW Motorrad. Плюс у тому, що немає дилерської націнки і можна ставити оригінал або якісний aftermarket за ситуацією. Гарантійні та відкличні роботи мають виконуватись в авторизованого дилера BMW, а все інше — планове ТО, ремонт, модифікації — робимо за цінами незалежної майстерні та з глибшою, BMW-першою увагою.",
        "bmw.q2": "У вас є нормальна діагностика BMW?",
        "bmw.a2": "Так. Працюємо з GS-911 (власним діагностичним інтерфейсом BMW) і з BMW ISTA / процедурами дилерського рівня там, де вони застосовні. Читаємо коди, робимо адаптивні скидання, стежимо за даними в реальному часі й пишемо висновок. Діагностика 50–350€ залежно від глибини, з письмовим звітом.",
        "bmw.q3": "Скільки коштує Inspection 2 / клапани?",
        "bmw.a3": "Від €350 — залежить від платформи і того, що мотоциклу справді потрібно. Для R 1250 GS / GSA на клапанному інтервалі — орієнтуйтеся на €450–€650 з урахуванням усіх рідин, перевірки клапанів і синхронізації дроселів. Письмовий кошторис до того, як візьмемось за ключі.",
        "bmw.q4": "Робите трек-преп для S 1000 RR?",
        "bmw.a4": "Так — налаштування підвіски, апґрейд гальмівних ліній і колодок, встановлення сліків, регулювання ride-height і доводка карти ECU під трасу. Є і dyno, і інструмент для налаштування підвіски, щоб усе виставити як слід.",
        "bmw.q5": "Чи можете замовити рідкісні оригінальні запчастини BMW?",
        "bmw.a5": "Так — у нас каталожний доступ до оригінальних запчастин BMW Motorrad через дистриб'юторську мережу плюс до всіх великих aftermarket-каталогів. Якщо деталь існує для вашої моделі — замовимо.",
        "seo.localLead": "Iron Custom Motors знаходиться у São Domingos de Rana, Cascais. Ми працюємо з райдерами з Cascais, Estoril, Oeiras, Sintra, Lisbon і всього Greater Lisbon.",
        "seo.area1d": "Справжня майстерня з клієнтським lounge, а не віддалена стійка видачі запчастин. Можна записатися на сервіс, залишити мотоцикл або заїхати обговорити проєкт.",
        "seo.area2d": "Англійська, російська, українська і португальська — з письмовими кошторисами і зрозумілими наступними кроками.",
        "seo.area3d": "Діагностика, підбір запчастин, встановлення, апґрейди і супровід ідуть за одним стандартом майстерні.",
        "bmw.ctaEyebrow": "Коли ви готові — ми готові",
        "bmw.ctaTitle": "Привозьте ваш BMW.",
        "bmw.ctaText": "Напишіть модель, рік і коротко суть у WhatsApp. Зорієнтуємо щодо найближчого слота і пришлемо письмовий кошторис до початку робіт.",
        "bmw.btnBack": "На головну",
    },
    "pt": {
        "bmw.eyebrow": "BMW Motorrad · Cascais / Grande Lisboa",
        "bmw.h1": "Serviço BMW Motorrad<br/>em <span class=\"accent\">Cascais.</span>",
        "bmw.sub": "Oficina independente BMW para R, K, S, F e G. Diagnóstico, manutenção programada, reparação e tuning pela equipa que venceu o BMW Motorrad Customizing Championship 2023.",
        "bmw.breadHome": "Início",
        "bmw.h1Crumb": "Serviço BMW Motorrad",
        "bmw.btnWA": "WhatsApp",
        "bmw.btnSend": "Enviar pedido",
        "bmw.heroAlt": "Serviço de motas BMW Motorrad na oficina Iron Custom Motors em Cascais",

        "bmw.introEyebrow": "Porquê BMW connosco",
        "bmw.introTitle": "Expertise BMW profunda, <em>preços independentes.</em>",
        "bmw.introP1": "A Iron Custom Motors é uma oficina independente BMW Motorrad em Cascais, conduzida pela mesma equipa que venceu o BMW Motorrad Customizing Championship 2023 — o reconhecimento da própria BMW pela engenharia e pelo acabamento. A mota com que ganhamos troféus e a mota que deixa para revisão passam pelas mesmas mãos e pelo mesmo padrão.",
        "bmw.introP2": "Trabalhamos toda a linha BMW Motorrad — o boxer da R-series, o twin paralelo da F-series, o mono da G-series, o inline-4 da S-series e o inline-6 da K-series. Cada plataforma tem as suas manias e os seus pontos fracos, e conhecemo-los porque temos estas motas na oficina semana após semana. Isto é especialização BMW a sério, não uma oficina genérica que «também aceita BMW».",
        "bmw.introP3": "Independente significa também sem markup de concessionário, liberdade para montar peças OEM ou aftermarket de qualidade conforme a intervenção pede, e uma conversa direta do início ao fim. Orçamento antes de começar, relatório escrito quando devolvemos a mota.",
        "bmw.toolsEyebrow": "Ferramenta especialista",
        "bmw.toolsTitle": "Diagnóstico e ferramenta <em>BMW-específica.</em>",
        "bmw.toolsLead": "A BMW Motorrad exige ferramenta que a maioria das oficinas independentes simplesmente não tem — por isso comprámo-la. É essa a diferença entre uma verdadeira oficina BMW e uma oficina que de vez em quando aceita uma.",
        "bmw.t1t": "Interface de diagnóstico GS-911",
        "bmw.t1d": "Lê e apaga códigos de avaria específicos BMW, corre resets adaptativos e mostra dados ao vivo dos sensores e indicadores de serviço.",
        "bmw.t2t": "BMW ISTA / diagnóstico tipo concessionário",
        "bmw.t2d": "Onde é preciso, corremos procedimentos equivalentes aos do concessionário para chegar aos menus de sistema mais profundos que um scanner genérico nunca vê.",
        "bmw.t3t": "Ferramenta Paralever / Telelever",
        "bmw.t3d": "A ferramenta correta de pré-carga e alinhamento para a geometria da suspensão dianteira e traseira BMW — não improvisos.",
        "bmw.t4t": "Kit de serviço ESA",
        "bmw.t4d": "Compressor de molas e o procedimento de substituição correto para amortecedores Electronic Suspension Adjustment (ESA).",
        "bmw.servicesEyebrow": "O que fazemos em BMW",
        "bmw.servicesTitle": "Serviço. Reparação. <em>Tuning.</em>",
        "bmw.servicesLead": "Da Inspection 1 a uma reconstrução completa de um airhead vintage — tudo com conhecimento e ferramenta específicos BMW.",
        "bmw.s1t": "Manutenção programada (Inspection 1 / 2)",
        "bmw.s1d": "Serviço por intervalo BMW — óleo, filtro, fluidos, verificação de travões, inspeção do cardan e folga de válvulas quando o intervalo o pede.",
        "bmw.s2t": "Válvulas — boxer / parallel twin / mono",
        "bmw.s2d": "Feito como deve ser, com apalpa-folgas e seleção de shims onde o motor o exige. R-series, F-series, G-series.",
        "bmw.s3t": "Transmissão final (cardan)",
        "bmw.s3d": "Troca de óleo do diferencial, inspeção dos rolamentos do braço basculante e verificação da pré-carga Paralever — o trabalho que mantém vivo o cardan de um GS, RT ou R-series a longo prazo.",
        "bmw.s4t": "Sangria ABS Pro / Integral ABS",
        "bmw.s4d": "Sangria completa do ABS integrado da BMW. Uma sangria de travões normal não leva o fluido aonde tem de ir aqui — exige o procedimento BMW próprio.",
        "bmw.s5t": "Afinação do motor boxer",
        "bmw.s5d": "Sincronização das borboletas, estabilização da marcha lenta, calibração do medidor de massa de ar e serviço de velas — o boxer a trabalhar tão suave como deve.",
        "bmw.s6t": "Suspensão",
        "bmw.s6d": "Serviço de ESA, Telelever e Paralever — retentores de forquilha, troca de óleo, ajuste de sag, retorno e compressão. Com a roda fora, tratamos também da <a href=\"/pt/montagem-de-pneus-mota/\">montagem e equilibragem de pneus</a> para a borracha larga das BMW e jantes de raios das GS, incluindo configurações tubeless-spoked e rodas custom.",
        "bmw.s7t": "Diagnóstico elétrico",
        "bmw.s7d": "Leitura completa de códigos e dados ao vivo com o GS-911. Bateria, carga, CAN-bus e reparação de cablagem e acessórios.",
        "bmw.s8t": "Tuning e upgrades",
        "bmw.s8d": "Instalação de escape com o respetivo re-flash do ECU (Akrapovič, Wilbers, Öhlins), upgrades de suspensão, ergonomia, proteção e equipamento de touring.",
        "bmw.issuesEyebrow": "Problemas BMW que conhecemos",
        "bmw.issuesTitle": "Padrões de falha BMW, <em>resolvidos antes de morderem.</em>",
        "bmw.issuesLead": "Anos nestas motas significam conhecer os pontos fracos de cor. Verificamos os itens de alto risco à partida — não depois de a mota deixar ficar em viagem.",
        "bmw.i1t": "Drift de válvulas do boxer",
        "bmw.i1d": "Comum no R 1200 e anteriores — sabemos quando as folgas precisam mesmo de ser medidas e quando é só o concessionário a cumprir tabela.",
        "bmw.i2t": "Desgaste de rolamentos da transmissão final",
        "bmw.i2d": "Sintomas precoces no R 1200/1250 GS e RT — apanhados com uma verificação de folga a sério antes de o diferencial morrer.",
        "bmw.i3t": "Falhas ABS / brake assist",
        "bmw.i3d": "Falhas de servo e de bomba nas R-series mais antigas. Diagnosticamos e reparamos onde o concessionário substituiria o módulo inteiro.",
        "bmw.i4t": "Estrias do cardan e juntas paralever",
        "bmw.i4d": "Desmontamos, limpamos, lubrificamos e substituímos onde há desgaste — o intervalo de serviço que a maioria dos concessionários salta sem dizer nada.",
        "bmw.i5t": "Bateria / carga em K 1600 e R 1250",
        "bmw.i5d": "Falhas do regulador do alternador e sintomas de carga baixa — lemos o battery management completo com diagnóstico de nível BMW.",
        "bmw.modelsEyebrow": "Modelos com que trabalhamos",
        "bmw.modelsTitle": "Toda a gama <em>BMW Motorrad.</em>",
        "bmw.modelsLead": "Produção atual, passado recente, clássicos vintage — se traz o símbolo da hélice, traga-a.",
        "bmw.m1t": "R-series (boxer)",
        "bmw.m1d": "R 1200 / 1250 / 1300 GS, GSA, RT, R, RS, família R nineT, família R 18.",
        "bmw.m2t": "F-series (parallel twin)",
        "bmw.m2d": "F 750 GS, F 800 GS / R / GT, F 850 GS / Adventure, F 900 GS / GS Adventure / R / XR.",
        "bmw.m3t": "G-series (mono)",
        "bmw.m3d": "G 310 GS, G 310 R, mais o G 450 X vintage — projetos legacy também são bem-vindos.",
        "bmw.m4t": "S-series (inline-4)",
        "bmw.m4d": "S 1000 R, S 1000 RR, S 1000 XR, M 1000 RR — track-prep e dyno tuning disponíveis.",
        "bmw.m5t": "K-series (inline-6 e anteriores inline-4)",
        "bmw.m5d": "K 1600 GT, GTL, B, Grand America; família K 1200/1300; e o legacy K airhead.",
        "bmw.m6t": "Clássico / airhead",
        "bmw.m6d": "R 80/100 vintage, R 90 S, K-bricks. Restauro e serviço contínuo, ambos bem-vindos.",
        "bmw.partsEyebrow": "Peças e acessórios",
        "bmw.partsTitle": "Acesso aos <em>principais catálogos BMW.</em>",
        "bmw.partsLead": "Encomendamos através das redes internacionais de catálogos de acessórios, peças OEM e aftermarket BMW Motorrad. Seja o que for que a sua mota precise — OEM, performance, touring ou proteção — pedimos diretamente a fornecedores em quem confiamos.",
        "bmw.partsList": "<strong>Catálogos:</strong> Wunderlich · Touratech · Hepco &amp; Becker · SW-Motech · Akrapovič · Wilbers · Öhlins · Brembo · AltRider · Rizoma · Mitas · Avon · peças originais BMW Motorrad via rede de distribuidores. Pode encomendar mesmo sem agendar serviço.",
        "bmw.faqEyebrow": "FAQ",
        "bmw.faqTitle": "Perguntas frequentes.",
        "bmw.q1": "São concessionário BMW autorizado?",
        "bmw.a1": "Não — a Iron Custom Motors é uma oficina independente BMW Motorrad. A vantagem é não haver markup de concessionário e poder montar peças OEM ou aftermarket de qualidade. O trabalho de garantia e recall tem de ser feito num concessionário BMW autorizado, mas tudo o resto — manutenção, reparação, modificações — fazemos a preços de oficina independente e com uma atenção BMW mais profunda.",
        "bmw.q2": "Têm equipamento de diagnóstico BMW a sério?",
        "bmw.a2": "Sim. Corremos o GS-911 (a interface de diagnóstico da própria BMW) e BMW ISTA / equivalente de concessionário onde se aplica. Lemos códigos, corremos resets adaptativos, acompanhamos os dados ao vivo e escrevemos o que encontramos. Diagnóstico 50–350€ conforme a profundidade, com relatório escrito.",
        "bmw.q3": "Quanto custa uma Inspection 2 / serviço de válvulas?",
        "bmw.a3": "A partir de €350, conforme a plataforma e o que a mota precisa de facto. Para um R 1250 GS / GSA no intervalo de válvulas, conte com €450–€650 incluindo todos os fluidos, verificação de válvulas e sincronização das borboletas. Orçamento escrito antes de mexermos.",
        "bmw.q4": "Fazem preparação track-day para S 1000 RR?",
        "bmw.a4": "Sim — afinação de suspensão, upgrade de linhas e pastilhas de travão, montagem de slicks, ride-height e afinação do mapa do ECU para o circuito. Temos o dyno e a ferramenta de suspensão para acertar como deve ser.",
        "bmw.q5": "Conseguem peças OEM BMW que não estão em stock local?",
        "bmw.a5": "Sim — temos acesso de catálogo a peças OEM BMW Motorrad pela nossa rede de distribuidores, mais todos os grandes catálogos aftermarket. Se a peça existe para o seu modelo, conseguimos encomendá-la.",
        "seo.localLead": "A Iron Custom Motors fica em São Domingos de Rana, Cascais. Trabalhamos com riders de Cascais, Estoril, Oeiras, Sintra, Lisboa e de toda a Grande Lisboa.",
        "seo.area1d": "Uma oficina a sério com lounge para clientes, não um balcão remoto de peças. Marque serviço, deixe a mota ou passe por cá para conversar sobre um projeto.",
        "seo.area2d": "Inglês, russo, ucraniano e português — com orçamentos escritos e próximos passos claros.",
        "seo.area3d": "Diagnóstico, sourcing de peças, instalação, upgrades e acompanhamento seguem todos o padrão de uma só oficina.",
        "bmw.ctaEyebrow": "Prontos quando estiver",
        "bmw.ctaTitle": "Traga o seu BMW.",
        "bmw.ctaText": "Envie o modelo, o ano e uma descrição breve por WhatsApp. Voltamos com o slot disponível mais próximo e um orçamento escrito antes de qualquer trabalho começar.",
        "bmw.btnBack": "Voltar ao início",
    },
}

# ====================================================================================
# Harley-Davidson
# ====================================================================================
PAGE_I18N["harley-service"] = {
    "en": {
        "hd.eyebrow": "Harley-Davidson · Cascais / Greater Lisbon",
        "hd.h1": "Harley-Davidson service<br/>in <span class=\"accent\">Cascais.</span>",
        "hd.sub": "Independent Harley specialist for Sportster, Softail, Touring and Pan America. Diagnostics, service, parts and custom work from a workshop with multiple international championship trophies built on Harley-Davidson platforms.",
        "hd.breadHome": "Home",
        "hd.h1Crumb": "Harley-Davidson service",
        "hd.btnWA": "WhatsApp us",
        "hd.btnSend": "Send a request",
        "hd.heroAlt": "Harley-Davidson motorcycles in service at Iron Custom Motors workshop in Cascais",

        "hd.introEyebrow": "Why Harleys come to us",
        "hd.introTitle": "Harley is our <em>deepest specialization.</em>",
        "hd.introP1": "Iron Custom Motors has worked Harley-Davidson platforms for over a decade. Several of our internationally award-winning builds — including projects that placed at the AMD World Championship of Custom Bike Building — were Harley-based. That history isn't decoration. It's why we know these motorcycles inside out. You can see that Harley / American custom experience in <a href=\"/projects/joker/\">Joker</a>, <a href=\"/projects/true-religion/\">True Religion</a> and <a href=\"/projects/sturmvogel/\">Sturmvogel</a>.",
        "hd.introP2": "We're an independent Harley-Davidson workshop, and Harley is the brand we work on most. Service, repair, modifications, performance upgrades, full custom — none of it is a side gig. It's the core of what we do, week in, week out.",
        "hd.introP3": "We service every modern platform: Sportster (XL, RH Sportster S, Nightster), the Softail family, Dyna (legacy), Touring (Road King, Street Glide, Road Glide, Electra Glide, Tri Glide), V-Rod (legacy) and Pan America. Whether it's a stock daily commuter or a 2003 Twin Cam with 80,000 miles, we know what your bike needs.",

        "hd.toolsEyebrow": "Specialist tooling",
        "hd.toolsTitle": "Harley-specific <em>diagnostic and tools.</em>",
        "hd.toolsLead": "Harley-Davidson-specific diagnostic gear, performance tuners and service tooling, built up over a decade of Harley work. This is what separates a Harley specialist from a general workshop.",
        "hd.t1t": "Digital Technician II / equivalent diagnostic",
        "hd.t1d": "Dealer-grade Harley diagnostics for ECM read/write, live data, adaptive resets and module programming.",
        "hd.t2t": "In-house dyno cell",
        "hd.t2d": "Dyno-tuned ECU maps for Stage I/II/IV setups, exhaust upgrades and individual customer tunes.",
        "hd.t3t": "Compensator / primary tooling",
        "hd.t3d": "Specialist pullers and torque procedures for the compensator and primary sprocket — critical on Twin Cam and Milwaukee-Eight.",
        "hd.t4t": "Race Tuner / Power Vision / SE Pro Street",
        "hd.t4d": "Support for the major Harley aftermarket tuners — install, map, dyno-verify.",

        "hd.servicesEyebrow": "What we do on Harley",
        "hd.servicesTitle": "Service. Performance. <em>Custom.</em>",
        "hd.servicesLead": "Across modern and legacy Harley platforms — from routine service intervals to full Stage IV builds.",
        "hd.s1t": "Scheduled service (5k / 10k / 25k)",
        "hd.s1d": "Harley interval service by platform — engine, primary and transmission oils, with every check the official schedule calls for.",
        "hd.s2t": "Proper Harley fluids",
        "hd.s2d": "We use the correct fluid spec for each platform. Twin Cam, Milwaukee-Eight and Revolution Max each have their own requirements.",
        "hd.s3t": "Drive belt inspection, tension, replacement",
        "hd.s3d": "Belt tension matters, and most non-specialist shops get it wrong. We set it with the proper measurement procedure.",
        "hd.s4t": "Compensator & primary chain service",
        "hd.s4d": "Inspection, torque verification, replacement where worn. Critical for Twin Cam vibration issues.",
        "hd.s5t": "Stage I / Stage II / Stage IV upgrades",
        "hd.s5d": "Dyno-tuned packages — intake, exhaust, cams, heads, bigger displacement. Estimated power gain is documented before any work starts.",
        "hd.s6t": "Dyno-tuned exhaust + ECU mapping",
        "hd.s6d": "Vance &amp; Hines, Screamin' Eagle Pro, S&amp;S, Rinehart, Bassani — installed and dyno-mapped to your bike's specifics.",
        "hd.s7t": "Suspension upgrades",
        "hd.s7d": "Öhlins, Progressive, Legend Air, Race Tech — height changes, ride-quality fixes, full rebuilds.",
        "hd.s8t": "Full custom — frame, paint, hand-built parts",
        "hd.s8d": "Our championship work. Frame mods, paint, leather, hand-machined components — proven on Harley-based builds like <a href=\"/projects/joker/\">Joker</a>, <a href=\"/projects/true-religion/\">True Religion</a> and <a href=\"/projects/sturmvogel/\">Sturmvogel</a>. Bring the brief. For wide Harley tyres, spoked wheels and custom wheel setups, see our <a href=\"/motorcycle-tyre-service/\">motorcycle tyre service</a>.",

        "hd.issuesEyebrow": "Typical Harley issues we know",
        "hd.issuesTitle": "We've seen these <em>a thousand times.</em>",
        "hd.issuesLead": "When you specialize, the same problems turn up every week. We know what to check first and what just needs adjusting.",
        "hd.i1t": "Drive belt tension misadjusted",
        "hd.i1d": "The most common issue on bikes arriving from non-specialist shops. We reset it with the proper procedure and gauge.",
        "hd.i2t": "Compensator bearing chatter",
        "hd.i2d": "The signature Twin Cam / Milwaukee-Eight noise. We diagnose it and fix it with the right tooling and torque sequence.",
        "hd.i3t": "Stator and voltage regulator failures",
        "hd.i3d": "Common on Touring models. We read the symptoms on the diagnostic before replacing anything — no parts cannon.",
        "hd.i4t": "Primary chain stretch and adjuster wear",
        "hd.i4d": "The adjustment interval gets missed more often than not. We check it and reset to factory spec.",
        "hd.i5t": "Stock exhaust map vs. aftermarket pipes",
        "hd.i5d": "Fit aftermarket pipes without remapping and your fuel mix is off. We dyno and remap it properly.",

        "hd.modelsEyebrow": "Models we service",
        "hd.modelsTitle": "Across the Harley <em>family tree.</em>",
        "hd.modelsLead": "Current production, classic Twin Cam and earlier, custom builds — bring it in.",
        "hd.m1t": "Sportster",
        "hd.m1d": "XL 883 / 1200, XL Forty-Eight, XL 1200 Roadster, XL Iron, RH 1250 Sportster S, RH 975 Nightster.",
        "hd.m2t": "Softail",
        "hd.m2d": "Heritage Classic, Fat Boy, Breakout, Fat Bob, Street Bob, Sport Glide, Low Rider, Low Rider S, Slim, Standard.",
        "hd.m3t": "Dyna (legacy)",
        "hd.m3d": "Fat Bob, Wide Glide, Super Glide, Low Rider, Street Bob — the pre-2018 platform.",
        "hd.m4t": "Touring (CVO and standard)",
        "hd.m4d": "Road King, Street Glide, Road Glide, Electra Glide, Tri Glide Ultra, CVO Limited, CVO Street Glide.",
        "hd.m5t": "Pan America",
        "hd.m5d": "Pan America 1250 Standard and Special — the Adventure platform with the Revolution Max engine.",
        "hd.m6t": "V-Rod (legacy) &amp; classic / custom",
        "hd.m6d": "Night Rod, V-Rod Muscle, plus vintage Shovelhead, Knucklehead and Panhead projects.",

        "hd.partsEyebrow": "Parts and aftermarket",
        "hd.partsTitle": "Catalog access for <em>major Harley parts.</em>",
        "hd.partsLead": "We source through the large Harley OEM and aftermarket catalog networks — direct access to thousands of SKUs across parts, performance, custom hardware and exhausts.",
        "hd.partsList": "<strong>Catalogs we work with:</strong> Drag Specialties · Custom Chrome · Biltwell · V-Twin · J&amp;P Cycles · Performance Machine · S&amp;S Cycle · Vance &amp; Hines · Screamin' Eagle Performance · Roland Sands Design · Klock Werks · Rinehart · Bassani · Burly Brand · OEM Harley-Davidson parts via distributor network.",

        "hd.faqEyebrow": "FAQ",
        "hd.faqTitle": "Common questions.",
        "hd.q1": "Are you an authorized Harley-Davidson dealer?",
        "hd.a1": "No — we're an independent Harley specialist, and that works in your favour: no dealer mark-up, the freedom to fit OEM or aftermarket performance parts, and deep platform-specific know-how rather than just a brand badge. We've worked Harley for over a decade, with multiple internationally awarded Harley-based custom builds behind us.",
        "hd.q2": "Can you do Stage I / II / IV upgrades?",
        "hd.a2": "Yes — this is core work for us. We build dyno-tuned packages with documented power gains. Stage I is intake, exhaust and a map. Stage II adds cams and head work. Stage IV is a full performance build with bigger displacement. Every Stage comes as a written quote with a parts list and expected results before work starts.",
        "hd.q3": "Do you do custom and vintage Harleys?",
        "hd.a3": "Yes — it's what we built our reputation on. Several of our custom Harley projects placed at the AMD World Championship of Custom Bike Building. Bring the bike or bring the dream — frame work, hand-built parts, paint, leather, ECU work, the lot.",
        "hd.q4": "How much for a Harley 25,000-km major service?",
        "hd.a4": "From €400, depending on the platform and what it needs. That covers engine, primary and transmission oils, drive belt inspection, brake fluid, plus the platform-specific items. You get a written estimate before any work starts.",
        "hd.q5": "Can you import OEM Harley parts into Portugal?",
        "hd.a5": "Yes — we have catalog access to OEM and Genuine Harley parts. We source whatever your bike needs, including hard-to-find items that EU stores don't stock.",

        "hd.ctaEyebrow": "Ready when you are",
        "hd.ctaTitle": "Book your Harley in.",
        "hd.ctaText": "Send the model, year and what's needed over WhatsApp. We'll come back with the next available slot and a written estimate before any work starts.",
        "hd.btnBack": "Back to home",
    },
    "ru": {
        "hd.eyebrow": "Harley-Davidson · Кашкайш / Большой Лиссабон",
        "hd.h1": "Сервис Harley-Davidson<br/>в <span class=\"accent\">Кашкайше.</span>",
        "hd.sub": "Независимый специалист по Harley — Sportster, Softail, Touring и Pan America. Диагностика, сервис, запчасти и кастом. За плечами мастерской несколько международных чемпионских трофеев, заработанных именно на платформах Harley-Davidson.",
        "hd.breadHome": "Главная",
        "hd.h1Crumb": "Сервис Harley-Davidson",
        "hd.btnWA": "WhatsApp",
        "hd.btnSend": "Отправить заявку",
        "hd.heroAlt": "Мотоциклы Harley-Davidson на сервисе в мастерской Iron Custom Motors, Кашкайш",

        "hd.introEyebrow": "Почему Harley — к нам",
        "hd.introTitle": "Harley — наша <em>самая глубокая специализация.</em>",
        "hd.introP1": "Iron Custom Motors работает с платформами Harley-Davidson больше десяти лет. Несколько наших кастом-сборок с международным признанием — в том числе проекты, бравшие призовые места на AMD World Championship of Custom Bike Building — были построены на базе Harley. Эта история не для красоты: именно она дала нам понимание этих мотоциклов изнутри. Тот же опыт Harley / American custom виден в проектах <a href=\"/ru/projects/joker/\">Joker</a>, <a href=\"/ru/projects/true-religion/\">True Religion</a> и <a href=\"/ru/projects/sturmvogel/\">Sturmvogel</a>.",
        "hd.introP2": "Мы — независимая мастерская по Harley-Davidson, и это бренд, с которым мы работаем больше всего. Сервис, ремонт, модификации, апгрейды, полный кастом — для нас это не подработка на стороне, а основная работа каждую неделю.",
        "hd.introP3": "Берём все современные платформы: Sportster (XL, RH Sportster S, Nightster), семейство Softail, Dyna (legacy), Touring (Road King, Street Glide, Road Glide, Electra Glide, Tri Glide), V-Rod (legacy) и Pan America. Стоковый мотоцикл на каждый день или Twin Cam 2003 года с пробегом 130 000 км — мы разберёмся, что ему нужно.",

        "hd.toolsEyebrow": "Специализированный инструмент",
        "hd.toolsTitle": "Диагностика и инструмент <em>под Harley.</em>",
        "hd.toolsLead": "Диагностическое оборудование под Harley-Davidson, тюнеры и сервисный инструмент — всё это собиралось за десять лет работы с маркой. Именно это отличает специалиста по Harley от мастерской «на все руки».",
        "hd.t1t": "Digital Technician II / эквивалент",
        "hd.t1d": "Дилерская диагностика Harley: чтение и запись ECM, живые данные, адаптивные сбросы, программирование модулей.",
        "hd.t2t": "Свой дино-стенд",
        "hd.t2d": "Дино-настройка прошивок ECU под сетапы Stage I/II/IV, под выхлоп и под индивидуальные карты конкретного клиента.",
        "hd.t3t": "Инструмент компенсатора и primary",
        "hd.t3d": "Специальные съёмники и процедуры затяжки для compensator и primary sprocket — без них к Twin Cam и Milwaukee-Eight лучше не подходить.",
        "hd.t4t": "Race Tuner / Power Vision / SE Pro Street",
        "hd.t4d": "Работаем со всеми основными афтермаркет-тюнерами Harley: установка, прошивка карты, проверка на дино.",

        "hd.servicesEyebrow": "Что делаем на Harley",
        "hd.servicesTitle": "Сервис. Производительность. <em>Кастом.</em>",
        "hd.servicesLead": "Современные и legacy-платформы Harley — от планового ТО до полных сборок Stage IV.",
        "hd.s1t": "Плановое ТО (5k / 10k / 25k)",
        "hd.s1d": "Регламентное ТО Harley по вашей платформе: масла двигателя, primary, КПП и все проверки по официальному регламенту.",
        "hd.s2t": "Правильные жидкости Harley",
        "hd.s2d": "Под каждую платформу заливаем то, что положено по спецификации: у Twin Cam, Milwaukee-Eight и Revolution Max требования разные.",
        "hd.s3t": "Ремень привода — осмотр, натяжение, замена",
        "hd.s3d": "Натяг ремня — вещь критичная, и в неспециализированных сервисах его чаще всего выставляют неправильно. Мы делаем это по нормальной процедуре, с замером.",
        "hd.s4t": "Сервис компенсатора и primary chain",
        "hd.s4d": "Осмотр, проверка момента затяжки, замена при износе. Без этого с вибрациями Twin Cam не разобраться.",
        "hd.s5t": "Апгрейды Stage I / Stage II / Stage IV",
        "hd.s5d": "Дино-настроенные пакеты: впуск, выпуск, валы, головки, увеличенный объём. Ожидаемый прирост мощности фиксируем на бумаге ещё до начала работ.",
        "hd.s6t": "Дино-настроенный выхлоп + прошивка ЭБУ",
        "hd.s6d": "Vance &amp; Hines, Screamin' Eagle Pro, S&amp;S, Rinehart, Bassani — ставим и калибруем на дино под конкретный мотоцикл.",
        "hd.s7t": "Апгрейды подвески",
        "hd.s7d": "Öhlins, Progressive, Legend Air, Race Tech — меняем высоту, доводим управляемость и комфорт, делаем полный ребилд.",
        "hd.s8t": "Полный кастом — рама, краска, ручные детали",
        "hd.s8d": "Наша чемпионская работа. Доработка рамы, покраска, кожа, фрезеровка под ТЗ — проверено на Harley-based проектах вроде <a href=\"/ru/projects/joker/\">Joker</a>, <a href=\"/ru/projects/true-religion/\">True Religion</a> и <a href=\"/ru/projects/sturmvogel/\">Sturmvogel</a>. Приносите бриф. Для широких Harley-шин, спицованных колёс и кастомных колёсных сетапов используйте наш <a href=\"/ru/shinomontazh-mototsiklov/\">мотоциклетный шиномонтаж</a>.",

        "hd.issuesEyebrow": "Типичные болезни Harley",
        "hd.issuesTitle": "Мы это видели <em>тысячу раз.</em>",
        "hd.issuesLead": "Когда специализируешься, одни и те же болячки приходят каждую неделю. Мы уже знаем, что смотреть в первую очередь, а где достаточно простой регулировки.",
        "hd.i1t": "Неправильно отрегулирован ремень привода",
        "hd.i1d": "Самое частое, с чем приезжают из неспециализированных сервисов. Сбрасываем и выставляем заново — по процедуре и с измерителем.",
        "hd.i2t": "Стук компенсатора",
        "hd.i2d": "Фирменный звук Twin Cam и Milwaukee-Eight. Находим причину и устраняем правильным инструментом и в правильной последовательности затяжки.",
        "hd.i3t": "Отказы статора и регулятора напряжения",
        "hd.i3d": "Частая история на моделях Touring. Сначала читаем симптомы диагностикой, и только потом меняем — без стрельбы запчастями наугад.",
        "hd.i4t": "Растяжение primary chain и износ натяжителя",
        "hd.i4d": "Интервал регулировки нередко пропускают. Мы проверяем и возвращаем всё к заводской спецификации.",
        "hd.i5t": "Заводская карта vs афтермаркет-выхлоп",
        "hd.i5d": "Поставили афтермаркет-выхлоп и не перепрошили — смесь уже неправильная. Снимаем на дино и переписываем карту как надо.",

        "hd.modelsEyebrow": "Модели на которых работаем",
        "hd.modelsTitle": "Всё семейное древо <em>Harley.</em>",
        "hd.modelsLead": "Текущее производство, классический Twin Cam и более ранние, кастом-сборки — привозите.",
        "hd.m1t": "Sportster",
        "hd.m1d": "XL 883 / 1200, XL Forty-Eight, XL 1200 Roadster, XL Iron, RH 1250 Sportster S, RH 975 Nightster.",
        "hd.m2t": "Softail",
        "hd.m2d": "Heritage Classic, Fat Boy, Breakout, Fat Bob, Street Bob, Sport Glide, Low Rider, Low Rider S, Slim, Standard.",
        "hd.m3t": "Dyna (legacy)",
        "hd.m3d": "Fat Bob, Wide Glide, Super Glide, Low Rider, Street Bob — платформа до 2018 года.",
        "hd.m4t": "Touring (CVO и стандарт)",
        "hd.m4d": "Road King, Street Glide, Road Glide, Electra Glide, Tri Glide Ultra, CVO Limited, CVO Street Glide.",
        "hd.m5t": "Pan America",
        "hd.m5d": "Pan America 1250 Standard и Special — Adventure-платформа на двигателе Revolution Max.",
        "hd.m6t": "V-Rod (legacy) и классика / кастом",
        "hd.m6d": "Night Rod, V-Rod Muscle, плюс винтажные Shovelhead, Knucklehead и Panhead.",

        "hd.partsEyebrow": "Запчасти и афтермаркет",
        "hd.partsTitle": "Доступ к <em>крупнейшим каталогам Harley.</em>",
        "hd.partsLead": "Заказываем через крупные каталожные сети OEM и афтермаркета Harley. Это прямой доступ к тысячам артикулов — запчасти, перформанс, кастом-фурнитура, выхлопы.",
        "hd.partsList": "<strong>Каталоги:</strong> Drag Specialties · Custom Chrome · Biltwell · V-Twin · J&amp;P Cycles · Performance Machine · S&amp;S Cycle · Vance &amp; Hines · Screamin' Eagle Performance · Roland Sands Design · Klock Werks · Rinehart · Bassani · Burly Brand · оригинальные запчасти Harley-Davidson через дистрибьюторскую сеть.",

        "hd.faqEyebrow": "FAQ",
        "hd.faqTitle": "Частые вопросы.",
        "hd.q1": "Вы официальный дилер Harley-Davidson?",
        "hd.a1": "Нет, мы независимый специалист по Harley — и это вам на руку: никакой дилерской наценки, свобода ставить оригинал или performance-афтермаркет, и реальная экспертиза по каждой платформе, а не просто шильдик с брендом. С Harley мы работаем больше десяти лет, и за нами несколько кастом-сборок на базе Harley с международными наградами.",
        "hd.q2": "Делаете Stage I / II / IV апгрейды?",
        "hd.a2": "Да, это для нас профильная работа. Собираем дино-настроенные пакеты с задокументированным приростом мощности. Stage I — это впуск, выхлоп и карта. Stage II добавляет валы и обработку головок. Stage IV — полная сборка с увеличенным объёмом. По каждому Stage даём письменную смету со списком запчастей и ожидаемым результатом ещё до начала работ.",
        "hd.q3": "Берёте кастом и винтажные Harley?",
        "hd.a3": "Да — на этом и построена наша репутация. Несколько наших кастом-проектов на Harley брали призовые места на AMD World Championship of Custom Bike Building. Привозите мотоцикл или просто идею — рама, детали ручной работы, окраска, кожа, работа с ECU, всё что угодно.",
        "hd.q4": "Сколько стоит Harley major service на 25,000 км?",
        "hd.a4": "От €400 — зависит от платформы и от того, что реально нужно. В работу входят масла двигателя, primary и КПП, осмотр ремня, тормозная жидкость и пункты, специфичные для платформы. Письменную смету даём до начала работ.",
        "hd.q5": "Можете заказать оригинальные Harley-запчасти в Португалию?",
        "hd.a5": "Да — у нас каталожный доступ к OEM и Genuine Harley. Закажем то, что нужно мотоциклу, в том числе редкие позиции, которых нет в магазинах по ЕС.",

        "hd.ctaEyebrow": "Когда готовы — мы готовы",
        "hd.ctaTitle": "Записывайте Harley на сервис.",
        "hd.ctaText": "Напишите в WhatsApp модель, год и что нужно сделать. Сориентируем по ближайшему слоту и пришлём письменную смету до начала работ.",
        "hd.btnBack": "На главную",
    },
    "uk": {
        "hd.eyebrow": "Harley-Davidson · Кашкайш / Великий Лісабон",
        "hd.h1": "Сервіс Harley-Davidson<br/>у <span class=\"accent\">Кашкайші.</span>",
        "hd.sub": "Незалежний спеціаліст із Harley — Sportster, Softail, Touring і Pan America. Діагностика, сервіс, запчастини та кастом. За плечима майстерні кілька міжнародних чемпіонських трофеїв, здобутих саме на платформах Harley-Davidson.",
        "hd.breadHome": "Головна",
        "hd.h1Crumb": "Сервіс Harley-Davidson",
        "hd.btnWA": "WhatsApp",
        "hd.btnSend": "Надіслати заявку",
        "hd.heroAlt": "Мотоцикли Harley-Davidson на сервісі в майстерні Iron Custom Motors, Кашкайш",

        "hd.introEyebrow": "Чому Harley — до нас",
        "hd.introTitle": "Harley — наша <em>найглибша спеціалізація.</em>",
        "hd.introP1": "Iron Custom Motors працює з платформами Harley-Davidson понад десять років. Кілька наших кастом-збірок із міжнародним визнанням — серед них проєкти, що посідали призові місця на AMD World Championship of Custom Bike Building — побудовані на базі Harley. Ця історія не для краси: саме вона дала нам розуміння цих мотоциклів зсередини. Той самий досвід Harley / American custom видно в проєктах <a href=\"/uk/projects/joker/\">Joker</a>, <a href=\"/uk/projects/true-religion/\">True Religion</a> і <a href=\"/uk/projects/sturmvogel/\">Sturmvogel</a>.",
        "hd.introP2": "Ми — незалежна майстерня з Harley-Davidson, і це бренд, з яким працюємо найбільше. Сервіс, ремонт, модифікації, апґрейди, повний кастом — для нас це не підробіток, а основна робота щотижня.",
        "hd.introP3": "Беремо всі сучасні платформи: Sportster (XL, RH Sportster S, Nightster), родину Softail, Dyna (legacy), Touring (Road King, Street Glide, Road Glide, Electra Glide, Tri Glide), V-Rod (legacy) і Pan America. Стоковий мотоцикл на щодень чи Twin Cam 2003 року з пробігом 130 000 км — розберемося, що йому потрібно.",

        "hd.toolsEyebrow": "Спеціалізований інструмент",
        "hd.toolsTitle": "Діагностика й інструмент <em>під Harley.</em>",
        "hd.toolsLead": "Діагностичне обладнання під Harley-Davidson, тюнери та сервісний інструмент — усе це збиралося за десять років роботи з маркою. Саме це відрізняє спеціаліста з Harley від майстерні «на всі руки».",
        "hd.t1t": "Digital Technician II / еквівалент",
        "hd.t1d": "Дилерська діагностика Harley: читання і запис ECM, живі дані, адаптивні скидання, програмування модулів.",
        "hd.t2t": "Свій дино-стенд",
        "hd.t2d": "Дино-налаштування прошивок ECU під сетапи Stage I/II/IV, під вихлоп та індивідуальні карти конкретного клієнта.",
        "hd.t3t": "Інструмент компенсатора і primary",
        "hd.t3d": "Спеціальні знімачі та процедури затяжки для compensator і primary sprocket — без них до Twin Cam і Milwaukee-Eight краще не підходити.",
        "hd.t4t": "Race Tuner / Power Vision / SE Pro Street",
        "hd.t4d": "Працюємо з усіма основними афтермаркет-тюнерами Harley: встановлення, прошивка карти, перевірка на дино.",

        "hd.servicesEyebrow": "Що робимо на Harley",
        "hd.servicesTitle": "Сервіс. Продуктивність. <em>Кастом.</em>",
        "hd.servicesLead": "Сучасні й legacy-платформи Harley — від планового ТО до повних збірок Stage IV.",
        "hd.s1t": "Планове ТО (5k / 10k / 25k)",
        "hd.s1d": "Регламентне ТО Harley за вашою платформою: оливи двигуна, primary, КПП і всі перевірки за офіційним регламентом.",
        "hd.s2t": "Правильні рідини Harley",
        "hd.s2d": "Під кожну платформу заливаємо те, що належить за специфікацією: у Twin Cam, Milwaukee-Eight і Revolution Max вимоги різні.",
        "hd.s3t": "Ремінь приводу — огляд, натяг, заміна",
        "hd.s3d": "Натяг ременя — річ критична, і в неспеціалізованих сервісах його найчастіше виставляють неправильно. Ми робимо це за нормальною процедурою, із заміром.",
        "hd.s4t": "Сервіс компенсатора і primary chain",
        "hd.s4d": "Огляд, перевірка моменту затяжки, заміна за зносу. Без цього з вібраціями Twin Cam не розібратися.",
        "hd.s5t": "Апґрейди Stage I / Stage II / Stage IV",
        "hd.s5d": "Дино-налаштовані пакети: впуск, випуск, вали, головки, збільшений об'єм. Очікуваний приріст потужності фіксуємо на папері ще до початку робіт.",
        "hd.s6t": "Дино-налаштований вихлоп + прошивка ЕБУ",
        "hd.s6d": "Vance &amp; Hines, Screamin' Eagle Pro, S&amp;S, Rinehart, Bassani — ставимо й калібруємо на дино під конкретний мотоцикл.",
        "hd.s7t": "Апґрейди підвіски",
        "hd.s7d": "Öhlins, Progressive, Legend Air, Race Tech — змінюємо висоту, доводимо керованість і комфорт, робимо повний ребілд.",
        "hd.s8t": "Повний кастом — рама, фарба, ручні деталі",
        "hd.s8d": "Наша чемпіонська тема. Доробка рами, фарбування, шкіра, фрезерування під ТЗ — перевірено на Harley-based проєктах на кшталт <a href=\"/uk/projects/joker/\">Joker</a>, <a href=\"/uk/projects/true-religion/\">True Religion</a> і <a href=\"/uk/projects/sturmvogel/\">Sturmvogel</a>. Приносьте бриф. Під широку Harley-гуму, спицьовані колеса й кастомні колісні сетапи — наш <a href=\"/uk/shynomontazh-mototsykliv/\">мотоциклетний шиномонтаж</a>.",

        "hd.issuesEyebrow": "Типові болячки Harley",
        "hd.issuesTitle": "Ми це бачили <em>тисячу разів.</em>",
        "hd.issuesLead": "Коли спеціалізуєшся, ті самі болячки приходять щотижня. Ми вже знаємо, що дивитися насамперед, а де вистачить простого регулювання.",
        "hd.i1t": "Неправильно відрегульований ремінь приводу",
        "hd.i1d": "Найчастіше, з чим приїжджають із неспеціалізованих сервісів. Скидаємо й виставляємо заново — за процедурою і з вимірювачем.",
        "hd.i2t": "Стук компенсатора",
        "hd.i2d": "Фірмовий звук Twin Cam і Milwaukee-Eight. Знаходимо причину й усуваємо правильним інструментом і в правильній послідовності затяжки.",
        "hd.i3t": "Відмови статора й регулятора напруги",
        "hd.i3d": "Часта історія на моделях Touring. Спершу читаємо симптоми діагностикою і лише потім міняємо — без стрільби запчастинами навмання.",
        "hd.i4t": "Розтягнення primary chain і знос натягувача",
        "hd.i4d": "Інтервал регулювання нерідко пропускають. Ми перевіряємо й повертаємо все до заводської специфікації.",
        "hd.i5t": "Заводська карта vs афтермаркет-вихлоп",
        "hd.i5d": "Поставили афтермаркет-вихлоп і не перепрошили — суміш уже неправильна. Знімаємо на дино й переписуємо карту як треба.",

        "hd.modelsEyebrow": "Моделі, на яких працюємо",
        "hd.modelsTitle": "Усе родинне дерево <em>Harley.</em>",
        "hd.modelsLead": "Сучасне виробництво, класичний Twin Cam і ранніший, кастом-збірки — привозьте.",
        "hd.m1t": "Sportster",
        "hd.m1d": "XL 883 / 1200, XL Forty-Eight, XL 1200 Roadster, XL Iron, RH 1250 Sportster S, RH 975 Nightster.",
        "hd.m2t": "Softail",
        "hd.m2d": "Heritage Classic, Fat Boy, Breakout, Fat Bob, Street Bob, Sport Glide, Low Rider, Low Rider S, Slim, Standard.",
        "hd.m3t": "Dyna (legacy)",
        "hd.m3d": "Fat Bob, Wide Glide, Super Glide, Low Rider, Street Bob — платформа до 2018 року.",
        "hd.m4t": "Touring (CVO і стандарт)",
        "hd.m4d": "Road King, Street Glide, Road Glide, Electra Glide, Tri Glide Ultra, CVO Limited, CVO Street Glide.",
        "hd.m5t": "Pan America",
        "hd.m5d": "Pan America 1250 Standard і Special — Adventure-платформа з двигуном Revolution Max.",
        "hd.m6t": "V-Rod (legacy) та класика / кастом",
        "hd.m6d": "Night Rod, V-Rod Muscle, плюс вінтажні Shovelhead, Knucklehead і Panhead.",

        "hd.partsEyebrow": "Запчастини та афтермаркет",
        "hd.partsTitle": "Доступ до <em>найбільших каталогів Harley.</em>",
        "hd.partsLead": "Замовляємо через великі каталожні мережі OEM та афтермаркету Harley. Це прямий доступ до тисяч артикулів — запчастини, перформанс, кастом-фурнітура, вихлопи.",
        "hd.partsList": "<strong>Каталоги:</strong> Drag Specialties · Custom Chrome · Biltwell · V-Twin · J&amp;P Cycles · Performance Machine · S&amp;S Cycle · Vance &amp; Hines · Screamin' Eagle Performance · Roland Sands Design · Klock Werks · Rinehart · Bassani · Burly Brand · оригінальні запчастини Harley-Davidson через дистриб'юторську мережу.",

        "hd.faqEyebrow": "FAQ",
        "hd.faqTitle": "Часті питання.",
        "hd.q1": "Ви офіційний дилер Harley-Davidson?",
        "hd.a1": "Ні, ми незалежний спеціаліст із Harley — і це вам на користь: жодної дилерської націнки, свобода ставити оригінал чи performance-афтермаркет, і реальна експертиза з кожної платформи, а не просто шильдик із брендом. Із Harley ми працюємо понад десять років, і за нами кілька кастом-збірок на базі Harley з міжнародними нагородами.",
        "hd.q2": "Робите Stage I / II / IV апґрейди?",
        "hd.a2": "Так, це для нас профільна робота. Збираємо дино-налаштовані пакети із задокументованим приростом потужності. Stage I — це впуск, випуск і карта. Stage II додає вали й обробку головок. Stage IV — повна збірка зі збільшеним об'ємом. По кожному Stage даємо письмовий кошторис зі списком запчастин і очікуваним результатом ще до початку робіт.",
        "hd.q3": "Берете кастом і вінтажні Harley?",
        "hd.a3": "Так — на цьому й побудована наша репутація. Кілька наших кастом-проєктів на Harley посідали призові місця на AMD World Championship of Custom Bike Building. Привозьте мотоцикл або просто ідею — рама, деталі ручної роботи, фарбування, шкіра, робота з ECU, будь-що.",
        "hd.q4": "Скільки коштує Harley major service на 25,000 км?",
        "hd.a4": "Від €400 — залежить від платформи і від того, що реально потрібно. У роботу входять оливи двигуна, primary і КПП, огляд ременя, гальмівна рідина та пункти, специфічні для платформи. Письмовий кошторис даємо до початку робіт.",
        "hd.q5": "Чи можете замовити оригінальні Harley-запчастини в Португалію?",
        "hd.a5": "Так — у нас каталожний доступ до OEM і Genuine Harley. Замовимо те, що потрібно мотоциклу, зокрема рідкісні позиції, яких немає в магазинах по ЄС.",

        "hd.ctaEyebrow": "Коли ви готові — ми готові",
        "hd.ctaTitle": "Записуйте Harley на сервіс.",
        "hd.ctaText": "Напишіть у WhatsApp модель, рік і що треба зробити. Зорієнтуємо щодо найближчого слота і надішлемо письмовий кошторис до початку робіт.",
        "hd.btnBack": "На головну",
    },
    "pt": {
        "hd.eyebrow": "Harley-Davidson · Cascais / Grande Lisboa",
        "hd.h1": "Serviço Harley-Davidson<br/>em <span class=\"accent\">Cascais.</span>",
        "hd.sub": "Especialista independente Harley para Sportster, Softail, Touring e Pan America. Diagnóstico, serviço, peças e custom numa oficina com vários troféus de campeonato internacional conquistados em plataformas Harley-Davidson.",
        "hd.breadHome": "Início",
        "hd.h1Crumb": "Serviço Harley-Davidson",
        "hd.btnWA": "WhatsApp",
        "hd.btnSend": "Enviar pedido",
        "hd.heroAlt": "Motas Harley-Davidson em serviço na oficina Iron Custom Motors em Cascais",

        "hd.introEyebrow": "Porquê Harley connosco",
        "hd.introTitle": "Harley é a nossa <em>especialização mais profunda.</em>",
        "hd.introP1": "A Iron Custom Motors trabalha plataformas Harley-Davidson há mais de uma década. Várias das nossas construções custom premiadas internacionalmente — incluindo projetos que subiram ao pódio no AMD World Championship of Custom Bike Building — foram em base Harley. Essa história não é decoração: é a razão por que conhecemos estas motos por dentro. Essa experiência Harley / American custom vê-se em <a href=\"/pt/projects/joker/\">Joker</a>, <a href=\"/pt/projects/true-religion/\">True Religion</a> e <a href=\"/pt/projects/sturmvogel/\">Sturmvogel</a>.",
        "hd.introP2": "Somos uma oficina independente Harley-Davidson, e Harley é a marca com que mais trabalhamos. Serviço, reparação, modificações, upgrades de performance, custom completo — nada disto é trabalho secundário. É o núcleo do que fazemos todas as semanas.",
        "hd.introP3": "Trabalhamos com todas as plataformas modernas: Sportster (XL, RH Sportster S, Nightster), família Softail, Dyna (legacy), Touring (Road King, Street Glide, Road Glide, Electra Glide, Tri Glide), V-Rod (legacy) e Pan America. Seja uma stock daily ou uma Twin Cam de 2003 com 130 000 km, sabemos o que a sua moto precisa.",

        "hd.toolsEyebrow": "Ferramenta especialista",
        "hd.toolsTitle": "Diagnóstico e ferramenta <em>Harley-específica.</em>",
        "hd.toolsLead": "Equipamento de diagnóstico Harley-Davidson, tuners de performance e ferramenta de serviço, acumulados ao longo de uma década de trabalho em Harley. É isto que separa um especialista Harley de uma oficina genérica.",
        "hd.t1t": "Digital Technician II / equivalente",
        "hd.t1d": "Diagnóstico Harley ao nível de concessionário — leitura/escrita ECM, dados ao vivo, resets adaptativos e programação de módulos.",
        "hd.t2t": "Dyno próprio",
        "hd.t2d": "Mapas ECU dyno-tuned para setups Stage I/II/IV, upgrades de escape e maps individuais por cliente.",
        "hd.t3t": "Ferramenta compensador / primary",
        "hd.t3d": "Extratores e procedimentos de binário para o compensator e o primary sprocket — crítico em Twin Cam e Milwaukee-Eight.",
        "hd.t4t": "Race Tuner / Power Vision / SE Pro Street",
        "hd.t4d": "Suporte para os principais tuners aftermarket Harley — instalação, mapa e verificação em dyno.",

        "hd.servicesEyebrow": "O que fazemos em Harley",
        "hd.servicesTitle": "Serviço. Performance. <em>Custom.</em>",
        "hd.servicesLead": "Em plataformas Harley modernas e legacy — desde intervalos de serviço de rotina a builds Stage IV completos.",
        "hd.s1t": "Manutenção programada (5k / 10k / 25k)",
        "hd.s1d": "Serviço por intervalo Harley conforme a plataforma — óleos do motor, primary e transmissão, com todas as verificações que a tabela oficial exige.",
        "hd.s2t": "Fluidos Harley corretos",
        "hd.s2d": "Usamos a especificação de fluido certa para cada plataforma. Twin Cam, Milwaukee-Eight e Revolution Max têm, cada um, os seus requisitos.",
        "hd.s3t": "Correia de transmissão — inspeção, tensão, substituição",
        "hd.s3d": "A tensão da correia é crítica, e a maioria das oficinas não-especialistas erra aqui. Acertamos com o procedimento de medição correto.",
        "hd.s4t": "Serviço compensador e primary chain",
        "hd.s4d": "Inspeção, verificação de binário, substituição quando há desgaste. Crítico para a vibração em Twin Cam.",
        "hd.s5t": "Upgrades Stage I / Stage II / Stage IV",
        "hd.s5d": "Pacotes dyno-tuned — admissão, escape, cames, cabeças, maior cilindrada. O ganho de potência estimado fica documentado antes de começar o trabalho.",
        "hd.s6t": "Escape dyno-tuned + remapeamento ECU",
        "hd.s6d": "Vance &amp; Hines, Screamin' Eagle Pro, S&amp;S, Rinehart, Bassani — instalados e calibrados em dyno para a sua moto.",
        "hd.s7t": "Upgrades de suspensão",
        "hd.s7d": "Öhlins, Progressive, Legend Air, Race Tech — alterações de altura, correção de comportamento, reconstrução completa.",
        "hd.s8t": "Custom completo — quadro, pintura, peças à mão",
        "hd.s8d": "O nosso trabalho campeão. Modificações de quadro, pintura, couro, peças maquinadas à mão — provado em projetos Harley-based como <a href=\"/pt/projects/joker/\">Joker</a>, <a href=\"/pt/projects/true-religion/\">True Religion</a> e <a href=\"/pt/projects/sturmvogel/\">Sturmvogel</a>. Traga o brief. Para pneus Harley largos, rodas raiadas e setups custom de rodas, veja o nosso serviço de <a href=\"/pt/montagem-de-pneus-mota/\">montagem e equilibragem de pneus de mota</a>.",

        "hd.issuesEyebrow": "Problemas típicos Harley",
        "hd.issuesTitle": "Já vimos isto <em>mil vezes.</em>",
        "hd.issuesLead": "Quando há especialização, são sempre os mesmos problemas a aparecer todas as semanas. Sabemos o que verificar primeiro e o que só precisa de ajuste.",
        "hd.i1t": "Tensão de correia mal ajustada",
        "hd.i1d": "O problema mais comum quando a moto chega de oficinas não-especialistas. Repomos com procedimento e medidor corretos.",
        "hd.i2t": "Ruído do compensador",
        "hd.i2d": "O som assinatura das Twin Cam / Milwaukee-Eight. Diagnosticamos e corrigimos com a ferramenta e a sequência de binário certas.",
        "hd.i3t": "Falhas de stator e regulador de tensão",
        "hd.i3d": "Comum em modelos Touring. Lemos os sintomas no diagnóstico antes de substituir seja o que for — sem disparar peças à toa.",
        "hd.i4t": "Estiramento da primary chain e desgaste do ajustador",
        "hd.i4d": "O intervalo de ajuste é frequentemente ignorado. Verificamos e regulamos para a spec de fábrica.",
        "hd.i5t": "Mapa de fábrica vs ponteiras aftermarket",
        "hd.i5d": "Se montou ponteiras aftermarket sem remapear, a mistura está errada. Fazemos dyno e remapeamento como deve ser.",

        "hd.modelsEyebrow": "Modelos com que trabalhamos",
        "hd.modelsTitle": "Por toda a <em>árvore Harley.</em>",
        "hd.modelsLead": "Produção atual, Twin Cam clássico e anterior, custom — traga.",
        "hd.m1t": "Sportster",
        "hd.m1d": "XL 883 / 1200, XL Forty-Eight, XL 1200 Roadster, XL Iron, RH 1250 Sportster S, RH 975 Nightster.",
        "hd.m2t": "Softail",
        "hd.m2d": "Heritage Classic, Fat Boy, Breakout, Fat Bob, Street Bob, Sport Glide, Low Rider, Low Rider S, Slim, Standard.",
        "hd.m3t": "Dyna (legacy)",
        "hd.m3d": "Fat Bob, Wide Glide, Super Glide, Low Rider, Street Bob — plataforma pré-2018.",
        "hd.m4t": "Touring (CVO e standard)",
        "hd.m4d": "Road King, Street Glide, Road Glide, Electra Glide, Tri Glide Ultra, CVO Limited, CVO Street Glide.",
        "hd.m5t": "Pan America",
        "hd.m5d": "Pan America 1250 Standard e Special — Adventure com motor Revolution Max.",
        "hd.m6t": "V-Rod (legacy) e clássico / custom",
        "hd.m6d": "Night Rod, V-Rod Muscle, mais Shovelhead, Knucklehead e Panhead vintage.",

        "hd.partsEyebrow": "Peças e aftermarket",
        "hd.partsTitle": "Acesso aos <em>maiores catálogos Harley.</em>",
        "hd.partsLead": "Encomendamos através das grandes redes de catálogos OEM e aftermarket Harley — acesso direto a milhares de SKUs em peças, performance, hardware custom e escapes.",
        "hd.partsList": "<strong>Catálogos:</strong> Drag Specialties · Custom Chrome · Biltwell · V-Twin · J&amp;P Cycles · Performance Machine · S&amp;S Cycle · Vance &amp; Hines · Screamin' Eagle Performance · Roland Sands Design · Klock Werks · Rinehart · Bassani · Burly Brand · peças originais Harley-Davidson via rede de distribuidores.",

        "hd.faqEyebrow": "FAQ",
        "hd.faqTitle": "Perguntas frequentes.",
        "hd.q1": "São concessionário Harley-Davidson autorizado?",
        "hd.a1": "Não, somos especialista independente Harley — e isso joga a seu favor: sem markup de concessionário, liberdade para usar peças OEM ou de performance aftermarket, e conhecimento profundo de cada plataforma em vez de apenas o crachá da marca. Trabalhamos Harley há mais de uma década, com várias builds Harley premiadas internacionalmente.",
        "hd.q2": "Fazem upgrades Stage I / II / IV?",
        "hd.a2": "Sim — é trabalho central para nós. Montamos pacotes dyno-tuned com ganhos de potência documentados. Stage I é admissão, escape e mapa. Stage II acrescenta cames e trabalho de cabeças. Stage IV é um build completo de performance com maior cilindrada. Cada Stage chega como orçamento escrito, com lista de peças e resultados esperados, antes de começar.",
        "hd.q3": "Fazem Harley custom e vintage?",
        "hd.a3": "Sim — foi nisto que construímos a reputação. Vários dos nossos projetos custom Harley subiram ao pódio no AMD World Championship of Custom Bike Building. Traga a moto ou traga o sonho — trabalho de quadro, peças feitas à mão, pintura, couro, trabalho ECU, tudo.",
        "hd.q4": "Quanto custa um Harley major service de 25,000 km?",
        "hd.a4": "A partir de €400, conforme a plataforma e o que for preciso. Inclui óleos do motor, primary e transmissão, inspeção de correia, fluido de travões, mais os itens específicos da plataforma. Orçamento escrito antes de começar.",
        "hd.q5": "Conseguem importar peças OEM Harley para Portugal?",
        "hd.a5": "Sim — temos acesso de catálogo a peças OEM e Genuine Harley. Encomendamos o que a sua moto precisa, incluindo itens difíceis que as lojas da UE não têm em stock.",

        "hd.ctaEyebrow": "Prontos quando estiver",
        "hd.ctaTitle": "Agende a sua Harley.",
        "hd.ctaText": "Envie o modelo, o ano e o que é necessário via WhatsApp. Voltamos com o slot disponível mais próximo e um orçamento escrito antes de começar.",
        "hd.btnBack": "Voltar ao início",
    },
}

# ====================================================================================
# Ducati
# ====================================================================================
PAGE_I18N["ducati-service"] = {
    "en": {
        "duc.eyebrow": "Ducati · Cascais / Greater Lisbon",
        "duc.h1": "Ducati service<br/>in <span class=\"accent\">Cascais.</span>",
        "duc.sub": "Independent Ducati workshop — desmodromic valve service, electronics, suspension, exhaust install and full custom for Monster, Panigale, Multistrada, Scrambler, Streetfighter, Diavel.",
        "duc.breadHome": "Home",
        "duc.h1Crumb": "Ducati service",
        "duc.btnWA": "WhatsApp us",
        "duc.btnSend": "Send a request",
        "duc.heroAlt": "Ducati service bay at Iron Custom Motors workshop in Cascais",
        "duc.introEyebrow": "Why Ducati owners come to us",
        "duc.introTitle": "Desmo done <em>properly.</em>",
        "duc.introP1": "Iron Custom Motors is an independent Ducati specialist in Cascais. The desmodromic valve train, the layered electronics, semi-active suspension, dry and wet clutches — we know how each Ducati family behaves and where it likes to give trouble. The bike that makes most independent shops nervous is the one that's on our bench every week.",
        "duc.introP2": "The desmo service is where a lot of Ducati owners get blindsided by the bill at the dealer. We do it the way it's meant to be done — on the correct interval, at independent-workshop rates — and you get the work documented in writing, so there's no guessing about what was actually touched.",
        "duc.introP3": "We cover the modern range: Monster (air- and water-cooled), Panigale V2/V4, Multistrada V2/V4/V4 Rally, the Scrambler family, Streetfighter V2/V4, Diavel, Hypermotard, SuperSport. Everything from a daily street bike to a full track-day build for Estoril.",
        "duc.toolsEyebrow": "Specialist tooling",
        "duc.toolsTitle": "Ducati-specific <em>diagnostic and tools.</em>",
        "duc.toolsLead": "Proper Ducati diagnostics, the desmo-specific service tooling, and in-house dyno tuning. The desmo service in particular needs dedicated tools and a full shim-selection range that a general workshop simply doesn't stock — we do.",
        "duc.t1t": "Ducati Diagnostic System (DDS) / equivalent",
        "duc.t1d": "Read codes, watch live data, run ECU adaptations and component coding across the modern Ducati electronics.",
        "duc.t2t": "Desmo service tooling",
        "duc.t2d": "Rocker pullers, shim-selection kit, dedicated feeler gauges. The right tools to set clearances accurately, not by feel.",
        "duc.t3t": "Cam belt locking and timing tools (older models)",
        "duc.t3d": "The specific tools for cam belt service on pre-Panigale Ducati — done by the book, with the engine locked correctly.",
        "duc.t4t": "In-house dyno + Termignoni / Akrapovič tuning",
        "duc.t4d": "Dyno-verified ECU maps for full exhaust systems. We install, flash and confirm the result on the dyno.",
        "duc.servicesEyebrow": "What we do on Ducati",
        "duc.servicesTitle": "Service. <em>Desmo. Tuning.</em>",
        "duc.servicesLead": "Routine intervals, the desmo, custom suspension, exhaust and ECU work, track-day prep — and the rare jobs other shops would rather not take on.",
        "duc.s1t": "Desmo service (valve clearance)",
        "duc.s1d": "On the correct interval for the model: 24,000 km on older Ducati, 30,000 km intake / 60,000 km exhaust on Panigale V4 / Multi V4. Written before/after report.",
        "duc.s2t": "Scheduled service (oil + filter + checks)",
        "duc.s2d": "To Ducati intervals — oil, filter, fluids, brake check, chain inspection, plus the model-specific items.",
        "duc.s3t": "Cam belt service (older models)",
        "duc.s3d": "Done properly with locking tools and a new tensioner — required at the model's set interval, no shortcuts.",
        "duc.s4t": "Dry clutch service",
        "duc.s4d": "Older Monster, 916, 996, 999 — basket inspection, plate measurement, replacement where it's worn.",
        "duc.s5t": "Wet clutch service",
        "duc.s5d": "Modern Panigale, Multi V4, Streetfighter V4 — friction plate inspection, drag clearance, hydraulic bleed.",
        "duc.s6t": "Suspension service",
        "duc.s6d": "Öhlins service, semi-active suspension diagnostics (Sachs, Marzocchi), full fork and shock rebuild.",
        "duc.s7t": "Exhaust install (Termignoni, Akrapovič) + map",
        "duc.s7d": "Full system or slip-on with the matching ECU map — dyno-verified.",
        "duc.s8t": "Track-day prep",
        "duc.s8d": "Suspension setup, braided lines and pad upgrade, slick fitment, ride height and lap-time work. Ducati run wide rubber and sport-spec rims, so if you want a dedicated set of track wheels mounted and balanced we handle that through our <a href=\"/motorcycle-tyre-service/\">motorcycle tyre service</a>.",
        "duc.issuesEyebrow": "Typical Ducati issues we know",
        "duc.issuesTitle": "Where the <em>desmo bites.</em>",
        "duc.issuesLead": "Years on the platform mean we know how these bikes fail. Caught early, most of it is a routine fix. Left too long, it gets expensive.",
        "duc.i1t": "Valve clearance drift on desmo",
        "duc.i1d": "Usually missed because the service gets put off. We measure it properly and correct it with the right shims — not just nod at the symptom.",
        "duc.i2t": "Ride-by-wire throttle desync",
        "duc.i2d": "Common on the modern bikes. We re-sync it through DDS and confirm it's clean on live data.",
        "duc.i3t": "Battery / charging on bikes parked over winter",
        "duc.i3d": "A modern Ducati can flatten its own battery with all the electronics asleep. We diagnose it and set you up with a proper trickle charger.",
        "duc.i4t": "Dry clutch basket wear (older Monsters)",
        "duc.i4d": "That signature dry-clutch rattle hides real wear. We measure the basket clearances properly instead of guessing.",
        "duc.i5t": "Electronic suspension calibration errors",
        "duc.i5d": "Sachs / Marzocchi self-calibration faults. We reset them with the correct tool and check the damping actually responds.",
        "duc.modelsEyebrow": "Models we service",
        "duc.modelsTitle": "Across the Ducati <em>lineup.</em>",
        "duc.modelsLead": "Modern water-cooled, older air-cooled, track and supersport — bring it in.",
        "duc.m1t": "Monster",
        "duc.m1d": "696, 796, 821, 937, 950, 1100, 1200 — air-cooled and water-cooled versions.",
        "duc.m2t": "Panigale",
        "duc.m2d": "899, 959, 1199, 1299, V2, V4, V4 S, V4 R, V4 SP.",
        "duc.m3t": "Multistrada",
        "duc.m3d": "950, 1200, 1260, V2, V4, V4 S, V4 Rally, V4 Pikes Peak.",
        "duc.m4t": "Streetfighter",
        "duc.m4d": "848, V2, V4, V4 S, V4 SP.",
        "duc.m5t": "Scrambler",
        "duc.m5d": "Icon, Café Racer, Desert Sled, Full Throttle, Nightshift, 1100 Sport, 1100 Dark Pro.",
        "duc.m6t": "Diavel, Hypermotard, SuperSport &amp; classic",
        "duc.m6d": "Diavel 1260, Diavel V4; Hypermotard 821/939/950; SuperSport 939/950; plus 916/996/999 vintage projects.",
        "duc.partsEyebrow": "Parts and aftermarket",
        "duc.partsTitle": "Catalog access for <em>major Ducati parts.</em>",
        "duc.partsLead": "We source Ducati OEM, Ducati Performance and the best Italian and international Ducati aftermarket through trusted catalog and supplier networks. From a single brake pad to a full Akrapovič system to a CNC Racing dress kit — we'll order it in.",
        "duc.partsList": "<strong>Catalogs we work with:</strong> Ducati Performance · DucatiOmnia · Termignoni · Akrapovič · Öhlins · ÖHLINS Mechatronic · Brembo · STM Italy · Rizoma · CNC Racing · Ducabike · Carbonin · Spark · MWR · BST · OEM Ducati parts via distributor network.",
        "duc.faqEyebrow": "FAQ",
        "duc.faqTitle": "Common questions.",
        "duc.q1": "How often is desmo service really needed?",
        "duc.a1": "It depends on the model and year. Older Ducati: 24,000 km. Modern Panigale V4 / Multistrada V4: 30,000 km on the intake valves, 60,000 km on the exhaust valves. We check it against your bike's specific schedule before quoting.",
        "duc.q2": "How much does a desmo service cost at Iron Custom Motors?",
        "duc.a2": "It's priced per model — from €750 for older Monsters, up to €1,500+ for a Panigale V4 with full inspection. Against a dealer bill, that's usually 30–40% less. You get it in writing before any work starts.",
        "duc.q3": "Can you flash a Termignoni / Akrapovič map onto my Ducati?",
        "duc.a3": "Yes — we fit the exhaust (full system or slip-on) and upload the matched ECU map. Termignoni race kit, Akrapovič with eCU, third-party maps where needed. The result is dyno-verified and documented.",
        "duc.q4": "Do you do track-day prep for Panigale / Streetfighter / Multistrada?",
        "duc.a4": "Yes — suspension setup, brake lines and pads, slick fitment, ride height, ECU map dialled in to the circuit. We've prepped bikes for Estoril, Portimão and Jarama.",
        "duc.q5": "Are you an authorized Ducati dealer?",
        "duc.a5": "No — we're an independent Ducati workshop. The upside is transparent pricing (desmo at independent rates, not dealer rates) and the freedom to fit OEM Ducati Performance or top-tier aftermarket. We work with all the major Ducati distributors and have full catalog access.",
        "duc.ctaEyebrow": "Ready when you are",
        "duc.ctaTitle": "Bring your Ducati in.",
        "duc.ctaText": "Send the model, year and what it needs over WhatsApp. We'll come back with the nearest available slot and a written estimate before any work starts.",
        "duc.btnBack": "Back to home",
    },
    "ru": {
        "duc.eyebrow": "Ducati · Кашкайш / Большой Лиссабон",
        "duc.h1": "Сервис Ducati<br/>в <span class=\"accent\">Кашкайше.</span>",
        "duc.sub": "Независимая мастерская Ducati — десмодромный клапанный сервис, электроника, подвеска, установка выхлопа и полный кастом для Monster, Panigale, Multistrada, Scrambler, Streetfighter, Diavel.",
        "duc.breadHome": "Главная",
        "duc.h1Crumb": "Сервис Ducati",
        "duc.btnWA": "WhatsApp",
        "duc.btnSend": "Отправить заявку",
        "duc.heroAlt": "Зона сервиса Ducati в мастерской Iron Custom Motors, Кашкайш",

        "duc.introEyebrow": "Почему владельцы Ducati — к нам",
        "duc.introTitle": "Desmo сделанный <em>правильно.</em>",
        "duc.introP1": "Iron Custom Motors — независимый специалист по Ducati в Кашкайше. Десмодромный газораспределительный механизм, навороченная электроника, полуактивная подвеска, сухие и мокрые сцепления — мы знаем, как ведёт себя каждое семейство Ducati и где у него обычно вылезают проблемы. Мотоцикл, от которого нервничает большинство независимых сервисов, у нас на подъёмнике каждую неделю.",
        "duc.introP2": "Desmo-сервис — это то место, где у дилера многие владельцы Ducati неприятно удивляются счёту. Мы делаем его так, как положено: в нужный интервал, по ценам независимой мастерской — и отдаём работу с письменным отчётом, чтобы не оставалось вопросов, что именно трогали.",
        "duc.introP3": "Работаем со всей современной линейкой: Monster (воздушник и водянка), Panigale V2/V4, Multistrada V2/V4/V4 Rally, семейство Scrambler, Streetfighter V2/V4, Diavel, Hypermotard, SuperSport. От мотоцикла на каждый день до полного трек-билда под Эшторил.",

        "duc.toolsEyebrow": "Специализированный инструмент",
        "duc.toolsTitle": "Диагностика и инструмент <em>под Ducati.</em>",
        "duc.toolsLead": "Нормальная Ducati-диагностика, специальный инструмент под desmo-сервис и собственный дино для настройки. Desmo-сервис, в частности, требует отдельного инструмента и полного набора шайб под подбор зазоров, которых у обычного сервиса попросту нет в наличии — у нас есть.",
        "duc.t1t": "Ducati Diagnostic System (DDS) / эквивалент",
        "duc.t1d": "Читаем коды, смотрим живые данные, делаем ECU-адаптации и кодирование компонентов на всей современной электронике Ducati.",
        "duc.t2t": "Инструмент desmo-сервиса",
        "duc.t2d": "Съёмники коромысел, набор шайб под подбор, специальные щупы. Тот инструмент, которым зазоры выставляются точно, а не на глаз.",
        "duc.t3t": "Инструмент cam belt-локов (для старых моделей)",
        "duc.t3d": "Специальный инструмент для сервиса ремня ГРМ на до-Panigale Ducati — строго по процедуре, с правильной фиксацией.",
        "duc.t4t": "Свой дино + тюнинг под Termignoni / Akrapovič",
        "duc.t4d": "Дино-проверенные ECU-карты под полные выхлопные системы. Ставим, прошиваем и подтверждаем результат на дино.",

        "duc.servicesEyebrow": "Что делаем на Ducati",
        "duc.servicesTitle": "Сервис. <em>Desmo. Тюнинг.</em>",
        "duc.servicesLead": "Регламентные интервалы, desmo, кастом-подвеска, выхлоп и работа с ECU, трек-преп — и редкие работы, за которые другие сервисы браться не хотят.",
        "duc.s1t": "Desmo-сервис (зазоры клапанов)",
        "duc.s1d": "В нужный интервал по модели: 24,000 км на старых Ducati, 30,000 км по впуску / 60,000 км по выпуску на Panigale V4 / Multi V4. Письменный отчёт до и после.",
        "duc.s2t": "Плановое ТО (масло + фильтр + проверки)",
        "duc.s2d": "По регламенту Ducati — масло, фильтр, жидкости, тормоза, цепь, плюс позиции под конкретную модель.",
        "duc.s3t": "Сервис ремня ГРМ (старые модели)",
        "duc.s3d": "Делаем как положено, с фиксаторами и новым натяжителем — обязательно в регламентный интервал, без срезания углов.",
        "duc.s4t": "Сервис сухого сцепления",
        "duc.s4d": "Старые Monster, 916, 996, 999 — осмотр корзины, замер дисков, замена там, где есть износ.",
        "duc.s5t": "Сервис мокрого сцепления",
        "duc.s5d": "Современный Panigale, Multi V4, Streetfighter V4 — осмотр фрикционов, зазор на ведение, прокачка гидравлики.",
        "duc.s6t": "Подвеска",
        "duc.s6d": "Сервис Öhlins, диагностика полуактивной подвески (Sachs, Marzocchi), полный ребилд вилки и амортизатора.",
        "duc.s7t": "Выхлоп (Termignoni, Akrapovič) + карта",
        "duc.s7d": "Полная система или slip-on с подходящей ECU-картой — проверено на дино.",
        "duc.s8t": "Трек-преп",
        "duc.s8d": "Настройка подвески, армированные тормозные линии и колодки получше, установка сликов, ride height и работа над временем на круге. У Ducati широкая резина и спортивные диски, так что если нужен отдельный комплект трековых колёс — соберём и отбалансируем через наш <a href=\"/ru/shinomontazh-mototsiklov/\">шиномонтаж мотоциклов</a>.",

        "duc.issuesEyebrow": "Типичные болезни Ducati",
        "duc.issuesTitle": "Где <em>кусает desmo.</em>",
        "duc.issuesLead": "Годы на этой платформе — это понимание, как именно она ломается. Поймал вовремя — почти всё лечится рутинно. Затянул — выходит дорого.",
        "duc.i1t": "Уход зазоров клапанов на desmo",
        "duc.i1d": "Чаще всего пропускают, потому что сервис откладывают. Мы нормально замеряем и подбираем шайбу как надо — а не просто констатируем симптом.",
        "duc.i2t": "Десинхронизация ride-by-wire",
        "duc.i2d": "Частая история на современных. Пересинхронизируем через DDS и проверяем по живым данным, что всё чисто.",
        "duc.i3t": "АКБ / зарядка на «зимующих» мотоциклах",
        "duc.i3d": "Современный Ducati может посадить себе аккумулятор сам, при «спящей» электронике. Находим причину и советуем нормальный trickle charger.",
        "duc.i4t": "Износ корзины сухого сцепления (старый Monster)",
        "duc.i4d": "Тот самый фирменный стрёкот сухого сцепления прячет реальный износ. Мы замеряем зазоры корзины как надо, а не на слух.",
        "duc.i5t": "Ошибки калибровки электронной подвески",
        "duc.i5d": "Сбои самокалибровки Sachs / Marzocchi. Сбрасываем правильным инструментом и проверяем, что демпфирование реально отрабатывает.",

        "duc.modelsEyebrow": "Модели на которых работаем",
        "duc.modelsTitle": "Вся линейка <em>Ducati.</em>",
        "duc.modelsLead": "Современная водянка, старый воздушник, трек / суперспорт — привозите.",
        "duc.m1t": "Monster",
        "duc.m1d": "696, 796, 821, 937, 950, 1100, 1200 — воздушные и водяные версии.",
        "duc.m2t": "Panigale",
        "duc.m2d": "899, 959, 1199, 1299, V2, V4, V4 S, V4 R, V4 SP.",
        "duc.m3t": "Multistrada",
        "duc.m3d": "950, 1200, 1260, V2, V4, V4 S, V4 Rally, V4 Pikes Peak.",
        "duc.m4t": "Streetfighter",
        "duc.m4d": "848, V2, V4, V4 S, V4 SP.",
        "duc.m5t": "Scrambler",
        "duc.m5d": "Icon, Café Racer, Desert Sled, Full Throttle, Nightshift, 1100 Sport, 1100 Dark Pro.",
        "duc.m6t": "Diavel, Hypermotard, SuperSport и классика",
        "duc.m6d": "Diavel 1260, Diavel V4; Hypermotard 821/939/950; SuperSport 939/950; плюс винтажные 916/996/999.",

        "duc.partsEyebrow": "Запчасти и афтермаркет",
        "duc.partsTitle": "Доступ к <em>крупным каталогам Ducati.</em>",
        "duc.partsLead": "Заказываем Ducati OEM, Ducati Performance и топовый итальянский и международный афтермаркет через проверенные сети каталогов и поставщиков. От одной тормозной колодки до полной системы Akrapovič и dress-kit от CNC Racing — закажем.",
        "duc.partsList": "<strong>Каталоги:</strong> Ducati Performance · DucatiOmnia · Termignoni · Akrapovič · Öhlins · ÖHLINS Mechatronic · Brembo · STM Italy · Rizoma · CNC Racing · Ducabike · Carbonin · Spark · MWR · BST · оригинал Ducati через дистрибьюторскую сеть.",

        "duc.faqEyebrow": "FAQ",
        "duc.faqTitle": "Частые вопросы.",
        "duc.q1": "Как часто реально нужен desmo-сервис?",
        "duc.a1": "Зависит от модели и года. Старые Ducati: 24,000 км. Современный Panigale V4 / Multistrada V4: 30,000 км по впуску, 60,000 км по выпуску. Уточняем по конкретному регламенту вашего мотоцикла до сметы.",
        "duc.q2": "Сколько стоит desmo-сервис у Iron Custom Motors?",
        "duc.a2": "Цена по модели — от €750 для старых Monster, до €1,500+ для Panigale V4 с полной проверкой. По сравнению с дилерским счётом обычно на 30–40% дешевле. Письменная смета до начала работ.",
        "duc.q3": "Прошьёте карту Termignoni / Akrapovič на мой Ducati?",
        "duc.a3": "Да — ставим выхлоп (полную систему или slip-on) и заливаем подходящую ECU-карту. Termignoni race kit, Akrapovič с eCU, сторонние карты по запросу. Результат проверен на дино и задокументирован.",
        "duc.q4": "Делаете трек-преп для Panigale / Streetfighter / Multistrada?",
        "duc.a4": "Да — настройка подвески, тормозные линии и колодки, слики, ride height, ECU-карта под профиль трассы. Готовили мотоциклы под Эшторил, Портимау и Хараму.",
        "duc.q5": "Вы официальный дилер Ducati?",
        "duc.a5": "Нет — мы независимая мастерская Ducati. Плюс в прозрачных ценах (desmo по ценам независимой мастерской, а не дилерским) и в свободе ставить OEM Ducati Performance или топовый афтермаркет. Работаем со всеми крупными дистрибьюторами Ducati, полный доступ к каталогам есть.",

        "duc.ctaEyebrow": "Когда готовы — мы готовы",
        "duc.ctaTitle": "Привозите ваш Ducati.",
        "duc.ctaText": "Напишите модель, год и в двух словах суть в WhatsApp. Сориентируем по ближайшему слоту и пришлём письменную смету до начала работ.",
        "duc.btnBack": "На главную",
    },
    "uk": {
        "duc.eyebrow": "Ducati · Кашкайш / Великий Лісабон",
        "duc.h1": "Сервіс Ducati<br/>у <span class=\"accent\">Кашкайші.</span>",
        "duc.sub": "Незалежна майстерня Ducati — десмодромний клапанний сервіс, електроніка, підвіска, встановлення вихлопу й повний кастом для Monster, Panigale, Multistrada, Scrambler, Streetfighter, Diavel.",
        "duc.breadHome": "Головна",
        "duc.h1Crumb": "Сервіс Ducati",
        "duc.btnWA": "WhatsApp",
        "duc.btnSend": "Надіслати заявку",
        "duc.heroAlt": "Зона сервісу Ducati у майстерні Iron Custom Motors, Кашкайш",

        "duc.introEyebrow": "Чому власники Ducati — до нас",
        "duc.introTitle": "Desmo зроблений <em>правильно.</em>",
        "duc.introP1": "Iron Custom Motors — незалежний спеціаліст з Ducati у Кашкайші. Десмодромний газорозподільний механізм, нашпигована електроніка, напівактивна підвіска, сухі й мокрі зчеплення — ми знаємо, як поводиться кожна родина Ducati і де в неї зазвичай вилазять проблеми. Мотоцикл, від якого нервується більшість незалежних сервісів, у нас на підйомнику щотижня.",
        "duc.introP2": "Desmo-сервіс — це те місце, де в дилера багато власників Ducati неприємно дивуються рахунку. Ми робимо його так, як належить: у потрібний інтервал, за цінами незалежної майстерні — і віддаємо роботу з письмовим звітом, щоб не лишалося питань, що саме чіпали.",
        "duc.introP3": "Працюємо з усією сучасною лінійкою: Monster (повітряник і водянка), Panigale V2/V4, Multistrada V2/V4/V4 Rally, родина Scrambler, Streetfighter V2/V4, Diavel, Hypermotard, SuperSport. Від мотоцикла на щодень до повного трек-білда під Ешторил.",

        "duc.toolsEyebrow": "Спеціалізований інструмент",
        "duc.toolsTitle": "Діагностика й інструмент <em>під Ducati.</em>",
        "duc.toolsLead": "Нормальна Ducati-діагностика, спеціальний інструмент під desmo-сервіс і власний дино для налаштування. Desmo-сервіс, зокрема, вимагає окремого інструмента й повного набору шайб під підбір зазорів, яких у звичайного сервісу просто немає в наявності — у нас є.",
        "duc.t1t": "Ducati Diagnostic System (DDS) / еквівалент",
        "duc.t1d": "Читаємо коди, дивимось живі дані, робимо ECU-адаптації та кодування компонентів на всій сучасній електроніці Ducati.",
        "duc.t2t": "Інструмент desmo-сервісу",
        "duc.t2d": "Знімачі коромисел, набір шайб під підбір, спеціальні щупи. Той інструмент, яким зазори виставляються точно, а не на око.",
        "duc.t3t": "Інструмент cam belt-локів (для старих моделей)",
        "duc.t3d": "Спеціальний інструмент для сервісу ременя ГРМ на до-Panigale Ducati — суворо за процедурою, з правильною фіксацією.",
        "duc.t4t": "Свій дино + тюнінг під Termignoni / Akrapovič",
        "duc.t4d": "Дино-перевірені ECU-карти під повні вихлопні системи. Ставимо, прошиваємо й підтверджуємо результат на дино.",

        "duc.servicesEyebrow": "Що робимо на Ducati",
        "duc.servicesTitle": "Сервіс. <em>Desmo. Тюнінг.</em>",
        "duc.servicesLead": "Регламентні інтервали, desmo, кастом-підвіска, вихлоп і робота з ECU, трек-преп — і рідкісні роботи, за які інші сервіси братися не хочуть.",
        "duc.s1t": "Desmo-сервіс (зазори клапанів)",
        "duc.s1d": "У потрібний інтервал за моделлю: 24,000 км на старих Ducati, 30,000 км по впуску / 60,000 км по випуску на Panigale V4 / Multi V4. Письмовий звіт до і після.",
        "duc.s2t": "Планове ТО (олива + фільтр + перевірки)",
        "duc.s2d": "За регламентом Ducati — олива, фільтр, рідини, гальма, ланцюг, плюс позиції під конкретну модель.",
        "duc.s3t": "Сервіс ременя ГРМ (старі моделі)",
        "duc.s3d": "Робимо як належить, із фіксаторами та новим натягувачем — обов'язково в регламентний інтервал, без зрізання кутів.",
        "duc.s4t": "Сервіс сухого зчеплення",
        "duc.s4d": "Старі Monster, 916, 996, 999 — огляд корзини, замір дисків, заміна там, де є знос.",
        "duc.s5t": "Сервіс мокрого зчеплення",
        "duc.s5d": "Сучасний Panigale, Multi V4, Streetfighter V4 — огляд фрикційних дисків, зазор на ведення, прокачка гідравліки.",
        "duc.s6t": "Підвіска",
        "duc.s6d": "Сервіс Öhlins, діагностика напівактивної підвіски (Sachs, Marzocchi), повний ребілд вилки й амортизатора.",
        "duc.s7t": "Вихлоп (Termignoni, Akrapovič) + карта",
        "duc.s7d": "Повна система або slip-on із відповідною ECU-картою — перевірено на дино.",
        "duc.s8t": "Трек-преп",
        "duc.s8d": "Налаштування підвіски, армовані гальмівні лінії й кращі колодки, встановлення сліків, ride height і робота над часом на колі. У Ducati широка гума і спортивні диски, тож якщо потрібен окремий комплект трекових коліс — зберемо й відбалансуємо через наш <a href=\"/uk/shynomontazh-mototsykliv/\">шиномонтаж мотоциклів</a>.",

        "duc.issuesEyebrow": "Типові болячки Ducati",
        "duc.issuesTitle": "Де <em>кусає desmo.</em>",
        "duc.issuesLead": "Роки на цій платформі — це розуміння, як саме вона ламається. Спіймав вчасно — майже все лікується рутинно. Затягнув — виходить дорого.",
        "duc.i1t": "Дрейф зазорів клапанів на desmo",
        "duc.i1d": "Найчастіше пропускають, бо сервіс відкладають. Ми нормально заміряємо й підбираємо шайбу як треба — а не просто констатуємо симптом.",
        "duc.i2t": "Десинхронізація ride-by-wire",
        "duc.i2d": "Часта історія на сучасних. Пересинхронізуємо через DDS і перевіряємо за живими даними, що все чисто.",
        "duc.i3t": "АКБ / зарядка на «зимуючих» мотоциклах",
        "duc.i3d": "Сучасний Ducati може посадити собі акумулятор сам, при «сплячій» електроніці. Знаходимо причину й радимо нормальний trickle charger.",
        "duc.i4t": "Знос корзини сухого зчеплення (старий Monster)",
        "duc.i4d": "Той самий фірмовий стрекіт сухого зчеплення ховає реальний знос. Ми заміряємо зазори корзини як треба, а не на слух.",
        "duc.i5t": "Помилки калібрування електронної підвіски",
        "duc.i5d": "Збої самокалібрування Sachs / Marzocchi. Скидаємо правильним інструментом і перевіряємо, що демпфірування реально відпрацьовує.",

        "duc.modelsEyebrow": "Моделі, на яких працюємо",
        "duc.modelsTitle": "Уся лінійка <em>Ducati.</em>",
        "duc.modelsLead": "Сучасна водянка, старий повітряник, трек / суперспорт — приносьте.",
        "duc.m1t": "Monster",
        "duc.m1d": "696, 796, 821, 937, 950, 1100, 1200 — повітряні й водяні версії.",
        "duc.m2t": "Panigale",
        "duc.m2d": "899, 959, 1199, 1299, V2, V4, V4 S, V4 R, V4 SP.",
        "duc.m3t": "Multistrada",
        "duc.m3d": "950, 1200, 1260, V2, V4, V4 S, V4 Rally, V4 Pikes Peak.",
        "duc.m4t": "Streetfighter",
        "duc.m4d": "848, V2, V4, V4 S, V4 SP.",
        "duc.m5t": "Scrambler",
        "duc.m5d": "Icon, Café Racer, Desert Sled, Full Throttle, Nightshift, 1100 Sport, 1100 Dark Pro.",
        "duc.m6t": "Diavel, Hypermotard, SuperSport і класика",
        "duc.m6d": "Diavel 1260, Diavel V4; Hypermotard 821/939/950; SuperSport 939/950; плюс вінтажні 916/996/999.",

        "duc.partsEyebrow": "Запчастини й афтермаркет",
        "duc.partsTitle": "Доступ до <em>великих каталогів Ducati.</em>",
        "duc.partsLead": "Замовляємо Ducati OEM, Ducati Performance і топовий італійський і міжнародний афтермаркет через перевірені мережі каталогів і постачальників. Від однієї гальмівної колодки до повної системи Akrapovič і dress-kit від CNC Racing — замовимо.",
        "duc.partsList": "<strong>Каталоги:</strong> Ducati Performance · DucatiOmnia · Termignoni · Akrapovič · Öhlins · ÖHLINS Mechatronic · Brembo · STM Italy · Rizoma · CNC Racing · Ducabike · Carbonin · Spark · MWR · BST · оригінал Ducati через дистриб'юторську мережу.",

        "duc.faqEyebrow": "FAQ",
        "duc.faqTitle": "Часті питання.",
        "duc.q1": "Як часто реально потрібен desmo-сервіс?",
        "duc.a1": "Залежить від моделі й року. Старі Ducati: 24,000 км. Сучасний Panigale V4 / Multistrada V4: 30,000 км по впуску, 60,000 км по випуску. Уточнюємо за конкретним регламентом вашого мотоцикла до кошторису.",
        "duc.q2": "Скільки коштує desmo-сервіс в Iron Custom Motors?",
        "duc.a2": "Ціна за моделлю — від €750 для старих Monster, до €1,500+ для Panigale V4 з повною перевіркою. Порівняно з дилерським рахунком зазвичай на 30–40% дешевше. Письмовий кошторис до початку робіт.",
        "duc.q3": "Прошиєте карту Termignoni / Akrapovič на мій Ducati?",
        "duc.a3": "Так — ставимо вихлоп (повну систему чи slip-on) і заливаємо відповідну ECU-карту. Termignoni race kit, Akrapovič з eCU, сторонні карти за запитом. Результат перевірений на дино й задокументований.",
        "duc.q4": "Робите трек-преп для Panigale / Streetfighter / Multistrada?",
        "duc.a4": "Так — налаштування підвіски, гальмівні лінії й колодки, сліки, ride height, ECU-карта під профіль траси. Готували мотоцикли під Ешторил, Портімау і Хараму.",
        "duc.q5": "Ви офіційний дилер Ducati?",
        "duc.a5": "Ні — ми незалежна майстерня Ducati. Плюс у прозорих цінах (desmo за цінами незалежної майстерні, а не дилерськими) і у свободі ставити OEM Ducati Performance або топовий афтермаркет. Працюємо з усіма великими дистриб'юторами Ducati, повний доступ до каталогів є.",

        "duc.ctaEyebrow": "Коли ви готові — ми готові",
        "duc.ctaTitle": "Привозьте ваш Ducati.",
        "duc.ctaText": "Напишіть модель, рік і коротко суть у WhatsApp. Зорієнтуємо щодо найближчого слота і пришлемо письмовий кошторис до початку робіт.",
        "duc.btnBack": "На головну",
    },
    "pt": {
        "duc.eyebrow": "Ducati · Cascais / Grande Lisboa",
        "duc.h1": "Serviço Ducati<br/>em <span class=\"accent\">Cascais.</span>",
        "duc.sub": "Oficina independente Ducati — serviço desmodromico, electrónica, suspensão, instalação de escape e custom completo para Monster, Panigale, Multistrada, Scrambler, Streetfighter, Diavel.",
        "duc.breadHome": "Início",
        "duc.h1Crumb": "Serviço Ducati",
        "duc.btnWA": "WhatsApp",
        "duc.btnSend": "Enviar pedido",
        "duc.heroAlt": "Área de serviço Ducati na oficina Iron Custom Motors em Cascais",

        "duc.introEyebrow": "Porquê os donos Ducati vêm ter connosco",
        "duc.introTitle": "Desmo feito <em>como deve ser.</em>",
        "duc.introP1": "A Iron Custom Motors é uma especialista independente em Ducati em Cascais. O trem de válvulas desmodromico, a electrónica em camadas, a suspensão semi-activa, as embraiagens secas e húmidas — sabemos como se comporta cada família Ducati e onde costuma dar problemas. A moto que deixa a maioria das oficinas independentes nervosa é a que temos na bancada todas as semanas.",
        "duc.introP2": "O serviço desmodromico é onde muitos donos de Ducati levam um susto com a fatura do concessionário. Fazemo-lo como deve ser feito — no intervalo certo, a preços de oficina independente — e entregamos o trabalho documentado por escrito, para não restarem dúvidas sobre o que foi mexido.",
        "duc.introP3": "Cobrimos toda a gama moderna: Monster (refrigerado a ar e a água), Panigale V2/V4, Multistrada V2/V4/V4 Rally, a família Scrambler, Streetfighter V2/V4, Diavel, Hypermotard, SuperSport. Desde a moto de uso diário até à preparação completa de track-day para o Estoril.",

        "duc.toolsEyebrow": "Ferramenta especialista",
        "duc.toolsTitle": "Diagnóstico e ferramenta <em>Ducati-específica.</em>",
        "duc.toolsLead": "Diagnóstico Ducati a sério, a ferramenta específica do serviço desmodromico e capacidade de dyno-tuning na própria oficina. O serviço desmodromico, em particular, exige ferramentas dedicadas e uma gama completa de selecção de shims que uma oficina genérica simplesmente não tem em stock — nós temos.",
        "duc.t1t": "Ducati Diagnostic System (DDS) / equivalente",
        "duc.t1d": "Ler códigos, ver dados ao vivo, fazer adaptações de ECU e coding de componentes em toda a electrónica Ducati moderna.",
        "duc.t2t": "Ferramenta de serviço desmodromico",
        "duc.t2d": "Extractores de balancins, kit de selecção de shims, apalpa-folgas dedicados. As ferramentas certas para acertar as folgas com precisão, e não a olho.",
        "duc.t3t": "Ferramenta de cam belt e locks (modelos antigos)",
        "duc.t3d": "As ferramentas específicas para o serviço de correia de distribuição em Ducati pré-Panigale — feito segundo o procedimento, com o motor bem travado.",
        "duc.t4t": "Dyno próprio + tuning Termignoni / Akrapovič",
        "duc.t4d": "Mapas de ECU verificados em dyno para sistemas de escape completos. Instalamos, fazemos o flash e confirmamos o resultado no dyno.",

        "duc.servicesEyebrow": "O que fazemos em Ducati",
        "duc.servicesTitle": "Serviço. <em>Desmo. Tuning.</em>",
        "duc.servicesLead": "Intervalos de rotina, o desmo, suspensão custom, trabalho de escape e ECU, preparação de track-day — e os trabalhos raros em que outras oficinas preferem não tocar.",
        "duc.s1t": "Serviço desmodromico (folga das válvulas)",
        "duc.s1d": "No intervalo certo do modelo: 24,000 km em Ducati mais antigos, 30,000 km na admissão / 60,000 km no escape em Panigale V4 / Multi V4. Relatório escrito antes/depois.",
        "duc.s2t": "Manutenção programada (óleo + filtro + verificações)",
        "duc.s2d": "Pelos intervalos Ducati — óleo, filtro, fluidos, travões, corrente, mais os itens específicos do modelo.",
        "duc.s3t": "Serviço da correia de distribuição (modelos antigos)",
        "duc.s3d": "Feito como deve ser, com ferramentas de locking e tensor novo — obrigatório no intervalo do modelo, sem atalhos.",
        "duc.s4t": "Serviço de embraiagem seca",
        "duc.s4d": "Monster antigos, 916, 996, 999 — inspecção da cesta, medição dos discos, substituição quando há desgaste.",
        "duc.s5t": "Serviço de embraiagem húmida",
        "duc.s5d": "Panigale moderno, Multi V4, Streetfighter V4 — inspecção dos discos de fricção, folga de arrasto, sangria do hidráulico.",
        "duc.s6t": "Suspensão",
        "duc.s6d": "Serviço Öhlins, diagnóstico de suspensão semi-activa (Sachs, Marzocchi), reconstrução completa de forquilha e amortecedor.",
        "duc.s7t": "Escape (Termignoni, Akrapovič) + mapa",
        "duc.s7d": "Sistema completo ou slip-on com o mapa de ECU correspondente — verificado em dyno.",
        "duc.s8t": "Track-day prep",
        "duc.s8d": "Afinação de suspensão, linhas em malha e upgrade de pastilhas, montagem de slicks, ride-height e trabalho de tempos por volta. As Ducati calçam pneus largos e jantes de perfil desportivo, por isso se quiser um jogo de rodas dedicado à pista montado e equilibrado, tratamos disso no nosso <a href=\"/pt/montagem-de-pneus-mota/\">serviço de pneus de mota</a>.",

        "duc.issuesEyebrow": "Problemas típicos Ducati",
        "duc.issuesTitle": "Onde o <em>desmo morde.</em>",
        "duc.issuesLead": "Anos na plataforma significam saber como estas motos falham. Apanhado cedo, quase tudo é um fix de rotina. Deixado andar, fica caro.",
        "duc.i1t": "Drift das folgas das válvulas no desmo",
        "duc.i1d": "Costuma passar despercebido porque o serviço vai sendo adiado. Medimos como deve ser e corrigimos com o shim certo — não nos limitamos a confirmar o sintoma.",
        "duc.i2t": "Dessincronização ride-by-wire",
        "duc.i2d": "Comum nas motos modernas. Re-sincronizamos com DDS e confirmamos o funcionamento por dados ao vivo.",
        "duc.i3t": "Bateria / carga em motas paradas durante o inverno",
        "duc.i3d": "Uma Ducati moderna consegue descarregar a própria bateria com toda a electrónica em sleep. Diagnosticamos e recomendamos um trickle-charger como deve ser.",
        "duc.i4t": "Desgaste da cesta de embraiagem seca (Monsters antigos)",
        "duc.i4d": "Aquele chocalhar típico da embraiagem seca esconde desgaste real. Medimos as folgas da cesta como deve ser, sem adivinhar.",
        "duc.i5t": "Erros de calibração da suspensão electrónica",
        "duc.i5d": "Falhas de auto-calibração Sachs / Marzocchi. Resetamos com a ferramenta certa e confirmamos que o damping responde.",

        "duc.modelsEyebrow": "Modelos com que trabalhamos",
        "duc.modelsTitle": "Toda a linha <em>Ducati.</em>",
        "duc.modelsLead": "Água moderno, ar antigo, pista / supersport — traga.",
        "duc.m1t": "Monster",
        "duc.m1d": "696, 796, 821, 937, 950, 1100, 1200 — refrigerado a ar e a água.",
        "duc.m2t": "Panigale",
        "duc.m2d": "899, 959, 1199, 1299, V2, V4, V4 S, V4 R, V4 SP.",
        "duc.m3t": "Multistrada",
        "duc.m3d": "950, 1200, 1260, V2, V4, V4 S, V4 Rally, V4 Pikes Peak.",
        "duc.m4t": "Streetfighter",
        "duc.m4d": "848, V2, V4, V4 S, V4 SP.",
        "duc.m5t": "Scrambler",
        "duc.m5d": "Icon, Café Racer, Desert Sled, Full Throttle, Nightshift, 1100 Sport, 1100 Dark Pro.",
        "duc.m6t": "Diavel, Hypermotard, SuperSport e clássicos",
        "duc.m6d": "Diavel 1260, Diavel V4; Hypermotard 821/939/950; SuperSport 939/950; mais 916/996/999 vintage.",

        "duc.partsEyebrow": "Peças e aftermarket",
        "duc.partsTitle": "Acesso aos <em>principais catálogos Ducati.</em>",
        "duc.partsLead": "Encomendamos Ducati OEM, Ducati Performance e o melhor aftermarket italiano e internacional através de redes de catálogos e fornecedores de confiança. De uma pastilha de travão a um sistema Akrapovič completo a um dress-kit CNC Racing — fazemos o pedido.",
        "duc.partsList": "<strong>Catálogos:</strong> Ducati Performance · DucatiOmnia · Termignoni · Akrapovič · Öhlins · ÖHLINS Mechatronic · Brembo · STM Italy · Rizoma · CNC Racing · Ducabike · Carbonin · Spark · MWR · BST · peças OEM Ducati via rede de distribuidores.",

        "duc.faqEyebrow": "FAQ",
        "duc.faqTitle": "Perguntas frequentes.",
        "duc.q1": "Com que frequência é preciso o serviço desmodromico?",
        "duc.a1": "Depende do modelo e do ano. Ducati antigos: 24,000 km. Panigale V4 / Multistrada V4 modernos: 30,000 km na admissão, 60,000 km no escape. Confirmamos pelo plano específico da sua moto antes de orçamentar.",
        "duc.q2": "Quanto custa um serviço desmodromico na Iron Custom Motors?",
        "duc.a2": "É preço por modelo — desde €750 para Monsters antigos, até €1,500+ para um Panigale V4 com inspecção completa. Comparado com um concessionário, é tipicamente 30–40% menos. Entregue por escrito antes de começar o trabalho.",
        "duc.q3": "Conseguem fazer flash com mapa Termignoni / Akrapovič no meu Ducati?",
        "duc.a3": "Sim — instalamos o escape (sistema completo ou slip-on) e fazemos o upload do mapa de ECU correspondente. Termignoni race kit, Akrapovič com eCU, mapas de terceiros conforme necessário. Resultado verificado em dyno e documentado.",
        "duc.q4": "Fazem preparação track-day para Panigale / Streetfighter / Multistrada?",
        "duc.a4": "Sim — afinação de suspensão, linhas e pastilhas de travão, slicks, ride-height, mapa de ECU acertado ao perfil do circuito. Já preparámos motos para o Estoril, Portimão e Jarama.",
        "duc.q5": "São concessionário Ducati autorizado?",
        "duc.a5": "Não — somos uma oficina independente Ducati. A vantagem são preços transparentes (desmo a preços de oficina independente, não de concessionário) e a liberdade de montar OEM Ducati Performance ou aftermarket de topo. Trabalhamos com todos os principais distribuidores Ducati e temos acesso total a catálogos.",

        "duc.ctaEyebrow": "Prontos quando estiver",
        "duc.ctaTitle": "Traga o seu Ducati.",
        "duc.ctaText": "Envie modelo, ano e uma descrição breve via WhatsApp. Voltamos com o slot disponível mais próximo e um orçamento escrito antes de começar o trabalho.",
        "duc.btnBack": "Voltar ao início",
    },
}

# ====================================================================================
# Suzuki
# ====================================================================================
PAGE_I18N["suzuki-service"] = {
    "en": {
        "suz.eyebrow": "Suzuki · Cascais / Greater Lisbon",
        "suz.h1": "Suzuki service<br/>in <span class=\"accent\">Cascais.</span>",
        "suz.sub": "Independent Suzuki workshop — diagnostics, scheduled service, valve clearance, charging-system repair, suspension and tuning for GSX-R, GSX-S, V-Strom, SV650, Hayabusa, Katana, Bandit, Boulevard and DR-Z.",
        "suz.heroAlt": "Suzuki motorcycle on the lift at Iron Custom Motors workshop in Cascais",
        "suz.breadHome": "Home",
        "suz.h1Crumb": "Suzuki service",
        "suz.btnWA": "WhatsApp us",
        "suz.btnSend": "Send a request",
        "suz.btnBack": "Back to home",
        "suz.introTitle": "Japanese engineering, independent rates.",
        "suz.introEyebrow": "Why bring your Suzuki to us",
        "suz.introP1": "Iron Custom Motors is an independent Suzuki specialist in Cascais. Suzuki builds some of the most honest, hard-working engines on the road — the GSX-R inline-fours, the SV650 and V-Strom V-twins, the Hayabusa — but honest engineering still needs people who understand it properly. That's what we are: a Suzuki-first workshop, not a generic multi-brand shop that also takes Suzukis.",
        "suz.introP2": "The engineering culture here didn't come from nowhere. This is the team behind AMD World Championship custom builds, a Bonneville land-speed record, and the BMW Motorrad Customizing Championship 2023. We don't list that to impress you with trophies — we list it because that same standard of measurement, tolerance and finish is what now goes into a routine GSX-R valve check or a high-mileage V-Strom charging repair.",
        "suz.introP3": "Independent means no dealer mark-up, freedom to fit OEM or quality aftermarket parts as the job actually requires, and direct communication with the person doing the work. Written estimate before anything happens, written report after.",
        "suz.toolsTitle": "Suzuki-specific diagnostic and tools.",
        "suz.toolsEyebrow": "Specialist tooling",
        "suz.toolsLead": "Dealer-grade Suzuki diagnostics and the model-specific tooling that most independent workshops simply don't keep. This is the difference between a real Suzuki shop and a workshop that happens to take Suzukis.",
        "suz.t1t": "SDS — Suzuki Diagnostic System (or equivalent)",
        "suz.t1d": "Reads and clears Suzuki-specific fault codes, monitors live sensor data, runs ISC / throttle-body resets and checks the charging system under load.",
        "suz.t2t": "Throttle-body synchronisation",
        "suz.t2d": "Mercury-column and digital sync for inline-four GSX-R / GSX-S / Bandit / Hayabusa and the SV650 / V-Strom V-twins — smooth idle, clean fuelling.",
        "suz.t3t": "Charging-system load testing",
        "suz.t3d": "Dedicated testing of the stator and regulator/rectifier under real load — the single most important check on any high-mileage Suzuki.",
        "suz.t4t": "Suspension service tooling",
        "suz.t4d": "Fork seal, cartridge and shock service for GSX-R sport, V-Strom adventure and SV650 street geometry — sag setup and damping done properly.",
        "suz.servicesTitle": "Service. Repair. Tune.",
        "suz.servicesEyebrow": "What we do on Suzuki",
        "suz.servicesLead": "From a routine oil-and-filter to a full charging-system rebuild or a track-prepped GSX-R — all of it done with Suzuki-specific knowledge.",
        "suz.s1t": "01 Scheduled service",
        "suz.s1d": "Suzuki interval service — oil, filter, fluids, brake check, chain and sprocket inspection, plus model-specific items. From €150, consumables included.",
        "suz.s2t": "02 Valve clearance — twin / four",
        "suz.s2d": "Done properly with feeler gauges and shim selection. SV650 / V-Strom V-twin, GSX-R / GSX-S / Bandit / Hayabusa inline-four.",
        "suz.s3t": "03 Charging-system repair",
        "suz.s3d": "Stator, regulator/rectifier and battery diagnosis and replacement. The classic Suzuki repair — and the one we know best.",
        "suz.s4t": "04 Electrical diagnostics",
        "suz.s4d": "Full fault-code read and live data via SDS / equivalent. Fuel pump, ISC, sensors, accessory wiring and corrosion repair.",
        "suz.s5t": "05 Fuel system service",
        "suz.s5d": "Fuel-pump diagnosis, injector cleaning, throttle-body sync and idle stabilisation on injected Suzuki; carb clean and balance on classic models.",
        "suz.s6t": "06 Suspension service",
        "suz.s6d": "Fork seal replacement, oil change, cartridge and shock rebuild, sag and damping setup for GSX-R, V-Strom and SV650.",
        "suz.s7t": "07 Clutch and drivetrain",
        "suz.s7d": "Clutch inspection and replacement, chain and sprocket renewal, gearbox diagnosis. Slipper-clutch service where fitted.",
        "suz.s8t": "08 Tuning and upgrades",
        "suz.s8d": "Exhaust install with fuelling correction (Yoshimura, Akrapovič), suspension upgrades, ergonomics, protection and touring setup.",
        "suz.issuesTitle": "Suzuki failure patterns, checked before they bite.",
        "suz.issuesEyebrow": "Typical issues we know",
        "suz.issuesLead": "Years of Suzuki service mean we know where these bikes get tired. We check the high-risk items proactively — not after they leave you stranded on the way to Sintra.",
        "suz.i1t": "Regulator/rectifier failure",
        "suz.i1d": "the famous Suzuki weak point across GSX-R, SV650 and V-Strom generations. We load-test it before it cooks the battery and stator, and upgrade to a better-cooled unit where it makes sense.",
        "suz.i2t": "Stator and charging wear on high-mileage bikes",
        "suz.i2d": "caught with a proper load test, not a guess at the battery. We measure output cold and hot before it leaves you stranded.",
        "suz.i3t": "Cam chain tensioner wear",
        "suz.i3d": "a known rattle on certain Suzuki models. We diagnose it correctly instead of chasing the noise around the engine.",
        "suz.i4t": "Fuel pump and ISC issues",
        "suz.i4d": "hot-start hesitation and idle hunting on injected models. We test the pump and reset the ISC properly via diagnostics.",
        "suz.i5t": "Clutch wear and drag",
        "suz.i5d": "basket and plate inspection measured against spec, not by feel — especially on hard-ridden GSX-R and high-mileage V-Strom.",
        "suz.modelsTitle": "Across the Suzuki lineup.",
        "suz.modelsEyebrow": "Models we service",
        "suz.modelsLead": "Current production, recent past, modern classics — if it wears the S, bring it in.",
        "suz.m1t": "GSX-R (supersport)",
        "suz.m1d": "GSX-R600, GSX-R750, GSX-R1000 / R. Street, track prep and dyno tuning.",
        "suz.m2t": "GSX-S & GSX-8 (naked / sport)",
        "suz.m2d": "GSX-S750, GSX-S1000 / GT / F, GSX-8S, GSX-8R.",
        "suz.m3t": "Hayabusa & Katana",
        "suz.m3d": "GSX1300R Hayabusa (all generations), Katana 1000.",
        "suz.m4t": "SV650 & Bandit",
        "suz.m4d": "SV650 / SV650X, Bandit 650 / 1200 / 1250.",
        "suz.m5t": "V-Strom (adventure)",
        "suz.m5d": "V-Strom 650 (DL650), V-Strom 800 / 800DE, V-Strom 1000 (DL1000), V-Strom 1050 (DL1050).",
        "suz.m6t": "Cruiser & dual-sport",
        "suz.m6d": "Boulevard / Intruder M / C family, DR650, DR-Z400 and the new DR-Z4S / 4SM.",
        "suz.partsTitle": "Catalog access for major Suzuki parts.",
        "suz.partsEyebrow": "Parts and accessories",
        "suz.partsLead": "We source through OEM Suzuki and the major international aftermarket catalogs. Whatever your bike needs — OEM, performance, touring or protection — we order it directly through trusted suppliers.",
        "suz.partsList": "<strong>Catalogs we work with:</strong> OEM Suzuki parts via distributor network · Yoshimura · Akrapovič · Öhlins · K-Tech · Brembo · EBC · DID · Renthal · Rizoma · SW-Motech · Givi · Mitas · Avon. Order ahead even if you're not booking service.",
        "suz.faqTitle": "Common questions. (FAQ)",
        "suz.faqEyebrow": "FAQ",
        "suz.q1": "Are you an authorised Suzuki dealer?",
        "suz.a1": "No — Iron Custom Motors is an independent Suzuki workshop. The advantage is no dealer mark-up and freedom to use OEM or quality aftermarket parts. Recall and warranty work itself must go through an authorised Suzuki dealer, but everything else — scheduled service, repair, charging-system work, modifications — we handle at independent rates and with deeper, Suzuki-first attention.",
        "suz.q2": "How much does a Suzuki service cost?",
        "suz.a2": "Scheduled maintenance starts from €150, consumables included (air-filter replacement is charged separately). Valve-clearance check is from €250 for a V-twin (SV650 / V-Strom) and €400 for an inline-four (GSX-R / Bandit / Hayabusa); check-and-adjust from €300 (twin) and €650 (four). Hourly work is €50/hour. You always get a written estimate before any work starts. Prices from, taxes included.",
        "suz.q3": "Can you tune my GSX-R or fit a full exhaust?",
        "suz.a3": "Yes — we install slip-on or full systems (Yoshimura, Akrapovič) with the corresponding fuelling correction, plus suspension and ergonomics for street or track. Dyno-verified where the build calls for it.",
        "suz.q4": "Do you work on older or classic Suzuki?",
        "suz.a4": "Yes — air-cooled Bandits, older GSX-R, DR singles and classic Intruders are welcome. Carburettor clean and balance, charging-system rebuild and electrical repair are exactly the kind of work we enjoy.",
        "suz.q5": "Can you import OEM Suzuki parts to Portugal?",
        "suz.a5": "Yes — we have catalog access to OEM Suzuki parts via the distributor network plus all the major aftermarket catalogs. If a part exists for your model, we source it to Cascais.",
        "suz.q6": "My charging warning light came on — is that serious?",
        "suz.a6": "On a Suzuki, it usually points at the regulator/rectifier or stator — a well-known weak point on the brand. Don't keep riding it: a failing reg/rec can take the battery and stator with it. Bring it in, we'll load-test the whole charging system and tell you exactly what's needed in writing.",
        "seo.relatedTitle": "Continue through the same service system.",
        "seo.relatedEyebrow": "Related workshop paths",
        "seo.relatedLead": "Follow the most relevant next pages for service, parts, pricing, brand support and contact.",
        "seo.localTitle": "Serving Cascais, Lisbon and Greater Lisbon.",
        "seo.localEyebrow": "Local service area",
        "seo.localLead": "Iron Custom Motors is based in São Domingos de Rana, Cascais. We work with riders from Cascais, Estoril, Oeiras, Sintra, Lisbon and the wider Greater Lisbon area.",
        "seo.area1t": "Cascais workshop",
        "seo.area1d": "A real workshop and client lounge, not a remote parts counter. Book service, drop off the bike, or visit to discuss a project.",
        "seo.area2t": "Multilingual process",
        "seo.area2d": "English, Russian, Ukrainian and Portuguese communication with written estimates and clear next steps.",
        "seo.area3t": "One accountable path",
        "seo.area3d": "Diagnostics, parts sourcing, installation, upgrades and follow-up happen under one workshop standard.",
        "suz.ctaTitle": "Bring your Suzuki in.",
        "suz.ctaEyebrow": "Ready when you are",
        "suz.ctaText": "Send the model, year and a short description via WhatsApp. We'll come back with the closest available slot and a written estimate before work starts. Tue–Sat, 10:00–18:00."
    },
    "pt": {
        "suz.eyebrow": "Suzuki · Cascais / Grande Lisboa",
        "suz.h1": "Serviço Suzuki<br/>em <span class=\"accent\">Cascais.</span>",
        "suz.sub": "Oficina Suzuki independente — diagnóstico, manutenção programada, folga de válvulas, reparação do sistema de carga, suspensão e afinação para GSX-R, GSX-S, V-Strom, SV650, Hayabusa, Katana, Bandit, Boulevard e DR-Z.",
        "suz.heroAlt": "Mota Suzuki na plataforma da oficina Iron Custom Motors em Cascais",
        "suz.breadHome": "Início",
        "suz.h1Crumb": "Serviço Suzuki",
        "suz.btnWA": "WhatsApp",
        "suz.btnSend": "Enviar pedido",
        "suz.btnBack": "Voltar ao início",
        "suz.introTitle": "Engenharia japonesa, preços independentes.",
        "suz.introEyebrow": "Porque trazer a sua Suzuki até nós",
        "suz.introP1": "A Iron Custom Motors é uma oficina especialista em Suzuki, independente, em Cascais. A Suzuki constrói alguns dos motores mais honestos e trabalhadores da estrada — os quatro-em-linha GSX-R, os bicilíndricos em V da SV650 e da V-Strom, a Hayabusa — mas engenharia honesta continua a precisar de quem a perceba a sério. É isso que somos: uma oficina Suzuki em primeiro lugar, não uma oficina multimarca genérica que também aceita Suzukis.",
        "suz.introP2": "A cultura de engenharia desta casa não veio do nada. Esta é a equipa por trás de projetos custom Campeões do Mundo AMD, de um recorde de velocidade em Bonneville e do Campeonato de Customização BMW Motorrad 2023. Não o referimos para o impressionar com troféus — referimo-lo porque é exatamente esse padrão de medição, tolerância e acabamento que entra agora numa verificação de válvulas de rotina de uma GSX-R ou numa reparação de carga de uma V-Strom de muitos quilómetros.",
        "suz.introP3": "Independente significa sem margem de concessionário, liberdade para montar peças OEM ou de qualidade do mercado de acessórios conforme o trabalho exige, e comunicação direta com quem faz o serviço. Orçamento por escrito antes de tudo, relatório por escrito no fim.",
        "suz.toolsTitle": "Diagnóstico e ferramentas específicas Suzuki.",
        "suz.toolsEyebrow": "Ferramenta especialista",
        "suz.toolsLead": "Diagnóstico Suzuki ao nível do concessionário e as ferramentas específicas de cada modelo que a maioria das oficinas independentes simplesmente não tem. É esta a diferença entre uma verdadeira oficina Suzuki e uma oficina que apenas aceita Suzukis.",
        "suz.t1t": "SDS — Suzuki Diagnostic System (ou equivalente)",
        "suz.t1d": "Lê e apaga códigos de avaria específicos da Suzuki, monitoriza dados dos sensores em tempo real, executa reposições de ISC / corpo de borboleta e verifica o sistema de carga sob esforço.",
        "suz.t2t": "Sincronização dos corpos de borboleta",
        "suz.t2d": "Sincronização por coluna de mercúrio e digital para os quatro-em-linha GSX-R / GSX-S / Bandit / Hayabusa e os bicilíndricos SV650 / V-Strom — ralenti suave, alimentação limpa.",
        "suz.t3t": "Teste de carga do sistema elétrico",
        "suz.t3d": "Teste dedicado do estator e do regulador/retificador sob carga real — a verificação mais importante em qualquer Suzuki de muitos quilómetros.",
        "suz.t4t": "Ferramentas de suspensão",
        "suz.t4d": "Serviço de retentores, cartucho e amortecedor para a geometria desportiva GSX-R, aventura V-Strom e estrada SV650 — ajuste de sag e amortecimento feito como deve ser.",
        "suz.servicesTitle": "Serviço. Reparação. Afinação.",
        "suz.servicesEyebrow": "O que fazemos em Suzuki",
        "suz.servicesLead": "De uma mudança de óleo e filtro de rotina a uma reconstrução completa do sistema de carga ou uma GSX-R preparada para pista — tudo com conhecimento específico Suzuki.",
        "suz.s1t": "01 Manutenção programada",
        "suz.s1d": "Serviço por intervalo Suzuki — óleo, filtro, fluidos, verificação de travões, inspeção de corrente e cremalheiras, mais itens específicos do modelo. A partir de €150, consumíveis incluídos.",
        "suz.s2t": "02 Folga de válvulas — bicilíndrico / quatro cilindros",
        "suz.s2d": "Feita como deve ser, com apalpa-folgas e seleção de calços. Bicilíndrico em V SV650 / V-Strom, quatro-em-linha GSX-R / GSX-S / Bandit / Hayabusa.",
        "suz.s3t": "03 Reparação do sistema de carga",
        "suz.s3d": "Diagnóstico e substituição de estator, regulador/retificador e bateria. A reparação clássica da Suzuki — e a que melhor conhecemos.",
        "suz.s4t": "04 Diagnóstico elétrico",
        "suz.s4d": "Leitura completa de códigos e dados em tempo real via SDS / equivalente. Bomba de combustível, ISC, sensores, cablagem de acessórios e reparação de corrosão.",
        "suz.s5t": "05 Sistema de combustível",
        "suz.s5d": "Diagnóstico da bomba, limpeza de injetores, sincronização de borboletas e estabilização de ralenti em Suzuki de injeção; limpeza e equilíbrio de carburadores em modelos clássicos.",
        "suz.s6t": "06 Suspensão",
        "suz.s6d": "Substituição de retentores, mudança de óleo, reconstrução de cartucho e amortecedor, ajuste de sag e amortecimento para GSX-R, V-Strom e SV650.",
        "suz.s7t": "07 Embraiagem e transmissão",
        "suz.s7d": "Inspeção e substituição de embraiagem, renovação de corrente e cremalheiras, diagnóstico de caixa. Serviço de embraiagem anti-salto onde aplicável.",
        "suz.s8t": "08 Afinação e upgrades",
        "suz.s8d": "Instalação de escape com correção de alimentação (Yoshimura, Akrapovič), upgrades de suspensão, ergonomia, proteção e preparação de viagem.",
        "suz.issuesTitle": "Padrões de avaria Suzuki, verificados antes de morderem.",
        "suz.issuesEyebrow": "Problemas típicos que conhecemos",
        "suz.issuesLead": "Anos de serviço Suzuki ensinam onde estas motas se cansam. Verificamos os pontos de risco de forma proativa — não depois de o deixarem a pé a caminho de Sintra.",
        "suz.i1t": "Falha do regulador/retificador",
        "suz.i1d": "o famoso ponto fraco da Suzuki ao longo das gerações GSX-R, SV650 e V-Strom. Fazemos teste de carga antes que ele queime a bateria e o estator, e atualizamos para uma unidade melhor arrefecida quando faz sentido.",
        "suz.i2t": "Desgaste do estator e da carga em motas de muitos quilómetros",
        "suz.i2d": "detetado com um teste de carga adequado, não com um palpite sobre a bateria. Medimos a saída a frio e a quente antes que o deixe a pé.",
        "suz.i3t": "Desgaste do tensor da corrente de distribuição",
        "suz.i3d": "um ruído conhecido em certos modelos Suzuki. Diagnosticamo-lo corretamente em vez de andar à caça do som pelo motor.",
        "suz.i4t": "Problemas de bomba de combustível e ISC",
        "suz.i4d": "hesitação a quente e ralenti instável em modelos de injeção. Testamos a bomba e reiniciamos o ISC corretamente por diagnóstico.",
        "suz.i5t": "Desgaste e arrasto de embraiagem",
        "suz.i5d": "inspeção de cesto e discos medida contra a especificação, não ao tato — sobretudo em GSX-R muito usadas e V-Strom de muitos quilómetros.",
        "suz.modelsTitle": "Em toda a gama Suzuki.",
        "suz.modelsEyebrow": "Modelos que servimos",
        "suz.modelsLead": "Produção atual, passado recente, clássicos modernos — se traz o S, traga-a cá.",
        "suz.m1t": "GSX-R (supersport)",
        "suz.m1d": "GSX-R600, GSX-R750, GSX-R1000 / R. Estrada, preparação de pista e afinação em dinamómetro.",
        "suz.m2t": "GSX-S & GSX-8 (naked / sport)",
        "suz.m2d": "GSX-S750, GSX-S1000 / GT / F, GSX-8S, GSX-8R.",
        "suz.m3t": "Hayabusa & Katana",
        "suz.m3d": "GSX1300R Hayabusa (todas as gerações), Katana 1000.",
        "suz.m4t": "SV650 & Bandit",
        "suz.m4d": "SV650 / SV650X, Bandit 650 / 1200 / 1250.",
        "suz.m5t": "V-Strom (aventura)",
        "suz.m5d": "V-Strom 650 (DL650), V-Strom 800 / 800DE, V-Strom 1000 (DL1000), V-Strom 1050 (DL1050).",
        "suz.m6t": "Custom & trail",
        "suz.m6d": "família Boulevard / Intruder M / C, DR650, DR-Z400 e as novas DR-Z4S / 4SM.",
        "suz.partsTitle": "Acesso a catálogo das principais peças Suzuki.",
        "suz.partsEyebrow": "Peças e acessórios",
        "suz.partsLead": "Fornecemos através de OEM Suzuki e dos principais catálogos internacionais de acessórios. Seja o que a sua mota precisar — OEM, performance, viagem ou proteção — encomendamos diretamente a fornecedores de confiança.",
        "suz.partsList": "<strong>Catálogos com que trabalhamos:</strong> Peças OEM Suzuki via rede de distribuição · Yoshimura · Akrapovič · Öhlins · K-Tech · Brembo · EBC · DID · Renthal · Rizoma · SW-Motech · Givi · Mitas · Avon. Encomende com antecedência mesmo sem marcar serviço.",
        "suz.faqTitle": "Perguntas frequentes. (FAQ)",
        "suz.faqEyebrow": "FAQ",
        "suz.q1": "São concessionário oficial Suzuki?",
        "suz.a1": "Não — a Iron Custom Motors é uma oficina Suzuki independente. A vantagem é não haver margem de concessionário e termos liberdade para usar peças OEM ou de qualidade do mercado. Recalls e trabalho em garantia têm de passar por um concessionário oficial Suzuki, mas todo o resto — manutenção, reparação, trabalho no sistema de carga, modificações — tratamos a preços independentes e com atenção Suzuki em primeiro lugar.",
        "suz.q2": "Quanto custa um serviço Suzuki?",
        "suz.a2": "A manutenção programada começa a partir de €150, consumíveis incluídos (a substituição do filtro de ar é cobrada à parte). A verificação de folga de válvulas é a partir de €250 num bicilíndrico (SV650 / V-Strom) e €400 num quatro-em-linha (GSX-R / Bandit / Hayabusa); verificar e ajustar a partir de €300 (bicilíndrico) e €650 (quatro cilindros). Mão de obra a €50/hora. Recebe sempre um orçamento por escrito antes de qualquer trabalho. Preços a partir de, impostos incluídos.",
        "suz.q3": "Podem afinar a minha GSX-R ou montar um escape completo?",
        "suz.a3": "Sim — instalamos slip-on ou sistema completo (Yoshimura, Akrapovič) com a respetiva correção de alimentação, mais suspensão e ergonomia para estrada ou pista. Verificado em dinamómetro quando o trabalho o justifica.",
        "suz.q4": "Trabalham em Suzuki antigas ou clássicas?",
        "suz.a4": "Sim — Bandits refrigeradas a ar, GSX-R antigas, monocilíndricos DR e Intruders clássicas são bem-vindas. Limpeza e equilíbrio de carburadores, reconstrução do sistema de carga e reparação elétrica são precisamente o tipo de trabalho de que gostamos.",
        "suz.q5": "Podem importar peças OEM Suzuki para Portugal?",
        "suz.a5": "Sim — temos acesso a catálogo de peças OEM Suzuki pela rede de distribuição, além de todos os principais catálogos de acessórios. Se a peça existe para o seu modelo, trazemo-la até Cascais.",
        "suz.q6": "Acendeu-se a luz de carga — é grave?",
        "suz.a6": "Numa Suzuki, costuma apontar para o regulador/retificador ou para o estator — um ponto fraco bem conhecido da marca. Não continue a andar: um regulador a falhar pode levar a bateria e o estator com ele. Traga-a cá, fazemos o teste de carga a todo o sistema e dizemos-lhe por escrito exatamente o que é preciso.",
        "seo.relatedTitle": "Continue pelo mesmo sistema de serviço.",
        "seo.relatedEyebrow": "Caminhos relacionados",
        "seo.relatedLead": "Siga as próximas páginas mais relevantes para serviço, peças, preços, apoio por marca e contacto.",
        "seo.localTitle": "Ao serviço de Cascais, Lisboa e Grande Lisboa.",
        "seo.localEyebrow": "Área local de serviço",
        "seo.localLead": "A Iron Custom Motors está em São Domingos de Rana, Cascais. Trabalhamos com motociclistas de Cascais, Estoril, Oeiras, Sintra, Lisboa e toda a Grande Lisboa.",
        "seo.area1t": "Oficina em Cascais",
        "seo.area1d": "Uma oficina e lounge de cliente reais, não um balcão de peças remoto. Marque serviço, deixe a mota ou visite-nos para falar de um projeto.",
        "seo.area2t": "Processo multilingue",
        "seo.area2d": "Comunicação em inglês, russo, ucraniano e português, com orçamentos por escrito e passos claros.",
        "seo.area3t": "Um percurso responsável",
        "seo.area3d": "Diagnóstico, fornecimento de peças, montagem, upgrades e acompanhamento sob um único padrão de oficina.",
        "suz.ctaTitle": "Traga a sua Suzuki.",
        "suz.ctaEyebrow": "Quando estiver pronto",
        "suz.ctaText": "Envie o modelo, o ano e uma breve descrição por WhatsApp. Voltamos com a vaga mais próxima e um orçamento por escrito antes de começar. Ter–Sáb, 10:00–18:00."
    },
    "ru": {
        "suz.eyebrow": "Suzuki · Кашкайш / Большой Лиссабон",
        "suz.h1": "Сервис Suzuki<br/>в <span class=\"accent\">Кашкайше.</span>",
        "suz.sub": "Независимая мастерская Suzuki — диагностика, плановое ТО, регулировка клапанов, ремонт системы зарядки, подвеска и тюнинг для GSX-R, GSX-S, V-Strom, SV650, Hayabusa, Katana, Bandit, Boulevard и DR-Z.",
        "suz.heroAlt": "Мотоцикл Suzuki на подъёмнике в мастерской Iron Custom Motors, Кашкайш",
        "suz.breadHome": "Главная",
        "suz.h1Crumb": "Сервис Suzuki",
        "suz.btnWA": "WhatsApp",
        "suz.btnSend": "Отправить заявку",
        "suz.btnBack": "На главную",
        "suz.introTitle": "Японская инженерия, цены независимой мастерской.",
        "suz.introEyebrow": "Почему Suzuki стоит привезти к нам",
        "suz.introP1": "Iron Custom Motors — независимый специалист по Suzuki в Кашкайше. Suzuki делает одни из самых честных и выносливых моторов на дороге: рядные «четвёрки» GSX-R, V-образные «двойки» SV650 и V-Strom, легендарную Hayabusa. Но даже честной технике нужны люди, которые по-настоящему её понимают. Мы именно такие — мастерская, где Suzuki на первом месте, а не универсальный сервис, который заодно берёт и Suzuki.",
        "suz.introP2": "Инженерная культура здесь возникла не на пустом месте. Это команда, за плечами которой кастом-проекты — чемпионы мира AMD, рекорд скорости на Бонневиле и победа на BMW Motorrad Customizing Championship 2023. Мы говорим об этом не ради трофеев, а потому что тот же подход к замерам, допускам и качеству исполнения теперь идёт и в рутинную проверку клапанов GSX-R, и в ремонт зарядки V-Strom с большим пробегом.",
        "suz.introP3": "Независимая мастерская — это отсутствие дилерской наценки, свобода ставить оригинал или качественный неоригинал по делу, и прямой разговор с тем, кто делает работу. Письменная смета до начала, письменный отчёт после.",
        "suz.toolsTitle": "Диагностика и инструмент под Suzuki.",
        "suz.toolsEyebrow": "Специализированный инструмент",
        "suz.toolsLead": "Диагностика Suzuki дилерского уровня и модельный инструмент, которого у большинства независимых мастерских просто нет. Именно это отличает настоящий сервис Suzuki от мастерской, которая «тоже берёт Suzuki».",
        "suz.t1t": "SDS — Suzuki Diagnostic System (или аналог)",
        "suz.t1d": "Читает и сбрасывает фирменные коды ошибок Suzuki, показывает данные с датчиков в реальном времени, выполняет сброс ISC / дросселя и проверяет систему зарядки под нагрузкой.",
        "suz.t2t": "Синхронизация дроссельных заслонок",
        "suz.t2d": "Синхронизация ртутными колонками и цифровая — для рядных «четвёрок» GSX-R / GSX-S / Bandit / Hayabusa и V-образных SV650 / V-Strom. Ровный холостой ход, чистое смесеобразование.",
        "suz.t3t": "Нагрузочный тест системы зарядки",
        "suz.t3d": "Отдельная проверка статора и реле-регулятора под реальной нагрузкой — самая важная проверка на любой Suzuki с пробегом.",
        "suz.t4t": "Инструмент для подвески",
        "suz.t4d": "Замена сальников, обслуживание картриджа и амортизатора — спортивная геометрия GSX-R, эндуро V-Strom и дорожная SV650. Настройка преднатяга и демпфирования как положено.",
        "suz.servicesTitle": "ТО. Ремонт. Тюнинг.",
        "suz.servicesEyebrow": "Что делаем по Suzuki",
        "suz.servicesLead": "От рядовой замены масла с фильтром до полного восстановления системы зарядки или подготовки GSX-R к треку — всё со знанием конкретики Suzuki.",
        "suz.s1t": "01 Плановое ТО",
        "suz.s1d": "Сервис по регламенту Suzuki — масло, фильтр, жидкости, проверка тормозов, осмотр цепи и звёзд, плюс позиции по модели. От €150, расходники включены.",
        "suz.s2t": "02 Регулировка клапанов — «двойка» / «четвёрка»",
        "suz.s2d": "Делаем как надо — щупами и подбором шайб. V-образные SV650 / V-Strom, рядные GSX-R / GSX-S / Bandit / Hayabusa.",
        "suz.s3t": "03 Ремонт системы зарядки",
        "suz.s3d": "Диагностика и замена статора, реле-регулятора и АКБ. Классический ремонт Suzuki — и тот, что мы знаем лучше всего.",
        "suz.s4t": "04 Электродиагностика",
        "suz.s4d": "Полное чтение кодов и данных в реальном времени через SDS / аналог. Бензонасос, ISC, датчики, проводка допоборудования, борьба с коррозией.",
        "suz.s5t": "05 Топливная система",
        "suz.s5d": "Диагностика насоса, чистка форсунок, синхронизация заслонок и стабилизация холостого хода на инжекторных Suzuki; чистка и настройка карбюраторов на классике.",
        "suz.s6t": "06 Подвеска",
        "suz.s6d": "Замена сальников, замена масла, переборка картриджа и амортизатора, настройка преднатяга и демпфирования для GSX-R, V-Strom и SV650.",
        "suz.s7t": "07 Сцепление и трансмиссия",
        "suz.s7d": "Осмотр и замена сцепления, замена цепи и звёзд, диагностика КПП. Обслуживание проскальзывающего сцепления, где оно есть.",
        "suz.s8t": "08 Тюнинг и апгрейды",
        "suz.s8d": "Установка выхлопа с коррекцией смеси (Yoshimura, Akrapovič), апгрейд подвески, эргономика, защита и подготовка к дальним поездкам.",
        "suz.issuesTitle": "Слабые места Suzuki, находим до того, как подведут.",
        "suz.issuesEyebrow": "Типичные проблемы, которые знаем",
        "suz.issuesLead": "Годы работы с Suzuki — это знание того, где эти мотоциклы устают. Мы проверяем зоны риска заранее, а не после того, как мотоцикл встал по дороге в Синтру.",
        "suz.i1t": "Отказ реле-регулятора",
        "suz.i1d": "знаменитое слабое место Suzuki через поколения GSX-R, SV650 и V-Strom. Проверяем под нагрузкой, пока он не «убил» АКБ и статор, и при необходимости ставим лучше охлаждаемый узел.",
        "suz.i2t": "Износ статора и зарядки на больших пробегах",
        "suz.i2d": "выявляем нормальным нагрузочным тестом, а не гаданием по аккумулятору. Замеряем отдачу на холодную и на горячую, пока мотоцикл вас не подвёл.",
        "suz.i3t": "Износ натяжителя цепи ГРМ",
        "suz.i3d": "известный стук на некоторых моделях Suzuki. Диагностируем точно, а не гоняемся за звуком по всему мотору.",
        "suz.i4t": "Бензонасос и ISC",
        "suz.i4d": "провалы при горячем пуске и «плавающий» холостой на инжекторе. Проверяем насос и корректно сбрасываем ISC по диагностике.",
        "suz.i5t": "Износ и ведёт сцепление",
        "suz.i5d": "корзину и диски меряем по спецификации, а не «на руку» — особенно на отжигаемых GSX-R и V-Strom с большим пробегом.",
        "suz.modelsTitle": "Вся линейка Suzuki.",
        "suz.modelsEyebrow": "Модели, которые обслуживаем",
        "suz.modelsLead": "Текущее производство, недавнее прошлое, современная классика — если на баке буква S, привозите.",
        "suz.m1t": "GSX-R (суперспорт)",
        "suz.m1d": "GSX-R600, GSX-R750, GSX-R1000 / R. Дорога, подготовка к треку и настройка на стенде.",
        "suz.m2t": "GSX-S и GSX-8 (нейкед / спорт)",
        "suz.m2d": "GSX-S750, GSX-S1000 / GT / F, GSX-8S, GSX-8R.",
        "suz.m3t": "Hayabusa и Katana",
        "suz.m3d": "GSX1300R Hayabusa (все поколения), Katana 1000.",
        "suz.m4t": "SV650 и Bandit",
        "suz.m4d": "SV650 / SV650X, Bandit 650 / 1200 / 1250.",
        "suz.m5t": "V-Strom (адвенчер)",
        "suz.m5d": "V-Strom 650 (DL650), V-Strom 800 / 800DE, V-Strom 1000 (DL1000), V-Strom 1050 (DL1050).",
        "suz.m6t": "Круизеры и эндуро",
        "suz.m6d": "семейство Boulevard / Intruder M / C, DR650, DR-Z400 и новые DR-Z4S / 4SM.",
        "suz.partsTitle": "Доступ к каталогам основных запчастей Suzuki.",
        "suz.partsEyebrow": "Запчасти и аксессуары",
        "suz.partsLead": "Возим через оригинал Suzuki и крупнейшие международные каталоги неоригинала. Что нужно вашему мотоциклу — оригинал, спорт, туризм или защита — заказываем напрямую у проверенных поставщиков.",
        "suz.partsList": "<strong>Каталоги, с которыми работаем:</strong> оригинальные запчасти Suzuki через дистрибьюторскую сеть · Yoshimura · Akrapovič · Öhlins · K-Tech · Brembo · EBC · DID · Renthal · Rizoma · SW-Motech · Givi · Mitas · Avon. Можно заказать заранее, даже без записи на сервис.",
        "suz.faqTitle": "Частые вопросы. (FAQ)",
        "suz.faqEyebrow": "FAQ",
        "suz.q1": "Вы официальный дилер Suzuki?",
        "suz.a1": "Нет — Iron Custom Motors независимая мастерская Suzuki. Плюс в том, что нет дилерской наценки и есть свобода ставить оригинал или качественный неоригинал. Отзывные и гарантийные работы должны идти через официального дилера Suzuki, но всё остальное — ТО, ремонт, работа по зарядке, доработки — мы делаем по ценам независимой мастерской и с более глубоким вниманием к Suzuki.",
        "suz.q2": "Сколько стоит обслуживание Suzuki?",
        "suz.a2": "Плановое ТО — от €150, расходники включены (замена воздушного фильтра считается отдельно). Проверка зазоров клапанов — от €250 для V-образной «двойки» (SV650 / V-Strom) и €400 для рядной «четвёрки» (GSX-R / Bandit / Hayabusa); проверка с регулировкой — от €300 («двойка») и €650 («четвёрка»). Нормо-час — €50. Письменную смету вы получаете всегда до начала работ. Цены «от», налоги включены.",
        "suz.q3": "Можете настроить мою GSX-R или поставить полный выхлоп?",
        "suz.a3": "Да — ставим слипон или полную систему (Yoshimura, Akrapovič) с соответствующей коррекцией смеси, плюс подвеска и эргономика под дорогу или трек. С проверкой на стенде, когда того требует проект.",
        "suz.q4": "Беретесь за старые или классические Suzuki?",
        "suz.a4": "Да — воздушники Bandit, ранние GSX-R, одноцилиндровые DR и классические Intruder приветствуются. Чистка и синхронизация карбюраторов, восстановление зарядки и электроремонт — как раз та работа, которую мы любим.",
        "suz.q5": "Можете привезти оригинальные запчасти Suzuki в Португалию?",
        "suz.a5": "Да — у нас есть доступ к каталогу оригинальных запчастей Suzuki через дистрибьюторскую сеть плюс все крупные каталоги неоригинала. Если деталь существует для вашей модели, мы привезём её в Кашкайш.",
        "suz.q6": "Загорелась лампа зарядки — это серьёзно?",
        "suz.a6": "На Suzuki это чаще всего реле-регулятор или статор — хорошо известное слабое место марки. Не катайтесь дальше: умирающее реле-регулятор может утянуть за собой АКБ и статор. Привозите — проверим всю систему зарядки под нагрузкой и письменно скажем, что именно нужно.",
        "seo.relatedTitle": "Продолжите в той же сервисной системе.",
        "seo.relatedEyebrow": "Связанные направления",
        "seo.relatedLead": "Переходите к следующим важным страницам: сервис, запчасти, цены, бренды и контакт.",
        "seo.localTitle": "Работаем в Кашкайше, Лиссабоне и Большом Лиссабоне.",
        "seo.localEyebrow": "Локальная зона сервиса",
        "seo.localLead": "Iron Custom Motors находится в Сан-Домингуш-де-Рана, Кашкайш. Работаем с райдерами из Кашкайша, Эшторила, Оэйраша, Синтры, Лиссабона и всего Большого Лиссабона.",
        "seo.area1t": "Мастерская в Кашкайше",
        "seo.area1d": "Настоящая мастерская и лаундж для клиентов, а не удалённый прилавок с запчастями. Запишитесь на сервис, оставьте мотоцикл или приезжайте обсудить проект.",
        "seo.area2t": "Многоязычный процесс",
        "seo.area2d": "Общение на английском, русском, украинском и португальском, с письменными сметами и понятными шагами.",
        "seo.area3t": "Единая зона ответственности",
        "seo.area3d": "Диагностика, поставка запчастей, установка, апгрейды и сопровождение — под единым стандартом мастерской.",
        "suz.ctaTitle": "Привозите вашу Suzuki.",
        "suz.ctaEyebrow": "Когда будете готовы",
        "suz.ctaText": "Пришлите модель, год и короткое описание в WhatsApp. Вернёмся с ближайшим свободным окном и письменной сметой до начала работ. Вт–Сб, 10:00–18:00."
    },
    "uk": {
        "suz.eyebrow": "Suzuki · Кашкайш / Великий Лісабон",
        "suz.h1": "Сервіс Suzuki<br/>у <span class=\"accent\">Кашкайші.</span>",
        "suz.sub": "Незалежна майстерня Suzuki — діагностика, планове ТО, регулювання клапанів, ремонт системи заряджання, підвіска й тюнінг для GSX-R, GSX-S, V-Strom, SV650, Hayabusa, Katana, Bandit, Boulevard і DR-Z.",
        "suz.heroAlt": "Мотоцикл Suzuki на підйомнику в майстерні Iron Custom Motors, Кашкайш",
        "suz.breadHome": "Головна",
        "suz.h1Crumb": "Сервіс Suzuki",
        "suz.btnWA": "WhatsApp",
        "suz.btnSend": "Надіслати заявку",
        "suz.btnBack": "На головну",
        "suz.introTitle": "Японська інженерія, ціни незалежної майстерні.",
        "suz.introEyebrow": "Чому Suzuki варто привезти до нас",
        "suz.introP1": "Iron Custom Motors — незалежний спеціаліст із Suzuki в Кашкайші. Suzuki робить одні з найчесніших і найвитриваліших моторів на дорозі: рядні «четвірки» GSX-R, V-подібні «двійки» SV650 та V-Strom, легендарну Hayabusa. Але навіть чесній техніці потрібні люди, які по-справжньому її розуміють. Ми саме такі — майстерня, де Suzuki на першому місці, а не універсальний сервіс, який заразом бере й Suzuki.",
        "suz.introP2": "Інженерна культура тут виникла не на порожньому місці. Це команда, за плечима якої кастом-проєкти — чемпіони світу AMD, рекорд швидкості на Бонневілі та перемога на BMW Motorrad Customizing Championship 2023. Ми говоримо про це не заради трофеїв, а тому що той самий підхід до замірів, допусків і якості виконання тепер іде і в рутинну перевірку клапанів GSX-R, і в ремонт зарядки V-Strom із великим пробігом.",
        "suz.introP3": "Незалежна майстерня — це відсутність дилерської націнки, свобода ставити оригінал або якісний неоригінал по суті справи, і пряма розмова з тим, хто робить роботу. Письмовий кошторис до початку, письмовий звіт після.",
        "suz.toolsTitle": "Діагностика та інструмент під Suzuki.",
        "suz.toolsEyebrow": "Спеціалізований інструмент",
        "suz.toolsLead": "Діагностика Suzuki дилерського рівня та модельний інструмент, якого в більшості незалежних майстерень просто немає. Саме це відрізняє справжній сервіс Suzuki від майстерні, яка «теж бере Suzuki».",
        "suz.t1t": "SDS — Suzuki Diagnostic System (або аналог)",
        "suz.t1d": "Зчитує й скидає фірмові коди помилок Suzuki, показує дані з датчиків у реальному часі, виконує скидання ISC / дросельної заслінки й перевіряє систему заряджання під навантаженням.",
        "suz.t2t": "Синхронізація дросельних заслінок",
        "suz.t2d": "Синхронізація ртутними колонками та цифрова — для рядних «четвірок» GSX-R / GSX-S / Bandit / Hayabusa і V-подібних SV650 / V-Strom. Рівний холостий хід, чисте сумішоутворення.",
        "suz.t3t": "Навантажувальний тест системи заряджання",
        "suz.t3d": "Окрема перевірка статора й реле-регулятора під реальним навантаженням — найважливіша перевірка на будь-якій Suzuki з пробігом.",
        "suz.t4t": "Інструмент для підвіски",
        "suz.t4d": "Заміна сальників, обслуговування картриджа й амортизатора — спортивна геометрія GSX-R, ендуро V-Strom і дорожня SV650. Налаштування переднатягу й демпфування як належить.",
        "suz.servicesTitle": "ТО. Ремонт. Тюнінг.",
        "suz.servicesEyebrow": "Що робимо по Suzuki",
        "suz.servicesLead": "Від звичайної заміни оливи з фільтром до повного відновлення системи заряджання чи підготовки GSX-R до треку — усе зі знанням конкретики Suzuki.",
        "suz.s1t": "01 Планове ТО",
        "suz.s1d": "Сервіс за регламентом Suzuki — олива, фільтр, рідини, перевірка гальм, огляд ланцюга й зірок, плюс позиції за моделлю. Від €150, витратні матеріали включені.",
        "suz.s2t": "02 Регулювання клапанів — «двійка» / «четвірка»",
        "suz.s2d": "Робимо як треба — щупами й підбором шайб. V-подібні SV650 / V-Strom, рядні GSX-R / GSX-S / Bandit / Hayabusa.",
        "suz.s3t": "03 Ремонт системи заряджання",
        "suz.s3d": "Діагностика й заміна статора, реле-регулятора та АКБ. Класичний ремонт Suzuki — і той, який ми знаємо найкраще.",
        "suz.s4t": "04 Електродіагностика",
        "suz.s4d": "Повне зчитування кодів і даних у реальному часі через SDS / аналог. Бензонасос, ISC, датчики, проводка додаткового обладнання, боротьба з корозією.",
        "suz.s5t": "05 Паливна система",
        "suz.s5d": "Діагностика насоса, чистка форсунок, синхронізація заслінок і стабілізація холостого ходу на інжекторних Suzuki; чистка й налаштування карбюраторів на класиці.",
        "suz.s6t": "06 Підвіска",
        "suz.s6d": "Заміна сальників, заміна оливи, переборка картриджа й амортизатора, налаштування переднатягу й демпфування для GSX-R, V-Strom і SV650.",
        "suz.s7t": "07 Зчеплення й трансмісія",
        "suz.s7d": "Огляд і заміна зчеплення, заміна ланцюга й зірок, діагностика КПП. Обслуговування проковзувального зчеплення там, де воно є.",
        "suz.s8t": "08 Тюнінг і апгрейди",
        "suz.s8d": "Встановлення вихлопу з корекцією суміші (Yoshimura, Akrapovič), апгрейд підвіски, ергономіка, захист і підготовка до далеких поїздок.",
        "suz.issuesTitle": "Слабкі місця Suzuki, знаходимо до того, як підведуть.",
        "suz.issuesEyebrow": "Типові проблеми, які знаємо",
        "suz.issuesLead": "Роки роботи із Suzuki — це знання того, де ці мотоцикли втомлюються. Ми перевіряємо зони ризику заздалегідь, а не після того, як мотоцикл став на дорозі до Сінтри.",
        "suz.i1t": "Відмова реле-регулятора",
        "suz.i1d": "славнозвісне слабке місце Suzuki крізь покоління GSX-R, SV650 і V-Strom. Перевіряємо під навантаженням, поки воно не «вбило» АКБ і статор, і за потреби ставимо краще охолоджуваний вузол.",
        "suz.i2t": "Знос статора й зарядки на великих пробігах",
        "suz.i2d": "виявляємо нормальним навантажувальним тестом, а не вгадуванням по акумулятору. Заміряємо віддачу на холодну й на гарячу, поки мотоцикл вас не підвів.",
        "suz.i3t": "Знос натягувача ланцюга ГРМ",
        "suz.i3d": "відомий стук на деяких моделях Suzuki. Діагностуємо точно, а не ганяємося за звуком по всьому мотору.",
        "suz.i4t": "Бензонасос та ISC",
        "suz.i4d": "провали при гарячому пуску й «плаваючий» холостий на інжекторі. Перевіряємо насос і коректно скидаємо ISC за діагностикою.",
        "suz.i5t": "Знос і веде зчеплення",
        "suz.i5d": "кошик і диски міряємо за специфікацією, а не «на руку» — особливо на відпалюваних GSX-R і V-Strom із великим пробігом.",
        "suz.modelsTitle": "Уся лінійка Suzuki.",
        "suz.modelsEyebrow": "Моделі, які обслуговуємо",
        "suz.modelsLead": "Поточне виробництво, недавнє минуле, сучасна класика — якщо на баку літера S, привозьте.",
        "suz.m1t": "GSX-R (суперспорт)",
        "suz.m1d": "GSX-R600, GSX-R750, GSX-R1000 / R. Дорога, підготовка до треку й налаштування на стенді.",
        "suz.m2t": "GSX-S і GSX-8 (нейкед / спорт)",
        "suz.m2d": "GSX-S750, GSX-S1000 / GT / F, GSX-8S, GSX-8R.",
        "suz.m3t": "Hayabusa і Katana",
        "suz.m3d": "GSX1300R Hayabusa (усі покоління), Katana 1000.",
        "suz.m4t": "SV650 і Bandit",
        "suz.m4d": "SV650 / SV650X, Bandit 650 / 1200 / 1250.",
        "suz.m5t": "V-Strom (адвенчер)",
        "suz.m5d": "V-Strom 650 (DL650), V-Strom 800 / 800DE, V-Strom 1000 (DL1000), V-Strom 1050 (DL1050).",
        "suz.m6t": "Круїзери й ендуро",
        "suz.m6d": "родина Boulevard / Intruder M / C, DR650, DR-Z400 і нові DR-Z4S / 4SM.",
        "suz.partsTitle": "Доступ до каталогів основних запчастин Suzuki.",
        "suz.partsEyebrow": "Запчастини та аксесуари",
        "suz.partsLead": "Возимо через оригінал Suzuki і найбільші міжнародні каталоги неоригіналу. Що потрібно вашому мотоциклу — оригінал, спорт, туризм чи захист — замовляємо напряму в перевірених постачальників.",
        "suz.partsList": "<strong>Каталоги, з якими працюємо:</strong> оригінальні запчастини Suzuki через дистриб'юторську мережу · Yoshimura · Akrapovič · Öhlins · K-Tech · Brembo · EBC · DID · Renthal · Rizoma · SW-Motech · Givi · Mitas · Avon. Можна замовити заздалегідь, навіть без запису на сервіс.",
        "suz.faqTitle": "Поширені запитання. (FAQ)",
        "suz.faqEyebrow": "FAQ",
        "suz.q1": "Ви офіційний дилер Suzuki?",
        "suz.a1": "Ні — Iron Custom Motors незалежна майстерня Suzuki. Перевага в тому, що немає дилерської націнки і є свобода ставити оригінал або якісний неоригінал. Відкличні та гарантійні роботи мають іти через офіційного дилера Suzuki, але все інше — ТО, ремонт, робота із зарядкою, доопрацювання — ми робимо за цінами незалежної майстерні та з глибшою увагою до Suzuki.",
        "suz.q2": "Скільки коштує обслуговування Suzuki?",
        "suz.a2": "Планове ТО — від €150, витратні матеріали включені (заміна повітряного фільтра рахується окремо). Перевірка зазорів клапанів — від €250 для V-подібної «двійки» (SV650 / V-Strom) і €400 для рядної «четвірки» (GSX-R / Bandit / Hayabusa); перевірка з регулюванням — від €300 («двійка») і €650 («четвірка»). Нормо-година — €50. Письмовий кошторис ви отримуєте завжди до початку робіт. Ціни «від», податки включені.",
        "suz.q3": "Можете налаштувати мою GSX-R чи поставити повний вихлоп?",
        "suz.a3": "Так — ставимо сліпон чи повну систему (Yoshimura, Akrapovič) з відповідною корекцією суміші, плюс підвіска та ергономіка під дорогу або трек. З перевіркою на стенді, коли цього вимагає проєкт.",
        "suz.q4": "Беретеся за старі чи класичні Suzuki?",
        "suz.a4": "Так — повітрянки Bandit, ранні GSX-R, одноциліндрові DR і класичні Intruder вітаються. Чистка й синхронізація карбюраторів, відновлення зарядки та електроремонт — саме та робота, яку ми любимо.",
        "suz.q5": "Можете привезти оригінальні запчастини Suzuki до Португалії?",
        "suz.a5": "Так — у нас є доступ до каталогу оригінальних запчастин Suzuki через дистриб'юторську мережу плюс усі великі каталоги неоригіналу. Якщо деталь існує для вашої моделі, ми привеземо її до Кашкайша.",
        "suz.q6": "Загорілася лампа зарядки — це серйозно?",
        "suz.a6": "На Suzuki це найчастіше реле-регулятор або статор — добре відоме слабке місце марки. Не їздьте далі: реле-регулятор, що відмовляє, може потягнути за собою АКБ і статор. Привозьте — перевіримо всю систему заряджання під навантаженням і письмово скажемо, що саме потрібно.",
        "seo.relatedTitle": "Продовжте в тій самій сервісній системі.",
        "seo.relatedEyebrow": "Пов’язані напрямки",
        "seo.relatedLead": "Переходьте до наступних важливих сторінок: сервіс, запчастини, ціни, бренди та контакт.",
        "seo.localTitle": "Працюємо в Кашкайші, Лісабоні та Великому Лісабоні.",
        "seo.localEyebrow": "Локальна зона сервісу",
        "seo.localLead": "Iron Custom Motors розташована в Сан-Домінгуш-де-Рана, Кашкайш. Працюємо з райдерами з Кашкайша, Ешторіла, Оейраша, Сінтри, Лісабона й усього Великого Лісабона.",
        "seo.area1t": "Майстерня в Кашкайші",
        "seo.area1d": "Справжня майстерня й лаунж для клієнтів, а не віддалений прилавок із запчастинами. Запишіться на сервіс, залиште мотоцикл або приїздіть обговорити проєкт.",
        "seo.area2t": "Багатомовний процес",
        "seo.area2d": "Спілкування англійською, російською, українською та португальською, з письмовими кошторисами й зрозумілими кроками.",
        "seo.area3t": "Єдина зона відповідальності",
        "seo.area3d": "Діагностика, постачання запчастин, установка, апгрейди й супровід — за єдиним стандартом майстерні.",
        "suz.ctaTitle": "Привозьте вашу Suzuki.",
        "suz.ctaEyebrow": "Коли будете готові",
        "suz.ctaText": "Надішліть модель, рік і короткий опис у WhatsApp. Повернемося з найближчим вільним вікном і письмовим кошторисом до початку робіт. Вт–Сб, 10:00–18:00."
    }
}

# ====================================================================================
# Honda
# ====================================================================================
PAGE_I18N["honda-service"] = {
    "en": {
        "hon.eyebrow": "Honda · Cascais / Greater Lisbon",
        "hon.heroAlt": "Honda motorcycle on the lift at Iron Custom Motors workshop in Cascais, Greater Lisbon",
        "hon.breadHome": "Home",
        "hon.h1Crumb": "Honda service",
        "hon.btnWA": "WhatsApp us",
        "hon.btnSend": "Send a request",
        "hon.btnBack": "Back to home",
        "hon.h1": "Honda motorcycle service<br/>in <span class=\"accent\">Cascais.</span>",
        "hon.sub": "Independent Honda workshop — diagnostics, scheduled service, DCT service, valve clearance, electrical, suspension and tuning for Africa Twin, CB, CBR, Hornet, Gold Wing, VFR, Rebel and the small-bore fun bikes.",
        "hon.introTitle": "Honda reliability, independent-workshop care.",
        "hon.introEyebrow": "Why bring your Honda to us",
        "hon.introP1": "Iron Custom Motors is an independent Honda motorcycle specialist in Cascais. Honda has a reputation for building some of the most reliable engines on the road — and that reputation is earned. But \"reliable\" doesn't mean \"service-free,\" and it doesn't mean every workshop knows where a high-mileage Honda actually needs attention. We do.",
        "hon.introP2": "The engineering culture here isn't borrowed. Our team has stood on the podium where it counts — AMD World Championship builders, a Bonneville land-speed record, and BMW Motorrad Customizing Champions 2023. That's the level of mechanical discipline we bring to a routine oil-and-valve service on a CB650R, not just to a show bike. The same hands that built record-setting machines torque your fork pinch bolts.",
        "hon.introP3": "Independent means no dealer mark-up, freedom to fit OEM or quality aftermarket as the job calls for it, and direct communication. Written estimate before any work, written report after. That is the whole arrangement.",
        "hon.toolsTitle": "Honda-specific diagnostic and tools.",
        "hon.toolsEyebrow": "Specialist tooling",
        "hon.toolsLead": "A real Honda shop is defined by whether it can talk to the bike the way the factory does. We run dealer-grade Honda motorcycle diagnostics — not a generic OBD reader that only sees emissions codes.",
        "hon.t1t": "Honda MCS (Motorcycle Communication System)",
        "hon.t1d": "Honda's dedicated motorcycle diagnostic platform. Reads and clears DTCs across all ECUs, monitors live PGM-FI data, runs the \"Quick Doctor\" health check, and performs resets and adaptations a generic scanner can't reach.",
        "hon.t2t": "HDS / dealer-equivalent procedures",
        "hon.t2d": "Where a model calls for deeper system access or guided troubleshooting, we run Honda Diagnostic System protocols to get into the menus generic tools never see.",
        "hon.t3t": "DCT service capability",
        "hon.t3d": "Dual Clutch Transmission is the Honda differentiator most independent shops avoid. We service it properly — fluid and filter change to Honda's procedure, clutch behaviour diagnosis, and software-side checks for shift-quality complaints.",
        "hon.t4t": "Throttle, sync and PGM-FI tooling",
        "hon.t4d": "Throttle body synchronisation, idle and fuelling checks, injector and sensor live-data verification on the multi-cylinder bikes.",
        "hon.servicesTitle": "Service. Repair. Tune.",
        "hon.servicesEyebrow": "What we do on Honda",
        "hon.servicesLead": "From a first scheduled service on a new Transalp to a full electrical rebuild on a VFR — done with Honda-specific knowledge and the right tooling.",
        "hon.s1t": "01 Scheduled service (oil, filter, fluids, checks)",
        "hon.s1d": "Honda interval service — oil and filter, fluids, brake and chain inspection, plus model-specific items. Consumables included; from €150.",
        "hon.s2t": "02 DCT fluid + filter service",
        "hon.s2d": "Dual Clutch Transmission fluid and filter change to Honda's procedure, plus clutch engagement check and software-side verification. The job most workshops won't touch — we will, on Africa Twin DCT, NC750X DCT, Gold Wing DCT and the rest.",
        "hon.s3t": "03 Valve clearance — twin / four",
        "hon.s3d": "Done properly with feeler gauges and shim or bucket selection where the engine requires it. Honda's V4 and inline-4 valve work is labour-intensive and we price it honestly up front.",
        "hon.s4t": "04 Electrical diagnostics & charging",
        "hon.s4d": "Full fault-code read and live data with MCS. Regulator/rectifier, stator and charging-system diagnosis — a known Honda weak point we check first, not last.",
        "hon.s5t": "05 Suspension service",
        "hon.s5d": "Fork seal replacement, oil change, sag and preload setup, rebound and compression tuning. Showa and Öhlins rebuild where fitted. While the wheels are off, this is the natural moment for new rubber — see our <a href=\"/motorcycle-tyre-service/\">motorcycle tyre fitting and balancing</a> service.",
        "hon.s6t": "06 Brake service & ABS",
        "hon.s6d": "Pad and fluid service, caliper rebuild, full ABS bleed including Honda's combined-brake systems where fitted.",
        "hon.s7t": "07 Engine tune-up",
        "hon.s7d": "Throttle body sync, idle stabilisation, spark plug service, PGM-FI live-data check across twins and fours.",
        "hon.s8t": "08 Tuning and upgrades",
        "hon.s8d": "Exhaust install with the matched fuelling solution (Akrapovič, Yoshimura, SC-Project), suspension upgrades, ergonomics, touring and protection.",
        "hon.issuesTitle": "Honda failure patterns, checked before they bite.",
        "hon.issuesEyebrow": "Typical issues we know",
        "hon.issuesLead": "Honda builds reliable bikes — so the honest version is this: there aren't many weak points, but the ones that exist are well known, and we check them by default rather than waiting for a roadside failure.",
        "hon.i1t": "Regulator / rectifier failure",
        "hon.i1d": "The classic older-Honda fault — CBR, VFR and Hornet of a certain age cook their regulator/rectifier. We test charging output and connector condition before it strands you.",
        "hon.i2t": "Stator and high-mileage charging",
        "hon.i2d": "On higher-mileage bikes the stator and charging circuit drift. We read the full charging system rather than guessing at a flat battery.",
        "hon.i3t": "Cam chain tensioner wear",
        "hon.i3d": "Some Honda models develop tensioner rattle with age. We identify whether it's the tensioner, the chain, or a harmless cold-start noise.",
        "hon.i4t": "VFR / V4 valve-service labour",
        "hon.i4d": "The V4's valve service is genuinely labour-intensive — there's no shortcut. We tell you the real hours up front so the bill is never a surprise.",
        "hon.i5t": "DCT software & clutch behaviour",
        "hon.i5d": "Harsh or hesitant DCT shifts are often a software or clutch-adaptation issue, not a failure. We diagnose with MCS before anyone talks about replacing parts.",
        "hon.i6t": "Fuel pump",
        "hon.i6d": "Aging fuel pumps cause hot-start and high-load stumbles. We pressure-test rather than swap on a hunch.",
        "hon.modelsTitle": "Across the Honda lineup.",
        "hon.modelsEyebrow": "Models we service",
        "hon.modelsLead": "Current production, recent past, modern classics — if it wears the wing, bring it in.",
        "hon.m1t": "CB / Hornet family",
        "hon.m1d": "CB500F, CB650R, CB750 Hornet, CB1000R and CB1000 Hornet — the naked range we see most.",
        "hon.m2t": "CBR",
        "hon.m2d": "CBR500R, CBR650R, CBR600RR, and the CBR1000RR-R Fireblade — street, sport and track prep.",
        "hon.m3t": "Africa Twin",
        "hon.m3d": "CRF1100L Africa Twin, including the DCT models. Adventure setup, DCT service, long-travel suspension.",
        "hon.m4t": "NC750X & Transalp",
        "hon.m4d": "NC750X (manual and DCT) and the XL750 Transalp — the do-everything middleweights.",
        "hon.m5t": "Rebel",
        "hon.m5d": "CMX500 and CMX1100 Rebel — including the Rebel 1100 DCT.",
        "hon.m6t": "Gold Wing",
        "hon.m6d": "GL1800 Gold Wing — full touring service, DCT, suspension and electronics.",
        "hon.m7t": "VFR & CB1100",
        "hon.m7d": "VFR800 and VFR1200 V4s; the air-cooled CB1100 modern classic.",
        "hon.m8t": "CRF dual-sport & enduro",
        "hon.m8d": "CRF300L and CRF450 — dual-sport and enduro service and setup.",
        "hon.m9t": "Small fun bikes",
        "hon.m9d": "Grom / MSX125, Monkey and Dax — the little ones get the same attention as the big ones.",
        "hon.partsTitle": "Catalog access for major Honda parts.",
        "hon.partsEyebrow": "Parts and aftermarket",
        "hon.partsLead": "We source genuine Honda OEM parts through the distributor network, alongside top-tier aftermarket for performance, touring and protection. From a single OEM filter to a full exhaust system, we order it directly.",
        "hon.partsList": "<strong>Catalogs we work with:</strong> OEM Honda parts via distributor network · Akrapovič · Yoshimura · SC-Project · Öhlins · Showa service parts · Brembo · NGK · Pro Honda lubricants · Hepco & Becker · SW-Motech · Givi · Barkbusters · Mitas · Michelin · Pirelli. Order ahead even if you're not booking service.",
        "hon.faqTitle": "Common questions. (FAQ)",
        "hon.faqEyebrow": "FAQ",
        "hon.q1": "Are you an authorised Honda dealer?",
        "hon.a1": "No — Iron Custom Motors is an independent Honda motorcycle workshop. The advantage is no dealer mark-up and freedom to use OEM or quality aftermarket parts. Recall and warranty work itself must go to an authorised Honda dealer, but everything else — scheduled service, DCT service, repair, modifications — we handle at independent rates and with deeper, hands-on attention.",
        "hon.q2": "How much does a Honda service cost?",
        "hon.a2": "Scheduled maintenance starts from €150 with consumables included (air-filter replacement is charged separately). Valve-clearance work on the Japanese twins is €250 to check, €300 to check and adjust; on the inline-fours it's €400 to check, €650 to check and adjust. Other work is €50/hour. You get a written estimate before anything starts. All prices include tax.",
        "hon.q3": "Do you service Honda DCT (Dual Clutch Transmission)?",
        "hon.a3": "Yes — and this is a genuine differentiator. We do DCT fluid and filter changes to Honda's procedure, diagnose clutch-engagement and shift-quality issues with MCS, and verify the software side. Africa Twin DCT, NC750X DCT, Rebel 1100 DCT, Gold Wing DCT — all handled in-house.",
        "hon.q4": "Can you tune or upgrade my Honda?",
        "hon.a4": "Yes — exhaust systems with the matched fuelling solution, suspension upgrades, ergonomics and track prep for the CBR / Fireblade. We tell you honestly what delivers a real-world gain and what's just noise.",
        "hon.q5": "Can you import OEM Honda parts to Portugal?",
        "hon.a5": "Yes — we have catalog access to genuine Honda OEM parts through the distributor network plus all the major aftermarket catalogs. If a part exists for your model, we source it and bring it in.",
        "hon.q6": "My Honda is high-mileage — is it worth servicing here?",
        "hon.a6": "Absolutely. High-mileage Hondas are exactly where our charging-system, valve and DCT knowledge pays off. We check the known weak points proactively and keep a reliable bike reliable.",
        "seo.relatedTitle": "Continue through the same service system.",
        "seo.relatedEyebrow": "Related workshop paths",
        "seo.relatedLead": "Follow the most relevant next pages for service, parts, pricing, brand support and contact.",
        "seo.localTitle": "Serving Cascais, Lisbon and Greater Lisbon.",
        "seo.localEyebrow": "Local service area",
        "seo.localLead": "Iron Custom Motors is based in São Domingos de Rana, Cascais. We work with Honda riders from Cascais, Estoril, Oeiras, Sintra, Lisbon and the wider Greater Lisbon area.",
        "seo.area1t": "Cascais workshop",
        "seo.area1d": "A real workshop and client lounge, not a remote parts counter. Book service, drop off the bike, or visit to discuss a project.",
        "seo.area2t": "Multilingual process",
        "seo.area2d": "English, Russian, Ukrainian and Portuguese communication with written estimates and clear next steps.",
        "seo.area3t": "One accountable path",
        "seo.area3d": "Diagnostics, parts sourcing, installation, upgrades and follow-up happen under one workshop standard.",
        "hon.ctaTitle": "Bring your Honda in.",
        "hon.ctaEyebrow": "Ready when you are",
        "hon.ctaText": "Send the model, year and a short description via WhatsApp. We'll come back with the closest available slot and a written estimate before work starts. Tue–Sat, 10:00–18:00."
    },
    "pt": {
        "hon.eyebrow": "Honda · Cascais / Grande Lisboa",
        "hon.heroAlt": "Mota Honda na plataforma da oficina Iron Custom Motors em Cascais, Grande Lisboa",
        "hon.breadHome": "Início",
        "hon.h1Crumb": "Serviço Honda",
        "hon.btnWA": "WhatsApp",
        "hon.btnSend": "Enviar pedido",
        "hon.btnBack": "Voltar ao início",
        "hon.h1": "Serviço de motos Honda<br/>em <span class=\"accent\">Cascais.</span>",
        "hon.sub": "Oficina Honda independente — diagnóstico, manutenção programada, serviço DCT, folga de válvulas, eletricidade, suspensão e afinação para Africa Twin, CB, CBR, Hornet, Gold Wing, VFR, Rebel e as pequenas motos divertidas.",
        "hon.introTitle": "Fiabilidade Honda, cuidado de oficina independente.",
        "hon.introEyebrow": "Porque trazer a sua Honda até nós",
        "hon.introP1": "A Iron Custom Motors é uma especialista Honda independente em Cascais. A Honda tem a reputação de construir alguns dos motores mais fiáveis da estrada — e essa reputação é merecida. Mas \"fiável\" não quer dizer \"sem manutenção\", nem quer dizer que qualquer oficina sabe onde uma Honda com muitos quilómetros precisa realmente de atenção. Nós sabemos.",
        "hon.introP2": "A cultura de engenharia desta casa não é emprestada. A nossa equipa esteve no pódio que conta — construtores Campeões do Mundo AMD, um recorde de velocidade em Bonneville e Campeões de Customização BMW Motorrad 2023. É esse o nível de disciplina mecânica que aplicamos a uma simples mudança de óleo e válvulas numa CB650R, não só a uma mota de exposição. As mesmas mãos que construíram máquinas recordistas apertam os parafusos da sua forquilha.",
        "hon.introP3": "Independente significa sem margem de concessionário, liberdade para montar peças OEM ou aftermarket de qualidade conforme o trabalho exige, e comunicação direta. Orçamento escrito antes de qualquer trabalho, relatório escrito no fim. É esse o acordo, por inteiro.",
        "hon.toolsTitle": "Diagnóstico e ferramentas específicos Honda.",
        "hon.toolsEyebrow": "Ferramenta especialista",
        "hon.toolsLead": "Uma verdadeira oficina Honda define-se pela capacidade de comunicar com a mota como a fábrica o faz. Usamos diagnóstico Honda de nível concessionário — não um leitor OBD genérico que só vê códigos de emissões.",
        "hon.t1t": "Honda MCS (Motorcycle Communication System)",
        "hon.t1d": "A plataforma de diagnóstico dedicada às motos Honda. Lê e apaga DTCs em todas as ECU, monitoriza dados PGM-FI em tempo real, executa o teste de saúde \"Quick Doctor\" e realiza resets e adaptações que um scanner genérico não alcança.",
        "hon.t2t": "HDS / procedimentos equivalentes ao concessionário",
        "hon.t2d": "Quando um modelo exige acesso mais profundo ao sistema ou diagnóstico guiado, executamos os protocolos Honda Diagnostic System para entrar nos menus que as ferramentas genéricas nunca veem.",
        "hon.t3t": "Capacidade de serviço DCT",
        "hon.t3d": "A Dual Clutch Transmission é o diferenciador Honda que a maioria das oficinas independentes evita. Nós fazemo-lo corretamente — mudança de fluido e filtro segundo o procedimento Honda, diagnóstico do comportamento da embraiagem e verificações ao nível do software para queixas de qualidade de mudança.",
        "hon.t4t": "Sincronização, gás e PGM-FI",
        "hon.t4d": "Sincronização de corpos de borboleta, verificação de ralenti e alimentação, validação em tempo real de injetores e sensores nas motos multicilíndricas.",
        "hon.servicesTitle": "Serviço. Reparação. Afinação.",
        "hon.servicesEyebrow": "O que fazemos em Honda",
        "hon.servicesLead": "Da primeira revisão de uma Transalp nova a uma reconstrução elétrica completa de uma VFR — feito com conhecimento específico Honda e a ferramenta certa.",
        "hon.s1t": "01 Manutenção programada (óleo, filtro, fluidos, verificações)",
        "hon.s1d": "Revisão Honda por intervalo — óleo e filtro, fluidos, inspeção de travões e corrente, mais itens específicos do modelo. Consumíveis incluídos; desde 150 €.",
        "hon.s2t": "02 Serviço de fluido + filtro DCT",
        "hon.s2d": "Mudança de fluido e filtro da Dual Clutch Transmission segundo o procedimento Honda, mais verificação do engate da embraiagem e validação ao nível do software. O trabalho que a maioria das oficinas não toca — nós fazemos, na Africa Twin DCT, NC750X DCT, Gold Wing DCT e restantes.",
        "hon.s3t": "03 Folga de válvulas — bicilíndrico / quatro cilindros",
        "hon.s3d": "Feito corretamente com apalpa-folgas e seleção de calços onde o motor o exige. O trabalho de válvulas dos V4 e quatro-em-linha Honda é exigente em mão-de-obra e orçamentamo-lo com honestidade à partida.",
        "hon.s4t": "04 Diagnóstico elétrico e carga",
        "hon.s4d": "Leitura completa de códigos e dados em tempo real com MCS. Diagnóstico de regulator/rectifier, stator e sistema de carga — um ponto fraco conhecido da Honda que verificamos primeiro, não por último.",
        "hon.s5t": "05 Serviço de suspensão",
        "hon.s5d": "Substituição de retentores, mudança de óleo, regulação de sag e pré-carga, afinação de retorno e compressão. Revisão Showa e Öhlins quando montados. Com as rodas fora, é o momento natural para borracha nova — veja o nosso serviço de <a href=\"/pt/montagem-de-pneus-mota/\">montagem e equilibragem de pneus de mota</a>.",
        "hon.s6t": "06 Serviço de travões e ABS",
        "hon.s6d": "Pastilhas e fluido, reconstrução de pinças, purga completa do ABS incluindo os sistemas de travagem combinada Honda quando montados.",
        "hon.s7t": "07 Afinação de motor",
        "hon.s7d": "Sincronização de borboletas, estabilização de ralenti, velas, verificação de dados PGM-FI em bicilíndricos e quatro cilindros.",
        "hon.s8t": "08 Afinação e upgrades",
        "hon.s8d": "Montagem de escape com a solução de alimentação correspondente (Akrapovič, Yoshimura, SC-Project), upgrades de suspensão, ergonomia, viagem e proteção.",
        "hon.issuesTitle": "Padrões de falha Honda, verificados antes de morderem.",
        "hon.issuesEyebrow": "Problemas típicos que conhecemos",
        "hon.issuesLead": "A Honda constrói motos fiáveis — por isso a versão honesta é esta: não há muitos pontos fracos, mas os que existem são bem conhecidos, e verificamo-los por defeito em vez de esperar por uma avaria na estrada.",
        "hon.i1t": "Falha do regulator / rectifier",
        "hon.i1d": "A falha clássica das Honda mais antigas — CBR, VFR e Hornet de certa idade \"cozem\" o regulator/rectifier. Testamos a saída de carga e o estado dos conectores antes que o deixe a pé.",
        "hon.i2t": "Stator e carga em alta quilometragem",
        "hon.i2d": "Em motos com muitos quilómetros, o stator e o circuito de carga degradam-se. Lemos todo o sistema de carga em vez de adivinhar uma bateria descarregada.",
        "hon.i3t": "Desgaste do tensor de corrente de distribuição",
        "hon.i3d": "Alguns modelos Honda desenvolvem ruído do tensor com a idade. Identificamos se é o tensor, a corrente ou um ruído inofensivo de arranque a frio.",
        "hon.i4t": "Mão-de-obra de válvulas VFR / V4",
        "hon.i4d": "O serviço de válvulas do V4 é genuinamente exigente — não há atalhos. Dizemos-lhe as horas reais à partida para que a fatura nunca seja uma surpresa.",
        "hon.i5t": "Software e comportamento da embraiagem DCT",
        "hon.i5d": "Mudanças DCT bruscas ou hesitantes são muitas vezes uma questão de software ou de adaptação da embraiagem, não uma avaria. Diagnosticamos com MCS antes de falar em substituir peças.",
        "hon.i6t": "Bomba de combustível",
        "hon.i6d": "Bombas de combustível envelhecidas causam falhas em arranque a quente e a carga elevada. Testamos a pressão em vez de substituir por palpite.",
        "hon.modelsTitle": "Em toda a gama Honda.",
        "hon.modelsEyebrow": "Modelos que servimos",
        "hon.modelsLead": "Produção atual, passado recente, clássicos modernos — se tem a asa, traga-a.",
        "hon.m1t": "Família CB / Hornet",
        "hon.m1d": "CB500F, CB650R, CB750 Hornet, CB1000R e CB1000 Hornet.",
        "hon.m2t": "CBR",
        "hon.m2d": "CBR500R, CBR650R, CBR600RR e a CBR1000RR-R Fireblade — estrada, desporto e preparação de pista.",
        "hon.m3t": "Africa Twin",
        "hon.m3d": "CRF1100L Africa Twin, incluindo os modelos DCT.",
        "hon.m4t": "NC750X & Transalp",
        "hon.m4d": "NC750X (manual e DCT) e a XL750 Transalp.",
        "hon.m5t": "Rebel",
        "hon.m5d": "CMX500 e CMX1100 Rebel — incluindo a Rebel 1100 DCT.",
        "hon.m6t": "Gold Wing",
        "hon.m6d": "GL1800 Gold Wing — serviço completo de viagem, DCT, suspensão e eletrónica.",
        "hon.m7t": "VFR & CB1100",
        "hon.m7d": "VFR800 e VFR1200 V4; a CB1100 clássica moderna arrefecida a ar.",
        "hon.m8t": "CRF dual-sport & enduro",
        "hon.m8d": "CRF300L e CRF450.",
        "hon.m9t": "Pequenas motos divertidas",
        "hon.m9d": "Grom / MSX125, Monkey e Dax — as pequenas recebem a mesma atenção que as grandes.",
        "hon.partsTitle": "Acesso a catálogo para peças Honda principais.",
        "hon.partsEyebrow": "Peças e aftermarket",
        "hon.partsLead": "Fornecemos peças genuínas Honda OEM através da rede de distribuição, a par de aftermarket de topo para desempenho, viagem e proteção. De um único filtro OEM a um sistema de escape completo, encomendamos diretamente.",
        "hon.partsList": "<strong>Catálogos com que trabalhamos:</strong> Peças Honda OEM via rede de distribuição · Akrapovič · Yoshimura · SC-Project · Öhlins · Peças de serviço Showa · Brembo · NGK · Lubrificantes Pro Honda · Hepco & Becker · SW-Motech · Givi · Barkbusters · Mitas · Michelin · Pirelli.",
        "hon.faqTitle": "Perguntas frequentes. (FAQ)",
        "hon.faqEyebrow": "FAQ",
        "hon.q1": "São concessionário Honda autorizado?",
        "hon.a1": "Não — a Iron Custom Motors é uma oficina Honda independente. A vantagem é não haver margem de concessionário e a liberdade de usar peças OEM ou aftermarket de qualidade. As campanhas de recolha e o trabalho em garantia têm de ir a um concessionário autorizado, mas tudo o resto — manutenção, serviço DCT, reparação, modificações — tratamos a preços independentes e com atenção mais aprofundada.",
        "hon.q2": "Quanto custa uma revisão Honda?",
        "hon.a2": "A manutenção programada começa em 150 € com consumíveis incluídos (a substituição do filtro de ar é cobrada à parte). O serviço de válvulas nos bicilíndricos japoneses é 250 € para verificar, 300 € para verificar e ajustar; nos quatro-em-linha é 400 € para verificar, 650 € para verificar e ajustar. O restante trabalho é a 50 €/hora. Recebe um orçamento escrito antes de começar. Todos os preços incluem imposto.",
        "hon.q3": "Fazem serviço Honda DCT (Dual Clutch Transmission)?",
        "hon.a3": "Sim — e é um verdadeiro diferenciador. Fazemos mudança de fluido e filtro DCT segundo o procedimento Honda, diagnosticamos problemas de engate e qualidade de mudança com MCS e validamos o lado do software. Africa Twin DCT, NC750X DCT, Rebel 1100 DCT, Gold Wing DCT — tudo feito internamente.",
        "hon.q4": "Podem afinar ou fazer upgrade à minha Honda?",
        "hon.a4": "Sim — sistemas de escape com a solução de alimentação correspondente, upgrades de suspensão, ergonomia e preparação de pista para a CBR / Fireblade. Dizemos-lhe com honestidade o que dá ganho real e o que é só barulho.",
        "hon.q5": "Podem importar peças Honda OEM para Portugal?",
        "hon.a5": "Sim — temos acesso a catálogo de peças genuínas Honda OEM através da rede de distribuição, mais todos os principais catálogos aftermarket. Se a peça existe para o seu modelo, fornecemo-la.",
        "hon.q6": "A minha Honda tem muitos quilómetros — vale a pena servir aqui?",
        "hon.a6": "Sem dúvida. As Honda de alta quilometragem são exatamente onde o nosso conhecimento de sistema de carga, válvulas e DCT compensa. Verificamos os pontos fracos conhecidos de forma proativa e mantemos fiável uma mota fiável.",
        "seo.relatedTitle": "Continue pelo mesmo sistema de serviço.",
        "seo.relatedEyebrow": "Caminhos relacionados",
        "seo.relatedLead": "Siga as próximas páginas mais relevantes para serviço, peças, preços, apoio por marca e contacto.",
        "seo.localTitle": "Ao serviço de Cascais, Lisboa e Grande Lisboa.",
        "seo.localEyebrow": "Área local de serviço",
        "seo.localLead": "A Iron Custom Motors fica em São Domingos de Rana, Cascais. Trabalhamos com motociclistas Honda de Cascais, Estoril, Oeiras, Sintra, Lisboa e toda a Grande Lisboa.",
        "seo.area1t": "Oficina em Cascais",
        "seo.area1d": "Uma oficina e lounge de cliente reais, não um balcão de peças remoto.",
        "seo.area2t": "Processo multilingue",
        "seo.area2d": "Comunicação em português, inglês, russo e ucraniano, com orçamentos escritos e próximos passos claros.",
        "seo.area3t": "Um caminho responsável",
        "seo.area3d": "Diagnóstico, peças, montagem, upgrades e acompanhamento sob um único padrão de oficina.",
        "hon.ctaTitle": "Traga a sua Honda.",
        "hon.ctaEyebrow": "Quando estiver pronto",
        "hon.ctaText": "Envie modelo, ano e uma breve descrição por WhatsApp. Respondemos com a vaga disponível mais próxima e um orçamento escrito antes de começar. Ter–Sáb, 10:00–18:00."
    },
    "ru": {
        "hon.eyebrow": "Honda · Кашкайш / Большой Лиссабон",
        "hon.heroAlt": "Мотоцикл Honda на подъёмнике в мастерской Iron Custom Motors, Кашкайш, Большой Лиссабон",
        "hon.breadHome": "Главная",
        "hon.h1Crumb": "Сервис Honda",
        "hon.btnWA": "WhatsApp",
        "hon.btnSend": "Отправить заявку",
        "hon.btnBack": "На главную",
        "hon.h1": "Сервис мотоциклов Honda<br/>в <span class=\"accent\">Кашкайше.</span>",
        "hon.sub": "Независимая мастерская Honda — диагностика, регламентное ТО, обслуживание DCT, регулировка клапанов, электрика, подвеска и тюнинг для Africa Twin, CB, CBR, Hornet, Gold Wing, VFR, Rebel и небольших «весёлых» мотоциклов.",
        "hon.introTitle": "Надёжность Honda, забота независимой мастерской.",
        "hon.introEyebrow": "Почему Honda стоит привезти к нам",
        "hon.introP1": "Iron Custom Motors — независимый специалист по мотоциклам Honda в Кашкайше. У Honda репутация одних из самых надёжных моторов на дороге, и эта репутация заслуженная. Но «надёжный» не значит «не требует обслуживания» и не значит, что любая мастерская знает, где именно Honda с большим пробегом действительно нужно внимание. Мы знаем.",
        "hon.introP2": "Инженерная культура здесь не заёмная. Наша команда стояла на подиуме, который что-то значит: сборщики — чемпионы мира AMD, рекорд скорости на солёном озере Бонневиль и титул BMW Motorrad Customizing Champions 2023. Именно с такой механической дисциплиной мы подходим к обычной замене масла и проверке клапанов на CB650R, а не только к выставочному мотоциклу. Те же руки, что собирали рекордные машины, затягивают пинч-болты вашей вилки.",
        "hon.introP3": "Независимость означает отсутствие дилерской наценки, свободу ставить OEM или качественный aftermarket по ситуации и прямое общение. Письменная смета до работ, письменный отчёт после. Вот и весь договор.",
        "hon.toolsTitle": "Диагностика и инструмент под Honda.",
        "hon.toolsEyebrow": "Специализированный инструмент",
        "hon.toolsLead": "Настоящую мастерскую Honda определяет одно: умеет ли она «разговаривать» с мотоциклом так, как это делает завод. Мы используем дилерскую диагностику Honda, а не универсальный OBD-сканер, который видит лишь коды по эмиссии.",
        "hon.t1t": "Honda MCS (Motorcycle Communication System)",
        "hon.t1d": "Специализированная диагностическая платформа Honda для мотоциклов. Читает и стирает DTC по всем ECU, отслеживает живые данные PGM-FI, выполняет экспресс-проверку «Quick Doctor», делает сбросы и адаптации, недоступные универсальному сканеру.",
        "hon.t2t": "HDS / процедуры уровня дилера",
        "hon.t2d": "Когда модель требует более глубокого доступа к системам или пошаговой диагностики, мы выполняем протоколы Honda Diagnostic System и заходим в меню, которых универсальный инструмент никогда не видит.",
        "hon.t3t": "Обслуживание DCT",
        "hon.t3d": "Dual Clutch Transmission — тот самый «фирменный» узел Honda, который большинство независимых мастерских обходит стороной. Мы обслуживаем его правильно: замена масла и фильтра по процедуре Honda, диагностика поведения сцепления и проверки на уровне софта при жалобах на качество переключений.",
        "hon.t4t": "Синхронизация, газ и PGM-FI",
        "hon.t4d": "Синхронизация дроссельных заслонок, проверка холостого хода и подачи топлива, контроль живых данных форсунок и датчиков на многоцилиндровых моторах.",
        "hon.servicesTitle": "Сервис. Ремонт. Тюнинг.",
        "hon.servicesEyebrow": "Что делаем по Honda",
        "hon.servicesLead": "От первого ТО новой Transalp до полного восстановления электрики VFR — со знанием специфики Honda и правильным инструментом.",
        "hon.s1t": "01 Регламентное ТО (масло, фильтр, жидкости, проверки)",
        "hon.s1d": "ТО по интервалу Honda — масло и фильтр, жидкости, проверка тормозов и цепи плюс пункты по модели. Расходники включены; от 150 €.",
        "hon.s2t": "02 Замена масла + фильтра DCT",
        "hon.s2d": "Замена масла и фильтра Dual Clutch Transmission по процедуре Honda плюс проверка включения сцепления и контроль на уровне софта. Работа, за которую большинство мастерских не берётся, — мы берёмся: Africa Twin DCT, NC750X DCT, Gold Wing DCT и остальные.",
        "hon.s3t": "03 Регулировка клапанов — twin / four",
        "hon.s3d": "Делаем правильно: щупами и подбором шайб там, где этого требует мотор. Клапаны на V4 и рядных «четвёрках» Honda трудоёмки, и мы честно называем цену заранее.",
        "hon.s4t": "04 Диагностика электрики и зарядки",
        "hon.s4d": "Полное чтение кодов и живых данных через MCS. Диагностика regulator/rectifier, stator и системы зарядки — известное слабое место Honda, которое мы проверяем первым, а не последним.",
        "hon.s5t": "05 Обслуживание подвески",
        "hon.s5d": "Замена сальников, замена масла, настройка сэга и преднатяга, отбой и сжатие. Переборка Showa и Öhlins, где они стоят. Раз колёса всё равно сняты — самое время для новой резины: см. наш сервис <a href=\"/ru/shinomontazh-mototsiklov/\">монтажа и балансировки мотошин</a>.",
        "hon.s6t": "06 Тормоза и ABS",
        "hon.s6d": "Колодки и жидкость, переборка суппортов, полная прокачка ABS, включая комбинированные тормозные системы Honda, где они есть.",
        "hon.s7t": "07 Настройка двигателя",
        "hon.s7d": "Синхронизация заслонок, стабилизация холостого, свечи, контроль данных PGM-FI на «твинах» и «четвёрках».",
        "hon.s8t": "08 Тюнинг и апгрейды",
        "hon.s8d": "Установка выпуска с соответствующим решением по топливоподаче (Akrapovič, Yoshimura, SC-Project), апгрейды подвески, эргономика, туринг и защита.",
        "hon.issuesTitle": "Слабые места Honda, которые ловим заранее.",
        "hon.issuesEyebrow": "Типичные проблемы, которые знаем",
        "hon.issuesLead": "Honda строит надёжные мотоциклы, поэтому честная версия такова: слабых мест немного, но те, что есть, хорошо известны, и мы проверяем их по умолчанию, а не ждём отказа на трассе.",
        "hon.i1t": "Отказ regulator / rectifier",
        "hon.i1d": "Классическая болезнь старых Honda — CBR, VFR и Hornet определённого возраста «сжигают» regulator/rectifier. Проверяем зарядное напряжение и состояние разъёмов до того, как вы останетесь стоять.",
        "hon.i2t": "Stator и зарядка на больших пробегах",
        "hon.i2d": "На пробежных мотоциклах stator и цепь зарядки деградируют. Читаем всю систему зарядки, а не гадаем на разряженный аккумулятор.",
        "hon.i3t": "Износ натяжителя цепи ГРМ",
        "hon.i3d": "Некоторые модели Honda с возрастом начинают «трещать» натяжителем. Определяем, что это: натяжитель, цепь или безобидный звук на холодную.",
        "hon.i4t": "Трудоёмкость клапанов VFR / V4",
        "hon.i4d": "Сервис клапанов на V4 действительно трудоёмкий — обходных путей нет. Мы называем реальные часы заранее, чтобы счёт никогда не стал сюрпризом.",
        "hon.i5t": "Софт и поведение сцепления DCT",
        "hon.i5d": "Резкие или «задумчивые» переключения DCT часто связаны с софтом или адаптацией сцепления, а не с поломкой. Диагностируем через MCS прежде, чем кто-то заговорит о замене деталей.",
        "hon.i6t": "Топливный насос",
        "hon.i6d": "Стареющий топливный насос даёт провалы на горячем пуске и под нагрузкой. Проверяем давление, а не меняем «на угад».",
        "hon.modelsTitle": "По всей линейке Honda.",
        "hon.modelsEyebrow": "Модели, которые обслуживаем",
        "hon.modelsLead": "Текущее производство, недавнее прошлое, современная классика — если на баке «крыло», везите.",
        "hon.m1t": "Семейство CB / Hornet",
        "hon.m1d": "CB500F, CB650R, CB750 Hornet, CB1000R и CB1000 Hornet.",
        "hon.m2t": "CBR",
        "hon.m2d": "CBR500R, CBR650R, CBR600RR и CBR1000RR-R Fireblade — улица, спорт и подготовка к треку.",
        "hon.m3t": "Africa Twin",
        "hon.m3d": "CRF1100L Africa Twin, включая версии DCT.",
        "hon.m4t": "NC750X и Transalp",
        "hon.m4d": "NC750X (механика и DCT) и XL750 Transalp.",
        "hon.m5t": "Rebel",
        "hon.m5d": "CMX500 и CMX1100 Rebel — включая Rebel 1100 DCT.",
        "hon.m6t": "Gold Wing",
        "hon.m6d": "GL1800 Gold Wing — полный туринговый сервис, DCT, подвеска и электроника.",
        "hon.m7t": "VFR и CB1100",
        "hon.m7d": "VFR800 и VFR1200 V4; воздушник CB1100 в духе современной классики.",
        "hon.m8t": "CRF dual-sport и эндуро",
        "hon.m8d": "CRF300L и CRF450.",
        "hon.m9t": "Небольшие «весёлые» мотоциклы",
        "hon.m9d": "Grom / MSX125, Monkey и Dax — малышам столько же внимания, сколько и большим.",
        "hon.partsTitle": "Доступ к каталогам основных запчастей Honda.",
        "hon.partsEyebrow": "Запчасти и aftermarket",
        "hon.partsLead": "Поставляем оригинальные запчасти Honda OEM через дистрибьюторскую сеть, а также топовый aftermarket для производительности, туринга и защиты. От одного OEM-фильтра до полной выпускной системы — заказываем напрямую.",
        "hon.partsList": "<strong>Каталоги, с которыми работаем:</strong> Оригинал Honda OEM через дистрибьюторскую сеть · Akrapovič · Yoshimura · SC-Project · Öhlins · сервисные детали Showa · Brembo · NGK · смазки Pro Honda · Hepco & Becker · SW-Motech · Givi · Barkbusters · Mitas · Michelin · Pirelli.",
        "hon.faqTitle": "Частые вопросы. (FAQ)",
        "hon.faqEyebrow": "FAQ",
        "hon.q1": "Вы авторизованный дилер Honda?",
        "hon.a1": "Нет — Iron Custom Motors независимая мастерская Honda. Плюс в отсутствии дилерской наценки и свободе ставить OEM или качественный aftermarket. Отзывные кампании и гарантийные работы должны выполняться у авторизованного дилера Honda, но всё остальное — ТО, обслуживание DCT, ремонт, доработки — мы делаем по независимым ценам и с более глубоким вниманием.",
        "hon.q2": "Сколько стоит обслуживание Honda?",
        "hon.a2": "Регламентное ТО — от 150 € с включёнными расходниками (замена воздушного фильтра оплачивается отдельно). Регулировка клапанов на японских «твинах»: 250 € проверка, 300 € проверка с регулировкой; на рядных «четвёрках»: 400 € проверка, 650 € проверка с регулировкой. Прочие работы — 50 €/час. Письменную смету вы получаете до начала работ. Все цены с учётом налога.",
        "hon.q3": "Вы обслуживаете Honda DCT (Dual Clutch Transmission)?",
        "hon.a3": "Да — и это реальное преимущество. Делаем замену масла и фильтра DCT по процедуре Honda, диагностируем включение сцепления и качество переключений через MCS, проверяем софтовую часть. Africa Twin DCT, NC750X DCT, Rebel 1100 DCT, Gold Wing DCT — всё своими силами.",
        "hon.q4": "Можете настроить или доработать мою Honda?",
        "hon.a4": "Да — выпускные системы с соответствующим решением по топливоподаче, апгрейды подвески, эргономика и трековая подготовка CBR / Fireblade. Честно говорим, что даёт реальный прирост, а что — просто шум.",
        "hon.q5": "Можете привезти оригинальные запчасти Honda OEM в Португалию?",
        "hon.a5": "Да — у нас есть доступ к каталогам оригинала Honda OEM через дистрибьюторскую сеть плюс все основные каталоги aftermarket. Если деталь существует для вашей модели, мы её привезём.",
        "hon.q6": "У моей Honda большой пробег — есть смысл обслуживать здесь?",
        "hon.a6": "Безусловно. Honda с большим пробегом — именно тот случай, где наши знания по зарядке, клапанам и DCT окупаются. Проверяем известные слабые места заранее и сохраняем надёжный мотоцикл надёжным.",
        "seo.relatedTitle": "Продолжите в той же системе сервиса.",
        "seo.relatedEyebrow": "Связанные направления",
        "seo.relatedLead": "Переходите к следующим важным страницам: сервис, запчасти, цены, бренды и контакт.",
        "seo.localTitle": "Обслуживаем Кашкайш, Лиссабон и Большой Лиссабон.",
        "seo.localEyebrow": "Локальная зона сервиса",
        "seo.localLead": "Iron Custom Motors находится в Сан-Домингуш-де-Рана, Кашкайш. Работаем с владельцами Honda из Кашкайша, Эшторила, Оэйраша, Синтры, Лиссабона и всего Большого Лиссабона.",
        "seo.area1t": "Мастерская в Кашкайше",
        "seo.area1d": "Настоящая мастерская и зона ожидания для клиента, а не удалённая стойка с запчастями.",
        "seo.area2t": "Многоязычный процесс",
        "seo.area2d": "Общение на русском, английском, украинском и португальском с письменными сметами и понятными шагами.",
        "seo.area3t": "Один ответственный маршрут",
        "seo.area3d": "Диагностика, подбор запчастей, установка, апгрейды и сопровождение — по единому стандарту мастерской.",
        "hon.ctaTitle": "Привозите вашу Honda.",
        "hon.ctaEyebrow": "Когда будете готовы",
        "hon.ctaText": "Пришлите модель, год и короткое описание в WhatsApp. Вернёмся с ближайшим свободным окном и письменной сметой до начала работ. Вт–Сб, 10:00–18:00."
    },
    "uk": {
        "hon.eyebrow": "Honda · Кашкайш / Великий Лісабон",
        "hon.heroAlt": "Мотоцикл Honda на підйомнику в майстерні Iron Custom Motors, Кашкайш, Великий Лісабон",
        "hon.breadHome": "Головна",
        "hon.h1Crumb": "Сервіс Honda",
        "hon.btnWA": "WhatsApp",
        "hon.btnSend": "Надіслати заявку",
        "hon.btnBack": "На головну",
        "hon.h1": "Сервіс мотоциклів Honda<br/>у <span class=\"accent\">Кашкайші.</span>",
        "hon.sub": "Незалежна майстерня Honda — діагностика, регламентне ТО, обслуговування DCT, регулювання клапанів, електрика, підвіска та тюнінг для Africa Twin, CB, CBR, Hornet, Gold Wing, VFR, Rebel і невеликих «веселих» мотоциклів.",
        "hon.introTitle": "Надійність Honda, турбота незалежної майстерні.",
        "hon.introEyebrow": "Чому Honda варто привезти до нас",
        "hon.introP1": "Iron Custom Motors — незалежний спеціаліст із мотоциклів Honda у Кашкайші. Honda має репутацію одних із найнадійніших моторів на дорозі, і ця репутація заслужена. Але «надійний» не означає «не потребує обслуговування» і не означає, що будь-яка майстерня знає, де саме Honda з великим пробігом справді потребує уваги. Ми знаємо.",
        "hon.introP2": "Інженерна культура тут не позичена. Наша команда стояла на подіумі, який щось важить: збирачі — чемпіони світу AMD, рекорд швидкості на солоному озері Бонневіль і титул BMW Motorrad Customizing Champions 2023. Саме з такою механічною дисципліною ми підходимо до звичайної заміни мастила й перевірки клапанів на CB650R, а не лише до виставкового мотоцикла. Ті самі руки, що збирали рекордні машини, затягують пінч-болти вашої вилки.",
        "hon.introP3": "Незалежність означає відсутність дилерської націнки, свободу ставити OEM чи якісний aftermarket за ситуацією та пряме спілкування. Письмовий кошторис до робіт, письмовий звіт після. Ось і вся домовленість.",
        "hon.toolsTitle": "Діагностика та інструмент під Honda.",
        "hon.toolsEyebrow": "Спеціалізований інструмент",
        "hon.toolsLead": "Справжню майстерню Honda визначає одне: чи вміє вона «розмовляти» з мотоциклом так, як це робить завод. Ми використовуємо дилерську діагностику Honda, а не універсальний OBD-сканер, що бачить лише коди з емісії.",
        "hon.t1t": "Honda MCS (Motorcycle Communication System)",
        "hon.t1d": "Спеціалізована діагностична платформа Honda для мотоциклів. Читає та стирає DTC по всіх ECU, відстежує живі дані PGM-FI, виконує експрес-перевірку «Quick Doctor», робить скидання й адаптації, недоступні універсальному сканеру.",
        "hon.t2t": "HDS / процедури рівня дилера",
        "hon.t2d": "Коли модель потребує глибшого доступу до систем або покрокової діагностики, ми виконуємо протоколи Honda Diagnostic System і заходимо в меню, яких універсальний інструмент ніколи не бачить.",
        "hon.t3t": "Обслуговування DCT",
        "hon.t3d": "Dual Clutch Transmission — той самий «фірмовий» вузол Honda, який більшість незалежних майстерень оминає. Ми обслуговуємо його правильно: заміна мастила й фільтра за процедурою Honda, діагностика поведінки зчеплення та перевірки на рівні софту за скаргами на якість перемикань.",
        "hon.t4t": "Синхронізація, газ і PGM-FI",
        "hon.t4d": "Синхронізація дросельних заслінок, перевірка холостого ходу й подачі пального, контроль живих даних форсунок і датчиків на багатоциліндрових моторах.",
        "hon.servicesTitle": "Сервіс. Ремонт. Тюнінг.",
        "hon.servicesEyebrow": "Що робимо по Honda",
        "hon.servicesLead": "Від першого ТО нової Transalp до повного відновлення електрики VFR — зі знанням специфіки Honda та правильним інструментом.",
        "hon.s1t": "01 Регламентне ТО (мастило, фільтр, рідини, перевірки)",
        "hon.s1d": "ТО за інтервалом Honda — мастило й фільтр, рідини, перевірка гальм і ланцюга плюс пункти за моделлю. Витратні матеріали включені; від 150 €.",
        "hon.s2t": "02 Заміна мастила + фільтра DCT",
        "hon.s2d": "Заміна мастила й фільтра Dual Clutch Transmission за процедурою Honda плюс перевірка ввімкнення зчеплення та контроль на рівні софту. Робота, за яку більшість майстерень не береться, — ми беремося: Africa Twin DCT, NC750X DCT, Gold Wing DCT та інші.",
        "hon.s3t": "03 Регулювання клапанів — twin / four",
        "hon.s3d": "Робимо правильно: щупами та підбором шайб там, де цього вимагає мотор. Клапани на V4 і рядних «четвірках» Honda трудомісткі, і ми чесно називаємо ціну заздалегідь.",
        "hon.s4t": "04 Діагностика електрики та заряджання",
        "hon.s4d": "Повне зчитування кодів і живих даних через MCS. Діагностика regulator/rectifier, stator і системи заряджання — відоме слабке місце Honda, яке ми перевіряємо першим, а не останнім.",
        "hon.s5t": "05 Обслуговування підвіски",
        "hon.s5d": "Заміна сальників, заміна мастила, налаштування сегу й переднатягу, відбій і стиск. Перебирання Showa та Öhlins, де вони стоять. Якщо колеса все одно зняті — саме час для нової гуми: див. наш сервіс <a href=\"/uk/shynomontazh-mototsykliv/\">монтажу та балансування мотошин</a>.",
        "hon.s6t": "06 Гальма та ABS",
        "hon.s6d": "Колодки й рідина, перебирання супортів, повне прокачування ABS, включно з комбінованими гальмівними системами Honda, де вони є.",
        "hon.s7t": "07 Налаштування двигуна",
        "hon.s7d": "Синхронізація заслінок, стабілізація холостого, свічки, контроль даних PGM-FI на «твінах» і «четвірках».",
        "hon.s8t": "08 Тюнінг і апгрейди",
        "hon.s8d": "Встановлення випуску з відповідним рішенням щодо паливоподачі (Akrapovič, Yoshimura, SC-Project), апгрейди підвіски, ергономіка, тур і захист.",
        "hon.issuesTitle": "Слабкі місця Honda, які ловимо заздалегідь.",
        "hon.issuesEyebrow": "Типові проблеми, які знаємо",
        "hon.issuesLead": "Honda будує надійні мотоцикли, тож чесна версія така: слабких місць небагато, але ті, що є, добре відомі, і ми перевіряємо їх за замовчуванням, а не чекаємо на відмову на трасі.",
        "hon.i1t": "Відмова regulator / rectifier",
        "hon.i1d": "Класична хвороба старих Honda — CBR, VFR і Hornet певного віку «спалюють» regulator/rectifier. Перевіряємо зарядну напругу й стан розʼємів, поки ви не лишилися стояти.",
        "hon.i2t": "Stator і заряджання на великих пробігах",
        "hon.i2d": "На пробіжних мотоциклах stator і ланцюг заряджання деградують. Читаємо всю систему заряджання, а не гадаємо на розряджений акумулятор.",
        "hon.i3t": "Знос натяжника ланцюга ГРМ",
        "hon.i3d": "Деякі моделі Honda з віком починають «торохтіти» натяжником. Визначаємо, що це: натяжник, ланцюг чи безпечний звук на холодну.",
        "hon.i4t": "Трудомісткість клапанів VFR / V4",
        "hon.i4d": "Сервіс клапанів на V4 справді трудомісткий — обхідних шляхів немає. Ми називаємо реальні години заздалегідь, щоб рахунок ніколи не став несподіванкою.",
        "hon.i5t": "Софт і поведінка зчеплення DCT",
        "hon.i5d": "Різкі чи «задумливі» перемикання DCT часто повʼязані із софтом або адаптацією зчеплення, а не з поломкою. Діагностуємо через MCS, перш ніж хтось заговорить про заміну деталей.",
        "hon.i6t": "Паливний насос",
        "hon.i6d": "Старіючий паливний насос дає провали на гарячому пуску та під навантаженням. Перевіряємо тиск, а не міняємо «навмання».",
        "hon.modelsTitle": "По всій лінійці Honda.",
        "hon.modelsEyebrow": "Моделі, які обслуговуємо",
        "hon.modelsLead": "Поточне виробництво, недавнє минуле, сучасна класика — якщо на баку «крило», везіть.",
        "hon.m1t": "Родина CB / Hornet",
        "hon.m1d": "CB500F, CB650R, CB750 Hornet, CB1000R і CB1000 Hornet.",
        "hon.m2t": "CBR",
        "hon.m2d": "CBR500R, CBR650R, CBR600RR і CBR1000RR-R Fireblade — місто, спорт і підготовка до треку.",
        "hon.m3t": "Africa Twin",
        "hon.m3d": "CRF1100L Africa Twin, включно з версіями DCT.",
        "hon.m4t": "NC750X і Transalp",
        "hon.m4d": "NC750X (механіка та DCT) і XL750 Transalp.",
        "hon.m5t": "Rebel",
        "hon.m5d": "CMX500 і CMX1100 Rebel — включно з Rebel 1100 DCT.",
        "hon.m6t": "Gold Wing",
        "hon.m6d": "GL1800 Gold Wing — повний туровий сервіс, DCT, підвіска та електроніка.",
        "hon.m7t": "VFR і CB1100",
        "hon.m7d": "VFR800 і VFR1200 V4; повітрянник CB1100 у дусі сучасної класики.",
        "hon.m8t": "CRF dual-sport та ендуро",
        "hon.m8d": "CRF300L і CRF450.",
        "hon.m9t": "Невеликі «веселі» мотоцикли",
        "hon.m9d": "Grom / MSX125, Monkey і Dax — малечі стільки ж уваги, скільки й великим.",
        "hon.partsTitle": "Доступ до каталогів основних запчастин Honda.",
        "hon.partsEyebrow": "Запчастини й aftermarket",
        "hon.partsLead": "Постачаємо оригінальні запчастини Honda OEM через дистрибʼюторську мережу, а також топовий aftermarket для продуктивності, туру й захисту. Від одного OEM-фільтра до повної випускної системи — замовляємо напряму.",
        "hon.partsList": "<strong>Каталоги, з якими працюємо:</strong> Оригінал Honda OEM через дистрибʼюторську мережу · Akrapovič · Yoshimura · SC-Project · Öhlins · сервісні деталі Showa · Brembo · NGK · мастила Pro Honda · Hepco & Becker · SW-Motech · Givi · Barkbusters · Mitas · Michelin · Pirelli.",
        "hon.faqTitle": "Поширені запитання. (FAQ)",
        "hon.faqEyebrow": "FAQ",
        "hon.q1": "Ви авторизований дилер Honda?",
        "hon.a1": "Ні — Iron Custom Motors незалежна майстерня Honda. Перевага — відсутність дилерської націнки та свобода ставити OEM чи якісний aftermarket. Відкличні кампанії та гарантійні роботи мають виконуватися в авторизованого дилера Honda, але все інше — ТО, обслуговування DCT, ремонт, доробки — ми робимо за незалежними цінами та з глибшою увагою.",
        "hon.q2": "Скільки коштує обслуговування Honda?",
        "hon.a2": "Регламентне ТО — від 150 € із включеними витратними матеріалами (заміна повітряного фільтра оплачується окремо). Регулювання клапанів на японських «твінах»: 250 € перевірка, 300 € перевірка з регулюванням; на рядних «четвірках»: 400 € перевірка, 650 € перевірка з регулюванням. Інші роботи — 50 €/год. Письмовий кошторис ви отримуєте до початку робіт. Усі ціни з урахуванням податку.",
        "hon.q3": "Ви обслуговуєте Honda DCT (Dual Clutch Transmission)?",
        "hon.a3": "Так — і це справжня перевага. Робимо заміну мастила й фільтра DCT за процедурою Honda, діагностуємо ввімкнення зчеплення та якість перемикань через MCS, перевіряємо софтову частину. Africa Twin DCT, NC750X DCT, Rebel 1100 DCT, Gold Wing DCT — усе власними силами.",
        "hon.q4": "Можете налаштувати чи доробити мою Honda?",
        "hon.a4": "Так — випускні системи з відповідним рішенням щодо паливоподачі, апгрейди підвіски, ергономіка та трекова підготовка CBR / Fireblade. Чесно кажемо, що дає реальний приріст, а що — просто шум.",
        "hon.q5": "Можете привезти оригінальні запчастини Honda OEM до Португалії?",
        "hon.a5": "Так — у нас є доступ до каталогів оригіналу Honda OEM через дистрибʼюторську мережу плюс усі основні каталоги aftermarket. Якщо деталь існує для вашої моделі, ми її привеземо.",
        "hon.q6": "Моя Honda з великим пробігом — чи варто обслуговувати тут?",
        "hon.a6": "Безумовно. Honda з великим пробігом — саме той випадок, де наші знання із заряджання, клапанів і DCT окупаються. Перевіряємо відомі слабкі місця заздалегідь і зберігаємо надійний мотоцикл надійним.",
        "seo.relatedTitle": "Продовжте в тій самій системі сервісу.",
        "seo.relatedEyebrow": "Пов’язані напрямки",
        "seo.relatedLead": "Переходьте до наступних важливих сторінок: сервіс, запчастини, ціни, бренди та контакт.",
        "seo.localTitle": "Обслуговуємо Кашкайш, Лісабон і Великий Лісабон.",
        "seo.localEyebrow": "Локальна зона сервісу",
        "seo.localLead": "Iron Custom Motors розташована в Сан-Домінгуш-де-Рана, Кашкайш. Працюємо з власниками Honda з Кашкайша, Ешторіла, Оейраша, Сінтри, Лісабона та всього Великого Лісабона.",
        "seo.area1t": "Майстерня в Кашкайші",
        "seo.area1d": "Справжня майстерня та зона очікування для клієнта, а не віддалена стійка із запчастинами.",
        "seo.area2t": "Багатомовний процес",
        "seo.area2d": "Спілкування українською, англійською, російською та португальською з письмовими кошторисами та зрозумілими кроками.",
        "seo.area3t": "Один відповідальний маршрут",
        "seo.area3d": "Діагностика, добір запчастин, встановлення, апгрейди й супровід — за єдиним стандартом майстерні.",
        "hon.ctaTitle": "Привозьте вашу Honda.",
        "hon.ctaEyebrow": "Коли будете готові",
        "hon.ctaText": "Надішліть модель, рік і короткий опис у WhatsApp. Повернемося з найближчим вільним вікном і письмовим кошторисом до початку робіт. Вт–Сб, 10:00–18:00."
    }
}

# ====================================================================================
# Royal Enfield
# ====================================================================================
BRAND_HEAD["royal-enfield-service"] = {'en': {'title': 'Royal Enfield Service Lisbon & Cascais | Iron Custom Motors',
        'description': 'Independent Royal Enfield workshop in Cascais. Service, valve/tappet clearance, EFI/ECU '
                       'diagnostics, oil-leak fixes, custom builds and Bullet restoration for 350, 450, 650 and '
                       'classics.'},
 'pt': {'title': 'Serviço Royal Enfield Lisboa e Cascais | Iron Custom Motors',
        'description': 'Oficina independente Royal Enfield em Cascais. Manutenção, folgas de válvulas, diagnóstico '
                       'EFI/ECU, fugas de óleo, projetos custom e restauro de Bullet para 350, 450, 650 e clássicas.'},
 'ru': {'title': 'Сервис Royal Enfield в Лиссабоне и Кашкайше | ICM',
        'description': 'Независимый сервис Royal Enfield в Кашкайше. ТО, регулировка клапанов, диагностика EFI/ECU, '
                       'устранение течей масла, кастом и реставрация Bullet для 350, 450, 650 и классики.'},
 'uk': {'title': 'Сервіс Royal Enfield у Лісабоні та Кашкайші | ICM',
        'description': 'Незалежний сервіс Royal Enfield у Кашкайші. ТО, регулювання клапанів, діагностика EFI/ECU, '
                       'усунення течі мастила, кастом і реставрація Bullet для 350, 450, 650 та класики.'}}
PAGE_I18N["royal-enfield-service"] = {'en': {'ren.breadHome': 'Home',
        'ren.h1Crumb': 'Royal Enfield service',
        'ren.btnWA': 'WhatsApp us',
        'ren.btnSend': 'Send a request',
        'ren.btnBack': 'Back to home',
        'ren.eyebrow': 'Royal Enfield · Cascais / Greater Lisbon',
        'ren.heroAlt': 'Royal Enfield motorcycle on the lift at Iron Custom Motors workshop in Cascais, Greater Lisbon',
        'ren.h1': 'Royal Enfield service<br/>in <span class="accent">Cascais.</span>',
        'ren.sub': 'Independent Royal Enfield workshop for the 350 and 450 singles, the 650 twins and the classic '
                   'Bullets. Diagnostics, scheduled service, valve and tappet work, custom builds and restoration — by '
                   'a team with a genuine engineering pedigree.',
        'ren.introTitle': 'A real RE specialist, independent rates.',
        'ren.introEyebrow': 'Why bring your Royal Enfield to us',
        'ren.introP1': 'Iron Custom Motors is an independent Royal Enfield workshop in São Domingos de Rana, Cascais. '
                       'We service the full modern line-up — the J-platform 350 singles, the liquid-cooled 450s, the '
                       '648 parallel twins — and we welcome the classics: UCE and pre-unit Bullets, Continental GTs, '
                       'the older 500s.',
        'ren.introP2': 'Royal Enfield is the oldest motorcycle brand in continuous production, and the people who ride '
                       'them know exactly why. These bikes are about character, mechanical honesty and a riding '
                       "experience that doesn't need to be loud to be felt. Our job is to respect that — to keep the "
                       'bike doing what it was built to do, not to fight its nature with over-complication.',
        'ren.introP3': 'The engineering culture behind the workshop is the same one that earned ICM the AMD World '
                       'Champions title, a Bonneville land-speed record and the BMW Motorrad Customizing Championship '
                       '2023. We bring that standard to a Classic 350 as readily as to a competition build. And '
                       'because Royal Enfield is one of the most popular custom base bikes in the world — bobbers, '
                       'scramblers, café racers — there is no shop better placed to turn yours into something '
                       'personal. See our <a href="/custom/">custom & special projects</a>. From our workshop: read '
                       'the <a href="/blog/royal-enfield-bear-650-fork-oil-case-study/">Bear 650 fork-oil case '
                       'study</a>.<br/><br/>Independent means '
                       'no dealer mark-up, the freedom to fit OEM or quality aftermarket parts as the job actually '
                       'requires, and straight talk. Written estimate before the work, written report after.',
        'ren.toolsTitle': 'Royal Enfield diagnostics and tools.',
        'ren.toolsEyebrow': 'Specialist tooling',
        'ren.toolsLead': 'The modern Royal Enfield range is fuel-injected — the J-platform 350s and the 648 twins run '
                         'EFI with an ECU. The classics run carburettors. We are set up for both, which most general '
                         'workshops are not.',
        'ren.t1t': 'Dealer-level Royal Enfield diagnostics',
        'ren.t1d': 'We read and clear RE-specific ECU fault codes, monitor live sensor data, check fuelling and run '
                   'the resets the bike needs after service.',
        'ren.t2t': 'EFI and fuel-system work',
        'ren.t2d': 'Throttle-body cleaning and balance, idle and fuelling checks on the 350 and 650 EFI engines — done '
                   'to the figures, not by feel.',
        'ren.t3t': 'Carburettor tooling for classics',
        'ren.t3d': 'Proper bench work, jet selection and synchronisation for UCE and earlier Bullets, Continental GT '
                   '535 and the older 500s.',
        'ren.t4t': 'The right tools for valve and tappet work',
        'ren.t4d': 'Feeler gauges, the correct shims and tappet hardware, and the patience these engines reward. Valve '
                   'and tappet clearance is central to RE ownership and we treat it that way.',
        'ren.servicesTitle': 'Service. Repair. Build.',
        'ren.servicesEyebrow': 'What we do on Royal Enfield',
        'ren.servicesLead': 'From a first scheduled service on a new Hunter 350 to a ground-up Bullet restoration — '
                            'all of it with Royal Enfield knowledge and the right tools.',
        'ren.s1t': '01 Scheduled service',
        'ren.s1d': 'RE interval service: engine oil and filter, fluids, brake check, chain and fasteners, plus '
                   'valve/tappet clearance when the schedule calls for it.',
        'ren.s2t': '02 Valve & tappet clearance',
        'ren.s2d': 'Done properly with feeler gauges and correct shims. Central to RE health on both the singles and '
                   'the 650 twins — neglected, it costs you smoothness, economy and eventually the head.',
        'ren.s3t': '03 Charging & electrical',
        'ren.s3d': 'Regulator-rectifier and charging-system checks on higher-mileage bikes, battery, lighting and '
                   'accessory wiring. We chase the cause, not the symptom.',
        'ren.s4t': '04 Carburettor & EFI',
        'ren.s4d': 'Carb rebuilds and synchronisation on the classics; EFI cleaning, balance and fuelling checks on '
                   'the modern 350 and 650.',
        'ren.s5t': '05 Suspension & wheels',
        'ren.s5d': 'Fork seals and oil, rear shock service, sag setup, wheel bearings and tyres. While the wheels are '
                   'out, our <a href="/motorcycle-tyre-service/">tyre fitting and balancing service</a> sorts new '
                   'rubber properly in the same visit.',
        'ren.s6t': '06 Oil-leak rectification on classics',
        'ren.s6d': "The older Bullets and UCE engines are known for oil seepage. We don't chase it with sealant — we "
                   'find the source, replace seals and gaskets properly and set it right.',
        'ren.s7t': '07 Chain & final drive',
        'ren.s7d': 'Clean, lube and adjust; sprocket inspection and replacement. The cheapest preventive job there is, '
                   'and one vibration loves to undo over time — so we re-torque the right fasteners too.',
        'ren.s8t': '08 Custom & restoration',
        'ren.s8d': 'Bobbers, scramblers and café racers built from your RE; full restoration of a Bullet from tired to '
                   'right. See <a href="/upgrades-tuning/">upgrades & tuning</a> and <a href="/custom/">custom</a>.',
        'ren.issuesTitle': 'The things these bikes do, checked before they bite.',
        'ren.issuesEyebrow': 'Typical issues we know',
        'ren.issuesLead': 'We know Royal Enfields, so we check the right items proactively rather than waiting for '
                          'them to strand you.',
        'ren.i1t': 'Valve/tappet clearance drift',
        'ren.i1d': 'Central to every RE. We measure and adjust to spec — the difference between a sweet engine and a '
                   'rough, thirsty one.',
        'ren.i2t': 'Oil seepage on classics',
        'ren.i2d': 'A known trait of older Bullets and UCE engines. We trace the real source and seal it properly, not '
                   'cosmetically.',
        'ren.i3t': 'Charging / regulator-rectifier',
        'ren.i3d': 'Higher-mileage symptoms — weak charge, flat batteries. We read the charging system fully before '
                   'condemning a part.',
        'ren.i4t': 'Fasteners loosened by vibration',
        'ren.i4d': 'RE character includes vibration; over time it backs off bolts. We re-torque the points that matter '
                   'at every service.',
        'ren.i5t': 'Chain & final-drive wear',
        'ren.i5d': 'Neglected chains chew sprockets and cost many times the price of regular care. We catch it early.',
        'ren.i6t': 'Himalayan 411 first-gen niggles',
        'ren.i6d': 'The early Himalayan had teething issues, addressed over the years. We know the points to check on '
                   'these.',
        'ren.modelsTitle': 'Across the Royal Enfield line-up.',
        'ren.modelsEyebrow': 'Models we service',
        'ren.modelsLead': 'Current production, recent past and the classics — if it wears the gun-on-the-tank or the '
                          'Royal Enfield script, bring it in.',
        'ren.m1t': '350 J-platform singles',
        'ren.m1d': 'Classic 350, Bullet 350, Meteor 350, Hunter 350, Goan Classic 350.',
        'ren.m2t': '450 liquid-cooled singles (Sherpa)',
        'ren.m2d': 'Himalayan 450, Guerrilla 450.',
        'ren.m3t': '411 singles',
        'ren.m3d': 'Himalayan 411, Scram 411.',
        'ren.m4t': '648 parallel twins',
        'ren.m4d': 'Interceptor 650 (INT650), Continental GT 650, Super Meteor 650, Shotgun 650, Bear 650.',
        'ren.m5t': 'Classics & older',
        'ren.m5d': 'Bullet 500, Classic 500, Continental GT 535, Thunderbird and vintage Bullets. Restoration welcome.',
        'ren.partsTitle': 'Catalog access for Royal Enfield parts.',
        'ren.partsEyebrow': 'Parts and catalog access',
        'ren.partsLead': 'We source OEM Royal Enfield parts through the distributor network and work with the genuine '
                         'RE aftermarket — the brands owners actually use.',
        'ren.partsList': '<strong>Catalogs we work with:</strong> OEM Royal Enfield via distributor · Hitchcocks '
                         'Motorcycles · Powertronic (ECU tuning / fuel control) · S&S Cycle · Hagon · K&N · Hel · NGK '
                         "· DID · plus quality consumables. Order ahead even if you're not booking service. See <a "
                         'href="/parts/">parts & consumables</a>.',
        'ren.faqTitle': 'Common questions. (FAQ)',
        'ren.faqEyebrow': 'FAQ',
        'ren.q1': 'Are you an authorised Royal Enfield dealer?',
        'ren.a1': 'No — we are an independent Royal Enfield workshop. The advantage is no dealer mark-up and the '
                  'freedom to fit OEM or quality aftermarket parts. Warranty and recall work must go to an authorised '
                  'dealer, but scheduled service, repair, valve work, custom and restoration we handle at independent '
                  'rates with deeper, RE-first attention.',
        'ren.q2': 'How much does a Royal Enfield service cost?',
        'ren.a2': 'Scheduled maintenance starts from €150, consumables included (air-filter replacement charged '
                  'separately). The exact figure depends on the model and interval and is confirmed in a written '
                  'estimate before any work begins. Hourly rate for other work is €50/hour. See <a '
                  'href="/pricing/">pricing</a>.',
        'ren.q3': 'Do you do valve / tappet clearance service?',
        'ren.a3': "Yes — it's central to RE ownership and we do it properly. For the 650 parallel twin, a clearance "
                  'check is from €250 and check-plus-adjust from €300. Single-cylinder 350/450 valve work is quoted '
                  'per model and always confirmed in a written estimate first.',
        'ren.q4': 'Can you build a custom from my Royal Enfield or restore my Bullet?',
        'ren.a4': 'Yes. RE is one of the best custom platforms in the world, and restoration is part of who we are. '
                  "Bring the concept or the tired Bullet and we'll scope it — bobber, scrambler, café racer or a "
                  'faithful restoration.',
        'ren.q5': 'Can you import OEM and aftermarket parts to Portugal?',
        'ren.a5': 'Yes. We source OEM Royal Enfield through the distributor network and aftermarket from Hitchcocks, '
                  'Powertronic, Hagon, K&N and others. If the part exists for your model, we get it here.',
        'seo.relatedTitle': 'Continue through the same service system.',
        'seo.relatedEyebrow': 'Related workshop paths',
        'seo.localTitle': 'Serving Cascais, Estoril, Oeiras and Greater Lisbon.',
        'seo.localEyebrow': 'Local service area',
        'seo.localLead': 'Iron Custom Motors is based in São Domingos de Rana, Cascais. We work with Royal Enfield '
                         'riders from Cascais, Estoril, Oeiras, Sintra, Lisbon and the wider Greater Lisbon area.',
        'seo.area1t': 'Cascais workshop',
        'seo.area1d': 'a real workshop and client lounge, not a parts counter. Drop the bike off or come to talk '
                      'through a project.',
        'seo.area2t': 'Multilingual process',
        'seo.area2d': 'English, Portuguese, Russian and Ukrainian, with written estimates and clear next steps.',
        'seo.area3t': 'One accountable path',
        'seo.area3d': 'diagnostics, parts, installation and follow-up under one workshop standard.',
        'ren.ctaTitle': 'Bring your Royal Enfield in.',
        'ren.ctaEyebrow': 'Ready when you are',
        'ren.ctaText': "Send the model, year and a short description via WhatsApp. We'll reply with the closest slot "
                       'and a written estimate before work starts. Tue–Sat, 10:00–18:00.'},
 'pt': {'ren.breadHome': 'Início',
        'ren.h1Crumb': 'Serviço Royal Enfield',
        'ren.btnWA': 'WhatsApp',
        'ren.btnSend': 'Enviar pedido',
        'ren.btnBack': 'Voltar ao início',
        'ren.eyebrow': 'Royal Enfield · Cascais / Grande Lisboa',
        'ren.heroAlt': 'Mota Royal Enfield no elevador da oficina Iron Custom Motors em Cascais, Grande Lisboa',
        'ren.h1': 'Serviço Royal Enfield<br/>em <span class="accent">Cascais.</span>',
        'ren.sub': 'Oficina independente Royal Enfield para as monocilíndricas 350 e 450, as bicilíndricas 650 e as '
                   'clássicas Bullet. Diagnóstico, manutenção programada, válvulas e tuchos, projetos custom e '
                   'restauro — por uma equipa com pedigree de engenharia.',
        'ren.introTitle': 'Um verdadeiro especialista RE, a preços independentes.',
        'ren.introEyebrow': 'Porque trazer a sua Royal Enfield até nós',
        'ren.introP1': 'A Iron Custom Motors é uma oficina independente de Royal Enfield em São Domingos de Rana, '
                       'Cascais. Fazemos serviço a toda a gama moderna — as monocilíndricas 350 da plataforma J, as '
                       '450 de refrigeração líquida e as bicilíndricas paralelas 648 — e recebemos as clássicas: '
                       'Bullet UCE e pré-unit, Continental GT e as 500 mais antigas.',
        'ren.introP2': 'A Royal Enfield é a marca de motos mais antiga em produção contínua, e quem as conduz sabe bem '
                       'porquê. Estas motos vivem do carácter, da honestidade mecânica e de uma experiência de '
                       'condução que não precisa de ser barulhenta para se sentir. O nosso trabalho é respeitar isso — '
                       'manter a mota a fazer aquilo para que foi feita, sem a complicar contra a sua natureza.',
        'ren.introP3': 'A cultura de engenharia por trás da oficina é a mesma que valeu à ICM o título de Campeões do '
                       'Mundo AMD, um recorde de velocidade em Bonneville e o BMW Motorrad Customizing Championship '
                       '2023. Aplicamos esse padrão tanto a uma Classic 350 como a um projeto de competição. E como a '
                       'Royal Enfield é uma das bases custom mais populares do mundo — bobbers, scramblers, café '
                       'racers — não há melhor sítio para tornar a sua única. Veja <a href="/pt/custom/">custom e '
                       'projetos especiais</a>. Da nossa oficina: leia o <a '
                       'href="/pt/blog/royal-enfield-bear-650-fork-oil-case-study/">caso Bear 650 sobre óleo de '
                       'forquilha</a>.<br/><br/>Independente significa sem margem de concessionário, '
                       'liberdade para montar peças OEM ou de qualidade aftermarket conforme o trabalho exige, e '
                       'conversa franca. Orçamento por escrito antes, relatório por escrito depois.',
        'ren.toolsTitle': 'Diagnóstico e ferramentas Royal Enfield.',
        'ren.toolsEyebrow': 'Ferramenta especialista',
        'ren.toolsLead': 'A gama Royal Enfield moderna é de injeção — as 350 da plataforma J e as bicilíndricas 648 '
                         'usam EFI com ECU. As clássicas usam carburador. Estamos preparados para ambos, ao contrário '
                         'da maioria das oficinas generalistas.',
        'ren.t1t': 'Diagnóstico Royal Enfield ao nível de concessionário',
        'ren.t1d': 'Lemos e apagamos códigos de avaria específicos da ECU RE, acompanhamos dados em tempo real, '
                   'verificamos a alimentação e fazemos os resets que a mota precisa após o serviço.',
        'ren.t2t': 'Trabalho de EFI e sistema de combustível',
        'ren.t2d': 'Limpeza e equilíbrio do corpo de borboleta, verificação do ralenti e da injeção nos motores EFI '
                   '350 e 650 — feito pelos valores, não a olho.',
        'ren.t3t': 'Ferramenta de carburador para as clássicas',
        'ren.t3d': 'Trabalho de bancada como deve ser, seleção de gicleurs e sincronização para Bullet UCE e '
                   'anteriores, Continental GT 535 e as 500 mais antigas.',
        'ren.t4t': 'As ferramentas certas para válvulas e tuchos',
        'ren.t4d': 'Apalpa-folgas, os shims e tuchos corretos, e a paciência que estes motores recompensam. A folga de '
                   'válvulas e tuchos é central na vida de uma RE e é assim que a tratamos.',
        'ren.servicesTitle': 'Serviço. Reparação. Construção.',
        'ren.servicesEyebrow': 'O que fazemos em Royal Enfield',
        'ren.servicesLead': 'Do primeiro serviço de uma Hunter 350 nova ao restauro completo de uma Bullet — tudo com '
                            'conhecimento Royal Enfield e as ferramentas certas.',
        'ren.s1t': '01 Manutenção programada',
        'ren.s1d': 'serviço de intervalo RE: óleo e filtro, fluidos, travões, corrente e apertos, mais folga de '
                   'válvulas/tuchos quando o plano o exige.',
        'ren.s2t': '02 Folga de válvulas e tuchos',
        'ren.s2d': 'feita como deve ser, com apalpa-folgas e shims corretos. Central na saúde da RE, tanto nas '
                   'monocilíndricas como nas bicilíndricas 650.',
        'ren.s3t': '03 Carga e elétrico',
        'ren.s3d': 'verificação do regulador-retificador e do sistema de carga em motos de maior quilometragem, '
                   'bateria, iluminação e cablagem de acessórios. Procuramos a causa, não o sintoma.',
        'ren.s4t': '04 Carburador e EFI',
        'ren.s4d': 'reconstrução e sincronização de carburadores nas clássicas; limpeza, equilíbrio e verificação de '
                   'injeção de EFI nas 350 e 650 modernas.',
        'ren.s5t': '05 Suspensão e rodas',
        'ren.s5d': 'retentores e óleo da forquilha, serviço do amortecedor, regulação de sag, rolamentos e pneus. Com '
                   'as rodas fora, o nosso <a href="/pt/montagem-de-pneus-mota/">serviço de montagem e equilibragem de '
                   'pneus</a> trata da borracha nova na mesma visita.',
        'ren.s6t': '06 Eliminação de fugas de óleo nas clássicas',
        'ren.s6d': 'as Bullet e os motores UCE mais antigos são conhecidos por transpirar óleo. Não disfarçamos com '
                   'vedante — encontramos a origem e substituímos retentores e juntas como deve ser.',
        'ren.s7t': '07 Corrente e transmissão final',
        'ren.s7d': 'limpar, lubrificar e ajustar; inspeção e substituição de cremalheiras. O trabalho preventivo mais '
                   'barato que há — e que a vibração adora desfazer, por isso reapertamos também os fixadores certos.',
        'ren.s8t': '08 Custom e restauro',
        'ren.s8d': 'bobbers, scramblers e café racers a partir da sua RE; restauro completo de uma Bullet. Veja <a '
                   'href="/pt/upgrades-tuning/">upgrades e afinação</a> e <a href="/pt/custom/">custom</a>.',
        'ren.issuesTitle': 'Aquilo que estas motos fazem, verificado a tempo.',
        'ren.issuesEyebrow': 'Problemas típicos que conhecemos',
        'ren.issuesLead': 'Conhecemos as Royal Enfield, por isso verificamos os pontos certos de forma preventiva, em '
                          'vez de esperar que o deixem na estrada.',
        'ren.i1t': 'Variação da folga de válvulas/tuchos',
        'ren.i1d': 'Central em qualquer RE. Medimos e ajustamos ao valor — a diferença entre um motor doce e um motor '
                   'áspero e bebedor.',
        'ren.i2t': 'Transpiração de óleo nas clássicas',
        'ren.i2d': 'Traço conhecido das Bullet e motores UCE mais antigos. Localizamos a origem real e selamos como '
                   'deve ser, não por cosmética.',
        'ren.i3t': 'Carga / regulador-retificador',
        'ren.i3d': 'Sintomas de maior quilometragem — carga fraca, baterias descarregadas. Lemos o sistema de carga '
                   'por completo antes de condenar uma peça.',
        'ren.i4t': 'Fixadores soltos pela vibração',
        'ren.i4d': 'O carácter RE inclui vibração; com o tempo, solta parafusos. Reapertamos os pontos que importam em '
                   'cada serviço.',
        'ren.i5t': 'Desgaste de corrente e transmissão final',
        'ren.i5d': 'Correntes negligenciadas comem cremalheiras e custam muitas vezes o preço do cuidado regular. '
                   'Apanhamos cedo.',
        'ren.i6t': 'Detalhes da primeira Himalayan 411',
        'ren.i6d': 'A primeira Himalayan teve afinações iniciais, resolvidas ao longo dos anos. Sabemos os pontos a '
                   'verificar nestas.',
        'ren.modelsTitle': 'Por toda a gama Royal Enfield.',
        'ren.modelsEyebrow': 'Modelos que servimos',
        'ren.modelsLead': 'Produção atual, passado recente e as clássicas — se traz a espingarda no depósito ou a '
                          'assinatura Royal Enfield, traga-a.',
        'ren.m1t': 'Monocilíndricas 350 plataforma J',
        'ren.m1d': 'Classic 350, Bullet 350, Meteor 350, Hunter 350, Goan Classic 350.',
        'ren.m2t': 'Monocilíndricas 450 (Sherpa)',
        'ren.m2d': 'Himalayan 450, Guerrilla 450.',
        'ren.m3t': 'Monocilíndricas 411',
        'ren.m3d': 'Himalayan 411, Scram 411.',
        'ren.m4t': 'Bicilíndricas paralelas 648',
        'ren.m4d': 'Interceptor 650 (INT650), Continental GT 650, Super Meteor 650, Shotgun 650, Bear 650.',
        'ren.m5t': 'Clássicas e antigas',
        'ren.m5d': 'Bullet 500, Classic 500, Continental GT 535, Thunderbird e Bullets vintage. Restauro bem-vindo.',
        'ren.partsTitle': 'Acesso a catálogo para peças Royal Enfield.',
        'ren.partsEyebrow': 'Peças e acesso a catálogo',
        'ren.partsLead': 'Fornecemos peças OEM Royal Enfield através da rede de distribuição e trabalhamos com o '
                         'aftermarket RE genuíno — as marcas que os proprietários realmente usam.',
        'ren.partsList': '<strong>Catálogos com que trabalhamos:</strong> OEM Royal Enfield via distribuidor · '
                         'Hitchcocks Motorcycles · Powertronic (afinação de ECU / gestão de combustível) · S&S Cycle · '
                         'Hagon · K&N · Hel · NGK · DID · mais consumíveis de qualidade. Encomende com antecedência '
                         'mesmo sem marcar serviço. Veja <a href="/pt/parts/">peças e consumíveis</a>.',
        'ren.faqTitle': 'Perguntas frequentes. (FAQ)',
        'ren.faqEyebrow': 'FAQ',
        'ren.q1': 'São concessionário Royal Enfield autorizado?',
        'ren.a1': 'Não — somos uma oficina Royal Enfield independente. A vantagem é não haver margem de concessionário '
                  'e a liberdade de montar peças OEM ou aftermarket de qualidade. Garantia e recall têm de ir a um '
                  'concessionário autorizado, mas manutenção, reparação, válvulas, custom e restauro tratamos nós, a '
                  'preços independentes e com atenção RE em primeiro lugar.',
        'ren.q2': 'Quanto custa um serviço Royal Enfield?',
        'ren.a2': 'A manutenção programada começa nos 150 €, consumíveis incluídos (substituição de filtro de ar '
                  'cobrada à parte). O valor exato depende do modelo e do intervalo e é confirmado em orçamento por '
                  'escrito antes de qualquer trabalho. O valor à hora para outros trabalhos é 50 €/hora. Veja <a '
                  'href="/pt/pricing/">preços</a>.',
        'ren.q3': 'Fazem serviço de válvulas / tuchos?',
        'ren.a3': 'Sim — é central na vida de uma RE e fazemo-lo como deve ser. Para a bicilíndrica paralela 650, a '
                  'verificação de folga é a partir de 250 € e verificação mais ajuste a partir de 300 €. O trabalho '
                  'nas monocilíndricas 350/450 é orçamentado por modelo e sempre confirmado por escrito primeiro.',
        'ren.q4': 'Podem construir um custom a partir da minha Royal Enfield ou restaurar a minha Bullet?',
        'ren.a4': 'Sim. A RE é uma das melhores bases custom do mundo, e o restauro faz parte de quem somos. Traga o '
                  'conceito ou a Bullet cansada e definimos o âmbito — bobber, scrambler, café racer ou um restauro '
                  'fiel.',
        'ren.q5': 'Importam peças OEM e aftermarket para Portugal?',
        'ren.a5': 'Sim. Fornecemos OEM Royal Enfield pela rede de distribuição e aftermarket da Hitchcocks, '
                  'Powertronic, Hagon, K&N e outros. Se a peça existe para o seu modelo, trazemo-la.',
        'seo.relatedTitle': 'Continue pelo mesmo sistema de serviço.',
        'seo.relatedEyebrow': 'Caminhos relacionados',
        'seo.localTitle': 'A servir Cascais, Estoril, Oeiras e a Grande Lisboa.',
        'seo.localEyebrow': 'Área local de serviço',
        'seo.localLead': 'A Iron Custom Motors fica em São Domingos de Rana, Cascais. Trabalhamos com motociclistas '
                         'Royal Enfield de Cascais, Estoril, Oeiras, Sintra, Lisboa e toda a Grande Lisboa.',
        'seo.area1t': 'Oficina em Cascais',
        'seo.area1d': 'uma oficina e lounge a sério, não um balcão de peças. Deixe a mota ou venha falar de um '
                      'projeto.',
        'seo.area2t': 'Processo multilingue',
        'seo.area2d': 'português, inglês, russo e ucraniano, com orçamentos por escrito e próximos passos claros.',
        'seo.area3t': 'Um caminho responsável',
        'seo.area3d': 'diagnóstico, peças, montagem e acompanhamento sob um único padrão de oficina.',
        'ren.ctaTitle': 'Traga a sua Royal Enfield.',
        'ren.ctaEyebrow': 'Prontos quando estiver',
        'ren.ctaText': 'Envie modelo, ano e uma breve descrição por WhatsApp. Respondemos com a vaga mais próxima e um '
                       'orçamento por escrito antes de começar. Ter–Sáb, 10:00–18:00.'},
 'ru': {'ren.breadHome': 'Главная',
        'ren.h1Crumb': 'Сервис Royal Enfield',
        'ren.btnWA': 'WhatsApp',
        'ren.btnSend': 'Оставить заявку',
        'ren.btnBack': 'На главную',
        'ren.eyebrow': 'Royal Enfield · Кашкайш / Большой Лиссабон',
        'ren.heroAlt': 'Мотоцикл Royal Enfield на подъёмнике в мастерской Iron Custom Motors, Кашкайш, Большой '
                       'Лиссабон',
        'ren.h1': 'Сервис Royal Enfield<br/>в <span class="accent">Кашкайше.</span>',
        'ren.sub': 'Независимая мастерская Royal Enfield: одноцилиндровые 350 и 450, параллельные твины 650 и '
                   'классические Bullet. Диагностика, плановое ТО, клапаны, кастом и реставрация — командой с '
                   'настоящей инженерной школой.',
        'ren.introTitle': 'Настоящий спец по RE — по независимым ценам.',
        'ren.introEyebrow': 'Почему Royal Enfield стоит привезти к нам',
        'ren.introP1': 'Iron Custom Motors — это независимая мастерская Royal Enfield в Сан-Домингуш-де-Рана, Кашкайш. '
                       'Мы обслуживаем всю современную линейку: одноцилиндровые 350 на платформе J, 450 с жидкостным '
                       'охлаждением, параллельные твины 648 — и с радостью берём классику: Bullet UCE и долипных лет, '
                       'Continental GT, старшие 500.',
        'ren.introP2': 'Royal Enfield — старейшая марка мотоциклов в непрерывном производстве, и те, кто на них ездит, '
                       'прекрасно знают почему. Эти мотоциклы про характер, механическую честность и ощущение езды, '
                       'которому не нужно быть громким, чтобы его чувствовать. Наша задача — это уважать: сохранять '
                       'мотоцикл таким, каким он задуман, а не воевать с его натурой лишним усложнением.',
        'ren.introP3': 'За мастерской стоит та же инженерная школа, что принесла ICM титул чемпионов мира AMD, рекорд '
                       'скорости в Бонневиле и победу в BMW Motorrad Customizing Championship 2023. Тот же уровень мы '
                       'применяем и к Classic 350, и к гоночному проекту. А поскольку Royal Enfield — одна из самых '
                       'популярных в мире баз для кастома (бобберы, скрэмблеры, кафе-рейсеры), лучше места, чтобы '
                       'сделать ваш по-настоящему своим, не найти. Смотрите <a href="/ru/custom/">кастом и '
                       'спецпроекты</a>. Из нашей мастерской: читайте <a '
                       'href="/ru/blog/royal-enfield-bear-650-fork-oil-case-study/">разбор Bear 650 по маслу в '
                       'вилке</a>.<br/><br/>Независимость — это без наценки дилера, со свободой ставить OEM или '
                       'качественный афтермаркет по делу, и с честным разговором. Смета письменно до работы, отчёт '
                       'письменно после.',
        'ren.toolsTitle': 'Диагностика и инструмент Royal Enfield.',
        'ren.toolsEyebrow': 'Специализированный инструмент',
        'ren.toolsLead': 'Современная линейка Royal Enfield — впрысковая: 350 на платформе J и твины 648 работают на '
                         'EFI с ECU. Классика — на карбюраторах. Мы готовы и к тому, и к другому, в отличие от '
                         'большинства универсальных мастерских.',
        'ren.t1t': 'Диагностика Royal Enfield дилерского уровня',
        'ren.t1d': 'Читаем и стираем коды неисправностей ECU RE, смотрим данные датчиков в реальном времени, проверяем '
                   'смесь и выполняем сбросы, которые нужны мотоциклу после обслуживания.',
        'ren.t2t': 'Работа с EFI и топливной системой',
        'ren.t2d': 'Чистка и балансировка дроссельного узла, проверка холостого хода и смеси на впрысковых 350 и 650 — '
                   'по цифрам, а не на глаз.',
        'ren.t3t': 'Карбюраторный инструмент для классики',
        'ren.t3d': 'Нормальная работа на стенде, подбор жиклёров и синхронизация для Bullet UCE и более ранних, '
                   'Continental GT 535 и старших 500.',
        'ren.t4t': 'Правильный инструмент для клапанов',
        'ren.t4d': 'Щупы, нужные шайбы и детали привода клапанов и то терпение, которое эти моторы вознаграждают. '
                   'Зазоры клапанов — основа жизни RE, и мы относимся к ним именно так.',
        'ren.servicesTitle': 'Сервис. Ремонт. Постройка.',
        'ren.servicesEyebrow': 'Что делаем по Royal Enfield',
        'ren.servicesLead': 'От первого ТО на новой Hunter 350 до полной реставрации Bullet — всё со знанием Royal '
                            'Enfield и правильным инструментом.',
        'ren.s1t': '01 Плановое ТО',
        'ren.s1d': 'сервис по интервалу RE: масло и фильтр, жидкости, тормоза, цепь и крепёж, плюс зазоры клапанов, '
                   'когда того требует регламент.',
        'ren.s2t': '02 Зазоры клапанов',
        'ren.s2d': 'как положено, щупами и правильными шайбами. Основа здоровья RE как на одноцилиндровых, так и на '
                   'твинах 650.',
        'ren.s3t': '03 Зарядка и электрика',
        'ren.s3d': 'проверка реле-регулятора и системы зарядки на пробежных мотоциклах, аккумулятор, свет и проводка '
                   'аксессуаров. Ищем причину, а не симптом.',
        'ren.s4t': '04 Карбюратор и EFI',
        'ren.s4d': 'переборка и синхронизация карбюраторов на классике; чистка, балансировка и проверка смеси EFI на '
                   'современных 350 и 650.',
        'ren.s5t': '05 Подвеска и колёса',
        'ren.s5d': 'сальники и масло вилки, обслуживание заднего амортизатора, настройка преднатяга, подшипники и '
                   'шины. Пока колёса сняты, наш <a href="/ru/shinomontazh-mototsiklov/">шиномонтаж и балансировка</a> '
                   'поставит новую резину как надо за тот же визит.',
        'ren.s6t': '06 Устранение течей масла на классике',
        'ren.s6d': 'старшие Bullet и моторы UCE известны «потением» маслом. Мы не маскируем герметиком — находим '
                   'источник и меняем сальники и прокладки по-человечески.',
        'ren.s7t': '07 Цепь и финальный привод',
        'ren.s7d': 'чистка, смазка и регулировка; контроль и замена звёзд. Самая дешёвая профилактика — и та, что '
                   'вибрация любит расшатывать, поэтому мы протягиваем и нужный крепёж.',
        'ren.s8t': '08 Кастом и реставрация',
        'ren.s8d': 'бобберы, скрэмблеры и кафе-рейсеры из вашего RE; полная реставрация Bullet. Смотрите <a '
                   'href="/ru/upgrades-tuning/">апгрейды и тюнинг</a> и <a href="/ru/custom/">кастом</a>.',
        'ren.issuesTitle': 'То, что эти мотоциклы делают — проверяем заранее.',
        'ren.issuesEyebrow': 'Типичные проблемы, которые мы знаем',
        'ren.issuesLead': 'Мы знаем Royal Enfield, поэтому проверяем нужные узлы на опережение, а не ждём, пока они '
                          'подведут в дороге.',
        'ren.i1t': 'Уход зазоров клапанов',
        'ren.i1d': 'Основа любого RE. Замеряем и регулируем по норме — это разница между мягким мотором и грубым, '
                   'прожорливым.',
        'ren.i2t': '«Потение» маслом на классике',
        'ren.i2d': 'Известная черта старших Bullet и моторов UCE. Находим настоящий источник и герметизируем '
                   'нормально, а не косметически.',
        'ren.i3t': 'Зарядка / реле-регулятор',
        'ren.i3d': 'Симптомы пробега — слабый заряд, севшие аккумуляторы. Читаем систему зарядки целиком, прежде чем '
                   'списывать деталь.',
        'ren.i4t': 'Крепёж, ослабленный вибрацией',
        'ren.i4d': 'Характер RE включает вибрацию; со временем она отпускает болты. На каждом ТО протягиваем то, что '
                   'важно.',
        'ren.i5t': 'Износ цепи и финального привода',
        'ren.i5d': 'Запущенная цепь съедает звёзды и обходится в разы дороже регулярного ухода. Ловим рано.',
        'ren.i6t': 'Особенности первой Himalayan 411',
        'ren.i6d': 'У ранней Himalayan были детские болезни, устранённые с годами. Знаем, что на них проверять.',
        'ren.modelsTitle': 'По всей линейке Royal Enfield.',
        'ren.modelsEyebrow': 'Модели, которые обслуживаем',
        'ren.modelsLead': 'Текущее производство, недавнее прошлое и классика — если на баке «ружьё» или надпись Royal '
                          'Enfield, привозите.',
        'ren.m1t': 'Одноцилиндровые 350, платформа J',
        'ren.m1d': 'Classic 350, Bullet 350, Meteor 350, Hunter 350, Goan Classic 350.',
        'ren.m2t': 'Одноцилиндровые 450 (Sherpa)',
        'ren.m2d': 'Himalayan 450, Guerrilla 450.',
        'ren.m3t': 'Одноцилиндровые 411',
        'ren.m3d': 'Himalayan 411, Scram 411.',
        'ren.m4t': 'Параллельные твины 648',
        'ren.m4d': 'Interceptor 650 (INT650), Continental GT 650, Super Meteor 650, Shotgun 650, Bear 650.',
        'ren.m5t': 'Классика и старшие',
        'ren.m5d': 'Bullet 500, Classic 500, Continental GT 535, Thunderbird и винтажные Bullet. Реставрация '
                   'приветствуется.',
        'ren.partsTitle': 'Доступ к каталогам по запчастям Royal Enfield.',
        'ren.partsEyebrow': 'Запчасти и доступ к каталогам',
        'ren.partsLead': 'Поставляем оригинальные запчасти Royal Enfield через дистрибьюторскую сеть и работаем с '
                         'настоящим афтермаркетом RE — брендами, которыми реально пользуются владельцы.',
        'ren.partsList': '<strong>Каталоги, с которыми работаем:</strong> OEM Royal Enfield через дистрибьютора · '
                         'Hitchcocks Motorcycles · Powertronic (настройка ECU / управление смесью) · S&S Cycle · Hagon '
                         '· K&N · Hel · NGK · DID · плюс качественные расходники. Заказывайте заранее, даже без записи '
                         'на сервис. Смотрите <a href="/ru/parts/">запчасти и расходники</a>.',
        'ren.faqTitle': 'Частые вопросы. (FAQ)',
        'ren.faqEyebrow': 'FAQ',
        'ren.q1': 'Вы официальный дилер Royal Enfield?',
        'ren.a1': 'Нет — мы независимая мастерская Royal Enfield. Плюс в том, что нет дилерской наценки и есть свобода '
                  'ставить OEM или качественный афтермаркет. Гарантию и отзывные кампании должен делать официальный '
                  'дилер, но ТО, ремонт, клапаны, кастом и реставрацию мы делаем по независимым ценам и с вниманием '
                  'прежде всего к RE.',
        'ren.q2': 'Сколько стоит обслуживание Royal Enfield?',
        'ren.a2': 'Плановое ТО — от 150 €, расходники включены (замена воздушного фильтра считается отдельно). Точная '
                  'сумма зависит от модели и интервала и подтверждается письменной сметой до начала работ. Час работы '
                  'для прочих задач — 50 €/час. Смотрите <a href="/ru/pricing/">цены</a>.',
        'ren.q3': 'Делаете ли вы регулировку клапанов?',
        'ren.a3': 'Да — это основа жизни RE, и делаем как положено. Для параллельного твина 650 проверка зазоров — от '
                  '250 €, проверка с регулировкой — от 300 €. Работа по одноцилиндровым 350/450 считается по модели и '
                  'всегда подтверждается письменной сметой заранее.',
        'ren.q4': 'Построите кастом из моего Royal Enfield или восстановите мой Bullet?',
        'ren.a4': 'Да. RE — одна из лучших баз для кастома в мире, а реставрация — часть нашей сути. Привезите идею '
                  'или уставший Bullet, и мы определим объём — боббер, скрэмблер, кафе-рейсер или точная реставрация.',
        'ren.q5': 'Привезёте OEM и афтермаркет в Португалию?',
        'ren.a5': 'Да. Оригинал Royal Enfield — через дистрибьюторскую сеть, афтермаркет — от Hitchcocks, Powertronic, '
                  'Hagon, K&N и других. Если деталь существует для вашей модели, мы её привезём.',
        'seo.relatedTitle': 'Продолжите в той же системе сервиса.',
        'seo.relatedEyebrow': 'Связанные направления',
        'seo.localTitle': 'Обслуживаем Кашкайш, Эшторил, Оэйраш и Большой Лиссабон.',
        'seo.localEyebrow': 'Локальная зона сервиса',
        'seo.localLead': 'Iron Custom Motors находится в Сан-Домингуш-де-Рана, Кашкайш. Работаем с владельцами Royal '
                         'Enfield из Кашкайша, Эшторила, Оэйраша, Синтры, Лиссабона и всего Большого Лиссабона.',
        'seo.area1t': 'Мастерская в Кашкайше',
        'seo.area1d': 'настоящая мастерская и лаунж для клиентов, а не стойка с запчастями. Оставьте мотоцикл или '
                      'приезжайте обсудить проект.',
        'seo.area2t': 'Многоязычный процесс',
        'seo.area2d': 'русский, украинский, английский и португальский, с письменными сметами и понятными следующими '
                      'шагами.',
        'seo.area3t': 'Один ответственный путь',
        'seo.area3d': 'диагностика, запчасти, установка и сопровождение по единому стандарту мастерской.',
        'ren.ctaTitle': 'Привозите свой Royal Enfield.',
        'ren.ctaEyebrow': 'Когда вы готовы — мы готовы',
        'ren.ctaText': 'Пришлите модель, год и короткое описание в WhatsApp. Ответим с ближайшим окном и письменной '
                       'сметой до начала работ. Вт–Сб, 10:00–18:00.'},
 'uk': {'ren.breadHome': 'Головна',
        'ren.h1Crumb': 'Сервіс Royal Enfield',
        'ren.btnWA': 'WhatsApp',
        'ren.btnSend': 'Надіслати заявку',
        'ren.btnBack': 'На головну',
        'ren.eyebrow': 'Royal Enfield · Кашкайш / Великий Лісабон',
        'ren.heroAlt': 'Мотоцикл Royal Enfield на підіймачі в майстерні Iron Custom Motors, Кашкайш, Великий Лісабон',
        'ren.h1': 'Сервіс Royal Enfield<br/>у <span class="accent">Кашкайші.</span>',
        'ren.sub': 'Незалежна майстерня Royal Enfield: одноциліндрові 350 і 450, паралельні твіни 650 та класичні '
                   'Bullet. Діагностика, планове ТО, клапани, кастом і реставрація — командою зі справжньою інженерною '
                   'школою.',
        'ren.introTitle': 'Справжній фахівець із RE — за незалежними цінами.',
        'ren.introEyebrow': 'Чому Royal Enfield варто привезти до нас',
        'ren.introP1': 'Iron Custom Motors — незалежна майстерня Royal Enfield у Сан-Домінгуш-де-Рана, Кашкайш. Ми '
                       'обслуговуємо всю сучасну лінійку: одноциліндрові 350 на платформі J, 450 з рідинним '
                       'охолодженням, паралельні твіни 648 — і радо беремо класику: Bullet UCE і доагрегатних років, '
                       'Continental GT, старші 500.',
        'ren.introP2': 'Royal Enfield — найстаріша марка мотоциклів у безперервному виробництві, і ті, хто на них '
                       'їздить, добре знають чому. Ці мотоцикли — про характер, механічну чесність і відчуття їзди, '
                       'якому не потрібно бути гучним, щоб його відчувати. Наше завдання — це поважати: зберігати '
                       'мотоцикл таким, яким його задумано, а не воювати з його натурою зайвим ускладненням.',
        'ren.introP3': 'За майстернею стоїть та сама інженерна школа, що принесла ICM титул чемпіонів світу AMD, '
                       'рекорд швидкості в Бонневілі та перемогу в BMW Motorrad Customizing Championship 2023. Той '
                       'самий рівень ми застосовуємо і до Classic 350, і до гоночного проєкту. А оскільки Royal '
                       'Enfield — одна з найпопулярніших у світі баз для кастому (боббери, скремблери, кафе-рейсери), '
                       'кращого місця, щоб зробити ваш по-справжньому своїм, не знайти. Дивіться <a '
                       'href="/uk/custom/">кастом і спецпроєкти</a>. З нашої майстерні: читайте <a '
                       'href="/uk/blog/royal-enfield-bear-650-fork-oil-case-study/">розбір Bear 650 про масло у '
                       'вилці</a>.<br/><br/>Незалежність — це без націнки дилера, зі '
                       'свободою ставити OEM або якісний афтермаркет по суті, і з чесною розмовою. Кошторис письмово '
                       'до роботи, звіт письмово після.',
        'ren.toolsTitle': 'Діагностика та інструмент Royal Enfield.',
        'ren.toolsEyebrow': 'Спеціалізований інструмент',
        'ren.toolsLead': 'Сучасна лінійка Royal Enfield — упорскувана: 350 на платформі J і твіни 648 працюють на EFI '
                         'з ECU. Класика — на карбюраторах. Ми готові й до того, й до іншого, на відміну від більшості '
                         'універсальних майстерень.',
        'ren.t1t': 'Діагностика Royal Enfield дилерського рівня',
        'ren.t1d': 'Читаємо й стираємо коди несправностей ECU RE, дивимося дані датчиків у реальному часі, перевіряємо '
                   'суміш і виконуємо скидання, потрібні мотоциклу після обслуговування.',
        'ren.t2t': 'Робота з EFI і паливною системою',
        'ren.t2d': 'Чищення та балансування дросельного вузла, перевірка холостого ходу й суміші на упорскуваних 350 і '
                   '650 — за цифрами, а не на око.',
        'ren.t3t': 'Карбюраторний інструмент для класики',
        'ren.t3d': 'Нормальна робота на стенді, підбір жиклерів і синхронізація для Bullet UCE і ранніших, Continental '
                   'GT 535 та старших 500.',
        'ren.t4t': 'Правильний інструмент для клапанів',
        'ren.t4d': 'Щупи, потрібні шайби й деталі приводу клапанів і те терпіння, яке ці мотори винагороджують. Зазори '
                   'клапанів — основа життя RE, і ми ставимося до них саме так.',
        'ren.servicesTitle': 'Сервіс. Ремонт. Побудова.',
        'ren.servicesEyebrow': 'Що робимо з Royal Enfield',
        'ren.servicesLead': 'Від першого ТО на новій Hunter 350 до повної реставрації Bullet — усе зі знанням Royal '
                            'Enfield і правильним інструментом.',
        'ren.s1t': '01 Планове ТО',
        'ren.s1d': 'сервіс за інтервалом RE: мастило й фільтр, рідини, гальма, ланцюг і кріплення, плюс зазори '
                   'клапанів, коли цього вимагає регламент.',
        'ren.s2t': '02 Зазори клапанів',
        'ren.s2d': "як належить, щупами й правильними шайбами. Основа здоров'я RE як на одноциліндрових, так і на "
                   'твінах 650.',
        'ren.s3t': '03 Заряд і електрика',
        'ren.s3d': 'перевірка реле-регулятора й системи заряду на пробіжних мотоциклах, акумулятор, світло та проводка '
                   'аксесуарів. Шукаємо причину, а не симптом.',
        'ren.s4t': '04 Карбюратор і EFI',
        'ren.s4d': 'перебирання й синхронізація карбюраторів на класиці; чищення, балансування й перевірка суміші EFI '
                   'на сучасних 350 і 650.',
        'ren.s5t': '05 Підвіска й колеса',
        'ren.s5d': 'сальники й мастило вилки, обслуговування заднього амортизатора, налаштування переднатягу, '
                   'підшипники й шини. Поки колеса зняті, наш <a href="/uk/shynomontazh-mototsykliv/">шиномонтаж і '
                   'балансування</a> поставить нову гуму як слід за той самий візит.',
        'ren.s6t': '06 Усунення течі мастила на класиці',
        'ren.s6d': 'старші Bullet і мотори UCE відомі «пітнінням» мастила. Ми не маскуємо герметиком — знаходимо '
                   'джерело й міняємо сальники та прокладки по-людськи.',
        'ren.s7t': '07 Ланцюг і фінальний привід',
        'ren.s7d': 'чищення, змащення й регулювання; контроль і заміна зірок. Найдешевша профілактика — і та, що '
                   'вібрація любить розхитувати, тож ми протягуємо й потрібне кріплення.',
        'ren.s8t': '08 Кастом і реставрація',
        'ren.s8d': 'боббери, скремблери й кафе-рейсери з вашого RE; повна реставрація Bullet. Дивіться <a '
                   'href="/uk/upgrades-tuning/">апгрейди й тюнінг</a> і <a href="/uk/custom/">кастом</a>.',
        'ren.issuesTitle': 'Те, що ці мотоцикли роблять — перевіряємо заздалегідь.',
        'ren.issuesEyebrow': 'Типові проблеми, які ми знаємо',
        'ren.issuesLead': 'Ми знаємо Royal Enfield, тому перевіряємо потрібні вузли на випередження, а не чекаємо, '
                          'поки вони підведуть у дорозі.',
        'ren.i1t': 'Відхід зазорів клапанів',
        'ren.i1d': "Основа будь-якого RE. Заміряємо й регулюємо за нормою — це різниця між м'яким мотором і грубим, "
                   'ненажерливим.',
        'ren.i2t': '«Пітніння» мастила на класиці',
        'ren.i2d': 'Відома риса старших Bullet і моторів UCE. Знаходимо справжнє джерело й герметизуємо нормально, а '
                   'не косметично.',
        'ren.i3t': 'Заряд / реле-регулятор',
        'ren.i3d': 'Симптоми пробігу — слабкий заряд, сівші акумулятори. Читаємо систему заряду повністю, перш ніж '
                   'списувати деталь.',
        'ren.i4t': 'Кріплення, послаблене вібрацією',
        'ren.i4d': 'Характер RE включає вібрацію; з часом вона відпускає болти. На кожному ТО протягуємо те, що '
                   'важливо.',
        'ren.i5t': 'Знос ланцюга й фінального приводу',
        'ren.i5d': "Занедбаний ланцюг з'їдає зірки й коштує в рази дорожче за регулярний догляд. Ловимо рано.",
        'ren.i6t': 'Особливості першої Himalayan 411',
        'ren.i6d': 'У ранньої Himalayan були дитячі хвороби, усунені з роками. Знаємо, що на них перевіряти.',
        'ren.modelsTitle': 'По всій лінійці Royal Enfield.',
        'ren.modelsEyebrow': 'Моделі, які обслуговуємо',
        'ren.modelsLead': 'Поточне виробництво, нещодавнє минуле й класика — якщо на баку «рушниця» чи напис Royal '
                          'Enfield, привозьте.',
        'ren.m1t': 'Одноциліндрові 350, платформа J',
        'ren.m1d': 'Classic 350, Bullet 350, Meteor 350, Hunter 350, Goan Classic 350.',
        'ren.m2t': 'Одноциліндрові 450 (Sherpa)',
        'ren.m2d': 'Himalayan 450, Guerrilla 450.',
        'ren.m3t': 'Одноциліндрові 411',
        'ren.m3d': 'Himalayan 411, Scram 411.',
        'ren.m4t': 'Паралельні твіни 648',
        'ren.m4d': 'Interceptor 650 (INT650), Continental GT 650, Super Meteor 650, Shotgun 650, Bear 650.',
        'ren.m5t': 'Класика й старші',
        'ren.m5d': 'Bullet 500, Classic 500, Continental GT 535, Thunderbird і вінтажні Bullet. Реставрація вітається.',
        'ren.partsTitle': 'Доступ до каталогів із запчастин Royal Enfield.',
        'ren.partsEyebrow': 'Запчастини й доступ до каталогів',
        'ren.partsLead': "Постачаємо оригінальні запчастини Royal Enfield через дистриб'юторську мережу й працюємо зі "
                         'справжнім афтермаркетом RE — брендами, якими реально користуються власники.',
        'ren.partsList': "<strong>Каталоги, з якими працюємо:</strong> OEM Royal Enfield через дистриб'ютора · "
                         'Hitchcocks Motorcycles · Powertronic (налаштування ECU / керування сумішшю) · S&S Cycle · '
                         'Hagon · K&N · Hel · NGK · DID · плюс якісні витратні матеріали. Замовляйте заздалегідь, '
                         'навіть без запису на сервіс. Дивіться <a href="/uk/parts/">запчастини й витратні '
                         'матеріали</a>.',
        'ren.faqTitle': 'Часті запитання. (FAQ)',
        'ren.faqEyebrow': 'FAQ',
        'ren.q1': 'Ви офіційний дилер Royal Enfield?',
        'ren.a1': 'Ні — ми незалежна майстерня Royal Enfield. Перевага в тому, що немає дилерської націнки і є свобода '
                  'ставити OEM або якісний афтермаркет. Гарантію й відкличні кампанії має робити офіційний дилер, але '
                  'ТО, ремонт, клапани, кастом і реставрацію ми робимо за незалежними цінами й з увагою насамперед до '
                  'RE.',
        'ren.q2': 'Скільки коштує обслуговування Royal Enfield?',
        'ren.a2': 'Планове ТО — від 150 €, витратні матеріали включені (заміна повітряного фільтра рахується окремо). '
                  'Точна сума залежить від моделі та інтервалу й підтверджується письмовим кошторисом до початку '
                  'робіт. Година роботи для інших завдань — 50 €/год. Дивіться <a href="/uk/pricing/">ціни</a>.',
        'ren.q3': 'Чи робите ви регулювання клапанів?',
        'ren.a3': 'Так — це основа життя RE, і робимо як належить. Для паралельного твіна 650 перевірка зазорів — від '
                  '250 €, перевірка з регулюванням — від 300 €. Робота по одноциліндрових 350/450 рахується за моделлю '
                  'й завжди підтверджується письмовим кошторисом заздалегідь.',
        'ren.q4': 'Збудуєте кастом із мого Royal Enfield чи відновите мій Bullet?',
        'ren.a4': 'Так. RE — одна з найкращих баз для кастому у світі, а реставрація — частина нашої суті. Привезіть '
                  'ідею або втомлений Bullet, і ми визначимо обсяг — боббер, скремблер, кафе-рейсер чи точна '
                  'реставрація.',
        'ren.q5': 'Привезете OEM і афтермаркет до Португалії?',
        'ren.a5': "Так. Оригінал Royal Enfield — через дистриб'юторську мережу, афтермаркет — від Hitchcocks, "
                  'Powertronic, Hagon, K&N та інших. Якщо деталь існує для вашої моделі, ми її привеземо.',
        'seo.relatedTitle': 'Продовжіть у тій самій системі сервісу.',
        'seo.relatedEyebrow': "Пов'язані напрямки",
        'seo.localTitle': 'Обслуговуємо Кашкайш, Ешторіл, Оейраш і Великий Лісабон.',
        'seo.localEyebrow': 'Локальна зона сервісу',
        'seo.localLead': 'Iron Custom Motors розташована в Сан-Домінгуш-де-Рана, Кашкайш. Працюємо з власниками Royal '
                         'Enfield із Кашкайша, Ешторіла, Оейраша, Сінтри, Лісабона й усього Великого Лісабона.',
        'seo.area1t': 'Майстерня в Кашкайші',
        'seo.area1d': 'справжня майстерня й лаунж для клієнтів, а не стійка із запчастинами. Залиште мотоцикл або '
                      'приїздіть обговорити проєкт.',
        'seo.area2t': 'Багатомовний процес',
        'seo.area2d': 'українська, російська, англійська та португальська, з письмовими кошторисами й зрозумілими '
                      'наступними кроками.',
        'seo.area3t': 'Один відповідальний шлях',
        'seo.area3d': 'діагностика, запчастини, встановлення й супровід за єдиним стандартом майстерні.',
        'ren.ctaTitle': 'Привозьте свій Royal Enfield.',
        'ren.ctaEyebrow': 'Коли ви готові — ми готові',
        'ren.ctaText': 'Надішліть модель, рік і короткий опис у WhatsApp. Відповімо з найближчим вікном і письмовим '
                       'кошторисом до початку робіт. Вт–Сб, 10:00–18:00.'}}

# Triumph brand page content. Keep source-driven so future brand pages use the shared generator.
BRAND_HEAD["triumph-service"] = {'en': {'title': 'Triumph Service in Cascais & Lisbon | Iron Custom Motors',
        'description': 'Independent Triumph workshop in Cascais. Diagnostics, scheduled service, valve clearance, '
                       'throttle balance and tuning for Bonneville, Street Triple, Tiger, Trident, Rocket 3.'},
 'pt': {'title': 'Serviço Triumph em Cascais e Lisboa | Iron Custom Motors',
        'description': 'Oficina Triumph independente em Cascais. Diagnóstico, revisão, folga de válvulas, '
                       'sincronização e afinação para Bonneville, Street Triple, Tiger, Trident, Rocket 3.'},
 'ru': {'title': 'Сервис Triumph в Кашкайше и Лиссабоне | Iron Custom Motors',
        'description': 'Независимая мастерская Triumph в Кашкайше. Диагностика, ТО, регулировка клапанов, '
                       'синхронизация и тюнинг для Bonneville, Street Triple, Tiger, Trident, Rocket 3.'},
 'uk': {'title': 'Сервіс Triumph у Кашкайші та Лісабоні | Iron Custom Motors',
        'description': 'Незалежна майстерня Triumph у Кашкайші. Діагностика, ТО, регулювання клапанів, синхронізація '
                       'та тюнінг для Bonneville, Street Triple, Tiger, Trident, Rocket 3.'}}
PAGE_I18N["triumph-service"] = {'en': {'tri.eyebrow': 'Triumph · Cascais / Greater Lisbon',
        'tri.heroAlt': 'Triumph motorcycle on the lift at Iron Custom Motors workshop in Cascais',
        'tri.h1': 'Triumph service<br/>in <span class="accent">Cascais.</span>',
        'tri.sub': 'Independent Triumph workshop — diagnostics, scheduled service, valve-clearance, throttle-body '
                   'balancing, charging-system repair, suspension, ECU tuning and custom builds for Bonneville, Speed '
                   'Twin, Scrambler, Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3, Speed 400 and the '
                   'classics.',
        'tri.breadHome': 'Home',
        'tri.h1Crumb': 'Triumph service',
        'tri.btnWA': 'WhatsApp us',
        'tri.btnSend': 'Send a request',
        'tri.introEyebrow': 'Why bring your Triumph to us',
        'tri.introTitle': 'British character, independent rates.',
        'tri.introP1': 'Iron Custom Motors is an independent Triumph specialist in Cascais. Modern Triumph is one of '
                       'the most engineering-led marques on the road — the inline-triples that define the Street '
                       'Triple, Speed Triple, Trident and Tiger; the modern-classic parallel-twins under every '
                       'Bonneville, Speed Twin and Scrambler; the 2458cc triple of the Rocket 3. They are well-built, '
                       'characterful bikes — but they reward people who actually understand the platform rather than a '
                       'shop that happens to take Triumphs in alongside everything else.',
        'tri.introP2': "The engineering culture here didn't come from nowhere. This is the team behind AMD World "
                       'Championship custom builds, a Bonneville land-speed record, and the BMW Motorrad Customizing '
                       "Championship 2023. We don't list that to wave trophies — we list it because the same standard "
                       'of measurement, tolerance and finish is what now goes into a routine Street Triple valve check '
                       'or a high-mileage Bonneville charging repair.',
        'tri.introP3': "There's a second reason Triumph and this workshop fit together. The Triumph modern classics — "
                       "Bonneville, Scrambler, Thruxton, Bobber, Speed Twin — are one of the world's biggest bases for "
                       'café racers, scramblers and bespoke builds. That is exactly our craft. Service and custom live '
                       'under the same roof here, so the bike you service with us is the same bike we can <a '
                       'href="/custom/">build into something of your own</a>.',
        'tri.introP4': 'Independent means no dealer mark-up, freedom to fit OEM or quality aftermarket parts as the '
                       'job actually requires, and direct communication with the person doing the work. Written '
                       'estimate before anything happens, written report after.',
        'tri.toolsEyebrow': 'Specialist tooling',
        'tri.toolsTitle': 'Triumph-specific diagnostic and tools.',
        'tri.toolsLead': 'Dealer-level Triumph diagnostic access plus the platform-specific tooling most independent '
                         "workshops simply don't keep — including TuneECU, the tool the Triumph independent world has "
                         'relied on for years.',
        'tri.t1t': 'Dealer-grade Triumph diagnostics',
        'tri.t1d': 'Reads and clears Triumph-specific fault codes, monitors live sensor data, runs service resets and '
                   'checks the system under load. Modern Keihin/Continental-ECU Triumphs need this depth of access — a '
                   "generic OBD reader doesn't see the bike.",
        'tri.t2t': 'TuneECU — ECU diagnostics & remap',
        'tri.t2d': 'The well-known tool for ECU work on the older Keihin-ECU Triumphs (e.g. older Bonneville, Street '
                   'Triple, Tiger). We use it for fault reading, throttle-body balancing, map flashing and the remaps '
                   'that cure snatchy low-rpm fuelling on early ride-by-wire bikes.',
        'tri.t3t': 'Throttle-body balancing',
        'tri.t3d': 'Vacuum balancing across the triples and parallel-twins — the single biggest contributor to a '
                   'smooth idle and clean throttle on these engines.',
        'tri.t4t': 'Valve & shim tooling',
        'tri.t4d': 'Proper shim-selection tooling for the twin and triple valve trains, so a clearance job is measured '
                   'and corrected to spec — not estimated.',
        'tri.servicesEyebrow': 'What we do on Triumph',
        'tri.servicesTitle': 'Service. Repair. Tune. Build.',
        'tri.servicesLead': 'From a routine oil-and-filter to a valve-clearance service, an ECU remap, or a ground-up '
                            'Bonneville café racer — all of it done with Triumph-specific knowledge.',
        'tri.s1t': '01 — Scheduled service.',
        'tri.s1d': 'Triumph interval service: oil, filter, fluids, brake check, chain and sprocket inspection (or '
                   'shaft-drive check on Rocket 3 / Trophy), plus model-specific items. From €150, consumables '
                   'included.',
        'tri.s2t': '02 — Valve-clearance — twin & triple.',
        'tri.s2d': 'Shim-checked and corrected to spec. Parallel-twin Bonneville/Speed Twin/Scrambler and the '
                   'inline-triple Street Triple/Speed Triple/Trident/Tiger/Daytona.',
        'tri.s3t': '03 — Throttle-body balancing.',
        'tri.s3d': 'Vacuum balance on triples and twins for a clean idle and smooth fuelling — done with the bike at '
                   'proper temperature.',
        'tri.s4t': '04 — Charging & electrical.',
        'tri.s4d': 'Regulator/rectifier and stator diagnosis, battery and charging-circuit testing, fault-code reading '
                   'and accessory wiring. The check that matters most on higher-mileage and older Triumphs.',
        'tri.s5t': '05 — Suspension service.',
        'tri.s5d': 'Fork seal replacement, oil change, cartridge and shock rebuild, sag and damping setup — Scrambler '
                   '1200 long-travel, Tiger adventure, Speed Triple sport and the modern-classic chassis. While the '
                   'wheels are out, <a href="/motorcycle-tyre-service/">tyre fitting and balancing</a> is done in the '
                   'same visit.',
        'tri.s6t': '06 — ECU remap & tuning.',
        'tri.s6d': 'TuneECU work on the older Keihin bikes and dealer-grade tuning elsewhere — fuelling correction '
                   'after an exhaust, and the remap that fixes snatchy throttle on early ride-by-wire models.',
        'tri.s7t': '07 — Clutch & drivetrain.',
        'tri.s7d': 'Clutch inspection and replacement, cush-drive check, chain and sprocket renewal — or final-drive '
                   'service on the shaft-drive Rocket 3 and Trophy.',
        'tri.s8t': '08 — Custom & restoration.',
        'tri.s8d': 'Café racer, scrambler and bobber builds from a Bonneville or Speed Twin base, plus restoration of '
                   'carb and early-EFI classics. See <a href="/custom/">Custom & special projects</a> and <a '
                   'href="/upgrades-tuning/">Upgrades & tuning</a>.',
        'tri.issuesEyebrow': 'Typical issues we know',
        'tri.issuesTitle': 'Triumph patterns, checked before they bite.',
        'tri.issuesLead': 'Years on these bikes mean we know where they get tired. We check the high-risk items first '
                          '— not after they leave you stranded on the way to Sintra.',
        'tri.i1t': 'Valve-clearance drift on triples & twins.',
        'tri.i1d': "We measure at interval and adjust by shim selection — properly, when it's actually due, not on a "
                   'guess.',
        'tri.i2t': 'Throttle-body balance out.',
        'tri.i2d': "A lumpy idle or buzzy throttle on a triple or twin is very often a balance that's drifted. We "
                   're-balance it instead of chasing ghosts.',
        'tri.i3t': 'Snatchy low-rpm throttle on early ride-by-wire.',
        'tri.i3d': 'A known trait on some early ride-by-wire Bonnevilles and Tigers. Often genuinely improved with a '
                   'remap — we do it via TuneECU on the eligible bikes.',
        'tri.i4t': 'Regulator/rectifier & charging on higher-mileage bikes.',
        'tri.i4d': 'Load-tested cold and hot before it cooks the battery and stator — the check that matters on older '
                   'and high-mileage Triumphs.',
        'tri.i5t': 'Sprag (starter) clutch wear on the older air-cooled 865.',
        'tri.i5d': 'A known weak spot on the older air-cooled 865 Bonneville/Thruxton/Scrambler. We diagnose the '
                   'symptom correctly rather than throwing parts at it.',
        'tri.i6t': 'Clutch & cush-drive wear.',
        'tri.i6d': 'Measured against spec — especially on hard-ridden triples and high-mileage modern classics.',
        'tri.modelsEyebrow': 'Models we service',
        'tri.modelsTitle': 'Across the Triumph lineup.',
        'tri.modelsLead': 'Current production, recent past, modern classics and older bikes — if it wears the Triumph '
                          'badge, bring it in.',
        'tri.m1t': 'Modern classics (parallel twin)',
        'tri.m1d': 'Bonneville T100 / T120, Speed Twin 900 / 1200, Scrambler 900, Scrambler 1200 X / XE, Thruxton, '
                   'Bobber, Speedmaster.',
        'tri.m2t': 'Roadsters (triple)',
        'tri.m2d': 'Trident 660, Street Triple 660 / 765 (R / RS / Moto2), Speed Triple 1200 RS / RR, and the older '
                   'Speed Triple 1050.',
        'tri.m3t': 'Adventure (triple)',
        'tri.m3d': 'Tiger Sport 660, Tiger 850 Sport, Tiger 900 GT / Rally, Tiger 1200 GT / Rally Explorer, plus the '
                   'older Tiger 800 and Tiger Explorer 1200.',
        'tri.m4t': 'Sport',
        'tri.m4d': 'Daytona 660, and the older Daytona 675 / 765 (Moto2).',
        'tri.m5t': 'Power cruiser',
        'tri.m5d': 'Rocket 3 R / GT — 2458cc triple, shaft drive.',
        'tri.m6t': 'Small platform (single) & classics',
        'tri.m6d': 'Speed 400, Scrambler 400 X — plus carb and early-EFI Bonnevilles, older triples and restoration '
                   'projects, all welcome.',
        'tri.partsEyebrow': 'Parts and accessories',
        'tri.partsTitle': 'Catalog access for major Triumph parts.',
        'tri.partsLead': 'We source through OEM Triumph and the major international aftermarket catalogs. Whatever '
                         'your bike needs — OEM, performance, modern-classic style or touring — we order it directly '
                         'through trusted suppliers.',
        'tri.partsList': '<strong>Catalogs we work with:</strong> OEM Triumph parts via distributor network · Arrow · '
                         'Zard · Vance & Hines · Öhlins · Nitron · K-Tech · British Customs · LSL · K&N · Renthal · '
                         "DID · Mitas · Avon. Order ahead even if you're not booking service. See <a "
                         'href="/parts/">Parts & consumables</a>.',
        'tri.faqEyebrow': 'FAQ',
        'tri.faqTitle': 'Common questions. (FAQ)',
        'tri.q1': 'Are you an authorised Triumph dealer?',
        'tri.a1': 'No — Iron Custom Motors is an independent Triumph workshop. The advantage is no dealer mark-up and '
                  'freedom to use OEM or quality aftermarket parts. Recall and in-warranty work itself must go through '
                  'an authorised Triumph dealer, but everything else — scheduled service, repair, valve and throttle '
                  'work, remaps, modifications — we handle at independent rates and with deeper, Triumph-first '
                  'attention.',
        'tri.q2': 'How much does a Triumph service cost?',
        'tri.a2': 'Scheduled maintenance starts from €150, consumables included (air-filter replacement is charged '
                  'separately). A valve-clearance check is from €250 on a parallel-twin (Bonneville / Speed Twin / '
                  'Scrambler) and check-and-adjust from €300; the inline-triples (Street Triple, Speed Triple, '
                  'Trident, Tiger, Daytona, Rocket 3) are quoted per model in a written estimate. Hourly work is '
                  '€50/hour. You always get a written estimate before any work starts. Prices from, taxes included.',
        'tri.q3': 'Do you do valve / shim service on Triumphs?',
        'tri.a3': 'Yes — on both the parallel-twins and the inline-triples. We measure clearances and correct them by '
                  'shim selection to spec, then re-balance the throttle bodies so the bike runs the way it should '
                  'afterwards.',
        'tri.q4': 'Can you remap my Triumph or fix the snatchy throttle?',
        'tri.a4': 'Yes. On the older Keihin-ECU bikes we use TuneECU for diagnostics and remapping — including the '
                  'remap that smooths out snatchy low-rpm fuelling on early ride-by-wire Bonnevilles and Tigers. On '
                  'newer bikes we tune with dealer-grade access, including fuelling correction after an exhaust '
                  'fitment.',
        'tri.q5': 'Can you build a custom café racer or scrambler from my Bonneville?',
        'tri.a5': 'Yes — this is core to what we do. The Bonneville, Speed Twin and Scrambler are among the best bases '
                  'in the world for café racer, scrambler and bobber builds, and our team has the championship-level '
                  'fabrication to do it. Start at <a href="/custom/">Custom & special projects</a>.',
        'tri.q6': 'Can you import OEM or aftermarket Triumph parts to Portugal?',
        'tri.a6': 'Yes — we have catalog access to OEM Triumph parts via the distributor network plus all the major '
                  'aftermarket catalogs (Arrow, Öhlins, British Customs and more). If a part exists for your model, we '
                  'source it to Cascais.',
        'seo.relatedEyebrow': 'Related workshop paths',
        'seo.relatedTitle': 'Continue through the same service system.',
        'seo.relatedLead': 'These pages connect the most common next steps: service, parts, upgrades, pricing, '
                           'brand-specific help and the rider lounge.',
        'seo.localEyebrow': 'Local service area',
        'seo.localTitle': 'Serving Cascais, Lisbon and Greater Lisbon.',
        'seo.localLead': 'Iron Custom Motors is based in São Domingos de Rana, Cascais. We work with riders from '
                         'Cascais, Estoril, Oeiras, Sintra, Lisbon and the wider Greater Lisbon area.',
        'seo.area1t': 'Cascais workshop',
        'seo.area1d': 'A real workshop and client lounge, not a remote parts counter.',
        'seo.area2t': 'Multilingual process',
        'seo.area2d': 'English, Russian, Ukrainian and Portuguese, with written estimates.',
        'seo.area3t': 'One accountable path',
        'seo.area3d': 'diagnostics, parts, installation, upgrades and follow-up under one workshop standard.',
        'tri.ctaEyebrow': 'Ready when you are',
        'tri.ctaTitle': 'Bring your Triumph in.',
        'tri.ctaText': "Send the model, year and a short description via WhatsApp. We'll come back with the closest "
                       'available slot and a written estimate before work starts. Tue–Sat, 10:00–18:00.',
        'tri.btnBack': 'Back to home'},
 'pt': {'tri.eyebrow': 'Triumph · Cascais / Grande Lisboa',
        'tri.heroAlt': 'Mota Triumph no elevador da oficina Iron Custom Motors em Cascais',
        'tri.h1': 'Serviço Triumph<br/>em <span class="accent">Cascais.</span>',
        'tri.sub': 'Oficina Triumph independente — diagnóstico, revisão programada, folga de válvulas, sincronização '
                   'dos corpos de borboleta, reparação do sistema de carga, suspensão, afinação de ECU e projetos '
                   'personalizados para Bonneville, Speed Twin, Scrambler, Street Triple, Speed Triple, Trident, '
                   'Tiger, Daytona, Rocket 3, Speed 400 e as clássicas.',
        'tri.breadHome': 'Início',
        'tri.h1Crumb': 'Serviço Triumph',
        'tri.btnWA': 'WhatsApp',
        'tri.btnSend': 'Enviar pedido',
        'tri.introEyebrow': 'Porquê trazer a sua Triumph até nós',
        'tri.introTitle': 'Carácter britânico, preços independentes.',
        'tri.introP1': 'A Iron Custom Motors é uma especialista Triumph independente em Cascais. A Triumph moderna é '
                       'uma das marcas mais orientadas pela engenharia na estrada — os triplos em linha que definem a '
                       'Street Triple, a Speed Triple, a Trident e a Tiger; os bicilíndricos paralelos modern-classic '
                       'sob cada Bonneville, Speed Twin e Scrambler; o triplo de 2458cc da Rocket 3. São motas bem '
                       'construídas e com personalidade — mas recompensam quem percebe mesmo da plataforma, e não uma '
                       'oficina que aceita Triumphs entre tudo o resto.',
        'tri.introP2': 'A cultura de engenharia desta casa não surgiu do nada. Esta é a equipa por trás de construções '
                       'campeãs no AMD World Championship, de um recorde de velocidade em Bonneville e do BMW Motorrad '
                       'Customizing Championship 2023. Não o referimos para exibir troféus — referimo-lo porque o '
                       'mesmo padrão de medição, tolerância e acabamento é o que agora entra numa folga de válvulas de '
                       'rotina numa Street Triple ou numa reparação de carga de uma Bonneville com muitos quilómetros.',
        'tri.introP3': 'Há uma segunda razão para a Triumph e esta oficina encaixarem. As modern classics da Triumph — '
                       'Bonneville, Scrambler, Thruxton, Bobber, Speed Twin — são uma das maiores bases do mundo para '
                       'café racers, scramblers e projetos à medida. É exatamente o nosso ofício. Serviço e custom '
                       'vivem sob o mesmo teto, por isso a mota que connosco revê é a mesma que podemos <a '
                       'href="/pt/custom/">transformar em algo só seu</a>.',
        'tri.introP4': 'Independente significa sem margem de concessionário, liberdade para montar peças OEM ou '
                       'aftermarket de qualidade conforme o trabalho exige, e comunicação direta com quem faz o '
                       'serviço. Orçamento escrito antes de qualquer trabalho, relatório escrito depois.',
        'tri.toolsEyebrow': 'Ferramentas especializadas',
        'tri.toolsTitle': 'Diagnóstico e ferramentas específicos Triumph.',
        'tri.toolsLead': 'Acesso de diagnóstico Triumph ao nível do concessionário, mais o ferramental específico da '
                         'plataforma que a maioria das oficinas independentes simplesmente não tem — incluindo o '
                         'TuneECU, a ferramenta em que o mundo Triumph independente confia há anos.',
        'tri.t1t': 'Diagnóstico Triumph ao nível do concessionário',
        'tri.t1d': 'Lê e apaga códigos de avaria específicos Triumph, monitoriza dados em tempo real, executa resets '
                   'de serviço e verifica o sistema sob carga. As Triumph modernas com ECU Keihin/Continental exigem '
                   'esta profundidade de acesso — um leitor OBD genérico não "vê" a mota.',
        'tri.t2t': 'TuneECU — diagnóstico e remap de ECU',
        'tri.t2d': 'A conhecida ferramenta para trabalho de ECU nas Triumph mais antigas com ECU Keihin (ex.: '
                   'Bonneville, Street Triple e Tiger mais antigas). Usamo-la para leitura de avarias, sincronização '
                   'dos corpos de borboleta, gravação de mapas e os remaps que corrigem a alimentação irregular a '
                   'baixas rotações nas primeiras ride-by-wire.',
        'tri.t3t': 'Sincronização dos corpos de borboleta',
        'tri.t3d': 'Sincronização por vácuo nos triplos e bicilíndricos paralelos — o maior contributo para um ralenti '
                   'suave e um acelerador limpo nestes motores.',
        'tri.t4t': 'Ferramental de válvulas e shims',
        'tri.t4d': 'Ferramental de seleção de shims para a distribuição dos bicilíndricos e triplos, para que uma '
                   'folga de válvulas seja medida e corrigida ao valor de especificação — não estimada.',
        'tri.servicesEyebrow': 'O que fazemos na Triumph',
        'tri.servicesTitle': 'Serviço. Reparação. Afinação. Construção.',
        'tri.servicesLead': 'De uma muda de óleo e filtro de rotina a uma folga de válvulas, um remap de ECU ou uma '
                            'café racer de raiz sobre base Bonneville — tudo com conhecimento específico Triumph.',
        'tri.s1t': '01 — Revisão programada.',
        'tri.s1d': 'Serviço de intervalo Triumph: óleo, filtro, fluidos, travões, inspeção de corrente e cremalheira '
                   '(ou verificação da transmissão por cardan na Rocket 3 / Trophy), mais itens específicos do modelo. '
                   'Desde 150 €, consumíveis incluídos.',
        'tri.s2t': '02 — Folga de válvulas — bicilíndrico e triplo.',
        'tri.s2d': 'Verificada e corrigida por seleção de shims. Bonneville/Speed Twin/Scrambler bicilíndricos e os '
                   'triplos em linha Street Triple/Speed Triple/Trident/Tiger/Daytona.',
        'tri.s3t': '03 — Sincronização dos corpos de borboleta.',
        'tri.s3d': 'Equilíbrio por vácuo em triplos e bicilíndricos para um ralenti limpo e alimentação suave — com a '
                   'mota à temperatura correta.',
        'tri.s4t': '04 — Sistema de carga e elétrico.',
        'tri.s4d': 'Diagnóstico do regulador/retificador e do estator, teste da bateria e do circuito de carga, '
                   'leitura de avarias e cablagem de acessórios. A verificação que mais importa nas Triumph com muitos '
                   'quilómetros e mais antigas.',
        'tri.s5t': '05 — Serviço de suspensão.',
        'tri.s5d': 'Substituição de retentores de forquilha, muda de óleo, revisão de cartucho e amortecedor, ajuste '
                   'de sag e amortecimento — Scrambler 1200 de curso longo, Tiger de aventura, Speed Triple desportiva '
                   'e o chassis modern-classic. Com as rodas fora, a <a href="/pt/montagem-de-pneus-mota/">montagem e '
                   'equilíbrio de pneus</a> é feita na mesma visita.',
        'tri.s6t': '06 — Remap e afinação de ECU.',
        'tri.s6d': 'Trabalho com TuneECU nas Keihin mais antigas e afinação ao nível do concessionário nas restantes — '
                   'correção de alimentação após um escape e o remap que corrige o acelerador irregular nas primeiras '
                   'ride-by-wire.',
        'tri.s7t': '07 — Embraiagem e transmissão.',
        'tri.s7d': 'Inspeção e substituição de embraiagem, verificação do cardan de transmissão (cush-drive), '
                   'substituição de corrente e cremalheira — ou serviço de transmissão final na Rocket 3 e Trophy de '
                   'cardan.',
        'tri.s8t': '08 — Custom e restauro.',
        'tri.s8d': 'Café racer, scrambler e bobber sobre base Bonneville ou Speed Twin, mais restauro de clássicas a '
                   'carburador e early-EFI. Ver <a href="/pt/custom/">Custom e projetos especiais</a> e <a '
                   'href="/pt/upgrades-tuning/">Upgrades e afinação</a>.',
        'tri.issuesEyebrow': 'Problemas típicos que conhecemos',
        'tri.issuesTitle': 'Padrões Triumph, verificados antes de incomodarem.',
        'tri.issuesLead': 'Anos nestas motas significam que sabemos onde se cansam. Verificamos primeiro os itens de '
                          'maior risco — não depois de o deixarem a pé a caminho de Sintra.',
        'tri.i1t': 'Folga de válvulas a desviar em triplos e bicilíndricos.',
        'tri.i1d': 'Medimos ao intervalo e ajustamos por seleção de shims — corretamente, quando é mesmo devido, e não '
                   'por palpite.',
        'tri.i2t': 'Corpos de borboleta dessincronizados.',
        'tri.i2d': 'Um ralenti irregular ou acelerador "áspero" num triplo ou bicilíndrico é muitas vezes uma '
                   'sincronização que se desviou. Voltamos a sincronizar em vez de andar à procura de fantasmas.',
        'tri.i3t': 'Acelerador irregular a baixas rotações nas primeiras ride-by-wire.',
        'tri.i3d': 'Uma característica conhecida em algumas Bonneville e Tiger ride-by-wire iniciais. Muitas vezes '
                   'melhora de facto com um remap — fazemo-lo via TuneECU nas motas elegíveis.',
        'tri.i4t': 'Regulador/retificador e carga nas motas com muitos quilómetros.',
        'tri.i4d': 'Testado a frio e a quente antes de queimar a bateria e o estator — a verificação que importa nas '
                   'Triumph mais antigas e com muita quilometragem.',
        'tri.i5t': 'Desgaste do sprag (embraiagem de arranque) nas 865 a ar mais antigas.',
        'tri.i5d': 'Um ponto fraco conhecido nas Bonneville/Thruxton/Scrambler 865 a ar mais antigas. Diagnosticamos o '
                   'sintoma corretamente em vez de atirar peças ao problema.',
        'tri.i6t': 'Desgaste de embraiagem e cush-drive.',
        'tri.i6d': 'Medido contra a especificação — sobretudo em triplos muito usados e modern classics com '
                   'quilometragem.',
        'tri.modelsEyebrow': 'Modelos que servimos',
        'tri.modelsTitle': 'Em toda a gama Triumph.',
        'tri.modelsLead': 'Produção atual, passado recente, modern classics e motas mais antigas — se tem o emblema '
                          'Triumph, traga-a.',
        'tri.m1t': 'Modern classics (bicilíndrico paralelo)',
        'tri.m1d': 'Bonneville T100 / T120, Speed Twin 900 / 1200, Scrambler 900, Scrambler 1200 X / XE, Thruxton, '
                   'Bobber, Speedmaster.',
        'tri.m2t': 'Roadsters (triplo)',
        'tri.m2d': 'Trident 660, Street Triple 660 / 765 (R / RS / Moto2), Speed Triple 1200 RS / RR e a anterior '
                   'Speed Triple 1050.',
        'tri.m3t': 'Aventura (triplo)',
        'tri.m3d': 'Tiger Sport 660, Tiger 850 Sport, Tiger 900 GT / Rally, Tiger 1200 GT / Rally Explorer, mais as '
                   'anteriores Tiger 800 e Tiger Explorer 1200.',
        'tri.m4t': 'Desportiva',
        'tri.m4d': 'Daytona 660 e as anteriores Daytona 675 / 765 (Moto2).',
        'tri.m5t': 'Power cruiser',
        'tri.m5d': 'Rocket 3 R / GT — triplo de 2458cc, transmissão por cardan.',
        'tri.m6t': 'Plataforma pequena (monocilíndrica) e clássicas',
        'tri.m6d': 'Speed 400, Scrambler 400 X — mais Bonneville a carburador e early-EFI, triplos mais antigos e '
                   'projetos de restauro, todos bem-vindos.',
        'tri.partsEyebrow': 'Peças e acessórios',
        'tri.partsTitle': 'Acesso a catálogo para as principais peças Triumph.',
        'tri.partsLead': 'Fornecemos através da Triumph OEM e dos grandes catálogos aftermarket internacionais. O que '
                         'a sua mota precisar — OEM, performance, estilo modern-classic ou touring — encomendamos '
                         'diretamente a fornecedores de confiança.',
        'tri.partsList': '<strong>Catálogos com que trabalhamos:</strong> Peças OEM Triumph via rede de distribuição · '
                         'Arrow · Zard · Vance & Hines · Öhlins · Nitron · K-Tech · British Customs · LSL · K&N · '
                         'Renthal · DID · Mitas · Avon. Encomende com antecedência mesmo sem marcar serviço. Ver <a '
                         'href="/pt/parts/">Peças e consumíveis</a>.',
        'tri.faqEyebrow': 'FAQ',
        'tri.faqTitle': 'Perguntas frequentes. (FAQ)',
        'tri.q1': 'São concessionário Triumph autorizado?',
        'tri.a1': 'Não — a Iron Custom Motors é uma oficina Triumph independente. A vantagem é não haver margem de '
                  'concessionário e a liberdade de usar peças OEM ou aftermarket de qualidade. As campanhas de recolha '
                  'e o trabalho em garantia têm de passar por um concessionário Triumph autorizado, mas todo o resto — '
                  'revisão, reparação, válvulas e borboletas, remaps, modificações — tratamos a preços independentes e '
                  'com atenção Triumph-first.',
        'tri.q2': 'Quanto custa um serviço Triumph?',
        'tri.a2': 'A revisão programada começa em 150 €, consumíveis incluídos (a substituição do filtro de ar é '
                  'cobrada à parte). A verificação de folga de válvulas é a partir de 250 € num bicilíndrico paralelo '
                  '(Bonneville / Speed Twin / Scrambler) e a verificação com ajuste a partir de 300 €; os triplos em '
                  'linha (Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3) são orçamentados por modelo '
                  'num orçamento escrito. O trabalho à hora é 50 €/hora. Recebe sempre um orçamento escrito antes de '
                  'iniciar qualquer trabalho. Preços "desde", impostos incluídos.',
        'tri.q3': 'Fazem serviço de válvulas / shims em Triumph?',
        'tri.a3': 'Sim — tanto nos bicilíndricos paralelos como nos triplos em linha. Medimos as folgas e '
                  'corrigimo-las por seleção de shims ao valor de especificação, e depois voltamos a sincronizar os '
                  'corpos de borboleta para a mota ficar a trabalhar como deve.',
        'tri.q4': 'Fazem remap à minha Triumph ou corrigem o acelerador irregular?',
        'tri.a4': 'Sim. Nas mais antigas com ECU Keihin usamos o TuneECU para diagnóstico e remapping — incluindo o '
                  'remap que suaviza a alimentação irregular a baixas rotações nas primeiras Bonneville e Tiger '
                  'ride-by-wire. Nas mais recentes afinamos com acesso ao nível do concessionário, incluindo correção '
                  'de alimentação após a montagem de um escape.',
        'tri.q5': 'Constroem uma café racer ou scrambler à medida a partir da minha Bonneville?',
        'tri.a5': 'Sim — é central no que fazemos. A Bonneville, a Speed Twin e a Scrambler estão entre as melhores '
                  'bases do mundo para café racer, scrambler e bobber, e a nossa equipa tem a fabricação ao nível de '
                  'campeonato para o concretizar. Comece em <a href="/pt/custom/">Custom e projetos especiais</a>.',
        'tri.q6': 'Importam peças OEM ou aftermarket Triumph para Portugal?',
        'tri.a6': 'Sim — temos acesso a catálogo de peças OEM Triumph via rede de distribuição, mais todos os grandes '
                  'catálogos aftermarket (Arrow, Öhlins, British Customs e outros). Se a peça existe para o seu '
                  'modelo, trazemo-la até Cascais.',
        'seo.relatedEyebrow': 'Caminhos relacionados',
        'seo.relatedTitle': 'Continue pelo mesmo sistema de serviço.',
        'seo.relatedLead': 'Estas páginas ligam os passos seguintes mais comuns: serviço, peças, upgrades, preços, '
                           'apoio por marca e a zona de clientes.',
        'seo.localEyebrow': 'Área de serviço local',
        'seo.localTitle': 'A servir Cascais, Lisboa e a Grande Lisboa.',
        'seo.localLead': 'A Iron Custom Motors fica em São Domingos de Rana, Cascais. Trabalhamos com motociclistas de '
                         'Cascais, Estoril, Oeiras, Sintra, Lisboa e de toda a Grande Lisboa.',
        'seo.area1t': 'Oficina em Cascais',
        'seo.area1d': 'uma oficina real e um lounge de cliente, não um balcão de peças remoto.',
        'seo.area2t': 'Processo multilíngue',
        'seo.area2d': 'português, inglês, russo e ucraniano, com orçamentos escritos.',
        'seo.area3t': 'Um percurso responsável',
        'seo.area3d': 'diagnóstico, peças, montagem, upgrades e acompanhamento sob um único padrão de oficina.',
        'tri.ctaEyebrow': 'Quando estiver pronto',
        'tri.ctaTitle': 'Traga a sua Triumph.',
        'tri.ctaText': 'Envie modelo, ano e uma breve descrição por WhatsApp. Respondemos com a vaga mais próxima e um '
                       'orçamento escrito antes de começar. Ter–Sáb, 10:00–18:00.',
        'tri.btnBack': 'Voltar ao início'},
 'ru': {'tri.eyebrow': 'Triumph · Кашкайш / Большой Лиссабон',
        'tri.heroAlt': 'Мотоцикл Triumph на подъёмнике в мастерской Iron Custom Motors в Кашкайше',
        'tri.h1': 'Сервис Triumph<br/>в <span class="accent">Кашкайше.</span>',
        'tri.sub': 'Независимая мастерская Triumph — диагностика, плановое ТО, регулировка клапанов, синхронизация '
                   'дроссельных заслонок, ремонт системы зарядки, подвеска, прошивка ECU и кастом-проекты для '
                   'Bonneville, Speed Twin, Scrambler, Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3, '
                   'Speed 400 и классики.',
        'tri.breadHome': 'Главная',
        'tri.h1Crumb': 'Сервис Triumph',
        'tri.btnWA': 'Написать в WhatsApp',
        'tri.btnSend': 'Оставить заявку',
        'tri.introEyebrow': 'Почему Triumph стоит привезти к нам',
        'tri.introTitle': 'Британский характер, цены независимой мастерской.',
        'tri.introP1': 'Iron Custom Motors — независимый специалист по Triumph в Кашкайше. Современный Triumph — одна '
                       'из самых инженерных марок на дороге: рядные «триплы», которые определяют Street Triple, Speed '
                       'Triple, Trident и Tiger; современно-классические параллельные твины под каждой Bonneville, '
                       'Speed Twin и Scrambler; триплейный мотор 2458 куб. см у Rocket 3. Это добротные и характерные '
                       'мотоциклы — но они вознаграждают тех, кто действительно понимает платформу, а не мастерскую, '
                       'которая берёт Triumph «заодно со всем остальным».',
        'tri.introP2': 'Инженерная культура здесь возникла не на пустом месте. Это команда, за которой стоят '
                       'кастом-проекты — чемпионы AMD World Championship, рекорд скорости на солёном озере Bonneville '
                       'и победа в BMW Motorrad Customizing Championship 2023. Мы упоминаем это не ради кубков — а '
                       'потому что тот же уровень измерений, допусков и финиша теперь идёт в обычную проверку клапанов '
                       'Street Triple или в ремонт зарядки Bonneville с большим пробегом.',
        'tri.introP3': 'Есть и вторая причина, почему Triumph и эта мастерская так подходят друг другу. Современная '
                       'классика Triumph — Bonneville, Scrambler, Thruxton, Bobber, Speed Twin — одна из крупнейших в '
                       'мире баз для café racer, скрэмблеров и проектов на заказ. Это ровно наше ремесло. Сервис и '
                       'кастом живут под одной крышей, поэтому мотоцикл, который вы обслуживаете у нас, — это тот же '
                       'мотоцикл, который мы можем <a href="/ru/custom/">превратить в нечто ваше собственное</a>.',
        'tri.introP4': 'Независимость означает отсутствие дилерской наценки, свободу ставить OEM или качественный '
                       'aftermarket по реальной задаче и прямое общение с тем, кто делает работу. Письменная смета до '
                       'начала работ, письменный отчёт после.',
        'tri.toolsEyebrow': 'Специальный инструмент',
        'tri.toolsTitle': 'Диагностика и инструмент именно под Triumph.',
        'tri.toolsLead': 'Доступ к диагностике Triumph дилерского уровня плюс инструмент под платформу, которого у '
                         'большинства независимых мастерских попросту нет, — включая TuneECU, на который независимый '
                         'мир Triumph опирается уже много лет.',
        'tri.t1t': 'Диагностика Triumph дилерского уровня',
        'tri.t1d': 'Читает и стирает специфические для Triumph коды ошибок, отслеживает данные датчиков в реальном '
                   'времени, выполняет сервисные сбросы и проверяет систему под нагрузкой. Современным Triumph с ECU '
                   'Keihin/Continental нужен именно такой уровень доступа — обычный OBD-сканер мотоцикл «не видит».',
        'tri.t2t': 'TuneECU — диагностика и прошивка ECU',
        'tri.t2d': 'Известный инструмент для работы с ECU на старых Triumph с блоком Keihin (например, ранние '
                   'Bonneville, Street Triple, Tiger). Используем его для чтения ошибок, синхронизации дроссельных '
                   'заслонок, заливки карт и тех прошивок, что лечат рывки на низах у ранних ride-by-wire.',
        'tri.t3t': 'Синхронизация дроссельных заслонок',
        'tri.t3d': 'Вакуумная синхронизация на триплах и параллельных твинах — главный вклад в ровный холостой ход и '
                   'чистую работу газа на этих моторах.',
        'tri.t4t': 'Инструмент для клапанов и шайб',
        'tri.t4d': 'Правильный инструмент подбора регулировочных шайб для ГРМ твинов и триплов: зазор измеряется и '
                   'приводится к норме, а не «прикидывается на глаз».',
        'tri.servicesEyebrow': 'Что мы делаем с Triumph',
        'tri.servicesTitle': 'Сервис. Ремонт. Тюнинг. Сборка.',
        'tri.servicesLead': 'От обычной замены масла и фильтра до регулировки клапанов, прошивки ECU или café racer на '
                            'базе Bonneville «с нуля» — всё со знанием специфики Triumph.',
        'tri.s1t': '01 — Плановое ТО.',
        'tri.s1d': 'Сервис по интервалам Triumph: масло, фильтр, жидкости, проверка тормозов, осмотр цепи и звёзд (или '
                   'проверка кардана на Rocket 3 / Trophy), плюс пункты под конкретную модель. От 150 €, расходники '
                   'включены.',
        'tri.s2t': '02 — Регулировка клапанов — твин и трипл.',
        'tri.s2d': 'Замер и коррекция подбором шайб. Параллельные твины Bonneville/Speed Twin/Scrambler и рядные '
                   'триплы Street Triple/Speed Triple/Trident/Tiger/Daytona.',
        'tri.s3t': '03 — Синхронизация дроссельных заслонок.',
        'tri.s3d': 'Вакуумная балансировка на триплах и твинах для чистого холостого и плавного газа — на прогретом до '
                   'нужной температуры моторе.',
        'tri.s4t': '04 — Зарядка и электрика.',
        'tri.s4d': 'Диагностика реле-регулятора и статора, проверка АКБ и цепи зарядки, чтение ошибок и проводка '
                   'аксессуаров. Самая важная проверка на Triumph с пробегом и на старых моделях.',
        'tri.s5t': '05 — Обслуживание подвески.',
        'tri.s5d': 'Замена сальников вилки, замена масла, переборка картриджа и амортизатора, настройка преднатяга и '
                   'демпфирования — длинноходный Scrambler 1200, тревел-Tiger, спортивный Speed Triple и шасси '
                   'современной классики. Пока колёса сняты, <a href="/ru/shinomontazh-mototsiklov/">монтаж и '
                   'балансировка шин</a> делаются за тот же визит.',
        'tri.s6t': '06 — Прошивка и тюнинг ECU.',
        'tri.s6d': 'Работа в TuneECU на старых Keihin и тюнинг дилерского уровня на остальных — коррекция '
                   'топливоподачи после выпуска и прошивка, убирающая рывки газа на ранних ride-by-wire.',
        'tri.s7t': '07 — Сцепление и трансмиссия.',
        'tri.s7d': 'Осмотр и замена сцепления, проверка демпфера заднего колеса (cush-drive), замена цепи и звёзд — '
                   'либо обслуживание главной передачи на кардановых Rocket 3 и Trophy.',
        'tri.s8t': '08 — Кастом и реставрация.',
        'tri.s8d': 'Café racer, скрэмблер и боббер на базе Bonneville или Speed Twin, плюс реставрация карбюраторной и '
                   'ранней EFI-классики. См. <a href="/ru/custom/">Кастом и спецпроекты</a> и <a '
                   'href="/ru/upgrades-tuning/">Апгрейды и тюнинг</a>.',
        'tri.issuesEyebrow': 'Типичные слабые места, которые мы знаем',
        'tri.issuesTitle': 'Особенности Triumph — проверяем, пока не подвели.',
        'tri.issuesLead': 'Годы работы с этими мотоциклами означают, что мы знаем, где они устают. Сначала проверяем '
                          'самые рисковые узлы — а не после того, как мотоцикл бросит вас по дороге в Синтру.',
        'tri.i1t': 'Уход зазоров клапанов на триплах и твинах.',
        'tri.i1d': 'Меряем по интервалу и регулируем подбором шайб — корректно, когда это действительно нужно, а не '
                   'наугад.',
        'tri.i2t': 'Сбитая синхронизация заслонок.',
        'tri.i2d': 'Неровный холостой или «дёрганый» газ на трипле или твине — очень часто следствие ушедшей '
                   'синхронизации. Мы её восстанавливаем, а не гоняемся за призраками.',
        'tri.i3t': 'Рывки на низах у ранних ride-by-wire.',
        'tri.i3d': 'Известная черта некоторых ранних Bonneville и Tiger с ride-by-wire. Часто реально улучшается '
                   'прошивкой — делаем её через TuneECU на подходящих мотоциклах.',
        'tri.i4t': 'Реле-регулятор и зарядка на пробежных мотоциклах.',
        'tri.i4d': 'Нагрузочный тест на холодную и горячую — до того, как узел спалит АКБ и статор. Важная проверка '
                   'для старых и пробежных Triumph.',
        'tri.i5t': 'Износ бендикса (sprag-муфты стартера) на старых воздушниках 865.',
        'tri.i5d': 'Известное слабое место старых воздушных Bonneville/Thruxton/Scrambler 865. Мы корректно ставим '
                   'диагноз, а не закидываем проблему деталями.',
        'tri.i6t': 'Износ сцепления и cush-drive.',
        'tri.i6d': 'Меряем по спецификации — особенно на активно эксплуатируемых триплах и пробежной современной '
                   'классике.',
        'tri.modelsEyebrow': 'Какие модели обслуживаем',
        'tri.modelsTitle': 'По всей линейке Triumph.',
        'tri.modelsLead': 'Текущее производство, недавнее прошлое, современная классика и более старые мотоциклы — '
                          'если на нём шильдик Triumph, привозите.',
        'tri.m1t': 'Современная классика (параллельный твин)',
        'tri.m1d': 'Bonneville T100 / T120, Speed Twin 900 / 1200, Scrambler 900, Scrambler 1200 X / XE, Thruxton, '
                   'Bobber, Speedmaster.',
        'tri.m2t': 'Роадстеры (трипл)',
        'tri.m2d': 'Trident 660, Street Triple 660 / 765 (R / RS / Moto2), Speed Triple 1200 RS / RR и более ранний '
                   'Speed Triple 1050.',
        'tri.m3t': 'Адвенчер (трипл)',
        'tri.m3d': 'Tiger Sport 660, Tiger 850 Sport, Tiger 900 GT / Rally, Tiger 1200 GT / Rally Explorer, а также '
                   'прежние Tiger 800 и Tiger Explorer 1200.',
        'tri.m4t': 'Спорт',
        'tri.m4d': 'Daytona 660 и прежние Daytona 675 / 765 (Moto2).',
        'tri.m5t': 'Пауэр-круизер',
        'tri.m5d': 'Rocket 3 R / GT — трипл 2458 куб. см, кардан.',
        'tri.m6t': 'Малая платформа (одноцилиндровый) и классика',
        'tri.m6d': 'Speed 400, Scrambler 400 X — а также карбюраторные и ранние EFI Bonneville, более старые триплы и '
                   'реставрационные проекты, все приветствуются.',
        'tri.partsEyebrow': 'Запчасти и аксессуары',
        'tri.partsTitle': 'Доступ к каталогам по основным запчастям Triumph.',
        'tri.partsLead': 'Заказываем через OEM Triumph и крупные международные aftermarket-каталоги. Что бы ни '
                         'понадобилось вашему мотоциклу — OEM, performance, modern-classic стиль или туринг — привозим '
                         'напрямую через проверенных поставщиков.',
        'tri.partsList': '<strong>Каталоги, с которыми работаем:</strong> OEM-запчасти Triumph через дистрибьюторскую '
                         'сеть · Arrow · Zard · Vance & Hines · Öhlins · Nitron · K-Tech · British Customs · LSL · K&N '
                         '· Renthal · DID · Mitas · Avon. Заказывайте заранее, даже без записи на сервис. См. <a '
                         'href="/ru/parts/">Запчасти и расходники</a>.',
        'tri.faqEyebrow': 'FAQ',
        'tri.faqTitle': 'Частые вопросы. (FAQ)',
        'tri.q1': 'Вы официальный дилер Triumph?',
        'tri.a1': 'Нет — Iron Custom Motors независимая мастерская Triumph. Плюс в отсутствии дилерской наценки и '
                  'свободе использовать OEM или качественный aftermarket. Отзывные кампании и гарантийные работы '
                  'должны идти через официального дилера Triumph, но всё остальное — плановое ТО, ремонт, клапаны и '
                  'заслонки, прошивки, доработки — мы делаем по ценам независимой мастерской и с более глубоким, '
                  'Triumph-first вниманием.',
        'tri.q2': 'Сколько стоит обслуживание Triumph?',
        'tri.a2': 'Плановое ТО — от 150 €, расходники включены (замена воздушного фильтра считается отдельно). '
                  'Проверка зазоров клапанов — от 250 € на параллельном твине (Bonneville / Speed Twin / Scrambler), '
                  'проверка с регулировкой — от 300 €; рядные триплы (Street Triple, Speed Triple, Trident, Tiger, '
                  'Daytona, Rocket 3) считаются по модели в письменной смете. Почасовая работа — 50 €/час. Письменную '
                  'смету вы получаете всегда до начала работ. Цены «от», налоги включены.',
        'tri.q3': 'Делаете ли вы регулировку клапанов / по шайбам на Triumph?',
        'tri.a3': 'Да — и на параллельных твинах, и на рядных триплах. Меряем зазоры и приводим их к норме подбором '
                  'шайб, после чего заново синхронизируем дроссельные заслонки, чтобы мотоцикл работал как положено.',
        'tri.q4': 'Можете прошить мой Triumph или убрать рывки газа?',
        'tri.a4': 'Да. На старых мотоциклах с ECU Keihin используем TuneECU для диагностики и прошивки — включая '
                  'прошивку, которая сглаживает рывки на низах у ранних ride-by-wire Bonneville и Tiger. На новых '
                  'настраиваем с доступом дилерского уровня, в том числе коррекцию топливоподачи после установки '
                  'выпуска.',
        'tri.q5': 'Соберёте кастомный café racer или скрэмблер из моей Bonneville?',
        'tri.a5': 'Да — это в самом ядре того, что мы делаем. Bonneville, Speed Twin и Scrambler — одни из лучших в '
                  'мире баз для café racer, скрэмблера и боббера, а у нашей команды есть изготовление деталей '
                  'чемпионского уровня, чтобы это воплотить. Начните с <a href="/ru/custom/">Кастома и '
                  'спецпроектов</a>.',
        'tri.q6': 'Можете привезти OEM или aftermarket запчасти Triumph в Португалию?',
        'tri.a6': 'Да — у нас есть доступ к каталогу OEM-запчастей Triumph через дистрибьюторскую сеть плюс все '
                  'крупные aftermarket-каталоги (Arrow, Öhlins, British Customs и другие). Если деталь существует для '
                  'вашей модели, мы привезём её в Кашкайш.',
        'seo.relatedEyebrow': 'Связанные разделы',
        'seo.relatedTitle': 'Продолжите в той же системе сервиса.',
        'seo.relatedLead': 'Эти страницы связывают самые частые следующие шаги: сервис, запчасти, апгрейды, цены, '
                           'помощь по марке и клиентскую зону.',
        'seo.localEyebrow': 'Зона обслуживания',
        'seo.localTitle': 'Обслуживаем Кашкайш, Лиссабон и Большой Лиссабон.',
        'seo.localLead': 'Iron Custom Motors находится в Сан-Домингуш-де-Рана, Кашкайш. Мы работаем с райдерами из '
                         'Кашкайша, Эшторила, Оэйраша, Синтры, Лиссабона и всего региона Большого Лиссабона.',
        'seo.area1t': 'Мастерская в Кашкайше',
        'seo.area1d': 'настоящая мастерская и лаундж для клиента, а не удалённая стойка запчастей.',
        'seo.area2t': 'Многоязычный процесс',
        'seo.area2d': 'русский, английский, украинский и португальский, с письменными сметами.',
        'seo.area3t': 'Один ответственный маршрут',
        'seo.area3d': 'диагностика, запчасти, установка, апгрейды и сопровождение под единым стандартом мастерской.',
        'tri.ctaEyebrow': 'Когда будете готовы',
        'tri.ctaTitle': 'Привозите свой Triumph.',
        'tri.ctaText': 'Пришлите модель, год и короткое описание в WhatsApp. Вернёмся с ближайшим свободным окном и '
                       'письменной сметой до начала работ. Вт–Сб, 10:00–18:00.',
        'tri.btnBack': 'На главную'},
 'uk': {'tri.eyebrow': 'Triumph · Кашкайш / Великий Лісабон',
        'tri.heroAlt': 'Мотоцикл Triumph на підйомнику в майстерні Iron Custom Motors у Кашкайші',
        'tri.h1': 'Сервіс Triumph<br/>у <span class="accent">Кашкайші.</span>',
        'tri.sub': 'Незалежна майстерня Triumph — діагностика, планове ТО, регулювання клапанів, синхронізація '
                   'дросельних заслінок, ремонт системи заряджання, підвіска, прошивка ECU та кастом-проєкти для '
                   'Bonneville, Speed Twin, Scrambler, Street Triple, Speed Triple, Trident, Tiger, Daytona, Rocket 3, '
                   'Speed 400 і класики.',
        'tri.breadHome': 'Головна',
        'tri.h1Crumb': 'Сервіс Triumph',
        'tri.btnWA': 'Написати у WhatsApp',
        'tri.btnSend': 'Залишити заявку',
        'tri.introEyebrow': 'Чому Triumph варто привезти до нас',
        'tri.introTitle': 'Британський характер, ціни незалежної майстерні.',
        'tri.introP1': 'Iron Custom Motors — незалежний спеціаліст із Triumph у Кашкайші. Сучасний Triumph — одна з '
                       'найбільш інженерних марок на дорозі: рядні «трипли», які визначають Street Triple, Speed '
                       'Triple, Trident і Tiger; сучасно-класичні паралельні твіни під кожною Bonneville, Speed Twin і '
                       'Scrambler; трипловий мотор 2458 куб. см у Rocket 3. Це добротні й характерні мотоцикли — але '
                       'вони винагороджують тих, хто справді розуміє платформу, а не майстерню, яка бере Triumph '
                       '«заодно з усім іншим».',
        'tri.introP2': 'Інженерна культура тут виникла не на порожньому місці. Це команда, за якою стоять '
                       'кастом-проєкти — чемпіони AMD World Championship, рекорд швидкості на солоному озері '
                       'Bonneville і перемога в BMW Motorrad Customizing Championship 2023. Ми згадуємо це не заради '
                       'кубків — а тому що той самий рівень вимірювань, допусків і фінішу тепер іде у звичайну '
                       'перевірку клапанів Street Triple чи в ремонт заряджання Bonneville з великим пробігом.',
        'tri.introP3': 'Є й друга причина, чому Triumph і ця майстерня так пасують одне одному. Сучасна класика '
                       'Triumph — Bonneville, Scrambler, Thruxton, Bobber, Speed Twin — одна з найбільших у світі баз '
                       'для café racer, скремблерів і проєктів на замовлення. Це саме наше ремесло. Сервіс і кастом '
                       'живуть під одним дахом, тож мотоцикл, який ви обслуговуєте в нас, — це той самий мотоцикл, '
                       'який ми можемо <a href="/uk/custom/">перетворити на щось ваше власне</a>.',
        'tri.introP4': 'Незалежність означає відсутність дилерської націнки, свободу ставити OEM чи якісний '
                       'aftermarket за реальною задачею і пряме спілкування з тим, хто виконує роботу. Письмовий '
                       'кошторис до початку робіт, письмовий звіт після.',
        'tri.toolsEyebrow': 'Спеціальний інструмент',
        'tri.toolsTitle': 'Діагностика та інструмент саме під Triumph.',
        'tri.toolsLead': 'Доступ до діагностики Triumph дилерського рівня плюс інструмент під платформу, якого в '
                         'більшості незалежних майстерень просто немає, — зокрема TuneECU, на який незалежний світ '
                         'Triumph спирається вже багато років.',
        'tri.t1t': 'Діагностика Triumph дилерського рівня',
        'tri.t1d': 'Зчитує й стирає специфічні для Triumph коди помилок, відстежує дані датчиків у реальному часі, '
                   'виконує сервісні скидання та перевіряє систему під навантаженням. Сучасним Triumph з ECU '
                   'Keihin/Continental потрібен саме такий рівень доступу — звичайний OBD-сканер мотоцикл «не бачить».',
        'tri.t2t': 'TuneECU — діагностика та прошивка ECU',
        'tri.t2d': 'Відомий інструмент для роботи з ECU на старих Triumph із блоком Keihin (наприклад, ранні '
                   'Bonneville, Street Triple, Tiger). Використовуємо його для зчитування помилок, синхронізації '
                   'дросельних заслінок, заливання карт і тих прошивок, що лікують ривки на низах у ранніх '
                   'ride-by-wire.',
        'tri.t3t': 'Синхронізація дросельних заслінок',
        'tri.t3d': 'Вакуумна синхронізація на триплах і паралельних твінах — головний внесок у рівний холостий хід і '
                   'чисту роботу газу на цих моторах.',
        'tri.t4t': 'Інструмент для клапанів і шайб',
        'tri.t4d': 'Правильний інструмент підбору регулювальних шайб для ГРМ твінів і триплів: зазор вимірюється і '
                   'доводиться до норми, а не «прикидається на око».',
        'tri.servicesEyebrow': 'Що ми робимо з Triumph',
        'tri.servicesTitle': 'Сервіс. Ремонт. Тюнінг. Збірка.',
        'tri.servicesLead': 'Від звичайної заміни оливи й фільтра до регулювання клапанів, прошивки ECU чи café racer '
                            'на базі Bonneville «з нуля» — усе зі знанням специфіки Triumph.',
        'tri.s1t': '01 — Планове ТО.',
        'tri.s1d': 'Сервіс за інтервалами Triumph: олива, фільтр, рідини, перевірка гальм, огляд ланцюга і зірок (або '
                   'перевірка кардана на Rocket 3 / Trophy), плюс пункти під конкретну модель. Від 150 €, витратні '
                   'матеріали включені.',
        'tri.s2t': '02 — Регулювання клапанів — твін і трипл.',
        'tri.s2d': 'Замір і корекція підбором шайб. Паралельні твіни Bonneville/Speed Twin/Scrambler та рядні трипли '
                   'Street Triple/Speed Triple/Trident/Tiger/Daytona.',
        'tri.s3t': '03 — Синхронізація дросельних заслінок.',
        'tri.s3d': 'Вакуумне балансування на триплах і твінах для чистого холостого ходу і плавного газу — на '
                   'прогрітому до потрібної температури моторі.',
        'tri.s4t': '04 — Заряджання та електрика.',
        'tri.s4d': 'Діагностика реле-регулятора і статора, перевірка АКБ і кола заряджання, зчитування помилок і '
                   'проводка аксесуарів. Найважливіша перевірка на Triumph із пробігом і на старих моделях.',
        'tri.s5t': '05 — Обслуговування підвіски.',
        'tri.s5d': 'Заміна сальників вилки, заміна оливи, переборка картриджа й амортизатора, налаштування переднатягу '
                   'та демпфування — довгоходовий Scrambler 1200, тревел-Tiger, спортивний Speed Triple і шасі '
                   'сучасної класики. Поки колеса зняті, <a href="/uk/shynomontazh-mototsykliv/">монтаж і балансування '
                   'шин</a> робляться за той самий візит.',
        'tri.s6t': '06 — Прошивка та тюнінг ECU.',
        'tri.s6d': 'Робота в TuneECU на старих Keihin і тюнінг дилерського рівня на інших — корекція паливоподачі '
                   'після випуску і прошивка, що прибирає ривки газу на ранніх ride-by-wire.',
        'tri.s7t': '07 — Зчеплення і трансмісія.',
        'tri.s7d': 'Огляд і заміна зчеплення, перевірка демпфера заднього колеса (cush-drive), заміна ланцюга і зірок '
                   '— або обслуговування головної передачі на карданних Rocket 3 і Trophy.',
        'tri.s8t': '08 — Кастом і реставрація.',
        'tri.s8d': 'Café racer, скремблер і боббер на базі Bonneville чи Speed Twin, плюс реставрація карбюраторної та '
                   'ранньої EFI-класики. Див. <a href="/uk/custom/">Кастом і спецпроєкти</a> та <a '
                   'href="/uk/upgrades-tuning/">Апгрейди і тюнінг</a>.',
        'tri.issuesEyebrow': 'Типові слабкі місця, які ми знаємо',
        'tri.issuesTitle': 'Особливості Triumph — перевіряємо, поки не підвели.',
        'tri.issuesLead': 'Роки роботи з цими мотоциклами означають, що ми знаємо, де вони втомлюються. Спершу '
                          'перевіряємо найризикованіші вузли — а не після того, як мотоцикл покине вас дорогою до '
                          'Сінтри.',
        'tri.i1t': 'Відхід зазорів клапанів на триплах і твінах.',
        'tri.i1d': 'Міряємо за інтервалом і регулюємо підбором шайб — коректно, коли це справді потрібно, а не '
                   'навмання.',
        'tri.i2t': 'Збита синхронізація заслінок.',
        'tri.i2d': 'Нерівний холостий чи «смикучий» газ на триплі або твіні — дуже часто наслідок збитої '
                   'синхронізації. Ми її відновлюємо, а не ганяємося за привидами.',
        'tri.i3t': 'Ривки на низах у ранніх ride-by-wire.',
        'tri.i3d': 'Відома риса деяких ранніх Bonneville і Tiger з ride-by-wire. Часто справді покращується прошивкою '
                   '— робимо її через TuneECU на придатних мотоциклах.',
        'tri.i4t': 'Реле-регулятор і заряджання на пробігових мотоциклах.',
        'tri.i4d': 'Навантажувальний тест на холодну й гарячу — до того, як вузол спалить АКБ і статор. Важлива '
                   'перевірка для старих і пробігових Triumph.',
        'tri.i5t': 'Знос бендикса (sprag-муфти стартера) на старих повітряниках 865.',
        'tri.i5d': 'Відоме слабке місце старих повітряних Bonneville/Thruxton/Scrambler 865. Ми коректно ставимо '
                   'діагноз, а не закидаємо проблему деталями.',
        'tri.i6t': 'Знос зчеплення і cush-drive.',
        'tri.i6d': 'Міряємо за специфікацією — особливо на активно експлуатованих триплах і пробіговій сучасній '
                   'класиці.',
        'tri.modelsEyebrow': 'Які моделі обслуговуємо',
        'tri.modelsTitle': 'По всій лінійці Triumph.',
        'tri.modelsLead': 'Поточне виробництво, нещодавнє минуле, сучасна класика й старіші мотоцикли — якщо на ньому '
                          'шильдик Triumph, привозьте.',
        'tri.m1t': 'Сучасна класика (паралельний твін)',
        'tri.m1d': 'Bonneville T100 / T120, Speed Twin 900 / 1200, Scrambler 900, Scrambler 1200 X / XE, Thruxton, '
                   'Bobber, Speedmaster.',
        'tri.m2t': 'Роадстери (трипл)',
        'tri.m2d': 'Trident 660, Street Triple 660 / 765 (R / RS / Moto2), Speed Triple 1200 RS / RR і раніший Speed '
                   'Triple 1050.',
        'tri.m3t': 'Адвенчер (трипл)',
        'tri.m3d': 'Tiger Sport 660, Tiger 850 Sport, Tiger 900 GT / Rally, Tiger 1200 GT / Rally Explorer, а також '
                   'попередні Tiger 800 і Tiger Explorer 1200.',
        'tri.m4t': 'Спорт',
        'tri.m4d': 'Daytona 660 і попередні Daytona 675 / 765 (Moto2).',
        'tri.m5t': 'Пауер-круїзер',
        'tri.m5d': 'Rocket 3 R / GT — трипл 2458 куб. см, кардан.',
        'tri.m6t': 'Мала платформа (одноциліндровий) і класика',
        'tri.m6d': 'Speed 400, Scrambler 400 X — а також карбюраторні та ранні EFI Bonneville, старіші трипли і '
                   'реставраційні проєкти, усі вітаються.',
        'tri.partsEyebrow': 'Запчастини та аксесуари',
        'tri.partsTitle': 'Доступ до каталогів за основними запчастинами Triumph.',
        'tri.partsLead': 'Замовляємо через OEM Triumph і великі міжнародні aftermarket-каталоги. Що б не знадобилося '
                         'вашому мотоциклу — OEM, performance, modern-classic стиль чи туринг — привозимо напряму '
                         'через перевірених постачальників.',
        'tri.partsList': "<strong>Каталоги, з якими працюємо:</strong> OEM-запчастини Triumph через дистриб'юторську "
                         'мережу · Arrow · Zard · Vance & Hines · Öhlins · Nitron · K-Tech · British Customs · LSL · '
                         'K&N · Renthal · DID · Mitas · Avon. Замовляйте заздалегідь, навіть без запису на сервіс. '
                         'Див. <a href="/uk/parts/">Запчастини та витратні матеріали</a>.',
        'tri.faqEyebrow': 'FAQ',
        'tri.faqTitle': 'Часті запитання. (FAQ)',
        'tri.q1': 'Ви офіційний дилер Triumph?',
        'tri.a1': 'Ні — Iron Custom Motors незалежна майстерня Triumph. Перевага — відсутність дилерської націнки і '
                  'свобода використовувати OEM чи якісний aftermarket. Відкличні кампанії та гарантійні роботи мають '
                  'іти через офіційного дилера Triumph, але все інше — планове ТО, ремонт, клапани і заслінки, '
                  'прошивки, доробки — ми робимо за цінами незалежної майстерні та з глибшою, Triumph-first увагою.',
        'tri.q2': 'Скільки коштує обслуговування Triumph?',
        'tri.a2': 'Планове ТО — від 150 €, витратні матеріали включені (заміна повітряного фільтра рахується окремо). '
                  'Перевірка зазорів клапанів — від 250 € на паралельному твіні (Bonneville / Speed Twin / Scrambler), '
                  'перевірка з регулюванням — від 300 €; рядні трипли (Street Triple, Speed Triple, Trident, Tiger, '
                  'Daytona, Rocket 3) рахуються за моделлю в письмовому кошторисі. Погодинна робота — 50 €/год. '
                  'Письмовий кошторис ви отримуєте завжди до початку робіт. Ціни «від», податки включені.',
        'tri.q3': 'Чи робите ви регулювання клапанів / за шайбами на Triumph?',
        'tri.a3': 'Так — і на паралельних твінах, і на рядних триплах. Міряємо зазори й доводимо їх до норми підбором '
                  'шайб, після чого знову синхронізуємо дросельні заслінки, щоб мотоцикл працював як належить.',
        'tri.q4': 'Чи можете прошити мій Triumph або прибрати ривки газу?',
        'tri.a4': 'Так. На старих мотоциклах з ECU Keihin використовуємо TuneECU для діагностики та прошивки — зокрема '
                  'прошивку, що згладжує ривки на низах у ранніх ride-by-wire Bonneville і Tiger. На новіших '
                  'налаштовуємо з доступом дилерського рівня, зокрема корекцію паливоподачі після встановлення '
                  'випуску.',
        'tri.q5': 'Чи зберете кастомний café racer або скремблер із моєї Bonneville?',
        'tri.a5': 'Так — це в самому ядрі того, що ми робимо. Bonneville, Speed Twin і Scrambler — одні з найкращих у '
                  'світі баз для café racer, скремблера й боббера, а наша команда має виготовлення деталей '
                  'чемпіонського рівня, щоб це втілити. Почніть із <a href="/uk/custom/">Кастому і спецпроєктів</a>.',
        'tri.q6': 'Чи можете привезти OEM або aftermarket запчастини Triumph до Португалії?',
        'tri.a6': "Так — у нас є доступ до каталогу OEM-запчастин Triumph через дистриб'юторську мережу плюс усі "
                  'великі aftermarket-каталоги (Arrow, Öhlins, British Customs та інші). Якщо деталь існує для вашої '
                  'моделі, ми привеземо її до Кашкайша.',
        'seo.relatedEyebrow': "Пов'язані розділи",
        'seo.relatedTitle': 'Продовжте в тій самій системі сервісу.',
        'seo.relatedLead': "Ці сторінки пов'язують найчастіші наступні кроки: сервіс, запчастини, апгрейди, ціни, "
                           'допомогу по марці та клієнтську зону.',
        'seo.localEyebrow': 'Зона обслуговування',
        'seo.localTitle': 'Обслуговуємо Кашкайш, Лісабон і Великий Лісабон.',
        'seo.localLead': 'Iron Custom Motors розташована в Сан-Домінгуш-де-Рана, Кашкайш. Ми працюємо з райдерами з '
                         'Кашкайша, Ешторіла, Оейраша, Сінтри, Лісабона і всього регіону Великого Лісабона.',
        'seo.area1t': 'Майстерня в Кашкайші',
        'seo.area1d': 'справжня майстерня і лаунж для клієнта, а не віддалена стійка запчастин.',
        'seo.area2t': 'Багатомовний процес',
        'seo.area2d': 'українська, англійська, російська і португальська, з письмовими кошторисами.',
        'seo.area3t': 'Один відповідальний маршрут',
        'seo.area3d': 'діагностика, запчастини, встановлення, апгрейди і супровід під єдиним стандартом майстерні.',
        'tri.ctaEyebrow': 'Коли будете готові',
        'tri.ctaTitle': 'Привозьте свій Triumph.',
        'tri.ctaText': 'Надішліть модель, рік і короткий опис у WhatsApp. Повернемося з найближчим вільним вікном і '
                       'письмовим кошторисом до початку робіт. Вт–Сб, 10:00–18:00.',
        'tri.btnBack': 'На головну'}}

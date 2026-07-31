"""
Per-page translations for title, description, and OG.
Brand name "Iron Custom Motors" stays as-is across all languages.
"""

# Pattern: PAGE_META[page_id] = { lang: {title, description} }
# Page IDs match URL path (without lang prefix, without leading/trailing slash).

PAGE_META = {
    # --------- Home ---------
    "": {
        "en": {
            "title": "Iron Custom Motors | Premium Motorcycle Service in Cascais",
            "description": "Premium motorcycle service in Cascais. Diagnostics, maintenance, repair, spare parts, consumables, upgrades, tuning, and custom motorcycle projects. Service in English, Russian, Ukrainian, Portuguese.",
            "og_description": "Premium motorcycle service, parts, upgrades, and custom expertise in Cascais. World-champion engineering culture.",
            "twitter_description": "World-champion engineering. Premium motorcycle service in Cascais.",
        },
        "ru": {
            "title": "Iron Custom Motors | Премиальный мотосервис в Кашкайше (Лиссабон)",
            "description": "Премиальный мотосервис в Кашкайше под Лиссабоном. Диагностика, обслуживание, ремонт, оригинальные и тюнинг-запчасти, расходники, апгрейды и кастом-проекты. Сервис на английском, русском, украинском, португальском.",
            "og_description": "Премиальный мотосервис, запчасти, апгрейды и кастом-экспертиза в Кашкайше. Команда чемпионов мира.",
            "twitter_description": "Инженерия мирового уровня. Премиальный мотосервис в Кашкайше.",
        },
        "uk": {
            "title": "Iron Custom Motors | Преміальний мотосервіс у Кашкайші (Лісабон)",
            "description": "Преміальний мотосервіс у Кашкайші біля Лісабона. Діагностика, обслуговування, ремонт, оригінальні та тюнінг-запчастини, витратні матеріали, апґрейди та кастом-проєкти. Сервіс англійською, російською, українською, португальською.",
            "og_description": "Преміальний мотосервіс, запчастини, апґрейди та кастом-експертиза у Кашкайші. Команда чемпіонів світу.",
            "twitter_description": "Інженерія світового рівня. Преміальний мотосервіс у Кашкайші.",
        },
        "pt": {
            "title": "Oficina de Motos Premium em Cascais (Lisboa) | Iron Custom Motors",
            "description": "Oficina de motos premium em Cascais, Grande Lisboa. Diagnóstico, manutenção, reparação, peças originais e tuning, consumíveis, upgrades e projetos custom. Atendimento em inglês, russo, ucraniano e português.",
            "og_description": "Serviço premium de motos, peças, upgrades e expertise custom em Cascais. Cultura de engenharia campeã mundial.",
            "twitter_description": "Engenharia campeã mundial. Serviço premium de motos em Cascais.",
        },
    },
    # --------- Motorcycle Service ---------
    "motorcycle-service": {
        "en": {
            "title": "Motorcycle Service & Repair in Cascais | Iron Custom Motors",
            "description": "Premium motorcycle service in Cascais — diagnostics, maintenance, brakes, suspension, electrical and general repair.",
        },
        "ru": {
            "title": "Сервис и ремонт мотоциклов в Кашкайше | Iron Custom Motors",
            "description": "Премиальный мотосервис в Кашкайше — диагностика, плановое ТО, тормоза, подвеска, электрика и общий ремонт мотоциклов.",
        },
        "uk": {
            "title": "Сервіс і ремонт мотоциклів у Кашкайші | Iron Custom Motors",
            "description": "Преміальний мотосервіс у Кашкайші — діагностика, планове ТО, гальма, підвіска, електрика та загальний ремонт мотоциклів.",
        },
        "pt": {
            "title": "Oficina de Motos em Cascais — Serviço e Reparação | ICM",
            "description": "Oficina de motos em Cascais — diagnóstico, manutenção, travões, suspensão, sistema elétrico e reparação geral.",
        },
    },
    # --------- Parts ---------
    "parts": {
        "en": {
            "title": "Motorcycle Parts & Consumables in Cascais | Iron Custom Motors",
            "description": "Spare parts, service consumables, accessories and tuning components for motorcycles. Sourced through major international catalogs. Cascais, Portugal.",
        },
        "ru": {
            "title": "Запчасти и расходники для мотоциклов в Кашкайше | Iron Custom Motors",
            "description": "Оригинальные и неоригинальные запчасти, расходники, аксессуары и тюнинг-компоненты для мотоциклов. Поставка из крупных международных каталогов. Кашкайш, Португалия.",
        },
        "uk": {
            "title": "Запчастини та витратні матеріали для мотоциклів у Кашкайші | Iron Custom Motors",
            "description": "Оригінальні та неоригінальні запчастини, витратні матеріали, аксесуари й тюнінг-компоненти для мотоциклів. Постачання з провідних міжнародних каталогів. Кашкайш, Португалія.",
        },
        "pt": {
            "title": "Peças e Consumíveis de Motos em Cascais | Iron Custom Motors",
            "description": "Peças originais e aftermarket, consumíveis de serviço, acessórios e componentes de tuning para motos. Provenientes dos principais catálogos internacionais. Cascais, Portugal.",
        },
    },
    # --------- Upgrades & Tuning ---------
    "upgrades-tuning": {
        "en": {
            "title": "Motorcycle Upgrades & Tuning in Cascais | Iron Custom Motors",
            "description": "Performance, suspension, brakes, exhaust, lighting, touring and luggage upgrades. Selected for how you actually ride. Cascais, Portugal.",
        },
        "ru": {
            "title": "Апгрейды и тюнинг мотоциклов в Кашкайше | Iron Custom Motors",
            "description": "Апгрейды по производительности, подвеске, тормозам, выхлопу, освещению, тур-обвесу и кофрам. Подобрано под ваш реальный стиль езды. Кашкайш, Португалия.",
        },
        "uk": {
            "title": "Апґрейди та тюнінг мотоциклів у Кашкайші | Iron Custom Motors",
            "description": "Апґрейди по продуктивності, підвісці, гальмах, вихлопу, освітленню, тур-обвісу та кофрах. Підібрано під ваш реальний стиль їзди. Кашкайш, Португалія.",
        },
        "pt": {
            "title": "Upgrades e Tuning de Motos em Cascais | Iron Custom Motors",
            "description": "Upgrades de performance, suspensão, travões, escape, iluminação, touring e bagagem. Selecionados para o seu estilo de condução real. Cascais, Portugal.",
        },
    },
    # --------- Custom ---------
    "custom": {
        "en": {
            "title": "Custom Motorcycle Projects in Portugal | Iron Custom Motors",
            "description": "Custom motorcycle consultations, bespoke builds and individual engineering by the team behind AMD World Championship and Bonneville record motorcycles.",
        },
        "ru": {
            "title": "Кастом-мотоциклы и спецпроекты в Португалии | Iron Custom Motors",
            "description": "Кастом-консультации, индивидуальные сборки и инженерные решения от команды, построившей чемпионов AMD World Championship и рекордсменов Bonneville.",
        },
        "uk": {
            "title": "Кастом-мотоцикли та спецпроєкти у Португалії | Iron Custom Motors",
            "description": "Кастом-консультації, індивідуальні збірки та інженерні рішення від команди, яка побудувала чемпіонів AMD World Championship і рекордсменів Bonneville.",
        },
        "pt": {
            "title": "Motos Custom e Projetos Especiais em Portugal | Iron Custom Motors",
            "description": "Consultas custom, construções à medida e engenharia individual pela equipa por trás dos campeões AMD World Championship e do recorde Bonneville.",
        },
    },
    # --------- Pre-Purchase Inspection ---------
    "pre-purchase-inspection": {
        "en": {
            "title": "Motorcycle Pre-Purchase Inspection in Cascais & Lisbon",
            "description": "Independent motorcycle pre-purchase inspection in Cascais & Lisbon. Compression test, videoscope cylinder check, written report. English-speaking. From €150.",
        },
        "ru": {
            "title": "Проверка мотоцикла перед покупкой · Кашкайш, Лиссабон",
            "description": "Независимая проверка мотоцикла перед покупкой в Кашкайше и Лиссабоне. Замер компрессии, осмотр цилиндра видеоскопом, письменный отчёт. От 150 €.",
        },
        "uk": {
            "title": "Перевірка мотоцикла перед купівлею · Кашкайш, Лісабон",
            "description": "Незалежна перевірка мотоцикла перед купівлею в Кашкайші та Лісабоні. Замір компресії, огляд циліндра відеоскопом, письмовий звіт. Від 150 €.",
        },
        "pt": {
            "title": "Inspeção Pré-Compra de Mota em Cascais e Lisboa",
            "description": "Inspeção pré-compra de mota independente em Cascais e Lisboa. Teste de compressão, inspeção do cilindro com videoscópio e relatório escrito. Desde 150 €.",
        },
    },
}

# --------- New hub/landing pages (added when nav moved off anchors) ---------
# Import on demand so we keep a single source of truth for new-page meta.
try:
    from new_pages_data import PAGE_HEAD_META as _NEW_PAGES_META
    for _pid, _langs in _NEW_PAGES_META.items():
        PAGE_META[_pid] = _langs
except ImportError:
    pass

# --------- Authorized Dealer hub ---------
try:
    from authorized_dealer_data import AUTHORIZED_DEALER_HEAD as _AUTHORIZED_DEALER_META
    PAGE_META["authorized-dealer"] = _AUTHORIZED_DEALER_META
except ImportError:
    pass

# --------- Brand-specific service pages ---------
try:
    from brand_pages_data import BRAND_HEAD as _BRAND_META
    for _pid, _langs in _BRAND_META.items():
        PAGE_META[_pid] = _langs
except ImportError:
    pass

# --------- News section ---------
try:
    from news_data import NEWS_HUB_META as _NEWS_HUB, NEWS_ARTICLES as _NEWS_ARTS
    # Hub: page_id = "news"
    PAGE_META["news"] = _NEWS_HUB
    # Each article: page_id = "news/<slug>"
    for _slug, _data in _NEWS_ARTS.items():
        PAGE_META[f"news/{_slug}"] = _data["meta"]
except ImportError:
    pass

# --------- Blog section ---------
try:
    from blog_data import BLOG_HUB_META as _BLOG_HUB, BLOG_POSTS as _BLOG_POSTS
    # Hub: page_id = "blog"
    PAGE_META["blog"] = _BLOG_HUB
    # Future posts: page_id = "blog/<slug>"
    for _slug, _data in _BLOG_POSTS.items():
        PAGE_META[f"blog/{_slug}"] = _data["meta"]
except ImportError:
    pass

# --------- Data-driven project pages ---------
try:
    from project_pages_data import PROJECT_PAGE_META as _PROJECT_PAGE_META
    for _slug, _langs in _PROJECT_PAGE_META.items():
        PAGE_META[_slug] = _langs
except ImportError:
    pass

OG_LOCALES = {
    "en": "en_US",
    "ru": "ru_RU",
    "uk": "uk_UA",
    "pt": "pt_PT",
}

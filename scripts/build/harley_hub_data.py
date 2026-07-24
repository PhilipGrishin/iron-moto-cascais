"""Supplemental data for the multilingual Harley Hub page family."""

from __future__ import annotations


PAGE_CONFIG = {
    "A": {
        "key": "tuning",
        "slug": "harley-tuning",
        "hero": "/photos/harley/harley-tuning-hero.jpg",
        "hero_dims": (4000, 2667),
        "schema_type": "Service",
    },
    "B": {
        "key": "hub",
        "slug": "harley",
        "hero": "/photos/harley/harley-hub-hero.jpg",
        "hero_dims": (5712, 4284),
        "schema_type": "CollectionPage",
    },
    "C": {
        "key": "custom",
        "slug": "harley-custom",
        "hero": "/photos/harley/harley-custom-hero.jpg",
        "hero_dims": (4000, 2667),
        "schema_type": "Service",
    },
}

LANGUAGE_HEADINGS = {
    "ENGLISH": "en",
    "PORTUGUÊS (pt-PT)": "pt",
    "РУССКИЙ": "ru",
    "УКРАЇНСЬКА": "uk",
}

HREFLANG_CODES = {
    "en": "en",
    "pt": "pt-PT",
    "ru": "ru",
    "uk": "uk",
}

UI = {
    "en": {
        "home": "Home",
        "hub": "Harley Hub",
        "latest": "Latest Harley stories",
        "readMore": "Read article",
        "viewProject": "View project",
        "noPosts": "New Harley workshop stories will appear here.",
        "serviceTypeTuning": "Harley-Davidson tuning and stage upgrades",
        "serviceTypeCustom": "Custom Harley-Davidson builds",
    },
    "pt": {
        "home": "Início",
        "hub": "Harley Hub",
        "latest": "Últimas histórias Harley",
        "readMore": "Ler artigo",
        "viewProject": "Ver projeto",
        "noPosts": "As novas histórias Harley da oficina vão aparecer aqui.",
        "serviceTypeTuning": "Tuning e upgrades de stage Harley-Davidson",
        "serviceTypeCustom": "Customização Harley-Davidson",
    },
    "ru": {
        "home": "Главная",
        "hub": "Harley Hub",
        "latest": "Последние истории Harley",
        "readMore": "Читать статью",
        "viewProject": "Смотреть проект",
        "noPosts": "Новые истории Harley из мастерской будут появляться здесь.",
        "serviceTypeTuning": "Тюнинг и stage-апгрейды Harley-Davidson",
        "serviceTypeCustom": "Кастом Harley-Davidson",
    },
    "uk": {
        "home": "Головна",
        "hub": "Harley Hub",
        "latest": "Останні історії Harley",
        "readMore": "Читати статтю",
        "viewProject": "Дивитися проєкт",
        "noPosts": "Нові історії Harley з майстерні з'являтимуться тут.",
        "serviceTypeTuning": "Тюнінг і stage-апґрейди Harley-Davidson",
        "serviceTypeCustom": "Кастом Harley-Davidson",
    },
}

PORTFOLIO_ORDER = (
    "sturmvogel",
    "joker",
    "hellboy",
    "true-religion",
)

PORTFOLIO = {
    "sturmvogel": {
        "name": "Sturmvogel",
        "image": "/photos/projects/sturmvogel.jpg",
        "dims": (1200, 800),
        "copy": {
            "en": "Sturmvogel took second place in the Café Racer category at Ericeira Kustom Fest 2026. This dieselpunk custom also carries AMD World Championship history across Italy, Ukraine and Portugal.",
            "pt": "A Sturmvogel conquistou o 2.º lugar na categoria Café Racer no Ericeira Kustom Fest 2026. Esta custom dieselpunk traz também uma história ligada ao AMD World Championship em Itália, na Ucrânia e em Portugal.",
            "ru": "Sturmvogel занял 2-е место в категории Café Racer на Ericeira Kustom Fest 2026. За этим дизельпанк-кастом также стоит история AMD World Championship в Италии, Украине и Португалии.",
            "uk": "Sturmvogel посів 2-е місце в категорії Café Racer на Ericeira Kustom Fest 2026. За цим дизельпанк-кастом також стоїть історія AMD World Championship в Італії, Україні та Португалії.",
        },
    },
    "joker": {
        "name": "Joker",
        "image": "/photos/projects/joker.jpg",
        "dims": (1200, 900),
        "copy": {
            "en": "Joker is a Harley-Davidson Dyna Street Bob with a bold urban stance and pop-art energy. Built in Kharkiv, it combines oversized custom wheels, revised suspension geometry and a nine-colour paint scheme.",
            "pt": "A Joker é uma Harley-Davidson Dyna Street Bob com postura urbana arrojada e energia pop-art. Construída em Kharkiv, combina rodas custom sobredimensionadas, geometria de suspensão revista e um esquema de pintura de nove cores.",
            "ru": "Joker — Harley-Davidson Dyna Street Bob с агрессивной городской посадкой и поп-арт-энергетикой. Построенный в Харькове проект сочетает увеличенные кастом-колёса, переработанную геометрию подвески и девятицветную окраску.",
            "uk": "Joker — Harley-Davidson Dyna Street Bob з агресивною міською посадкою та поп-арт-енергетикою. Збудований у Харкові проєкт поєднує збільшені кастом-колеса, перероблену геометрію підвіски та дев'ятиколірне фарбування.",
        },
    },
    "hellboy": {
        "name": "Hell Boy",
        "image": "/photos/projects/hellboy.jpg",
        "dims": (1200, 900),
        "copy": {
            "en": "Hell Boy won Best Paint at Ericeira Kustom Fest 2026. Built in Ukraine, this comic-art custom trike is defined by its airbrush work and 360-section rear tyre.",
            "pt": "A Hell Boy venceu o Best Paint no Ericeira Kustom Fest 2026. Construído na Ucrânia, este triciclo custom de comic-art distingue-se pelo trabalho de aerografia e pelo pneu traseiro de secção 360.",
            "ru": "Hell Boy победил в категории Best Paint на Ericeira Kustom Fest 2026. Построенный в Украине comic-art трайк выделяется аэрографией и задней шиной шириной 360.",
            "uk": "Hell Boy переміг у категорії Best Paint на Ericeira Kustom Fest 2026. Збудований в Україні comic-art трайк вирізняється аерографією та задньою шиною шириною 360.",
        },
    },
    "true-religion": {
        "name": "True Religion",
        "image": "/photos/projects/true-religion.jpg",
        "dims": (1200, 900),
        "copy": {
            "en": "True Religion is an American custom shaped by freedom, attitude and the timeless Harley-Davidson spirit. Built in Ukraine, it draws on denim culture, classic chopper proportions and the atmosphere of the open road.",
            "pt": "A True Religion é uma custom americana moldada pela liberdade, atitude e pelo espírito intemporal Harley-Davidson. Construída na Ucrânia, inspira-se na cultura denim, nas proporções clássicas de chopper e na atmosfera da estrada aberta.",
            "ru": "True Religion — американский кастом, построенный вокруг свободы, характера и вневременного духа Harley-Davidson. Проект создан в Украине и опирается на деним-культуру, классические пропорции чоппера и атмосферу открытой дороги.",
            "uk": "True Religion — американський кастом, побудований навколо свободи, характеру та позачасового духу Harley-Davidson. Проєкт створено в Україні з опорою на денім-культуру, класичні пропорції чопера та атмосферу відкритої дороги.",
        },
    },
}

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
    "cocktail",
    "fetish",
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
    "cocktail": {
        "name": "Cocktail",
        "image": "/photos/projects/cocktail-2400.jpg",
        "dims": (2400, 1600),
        "copy": {
            "en": "Cocktail is a 2008 Harley-Davidson Street Glide FLHX transformed into a full custom bagger in Kharkiv in 2013. A 26-inch front wheel, chromed Twin Cam 96, Legend Air Ride and onboard Sony Marine audio define the build.",
            "pt": "A Cocktail é uma Harley-Davidson Street Glide FLHX de 2008 transformada num bagger full custom em Kharkiv, em 2013. Uma roda dianteira de 26 polegadas, o Twin Cam 96 cromado, Legend Air Ride e áudio Sony Marine a bordo definem a construção.",
            "ru": "Cocktail — Harley-Davidson Street Glide FLHX 2008 года, превращённый в Харькове в 2013-м в полноценный кастом-бэггер. Проект определяют 26-дюймовое переднее колесо, хромированный Twin Cam 96, Legend Air Ride и бортовая аудиосистема Sony Marine.",
            "uk": "Cocktail — Harley-Davidson Street Glide FLHX 2008 року, перетворений у Харкові 2013-го на повноцінний кастом-беггер. Проєкт визначають 26-дюймове переднє колесо, хромований Twin Cam 96, Legend Air Ride і бортова аудіосистема Sony Marine.",
        },
    },
    "fetish": {
        "name": "Fetish",
        "image": "/photos/projects/fetish-2400.jpg",
        "dims": (2400, 1501),
        "copy": {
            "en": "Fetish is a 2013 full custom chopper built on a Harley-Davidson Rocker C. Air ride, a B-17 fork, a 26-inch solid front wheel and ZEX nitrous helped make it the first Ukrainian custom entered in the AMD World Championship.",
            "pt": "A Fetish é uma chopper full custom de 2013 construída sobre uma Harley-Davidson Rocker C. Air ride, forquilha B-17, roda dianteira maciça de 26 polegadas e nitro ZEX ajudaram a torná-la no primeiro custom ucraniano inscrito no Mundial AMD.",
            "ru": "Fetish — полноценно кастомный чоппер 2013 года на базе Harley-Davidson Rocker C. Пневмоподвеска, вилка B-17, цельное 26-дюймовое переднее колесо и закись ZEX помогли ему стать первым украинским кастомом, заявленным на чемпионат мира AMD.",
            "uk": "Fetish — повністю кастомний чопер 2013 року на базі Harley-Davidson Rocker C. Пневмопідвіска, вилка B-17, суцільне 26-дюймове переднє колесо й закис ZEX допомогли йому стати першим українським кастомом, заявленим на чемпіонат світу AMD.",
        },
    },
}

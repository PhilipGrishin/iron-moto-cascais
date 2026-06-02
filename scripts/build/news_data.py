"""
News section content: hub + individual articles.
Each article has full multilingual content (en, ru, uk, pt).

Article slug is keyed in NEWS_ARTICLES.
First article: "opens-new-workshop-in-cascais", published 2026-05-02.
"""

# ============================================================
# Hub /news/ — title + description + heading per language
# ============================================================

NEWS_HUB_META = {
    "en": {
        "title": "News — Iron Custom Motors Workshop in Cascais",
        "description": "Latest news from Iron Custom Motors workshop in Cascais — openings, events, custom builds, community rides and announcements from our motorcycle workshop in Greater Lisbon.",
    },
    "ru": {
        "title": "Новости — мастерская Iron Custom Motors в Кашкайше",
        "description": "Свежие новости мастерской Iron Custom Motors в Кашкайше — открытия, события, кастом-сборки, мото-встречи и анонсы из нашей мотомастерской в Большом Лиссабоне.",
    },
    "uk": {
        "title": "Новини — майстерня Iron Custom Motors у Кашкайші",
        "description": "Свіжі новини майстерні Iron Custom Motors у Кашкайші — відкриття, події, кастом-збірки, мото-зустрічі та анонси з нашої мотомайстерні у Великому Лісабоні.",
    },
    "pt": {
        "title": "Notícias — Oficina Iron Custom Motors em Cascais",
        "description": "Notícias da oficina Iron Custom Motors em Cascais — aberturas, eventos, builds custom, encontros de motociclistas e anúncios da nossa oficina na Grande Lisboa.",
    },
}

NEWS_HUB_BODY = {
    "en": {
        "eyebrow": "News · Iron Custom Motors",
        "h1": "Latest from <span class=\"accent\">the workshop.</span>",
        "sub": "Openings, events, custom builds, community rides — what's happening at Iron Custom Motors in Cascais.",
        "breadHome": "Home",
        "h1Crumb": "News",
        "readMore": "Read the story →",
        "noPosts": "More stories coming soon.",
    },
    "ru": {
        "eyebrow": "Новости · Iron Custom Motors",
        "h1": "Что нового<br/>в <span class=\"accent\">мастерской.</span>",
        "sub": "Открытия, события, кастом-сборки, мото-встречи — что происходит в Iron Custom Motors в Кашкайше.",
        "breadHome": "Главная",
        "h1Crumb": "Новости",
        "readMore": "Читать →",
        "noPosts": "Скоро ещё материалы.",
    },
    "uk": {
        "eyebrow": "Новини · Iron Custom Motors",
        "h1": "Що нового<br/>у <span class=\"accent\">майстерні.</span>",
        "sub": "Відкриття, події, кастом-збірки, мото-зустрічі — що відбувається в Iron Custom Motors у Кашкайші.",
        "breadHome": "Головна",
        "h1Crumb": "Новини",
        "readMore": "Читати →",
        "noPosts": "Скоро ще матеріали.",
    },
    "pt": {
        "eyebrow": "Notícias · Iron Custom Motors",
        "h1": "As novidades<br/>da <span class=\"accent\">oficina.</span>",
        "sub": "Aberturas, eventos, builds custom, encontros — o que está a acontecer na Iron Custom Motors em Cascais.",
        "breadHome": "Início",
        "h1Crumb": "Notícias",
        "readMore": "Ler a história →",
        "noPosts": "Mais histórias em breve.",
    },
}

# ============================================================
# Article 1: "Iron Custom Motors opens a new workshop in Cascais"
# Published 2026-05-02
# ============================================================

ARTICLE_OPENING_META = {
    "en": {
        "title": "Iron Custom Motors Opens a New Workshop in Cascais | Premium Motorcycle Service in Portugal",
        "description": "Iron Custom Motors opens a new motorcycle workshop in Cascais, Greater Lisbon. Premium service, tuning, custom projects, parts, a rider lounge and a growing motorcycle community in Portugal.",
        "excerpt": "Iron Custom Motors opens a new motorcycle workshop in Cascais, Greater Lisbon — bringing championship history, premium service standards, a rider lounge and a community-driven vision to Portugal.",
    },
    "ru": {
        "title": "Iron Custom Motors открывает мастерскую в Кашкайше | Премиальный мотосервис в Португалии",
        "description": "Iron Custom Motors открывает мотомастерскую в Кашкайше, Большой Лиссабон. Премиальный сервис, тюнинг, кастом-проекты, запчасти, лаунж для мотоциклистов и растущее мото-сообщество в Португалии.",
        "excerpt": "Iron Custom Motors открыл новую мотомастерскую в Кашкайше — привнося в Португалию чемпионскую историю, премиальные стандарты сервиса, лаунж для мотоциклистов и идею сильного сообщества.",
    },
    "uk": {
        "title": "Iron Custom Motors відкриває майстерню у Кашкайші | Преміальний мотосервіс у Португалії",
        "description": "Iron Custom Motors відкриває мотомайстерню у Кашкайші, Великий Лісабон. Преміальний сервіс, тюнінг, кастом-проєкти, запчастини, лаунж для мотоциклістів і зростаюча мото-спільнота у Португалії.",
        "excerpt": "Iron Custom Motors відкрив нову мотомайстерню у Кашкайші — привносячи в Португалію чемпіонську історію, преміальні стандарти сервісу, лаунж для мотоциклістів і ідею сильної спільноти.",
    },
    "pt": {
        "title": "Iron Custom Motors abre nova oficina em Cascais | Serviço Premium de Motos em Portugal",
        "description": "Iron Custom Motors abre uma nova oficina de motos em Cascais, Grande Lisboa. Serviço premium, tuning, projetos custom, peças, lounge para riders e uma comunidade de motociclistas em crescimento em Portugal.",
        "excerpt": "Iron Custom Motors abre uma nova oficina de motos em Cascais — trazendo para Portugal a sua história de campeonatos, padrões de serviço premium, um lounge para riders e uma visão construída sobre comunidade.",
    },
}

ARTICLE_OPENING_BODY = {
    "en": {
        "eyebrow": "News · 2 May 2026",
        "h1": "Iron Custom Motors opens a new workshop<br/>in <span class=\"accent\">Cascais.</span>",
        "lede": "Iron Custom Motors has opened a new motorcycle workshop in Cascais, Greater Lisbon, bringing to Portugal a brand with deep roots in custom culture, championship-winning projects, and years of hands-on engineering. The workshop focuses on premium motorcycle service, repair, upgrades, tuning, parts supply, and custom projects — while also creating a real meeting point for riders who want more than just a service appointment.",

        "s1.h2": "From a championship workshop to a new chapter",
        "s1.p1": "For Iron Custom Motors, this opening is much more than a new business address. It is the continuation of a long story that began in Kharkiv in 2010 and grew through years of workshop discipline, engineering ambition, and a deep love for motorcycles.",
        "s1.p2": "Over time, Iron Custom Motors became known not only for service and custom work, but also for projects that earned international recognition, world championship titles, and a place in modern custom motorcycle culture. That experience now arrives in Portugal with a clear mission: to build one of the most professional and respected motorcycle workshops in Cascais.",

        "s2.h2": "Why Portugal",
        "s2.p1": "The decision to open the new workshop in Portugal was natural. Portugal has a strong motorcycle culture, a beautiful riding environment, and a riding season that feels almost year-round compared with many other countries. The roads, the coastline, the climate, and the lifestyle all create the perfect setting for a workshop that wants to work closely with real riders.",
        "s2.p2": "Cascais and the Greater Lisbon area bring together local riders, international residents, and a large expat community that values quality, transparency, and strong service standards. For Iron Custom Motors, that combination made Portugal the obvious place for the next chapter.",

        "s3.h2": "Premium motorcycle service at the core",
        "s3.p1": "The new Iron Custom Motors workshop in Cascais is built first and foremost around quality motorcycle service. From scheduled maintenance and diagnostics to repair work, parts sourcing, upgrades, deep tuning, and custom builds, the goal is to offer a professional motorcycle service that riders can trust.",
        "s3.p2": "The workshop is built for those who care about how their motorcycle is maintained, how parts are selected, how work is explained, and how the final result feels on the road. Even when the task is routine service or a practical upgrade, the same standards apply: attention to detail, engineering logic, clean execution, and respect for the motorcycle as both a machine and a personal statement.",

        "s4.h2": "On the lift: every brand, every level of work",
        "s4.p1": "We service the full multi-brand lineup — BMW Motorrad, Harley-Davidson, Ducati, Triumph, KTM, Honda, Yamaha, Kawasaki, Suzuki, Aprilia, MV Agusta, Indian. From a 25,000 km major service to brake fluid bleed, from carb sync to ECU re-flash on an aftermarket exhaust — it's all under one roof.",
        "s4.p2": "We also have brand-specific diagnostic equipment and tooling, plus authorized-dealer access to the major international parts and aftermarket catalogs. That combination lets us do work properly, source exactly what your bike needs, and stand behind the result.",

        "s5.h2": "More than a service bay — a rider lounge",
        "s5.p1": "One of the most important parts of the new space is the rider lounge area. This is a large, carefully designed client zone where visitors can drink coffee, slow down, talk about motorcycles, and spend time in an atmosphere built around real motorcycle culture.",
        "s5.p2": "The lounge includes championship motorcycles, trophies, guitars, books, magazines, memorabilia, and objects that reflect the history and identity of Iron Custom Motors. It is a space that gives the workshop a different kind of meaning: not just a place to fix a bike, but a place to belong.",

        "s6.h2": "Building a motorcycle community in Cascais",
        "s6.p1": "Iron Custom Motors wants to build not only a premium motorcycle workshop in Cascais, but also a real motorcycle community around the project. Future plans include rider gatherings, presentations of new builds, community events, social evenings, shared rides, and road activities that bring people together around motorcycles and the lifestyle that surrounds them.",
        "s6.p2": "The tone is simple: riders are welcome. Visitors can come by, have coffee, discover the space, see the lounge, and get to know the team. The workshop should feel like a professional facility with human energy around it — a place where service quality and rider culture exist in the same environment.",

        "s7.h2": "The long-term vision",
        "s7.p1": "The long-term goal is clear. Iron Custom Motors wants to be one of the best professional motorcycle service centers in Cascais and a respected name for riders across Greater Lisbon. Not by trying to be everything for everyone, but by staying focused on what matters most: quality motorcycle service, strong workshop standards, honest communication, parts and upgrade expertise, and a motorcycle culture that people genuinely want to be part of.",
        "s7.p2": "The opening of the new workshop in Cascais marks the beginning of that work. For riders in Portugal, it means a new destination for premium motorcycle service, tuning, custom work, and everyday workshop support. For Iron Custom Motors, it is the next important step in a story that continues to grow.",

        "ctaEyebrow": "Visit us",
        "ctaTitle": "Coffee is ready. The lounge is open.",
        "ctaText": "If you ride, care about motorcycles, or simply want to discover the new workshop — you are welcome to come by during business hours. WhatsApp the team if you want to book a service while you're here.",

        "breadHome": "Home",
        "breadNews": "News",
        "h1Crumb": "Iron Custom Motors opens in Cascais",
        "btnWA": "WhatsApp us",
        "btnSend": "Send a request",
        "btnBack": "Back to news",

        "img1.alt": "Iron Custom Motors team and friends at the opening of the new workshop in Cascais, with a custom motorcycle in front and championship bikes in the background.",
        "img1.cap": "Opening day at the new Iron Custom Motors workshop in Cascais, 2 May 2026.",
        "img2.alt": "Riders gathered outside the Iron Custom Motors workshop in Cascais on opening day, motorcycles parked on cobblestones.",
        "img2.cap": "Outside the workshop on opening day — riders, motorcycles, conversation.",
        "img3.alt": "Inside the Iron Custom Motors workshop in Cascais — custom motorcycles, classic builds and a Liqui Moly partner banner.",
        "img3.cap": "Inside the new workshop floor — custom builds and classic motorcycles in service.",
        "img4.alt": "Royal Enfield motorcycle on an orange hydraulic lift inside Iron Custom Motors workshop in Cascais, ready for service.",
        "img4.cap": "Day one on the lift — service standards on real customer bikes.",

        "publishedISO": "2026-05-02",
        "publishedLabel": "Published 2 May 2026",
    },
    "ru": {
        "eyebrow": "Новости · 2 мая 2026",
        "h1": "Iron Custom Motors открывает мастерскую<br/>в <span class=\"accent\">Кашкайше.</span>",
        "lede": "Iron Custom Motors открыл новую мотомастерскую в Кашкайше, Большой Лиссабон, привнеся в Португалию бренд с глубокими корнями в кастом-культуре, проектами-чемпионами и годами инженерной практики. Мастерская сфокусирована на премиальном мотосервисе, ремонте, апгрейдах, тюнинге, поставке запчастей и кастом-проектах — и одновременно становится точкой притяжения для мотоциклистов, которым нужно больше, чем просто запись на ТО.",

        "s1.h2": "От чемпионской мастерской — к новой главе",
        "s1.p1": "Для Iron Custom Motors это открытие — гораздо больше, чем просто новый адрес. Это продолжение длинной истории, которая началась в Харькове в 2010 году и выросла через годы мастерской дисциплины, инженерных амбиций и глубокой любви к мотоциклам.",
        "s1.p2": "Со временем Iron Custom Motors стал известен не только сервисом и кастом-работами, но и проектами, получившими международное признание, мировые чемпионские титулы и место в современной кастом-культуре. Этот опыт теперь приходит в Португалию с ясной задачей: построить одну из самых профессиональных и уважаемых мотомастерских в Кашкайше.",

        "s2.h2": "Почему Португалия",
        "s2.p1": "Решение открыть мастерскую в Португалии было естественным. Здесь сильная мотокультура, красивая среда для езды и сезон, который ощущается почти круглогодичным по сравнению с большинством других стран. Дороги, побережье, климат и образ жизни — всё это идеальная среда для мастерской, которая хочет работать близко с настоящими байкерами.",
        "s2.p2": "Кашкайш и Большой Лиссабон объединяют местных мотоциклистов, иностранных резидентов и большое экспат-сообщество, которое ценит качество, прозрачность и сильные стандарты сервиса. Для Iron Custom Motors эта комбинация сделала Португалию очевидным местом для следующей главы.",

        "s3.h2": "Премиальный мотосервис — в основе",
        "s3.p1": "Новая мастерская Iron Custom Motors в Кашкайше построена прежде всего вокруг качественного мотосервиса. От планового ТО и диагностики до ремонта, поставки запчастей, апгрейдов, глубокого тюнинга и кастом-сборок — задача предложить профессиональный сервис, которому байкеры могут доверять.",
        "s3.p2": "Мастерская сделана для тех, кому важно, как обслуживают мотоцикл, как подбирают запчасти, как объясняют работу и как итог ощущается на дороге. Даже когда задача — рутинное ТО или практичный апгрейд, действуют те же стандарты: внимание к деталям, инженерная логика, аккуратность исполнения и уважение к мотоциклу как к технике и как к личному выбору.",

        "s4.h2": "На подъёмнике — любой бренд, любой уровень работ",
        "s4.p1": "Мы работаем с полным мульти-брендовым спектром — BMW Motorrad, Harley-Davidson, Ducati, Triumph, KTM, Honda, Yamaha, Kawasaki, Suzuki, Aprilia, MV Agusta, Indian. От ТО на 25 000 км до прокачки тормозов, от синхронизации карбюраторов до перепрошивки ЭБУ под афтермаркет-выхлоп — всё под одной крышей.",
        "s4.p2": "У нас также есть brand-специфичное диагностическое оборудование и инструмент, плюс авторизованный дилерский доступ к крупным международным каталогам запчастей и афтермаркета. Эта комбинация позволяет делать работу корректно, заказывать именно то, что нужно вашему мотоциклу, и нести ответственность за результат.",

        "s5.h2": "Не просто сервисная зона — лаунж для мотоциклистов",
        "s5.p1": "Одна из самых важных частей нового пространства — лаунж-зона для гостей. Это большая, специально продуманная клиентская зона, где можно выпить кофе, замедлиться, поговорить о мотоциклах и провести время в атмосфере, построенной вокруг настоящей мото-культуры.",
        "s5.p2": "В лаундже стоят чемпионские мотоциклы, кубки, гитары, книги, журналы, памятные вещи — всё, что отражает историю и характер Iron Custom Motors. Это пространство даёт мастерской другой смысл: не просто место, куда привозят чинить мотоцикл, а место, в которое хочется возвращаться.",

        "s6.h2": "Строим мото-сообщество в Кашкайше",
        "s6.p1": "Iron Custom Motors хочет построить не только премиальную мотомастерскую в Кашкайше, но и настоящее мото-сообщество вокруг проекта. В планах — встречи байкеров, презентации новых проектов, community-события, вечера, совместные выезды и road-активности, которые объединяют людей вокруг мотоциклов и стиля жизни, который их окружает.",
        "s6.p2": "Тон простой: байкеры здесь желанные гости. Можно заехать, выпить кофе, посмотреть пространство, увидеть лаунж и познакомиться с командой. Мастерская должна ощущаться как профессиональная площадка с живой энергией вокруг — где качество сервиса и культура райдеров живут в одной среде.",

        "s7.h2": "Долгосрочное видение",
        "s7.p1": "Долгосрочная цель — ясна. Iron Custom Motors хочет быть одним из лучших профессиональных мотосервисов в Кашкайше и уважаемым именем для байкеров по всему Большому Лиссабону. Не пытаясь быть всем для всех, а оставаясь сфокусированным на главном: качественный мотосервис, сильные стандарты мастерской, честная коммуникация, экспертиза по запчастям и апгрейдам и мото-культура, частью которой действительно хочется быть.",
        "s7.p2": "Открытие новой мастерской в Кашкайше — начало этой работы. Для байкеров в Португалии это новая точка для премиального мотосервиса, тюнинга, кастом-работ и ежедневной поддержки. Для Iron Custom Motors — следующий важный шаг в истории, которая продолжает расти.",

        "ctaEyebrow": "Заезжайте",
        "ctaTitle": "Кофе готов. Лаунж открыт.",
        "ctaText": "Если вы байкер, любите мотоциклы или просто хотите познакомиться с мастерской — заезжайте в рабочее время. В WhatsApp напишите команде, если хотите параллельно записаться на сервис.",

        "breadHome": "Главная",
        "breadNews": "Новости",
        "h1Crumb": "Iron Custom Motors открылся в Кашкайше",
        "btnWA": "WhatsApp",
        "btnSend": "Отправить заявку",
        "btnBack": "Ко всем новостям",

        "img1.alt": "Команда и друзья Iron Custom Motors на открытии новой мастерской в Кашкайше, кастом-мотоцикл впереди, чемпионские байки на заднем плане.",
        "img1.cap": "День открытия новой мастерской Iron Custom Motors в Кашкайше, 2 мая 2026.",
        "img2.alt": "Байкеры у входа в мастерскую Iron Custom Motors в Кашкайше в день открытия, мотоциклы на брусчатке.",
        "img2.cap": "У мастерской в день открытия — байкеры, мотоциклы, разговоры.",
        "img3.alt": "Внутри мастерской Iron Custom Motors в Кашкайше — кастом-мотоциклы, классика и партнёрский баннер Liqui Moly.",
        "img3.cap": "Внутри нового сервисного цеха — кастом-сборки и классика в работе.",
        "img4.alt": "Мотоцикл Royal Enfield на оранжевом гидравлическом подъёмнике в мастерской Iron Custom Motors в Кашкайше, готов к сервису.",
        "img4.cap": "Первый день на подъёмнике — стандарты сервиса на реальных клиентских мотоциклах.",

        "publishedISO": "2026-05-02",
        "publishedLabel": "Опубликовано 2 мая 2026",
    },
    "uk": {
        "eyebrow": "Новини · 2 травня 2026",
        "h1": "Iron Custom Motors відкриває майстерню<br/>у <span class=\"accent\">Кашкайші.</span>",
        "lede": "Iron Custom Motors відкрив нову мотомайстерню в Кашкайші, Великий Лісабон, привнісши в Португалію бренд із глибоким корінням у кастом-культурі, проєктами-чемпіонами та роками інженерної практики. Майстерня сфокусована на преміальному мотосервісі, ремонті, апґрейдах, тюнінгу, постачанні запчастин і кастом-проєктах — а також стає точкою тяжіння для мотоциклістів, яким потрібно більше, ніж просто запис на ТО.",

        "s1.h2": "Від чемпіонської майстерні — до нової глави",
        "s1.p1": "Для Iron Custom Motors це відкриття — набагато більше, ніж просто нова адреса. Це продовження довгої історії, що почалася у Харкові 2010 року й виросла через роки майстерної дисципліни, інженерних амбіцій і глибокої любові до мотоциклів.",
        "s1.p2": "З часом Iron Custom Motors став відомий не лише сервісом і кастом-роботами, а й проєктами, що отримали міжнародне визнання, світові чемпіонські титули й місце у сучасній кастом-культурі. Цей досвід тепер приходить у Португалію з ясною місією: побудувати одну з найпрофесійніших і найповажніших мотомайстерень у Кашкайші.",

        "s2.h2": "Чому Португалія",
        "s2.p1": "Рішення відкрити майстерню в Португалії було природним. Тут сильна мото-культура, красива середовище для їзди й сезон, що відчувається майже цілорічним порівняно з більшістю інших країн. Дороги, узбережжя, клімат і стиль життя — усе це ідеальне середовище для майстерні, яка хоче працювати близько з реальними байкерами.",
        "s2.p2": "Кашкайш і Великий Лісабон об'єднують місцевих мотоциклістів, іноземних резидентів і велику експат-спільноту, яка цінує якість, прозорість і сильні стандарти сервісу. Для Iron Custom Motors ця комбінація зробила Португалію очевидним місцем для наступної глави.",

        "s3.h2": "Преміальний мотосервіс — в основі",
        "s3.p1": "Нова майстерня Iron Custom Motors у Кашкайші побудована насамперед навколо якісного мотосервісу. Від планового ТО і діагностики до ремонту, постачання запчастин, апґрейдів, глибокого тюнінгу й кастом-збірок — задача запропонувати професійний сервіс, якому байкери можуть довіряти.",
        "s3.p2": "Майстерня зроблена для тих, кому важливо, як обслуговують мотоцикл, як підбирають запчастини, як пояснюють роботу і як результат відчувається на дорозі. Навіть коли задача — рутинне ТО або практичний апґрейд, діють ті самі стандарти: увага до деталей, інженерна логіка, акуратність виконання і повага до мотоцикла як до техніки і як до особистого вибору.",

        "s4.h2": "На підйомнику — будь-який бренд, будь-який рівень робіт",
        "s4.p1": "Працюємо з повним мульти-брендовим спектром — BMW Motorrad, Harley-Davidson, Ducati, Triumph, KTM, Honda, Yamaha, Kawasaki, Suzuki, Aprilia, MV Agusta, Indian. Від ТО на 25 000 км до прокачки гальм, від синхронізації карбюраторів до перепрошивки ЕБУ під афтермаркет-вихлоп — усе під одним дахом.",
        "s4.p2": "У нас також є brand-специфічне діагностичне обладнання та інструмент, плюс авторизований дилерський доступ до великих міжнародних каталогів запчастин і афтермаркету. Ця комбінація дозволяє робити роботу коректно, замовляти саме те, що потрібно вашому мотоциклу, і нести відповідальність за результат.",

        "s5.h2": "Не лише сервісна зона — лаунж для мотоциклістів",
        "s5.p1": "Одна з найважливіших частин нового простору — лаунж-зона для гостей. Це велика, спеціально продумана клієнтська зона, де можна випити кави, уповільнитись, поговорити про мотоцикли й провести час в атмосфері, побудованій навколо справжньої мото-культури.",
        "s5.p2": "У лаунжі стоять чемпіонські мотоцикли, кубки, гітари, книги, журнали, пам'ятні речі — усе, що відображає історію та характер Iron Custom Motors. Цей простір дає майстерні інший сенс: не просто місце, куди привозять чинити мотоцикл, а місце, до якого хочеться повертатись.",

        "s6.h2": "Будуємо мото-спільноту у Кашкайші",
        "s6.p1": "Iron Custom Motors хоче побудувати не лише преміальну мотомайстерню в Кашкайші, а й справжню мото-спільноту навколо проєкту. У планах — зустрічі байкерів, презентації нових проєктів, community-події, вечори, спільні виїзди і road-активності, що об'єднують людей навколо мотоциклів і стилю життя, який їх оточує.",
        "s6.p2": "Тон простий: байкери тут — бажані гості. Можна заїхати, випити кави, подивитися простір, побачити лаунж і познайомитися з командою. Майстерня має відчуватись як професійна площадка з живою енергією навколо — де якість сервісу і культура райдерів живуть в одному середовищі.",

        "s7.h2": "Довгострокове бачення",
        "s7.p1": "Довгострокова мета — ясна. Iron Custom Motors хоче бути одним із найкращих професійних мотосервісів у Кашкайші і шанованим іменем для байкерів по всьому Великому Лісабону. Не намагаючись бути всім для всіх, а залишаючись сфокусованим на головному: якісний мотосервіс, сильні стандарти майстерні, чесна комунікація, експертиза із запчастин і апґрейдів і мото-культура, частиною якої справді хочеться бути.",
        "s7.p2": "Відкриття нової майстерні у Кашкайші — початок цієї роботи. Для байкерів у Португалії це нова точка для преміального мотосервісу, тюнінгу, кастом-робіт і щоденної підтримки. Для Iron Custom Motors — наступний важливий крок в історії, що продовжує зростати.",

        "ctaEyebrow": "Заїжджайте",
        "ctaTitle": "Кава готова. Лаунж відкритий.",
        "ctaText": "Якщо ви байкер, любите мотоцикли або просто хочете познайомитись із майстернею — заїжджайте у робочий час. У WhatsApp напишіть команді, якщо хочете паралельно записатись на сервіс.",

        "breadHome": "Головна",
        "breadNews": "Новини",
        "h1Crumb": "Iron Custom Motors відкрився у Кашкайші",
        "btnWA": "WhatsApp",
        "btnSend": "Надіслати заявку",
        "btnBack": "До всіх новин",

        "img1.alt": "Команда і друзі Iron Custom Motors на відкритті нової майстерні у Кашкайші, кастом-мотоцикл попереду, чемпіонські байки на задньому плані.",
        "img1.cap": "День відкриття нової майстерні Iron Custom Motors у Кашкайші, 2 травня 2026.",
        "img2.alt": "Байкери біля входу в майстерню Iron Custom Motors у Кашкайші у день відкриття, мотоцикли на бруківці.",
        "img2.cap": "Біля майстерні у день відкриття — байкери, мотоцикли, розмови.",
        "img3.alt": "Усередині майстерні Iron Custom Motors у Кашкайші — кастом-мотоцикли, класика і партнерський банер Liqui Moly.",
        "img3.cap": "Усередині нового сервісного цеху — кастом-збірки і класика у роботі.",
        "img4.alt": "Мотоцикл Royal Enfield на помаранчевому гідравлічному підйомнику в майстерні Iron Custom Motors у Кашкайші, готовий до сервісу.",
        "img4.cap": "Перший день на підйомнику — стандарти сервісу на реальних клієнтських мотоциклах.",

        "publishedISO": "2026-05-02",
        "publishedLabel": "Опубліковано 2 травня 2026",
    },
    "pt": {
        "eyebrow": "Notícias · 2 de maio 2026",
        "h1": "Iron Custom Motors abre nova oficina<br/>em <span class=\"accent\">Cascais.</span>",
        "lede": "A Iron Custom Motors abriu uma nova oficina de motos em Cascais, Grande Lisboa, trazendo para Portugal uma marca com raízes profundas na cultura custom, projetos premiados em campeonatos e anos de engenharia prática. A oficina foca-se em serviço premium, reparação, upgrades, tuning, fornecimento de peças e projetos custom — e cria também um ponto de encontro real para riders que querem mais do que apenas marcar serviço.",

        "s1.h2": "De uma oficina campeã para um novo capítulo",
        "s1.p1": "Para a Iron Custom Motors, esta abertura é muito mais do que uma morada nova. É a continuação de uma longa história que começou em Kharkiv em 2010 e cresceu através de anos de disciplina de oficina, ambição de engenharia e amor profundo por motas.",
        "s1.p2": "Com o tempo, a Iron Custom Motors ficou conhecida não só pelo serviço e trabalho custom, mas também por projetos que ganharam reconhecimento internacional, títulos de campeonato mundial e um lugar na cultura custom moderna. Essa experiência chega agora a Portugal com uma missão clara: construir uma das oficinas de motos mais profissionais e respeitadas de Cascais.",

        "s2.h2": "Porquê Portugal",
        "s2.p1": "A decisão de abrir a oficina em Portugal foi natural. Portugal tem uma forte cultura motociclista, um ambiente bonito para andar e uma temporada quase de ano inteiro comparada com muitos outros países. As estradas, a costa, o clima e o estilo de vida criam o cenário perfeito para uma oficina que quer trabalhar próximo de riders reais.",
        "s2.p2": "Cascais e a Grande Lisboa juntam riders locais, residentes internacionais e uma grande comunidade expat que valoriza qualidade, transparência e padrões fortes de serviço. Para a Iron Custom Motors, essa combinação fez de Portugal o lugar óbvio para o próximo capítulo.",

        "s3.h2": "Serviço premium de motos no centro",
        "s3.p1": "A nova oficina Iron Custom Motors em Cascais está construída acima de tudo em torno de serviço de motos de qualidade. Da manutenção programada e diagnóstico ao trabalho de reparação, sourcing de peças, upgrades, tuning profundo e builds custom — o objetivo é oferecer um serviço de motos profissional em que os riders podem confiar.",
        "s3.p2": "A oficina foi construída para quem se importa com como a moto é mantida, como as peças são escolhidas, como o trabalho é explicado e como o resultado final se sente na estrada. Mesmo quando a tarefa é serviço de rotina ou um upgrade prático, aplicam-se os mesmos padrões: atenção ao detalhe, lógica de engenharia, execução limpa e respeito pela moto enquanto máquina e enquanto escolha pessoal.",

        "s4.h2": "No elevador — qualquer marca, qualquer nível de trabalho",
        "s4.p1": "Trabalhamos com todo o leque multi-marca — BMW Motorrad, Harley-Davidson, Ducati, Triumph, KTM, Honda, Yamaha, Kawasaki, Suzuki, Aprilia, MV Agusta, Indian. De um serviço grande de 25 000 km à sangria do fluido de travões, da sincronização de carburadores ao remapeamento ECU para um escape aftermarket — tudo sob o mesmo teto.",
        "s4.p2": "Temos também equipamento de diagnóstico e ferramenta específicos por marca, mais acesso de revendedor autorizado aos principais catálogos internacionais de peças e aftermarket. Esta combinação permite fazer o trabalho como deve ser, encomendar exatamente o que a sua moto precisa e responder pelo resultado.",

        "s5.h2": "Mais do que uma baia de serviço — um rider lounge",
        "s5.p1": "Uma das partes mais importantes do novo espaço é a área de rider lounge. É uma zona de cliente grande e cuidadosamente desenhada, onde os visitantes podem tomar café, abrandar, falar de motas e passar tempo numa atmosfera construída em torno de cultura motociclista real.",
        "s5.p2": "O lounge inclui motas campeãs, troféus, guitarras, livros, revistas, memorabilia e objetos que refletem a história e identidade da Iron Custom Motors. É um espaço que dá à oficina um significado diferente: não apenas um sítio para arranjar a moto, mas um sítio a que se quer pertencer.",

        "s6.h2": "A construir comunidade motociclista em Cascais",
        "s6.p1": "A Iron Custom Motors quer construir não só uma oficina premium em Cascais, mas também uma comunidade motociclista real à volta do projeto. Planos futuros incluem encontros de riders, apresentações de novas builds, eventos de comunidade, serões sociais, saídas conjuntas e atividades de estrada que juntam pessoas à volta das motas e do estilo de vida que as rodeia.",
        "s6.p2": "O tom é simples: riders são bem-vindos. Quem quiser pode passar, tomar café, descobrir o espaço, ver o lounge e conhecer a equipa. A oficina deve sentir-se como uma instalação profissional com energia humana à volta — onde qualidade de serviço e cultura de rider existem no mesmo ambiente.",

        "s7.h2": "A visão de longo prazo",
        "s7.p1": "O objetivo de longo prazo é claro. A Iron Custom Motors quer ser um dos melhores centros profissionais de serviço de motos em Cascais e um nome respeitado pelos riders de toda a Grande Lisboa. Não a tentar ser tudo para todos, mas mantendo o foco no que realmente importa: serviço de motos de qualidade, padrões fortes de oficina, comunicação honesta, expertise em peças e upgrades e uma cultura motociclista de que as pessoas genuinamente querem fazer parte.",
        "s7.p2": "A abertura da nova oficina em Cascais marca o início desse trabalho. Para os riders em Portugal, significa um novo destino para serviço premium, tuning, trabalho custom e suporte de oficina do dia-a-dia. Para a Iron Custom Motors, é o próximo passo importante numa história que continua a crescer.",

        "ctaEyebrow": "Visite-nos",
        "ctaTitle": "O café está pronto. O lounge está aberto.",
        "ctaText": "Se anda de mota, gosta de motos ou simplesmente quer descobrir a nova oficina — passe em horário comercial. Mande WhatsApp à equipa se quiser marcar serviço enquanto está cá.",

        "breadHome": "Início",
        "breadNews": "Notícias",
        "h1Crumb": "Iron Custom Motors abre em Cascais",
        "btnWA": "WhatsApp",
        "btnSend": "Enviar pedido",
        "btnBack": "Voltar às notícias",

        "img1.alt": "Equipa e amigos da Iron Custom Motors na abertura da nova oficina em Cascais, com uma mota custom em primeiro plano e motas campeãs ao fundo.",
        "img1.cap": "Dia de abertura da nova oficina Iron Custom Motors em Cascais, 2 de maio de 2026.",
        "img2.alt": "Riders à porta da oficina Iron Custom Motors em Cascais no dia da abertura, motas estacionadas em calçada portuguesa.",
        "img2.cap": "À porta da oficina no dia da abertura — riders, motas e conversa.",
        "img3.alt": "Dentro da oficina Iron Custom Motors em Cascais — motas custom, builds clássicas e um banner do parceiro Liqui Moly.",
        "img3.cap": "Dentro do novo espaço de oficina — builds custom e clássicas em serviço.",
        "img4.alt": "Moto Royal Enfield sobre um elevador hidráulico cor de laranja dentro da oficina Iron Custom Motors em Cascais, pronta para serviço.",
        "img4.cap": "Primeiro dia no elevador — padrões de serviço em motas reais de cliente.",

        "publishedISO": "2026-05-02",
        "publishedLabel": "Publicado a 2 de maio de 2026",
    },
}

# ============================================================
# Article 2: "Iron Custom Motors at Lisbon Motorcycle Film Fest 2026 with Beckman"
# Published 2026-05-23
# ============================================================

ARTICLE_LMFF_META = {
    "en": {
        "title": "Iron Custom Motors at Lisbon Motorcycle Film Fest 2026 with Beckman",
        "description": "On 23 May 2026, Iron Custom Motors joins Lisbon Motorcycle Film Fest with Beckman — the world champion cafe racer that defined our international custom motorcycle history.",
        "excerpt": "Iron Custom Motors takes part in Lisbon Motorcycle Film Fest 2026 with the championship-winning Beckman custom motorcycle — from Kharkiv to Cascais, bringing world-class custom history and premium motorcycle service to Portugal.",
    },
    "ru": {
        "title": "Iron Custom Motors на Lisbon Motorcycle Film Fest 2026 с мотоциклом Beckman",
        "description": "23 мая 2026 Iron Custom Motors участвует в Lisbon Motorcycle Film Fest с мотоциклом Beckman — чемпионом мира в классе Cafe Racer, определившим нашу международную кастом-историю.",
        "excerpt": "Iron Custom Motors на Lisbon Motorcycle Film Fest 2026 с чемпионским кастом-мотоциклом Beckman — из Харькова в Кашкайш, привнося в Португалию кастом-историю мирового уровня и премиальный мотосервис.",
    },
    "uk": {
        "title": "Iron Custom Motors на Lisbon Motorcycle Film Fest 2026 з мотоциклом Beckman",
        "description": "23 травня 2026 Iron Custom Motors бере участь у Lisbon Motorcycle Film Fest з мотоциклом Beckman — чемпіоном світу в класі Cafe Racer, що визначив нашу міжнародну кастом-історію.",
        "excerpt": "Iron Custom Motors на Lisbon Motorcycle Film Fest 2026 з чемпіонським кастом-мотоциклом Beckman — з Харкова в Кашкайш, привносячи в Португалію кастом-історію світового рівня і преміальний мотосервіс.",
    },
    "pt": {
        "title": "Iron Custom Motors no Lisbon Motorcycle Film Fest 2026 com a Beckman",
        "description": "A 23 de maio de 2026, a Iron Custom Motors participa no Lisbon Motorcycle Film Fest com a Beckman — a cafe racer campeã mundial que definiu a nossa história internacional de motas custom.",
        "excerpt": "A Iron Custom Motors participa no Lisbon Motorcycle Film Fest 2026 com a Beckman, a moto custom campeã — de Kharkiv para Cascais, trazendo para Portugal história custom de nível mundial e serviço premium de motos.",
    },
}

ARTICLE_LMFF_BODY = {
    "en": {
        "eyebrow": "News · 23 May 2026",
        "h1": "Iron Custom Motors at Lisbon Motorcycle Film Fest 2026:<br/><span class=\"accent\">Beckman</span> at the center of the celebration.",
        "lede": "On 23 May 2026, Iron Custom Motors is proud to be part of the Lisbon Motorcycle Film Fest — one of the most distinctive motorcycle culture events in Portugal and a recognized meeting point for riders, builders, artists, filmmakers and everyone who lives the two-wheel lifestyle. This year's edition marks a symbolic moment for us: we are presenting one of the most important motorcycles in our brand's history — ICM Beckman.",

        "s1.h2": "Why this event matters to Iron Custom Motors",
        "s1.p1": "Our story began in Kharkiv in 2010. Over the years, Iron Custom Motors grew from a workshop built on passion, engineering, and craftsmanship into a brand recognized far beyond its home city. Our motorcycles and custom projects reached the international stage, won major titles, earned professional respect, and helped define our identity as a workshop that does not follow trends, but builds machines with their own language, purpose, and character.",
        "s1.p2": "Today, as Iron Custom Motors continues its new chapter in Portugal, taking part in the Lisbon Motorcycle Film Fest feels natural. Portugal has a strong and growing motorcycle culture, a climate that supports riding for most of the year, and a community that values both the practical and emotional side of motorcycling. This is exactly the kind of environment where our brand belongs — close to riders, close to real road culture, and close to the community that gives motorcycles their meaning.",
        "s1.p3": "The Lisbon Motorcycle Film Fest brings together motorcycle films, talks, exhibitions, rides, and custom culture in one program, creating a unique space where motorcycles are seen not only as machines, but also as part of creativity, design, freedom, and personal identity. For us, that makes the festival the right place to present a project that carries so much of our history and philosophy.",

        "s2.h2": "Beckman: a championship motorcycle in Lisbon",
        "s2.p1": "At the center of our participation is <a href=\"/projects/beckman/\">ICM Beckman</a> — one of the most significant motorcycles ever created by Iron Custom Motors. Beckman is not simply a custom build from our archive. It is one of the motorcycles that shaped our reputation internationally and proved that our engineering and design could compete at the highest level.",
        "s2.p2": "Beckman became World Champion in the Cafe Racer Class at the AMD World Championship of Custom Bike Building in 2016. Later, the project also received the Best Engineering award at MBE Verona. These distinctions made Beckman one of the strongest symbols of our workshop's philosophy: uncompromising craftsmanship, real engineering depth, and a custom motorcycle built as a complete statement, not just as a visual exercise.",
        "s2.p3": "One of the most remarkable features of Beckman is its hand-built three-cylinder engine, designed and manufactured as part of the project. Together with a large number of handmade parts and highly detailed finishing solutions, Beckman became a motorcycle that represents the deepest side of Iron Custom Motors — the side where design, fabrication, mechanics, and artistic discipline all come together in one machine.",

        "s3.h2": "From world championships to a new home in Cascais",
        "s3.p1": "For us, bringing Beckman to the Lisbon Motorcycle Film Fest is more than an exhibition appearance. It is a bridge between our history and our future. Iron Custom Motors now continues its work in Cascais, where we are building a premium motorcycle workshop focused on high-quality service, parts and consumables, upgrades and tuning, and custom and special projects.",
        "s3.p2": "We are also building something more than a workshop: a place where riders can meet, talk, drink coffee, and feel part of a real motorcycle community. That is why our presence at the festival matters. We are not arriving as strangers. We are arriving with a story, with championship motorcycles, with proven experience, and with a clear intention to become one of the strongest and most respected motorcycle workshops in the Cascais and Greater Lisbon area.",

        "s4.h2": "A motorcycle culture event that fits our philosophy",
        "s4.p1": "The spirit of the Lisbon Motorcycle Film Fest aligns closely with what Iron Custom Motors believes in. Motorcycles are not only about transport. They are about identity, craftsmanship, freedom, road stories, aesthetics, and community.",
        "s4.p2": "A festival that combines cinema, custom culture, exhibitions, conversations, and riders in one place reflects exactly the kind of atmosphere we want to help grow around our new workshop in Portugal. This is why we are especially happy to present Beckman in this context. It is a motorcycle that carries history, achievement, and emotion. It speaks to builders, riders, designers, and everyone who understands that a truly great motorcycle can become much more than the sum of its parts.",

        "s5.h2": "See you in Lisbon",
        "s5.p1": "We are proud to be part of Lisbon Motorcycle Film Fest 2026, and we are happy to welcome everyone who wants to discover Iron Custom Motors, see Beckman in person, and become part of this new chapter with us. If you are in Lisbon this weekend, come meet us, see one of the defining motorcycles in our history, and share this celebration of motorcycle culture together.",
        "s5.p2": "Iron Custom Motors is now in Portugal — and this is only the beginning.",

        "ctaEyebrow": "After the festival",
        "ctaTitle": "Visit the new workshop in Cascais.",
        "ctaText": "If you met us at the festival, or want to bring your motorcycle to a workshop that takes engineering seriously — come by Iron Custom Motors in São Domingos de Rana. WhatsApp the team to book a service or just say hello.",

        "breadHome": "Home",
        "breadNews": "News",
        "h1Crumb": "Iron Custom Motors at Lisbon Motorcycle Film Fest 2026",
        "btnWA": "WhatsApp us",
        "btnSend": "Send a request",
        "btnBack": "Back to news",

        "img1.alt": "Iron Custom Motors team standing next to the ICM Beckman cafe racer, a championship-winning custom motorcycle with hand-built three-cylinder engine, displayed at the Lisbon Motorcycle Film Fest 2026.",
        "img1.cap": "ICM Beckman on display at Lisbon Motorcycle Film Fest 2026 — World Champion in the Cafe Racer Class, AMD World Championship of Custom Bike Building 2016.",
        "img2.alt": "Iron Custom Motors team with friends and festival guests at the Lisbon Motorcycle Film Fest 2026.",
        "img2.cap": "Meeting riders, builders and friends at the festival in Lisbon.",
        "img3.alt": "Custom and classic BMW motorcycles on display at the Lisbon Motorcycle Film Fest 2026, with a matte black BMW boxer cafe racer in the foreground.",
        "img3.cap": "The festival floor — custom builds from across the Portuguese and international scene.",
        "img4.alt": "BMW R100 GS Paris-Dakar replica in Marlboro livery, displayed at the Lisbon Motorcycle Film Fest 2026.",
        "img4.cap": "BMW R100 GS Paris-Dakar replica — rally heritage on the festival floor.",
        "img5.alt": "BMW R18 Maverick concept custom motorcycle by Maverick, presented at the Lisbon Motorcycle Film Fest 2026.",
        "img5.cap": "BMW R18 'Maverick' concept — another standout build at the festival.",

        "publishedISO": "2026-05-23",
        "publishedLabel": "Published 23 May 2026",
    },
    "ru": {
        "eyebrow": "Новости · 23 мая 2026",
        "h1": "Iron Custom Motors на Lisbon Motorcycle Film Fest 2026:<br/><span class=\"accent\">Beckman</span> в центре события.",
        "lede": "23 мая 2026 Iron Custom Motors участвует в Lisbon Motorcycle Film Fest — одном из самых ярких событий мотокультуры в Португалии и узнаваемой точке встречи байкеров, билдеров, художников, кинематографистов и всех, кто живёт жизнью на двух колёсах. Эта программа становится символичной и для нас: мы показываем один из самых важных мотоциклов в истории бренда — ICM Beckman.",

        "s1.h2": "Почему это событие важно для Iron Custom Motors",
        "s1.p1": "Наша история началась в Харькове в 2010 году. За годы Iron Custom Motors из мастерской, построенной на страсти, инженерии и мастерстве, вырос в бренд, известный далеко за пределами своего города. Наши мотоциклы и кастом-проекты выходили на международную сцену, брали крупные титулы, получали профессиональное признание и сформировали нашу идентичность — мастерскую, которая не идёт за модой, а строит машины со своим языком, целью и характером.",
        "s1.p2": "Сегодня, открыв новую главу в Португалии, участие в Lisbon Motorcycle Film Fest для нас — естественный шаг. В Португалии сильная и растущая мотокультура, климат, позволяющий ездить большую часть года, и сообщество, которое ценит и практическую, и эмоциональную сторону мотожизни. Это именно та среда, к которой принадлежит наш бренд — рядом с байкерами, рядом с настоящей дорожной культурой и рядом с теми, кто придаёт мотоциклам смысл.",
        "s1.p3": "Lisbon Motorcycle Film Fest собирает в одной программе мото-кино, дискуссии, выставки, заезды и кастом-культуру — это уникальное пространство, где мотоцикл рассматривается не только как техника, но и как часть творчества, дизайна, свободы и личной идентичности. Для нас фестиваль — правильное место, чтобы показать проект, в котором сходится столько нашей истории и философии.",

        "s2.h2": "Beckman: чемпионский мотоцикл в Лиссабоне",
        "s2.p1": "В центре нашего участия — <a href=\"/projects/beckman/\">ICM Beckman</a>, один из самых значимых мотоциклов, когда-либо созданных Iron Custom Motors. Beckman — это не просто кастом-сборка из нашего архива. Это один из мотоциклов, сформировавших нашу международную репутацию и доказавших, что наша инженерия и дизайн способны конкурировать на самом высоком уровне.",
        "s2.p2": "Beckman стал чемпионом мира в классе Cafe Racer на AMD World Championship of Custom Bike Building в 2016 году. Позже проект также получил награду Best Engineering на MBE Verona. Эти достижения сделали Beckman одним из самых сильных символов философии мастерской: бескомпромиссное мастерство, реальная инженерная глубина и кастом-мотоцикл как цельное высказывание, а не просто визуальное упражнение.",
        "s2.p3": "Одна из самых заметных черт Beckman — собственный трёхцилиндровый двигатель ручной сборки, спроектированный и изготовленный в рамках проекта. Вместе с большим количеством hand-made-деталей и тщательной финишной отделкой Beckman стал мотоциклом, представляющим самую глубокую сторону Iron Custom Motors — ту, где дизайн, фабрикация, механика и художественная дисциплина сходятся в одной машине.",

        "s3.h2": "От чемпионатов мира — к новому дому в Кашкайше",
        "s3.p1": "Привезти Beckman на Lisbon Motorcycle Film Fest для нас — больше, чем выставочный показ. Это мост между нашей историей и нашим будущим. Iron Custom Motors теперь работает в Кашкайше, где мы строим премиальную мотомастерскую, сфокусированную на качественном сервисе, запчастях и расходниках, апгрейдах и тюнинге, кастом и специальных проектах.",
        "s3.p2": "А ещё мы строим нечто большее, чем просто мастерская: место, где байкеры могут встретиться, поговорить, выпить кофе и почувствовать себя частью настоящего мотосообщества. Поэтому наше присутствие на фестивале имеет значение. Мы приезжаем не как незнакомцы. Мы приезжаем с историей, с чемпионскими мотоциклами, с проверенным опытом и с ясной задачей — стать одной из самых сильных и уважаемых мотомастерских в Кашкайше и Большом Лиссабоне.",

        "s4.h2": "Событие мотокультуры, совпадающее с нашей философией",
        "s4.p1": "Дух Lisbon Motorcycle Film Fest близок к тому, во что верит Iron Custom Motors. Мотоцикл — это не только транспорт. Это идентичность, мастерство, свобода, дорожные истории, эстетика и сообщество.",
        "s4.p2": "Фестиваль, объединяющий кино, кастом-культуру, выставки, разговоры и байкеров в одном месте, точно отражает атмосферу, которую мы хотим помочь вырастить вокруг новой мастерской в Португалии. Поэтому мы особенно рады показать Beckman в этом контексте. Это мотоцикл, в котором есть история, достижение и эмоция. Он говорит с билдерами, байкерами, дизайнерами и всеми, кто понимает: по-настоящему великий мотоцикл может стать гораздо большим, чем сумма своих частей.",

        "s5.h2": "Увидимся в Лиссабоне",
        "s5.p1": "Мы гордимся тем, что участвуем в Lisbon Motorcycle Film Fest 2026, и рады встретить всех, кто хочет познакомиться с Iron Custom Motors, увидеть Beckman вживую и стать частью этой новой главы вместе с нами. Если вы в Лиссабоне в эти выходные — приходите познакомиться, посмотрите один из определяющих мотоциклов в нашей истории и разделите этот праздник мотокультуры вместе.",
        "s5.p2": "Iron Custom Motors теперь в Португалии — и это только начало.",

        "ctaEyebrow": "После фестиваля",
        "ctaTitle": "Загляните в новую мастерскую в Кашкайше.",
        "ctaText": "Если познакомились с нами на фестивале или хотите привезти мотоцикл в мастерскую, которая серьёзно относится к инженерии — заезжайте в Iron Custom Motors в São Domingos de Rana. Напишите команде в WhatsApp, чтобы записаться на сервис или просто поздороваться.",

        "breadHome": "Главная",
        "breadNews": "Новости",
        "h1Crumb": "Iron Custom Motors на Lisbon Motorcycle Film Fest 2026",
        "btnWA": "WhatsApp",
        "btnSend": "Отправить заявку",
        "btnBack": "Ко всем новостям",

        "img1.alt": "Команда Iron Custom Motors рядом с кастом-мотоциклом ICM Beckman, чемпионом мира в классе Cafe Racer с трёхцилиндровым двигателем ручной сборки, на Lisbon Motorcycle Film Fest 2026.",
        "img1.cap": "ICM Beckman на Lisbon Motorcycle Film Fest 2026 — чемпион мира в классе Cafe Racer, AMD World Championship of Custom Bike Building 2016.",
        "img2.alt": "Команда Iron Custom Motors с друзьями и гостями фестиваля на Lisbon Motorcycle Film Fest 2026.",
        "img2.cap": "Знакомимся с байкерами, билдерами и друзьями на фестивале в Лиссабоне.",
        "img3.alt": "Кастом и классические мотоциклы BMW на выставке Lisbon Motorcycle Film Fest 2026, на переднем плане матовый чёрный BMW boxer cafe racer.",
        "img3.cap": "Выставочный зал фестиваля — кастом-сборки с португальской и международной сцены.",
        "img4.alt": "Реплика BMW R100 GS Paris-Dakar в ливрее Marlboro на Lisbon Motorcycle Film Fest 2026.",
        "img4.cap": "Реплика BMW R100 GS Paris-Dakar — ралли-наследие на фестивале.",
        "img5.alt": "Кастом-концепт BMW R18 'Maverick' от Maverick, представленный на Lisbon Motorcycle Film Fest 2026.",
        "img5.cap": "Концепт BMW R18 'Maverick' — ещё один яркий проект на фестивале.",

        "publishedISO": "2026-05-23",
        "publishedLabel": "Опубликовано 23 мая 2026",
    },
    "uk": {
        "eyebrow": "Новини · 23 травня 2026",
        "h1": "Iron Custom Motors на Lisbon Motorcycle Film Fest 2026:<br/><span class=\"accent\">Beckman</span> у центрі події.",
        "lede": "23 травня 2026 Iron Custom Motors бере участь у Lisbon Motorcycle Film Fest — одній з найяскравіших подій мотокультури у Португалії та впізнаваній точці зустрічі байкерів, білдерів, художників, кінематографістів і всіх, хто живе життям на двох колесах. Цей рік стає символічним і для нас: ми показуємо один з найважливіших мотоциклів в історії бренду — ICM Beckman.",

        "s1.h2": "Чому ця подія важлива для Iron Custom Motors",
        "s1.p1": "Наша історія почалася у Харкові 2010 року. За роки Iron Custom Motors із майстерні, побудованої на пристрасті, інженерії та майстерності, виріс у бренд, відомий далеко за межами свого міста. Наші мотоцикли та кастом-проєкти виходили на міжнародну сцену, брали великі титули, отримували професійне визнання і сформували нашу ідентичність — майстерню, що не йде за модою, а будує машини зі своєю мовою, метою та характером.",
        "s1.p2": "Сьогодні, відкривши нову главу в Португалії, участь у Lisbon Motorcycle Film Fest для нас — природний крок. У Португалії сильна й зростаюча мотокультура, клімат, що дозволяє їздити більшу частину року, і спільнота, яка цінує і практичну, і емоційну сторону мотожиття. Це саме те середовище, до якого належить наш бренд — поруч з байкерами, поруч зі справжньою дорожньою культурою і поруч з тими, хто надає мотоциклам сенс.",
        "s1.p3": "Lisbon Motorcycle Film Fest збирає в одній програмі мотокіно, дискусії, виставки, заїзди та кастом-культуру — це унікальний простір, де мотоцикл розглядається не лише як техніка, а й як частина творчості, дизайну, свободи та особистої ідентичності. Для нас фестиваль — правильне місце, щоб показати проєкт, у якому сходиться стільки нашої історії і філософії.",

        "s2.h2": "Beckman: чемпіонський мотоцикл у Лісабоні",
        "s2.p1": "У центрі нашої участі — <a href=\"/projects/beckman/\">ICM Beckman</a>, один з найзначніших мотоциклів, коли-небудь створених Iron Custom Motors. Beckman — це не просто кастом-збірка з нашого архіву. Це один з мотоциклів, що сформував нашу міжнародну репутацію і довів: наша інженерія та дизайн здатні конкурувати на найвищому рівні.",
        "s2.p2": "Beckman став чемпіоном світу в класі Cafe Racer на AMD World Championship of Custom Bike Building у 2016 році. Пізніше проєкт також отримав нагороду Best Engineering на MBE Verona. Ці досягнення зробили Beckman одним із найсильніших символів філософії майстерні: безкомпромісна майстерність, реальна інженерна глибина і кастом-мотоцикл як цілісне висловлювання, а не просто візуальна вправа.",
        "s2.p3": "Одна з найпомітніших рис Beckman — власний триціліндровий двигун ручної збірки, спроєктований і виготовлений у рамках проєкту. Разом із великою кількістю hand-made деталей і ретельним фінішним опрацюванням Beckman став мотоциклом, що представляє найглибшу сторону Iron Custom Motors — ту, де дизайн, фабрикація, механіка і художня дисципліна сходяться в одній машині.",

        "s3.h2": "Від чемпіонатів світу — до нової домівки в Кашкайші",
        "s3.p1": "Привезти Beckman на Lisbon Motorcycle Film Fest для нас — більше, ніж виставковий показ. Це міст між нашою історією та нашим майбутнім. Iron Custom Motors тепер працює в Кашкайші, де ми будуємо преміальну мотомайстерню, сфокусовану на якісному сервісі, запчастинах і витратниках, апґрейдах і тюнінгу, кастом і спеціальних проєктах.",
        "s3.p2": "А ще ми будуємо щось більше, ніж просто майстерня: місце, де байкери можуть зустрітися, поговорити, випити кави і відчути себе частиною справжньої мотоспільноти. Тому наша присутність на фестивалі має значення. Ми приїжджаємо не як незнайомці. Ми приїжджаємо з історією, з чемпіонськими мотоциклами, з перевіреним досвідом і з ясною задачею — стати однією з найсильніших і найповажніших мотомайстерень у Кашкайші та Великому Лісабоні.",

        "s4.h2": "Подія мотокультури, що збігається з нашою філософією",
        "s4.p1": "Дух Lisbon Motorcycle Film Fest близький до того, в що вірить Iron Custom Motors. Мотоцикл — це не лише транспорт. Це ідентичність, майстерність, свобода, дорожні історії, естетика і спільнота.",
        "s4.p2": "Фестиваль, що поєднує кіно, кастом-культуру, виставки, розмови і байкерів в одному місці, точно відображає атмосферу, яку ми хочемо допомогти виростити навколо нової майстерні в Португалії. Тому ми особливо раді показати Beckman у цьому контексті. Це мотоцикл, у якому є історія, досягнення і емоція. Він говорить із білдерами, байкерами, дизайнерами і всіма, хто розуміє: справді великий мотоцикл може стати набагато більшим, ніж сума своїх частин.",

        "s5.h2": "Побачимося в Лісабоні",
        "s5.p1": "Ми пишаємося тим, що беремо участь у Lisbon Motorcycle Film Fest 2026, і раді зустріти всіх, хто хоче познайомитися з Iron Custom Motors, побачити Beckman наживо і стати частиною цієї нової глави разом з нами. Якщо ви в Лісабоні цими вихідними — приходьте познайомитися, подивіться на один із визначальних мотоциклів у нашій історії і розділіть це свято мотокультури разом.",
        "s5.p2": "Iron Custom Motors тепер у Португалії — і це лише початок.",

        "ctaEyebrow": "Після фестивалю",
        "ctaTitle": "Завітайте до нової майстерні в Кашкайші.",
        "ctaText": "Якщо познайомилися з нами на фестивалі або хочете привезти мотоцикл у майстерню, що серйозно ставиться до інженерії — заїжджайте до Iron Custom Motors у São Domingos de Rana. Напишіть команді у WhatsApp, щоб записатися на сервіс або просто привітатися.",

        "breadHome": "Головна",
        "breadNews": "Новини",
        "h1Crumb": "Iron Custom Motors на Lisbon Motorcycle Film Fest 2026",
        "btnWA": "WhatsApp",
        "btnSend": "Надіслати заявку",
        "btnBack": "До всіх новин",

        "img1.alt": "Команда Iron Custom Motors поруч із кастом-мотоциклом ICM Beckman, чемпіоном світу в класі Cafe Racer із триціліндровим двигуном ручної збірки, на Lisbon Motorcycle Film Fest 2026.",
        "img1.cap": "ICM Beckman на Lisbon Motorcycle Film Fest 2026 — чемпіон світу в класі Cafe Racer, AMD World Championship of Custom Bike Building 2016.",
        "img2.alt": "Команда Iron Custom Motors з друзями і гостями фестивалю на Lisbon Motorcycle Film Fest 2026.",
        "img2.cap": "Знайомимося з байкерами, білдерами та друзями на фестивалі у Лісабоні.",
        "img3.alt": "Кастом і класичні мотоцикли BMW на виставці Lisbon Motorcycle Film Fest 2026, на передньому плані матовий чорний BMW boxer cafe racer.",
        "img3.cap": "Виставковий зал фестивалю — кастом-збірки з португальської й міжнародної сцени.",
        "img4.alt": "Репліка BMW R100 GS Paris-Dakar у лівреї Marlboro на Lisbon Motorcycle Film Fest 2026.",
        "img4.cap": "Репліка BMW R100 GS Paris-Dakar — ралійна спадщина на фестивалі.",
        "img5.alt": "Кастом-концепт BMW R18 'Maverick' від Maverick, представлений на Lisbon Motorcycle Film Fest 2026.",
        "img5.cap": "Концепт BMW R18 'Maverick' — ще один яскравий проєкт на фестивалі.",

        "publishedISO": "2026-05-23",
        "publishedLabel": "Опубліковано 23 травня 2026",
    },
    "pt": {
        "eyebrow": "Notícias · 23 de maio 2026",
        "h1": "Iron Custom Motors no Lisbon Motorcycle Film Fest 2026:<br/><span class=\"accent\">Beckman</span> no centro da celebração.",
        "lede": "A 23 de maio de 2026, a Iron Custom Motors participa no Lisbon Motorcycle Film Fest — um dos eventos de cultura motociclista mais distintivos de Portugal e um ponto de encontro reconhecido para riders, builders, artistas, cineastas e toda a gente que vive o estilo de vida sobre duas rodas. A edição deste ano marca um momento simbólico para nós: apresentamos uma das motas mais importantes da história da marca — a ICM Beckman.",

        "s1.h2": "Porquê este evento é importante para a Iron Custom Motors",
        "s1.p1": "A nossa história começou em Kharkiv em 2010. Ao longo dos anos, a Iron Custom Motors cresceu de uma oficina construída sobre paixão, engenharia e ofício, para uma marca reconhecida muito além da sua cidade natal. As nossas motas e projetos custom chegaram ao palco internacional, ganharam grandes títulos, conquistaram respeito profissional e ajudaram a definir a nossa identidade como uma oficina que não segue tendências, mas constrói máquinas com a sua própria linguagem, propósito e carácter.",
        "s1.p2": "Hoje, com a Iron Custom Motors a continuar o seu novo capítulo em Portugal, participar no Lisbon Motorcycle Film Fest é natural. Portugal tem uma cultura motociclista forte e em crescimento, um clima que permite andar a maior parte do ano e uma comunidade que valoriza tanto o lado prático como o emocional do mundo das motas. É exatamente o tipo de ambiente onde a nossa marca pertence — perto dos riders, perto da cultura de estrada real e perto da comunidade que dá sentido às motas.",
        "s1.p3": "O Lisbon Motorcycle Film Fest junta filmes de motas, conversas, exposições, saídas e cultura custom num só programa, criando um espaço único onde a moto é vista não só como máquina, mas como parte de criatividade, design, liberdade e identidade pessoal. Para nós, isso faz do festival o lugar certo para apresentar um projeto que carrega tanto da nossa história e filosofia.",

        "s2.h2": "Beckman: uma moto campeã em Lisboa",
        "s2.p1": "No centro da nossa participação está a <a href=\"/projects/beckman/\">ICM Beckman</a> — uma das motas mais significativas alguma vez criadas pela Iron Custom Motors. A Beckman não é simplesmente uma build custom do nosso arquivo. É uma das motas que moldou a nossa reputação internacionalmente e provou que a nossa engenharia e design podem competir ao mais alto nível.",
        "s2.p2": "A Beckman tornou-se Campeã do Mundo na Cafe Racer Class do AMD World Championship of Custom Bike Building em 2016. Mais tarde, o projeto recebeu também o prémio Best Engineering no MBE Verona. Estas distinções fizeram da Beckman um dos símbolos mais fortes da filosofia da nossa oficina: ofício sem compromissos, profundidade de engenharia real e uma moto custom construída como uma declaração completa, não apenas como exercício visual.",
        "s2.p3": "Uma das características mais notáveis da Beckman é o seu motor tricilíndrico feito à mão, desenhado e fabricado como parte do projeto. Em conjunto com um grande número de peças hand-made e acabamentos altamente detalhados, a Beckman tornou-se uma moto que representa o lado mais profundo da Iron Custom Motors — o lado onde design, fabrico, mecânica e disciplina artística se encontram numa só máquina.",

        "s3.h2": "Dos campeonatos mundiais a uma nova casa em Cascais",
        "s3.p1": "Para nós, trazer a Beckman ao Lisbon Motorcycle Film Fest é mais do que uma aparição em exposição. É uma ponte entre a nossa história e o nosso futuro. A Iron Custom Motors continua agora o seu trabalho em Cascais, onde estamos a construir uma oficina premium de motos focada em serviço de alta qualidade, peças e consumíveis, upgrades e tuning, e projetos custom e especiais.",
        "s3.p2": "Estamos também a construir algo mais do que uma oficina: um sítio onde os riders se podem encontrar, conversar, tomar café e sentir-se parte de uma comunidade motociclista real. É por isso que a nossa presença no festival é importante. Não chegamos como estranhos. Chegamos com uma história, com motas campeãs, com experiência comprovada e com uma intenção clara — tornarmo-nos uma das oficinas mais fortes e respeitadas da região de Cascais e Grande Lisboa.",

        "s4.h2": "Um evento de cultura motociclista que coincide com a nossa filosofia",
        "s4.p1": "O espírito do Lisbon Motorcycle Film Fest está próximo daquilo em que a Iron Custom Motors acredita. As motas não são apenas transporte. São identidade, ofício, liberdade, histórias de estrada, estética e comunidade.",
        "s4.p2": "Um festival que combina cinema, cultura custom, exposições, conversas e riders num só lugar reflete exatamente o tipo de atmosfera que queremos ajudar a fazer crescer à volta da nossa nova oficina em Portugal. É por isso que estamos particularmente felizes em apresentar a Beckman neste contexto. É uma moto que carrega história, conquista e emoção. Fala com builders, riders, designers e com toda a gente que percebe que uma moto verdadeiramente grande pode tornar-se muito mais do que a soma das suas partes.",

        "s5.h2": "Até já em Lisboa",
        "s5.p1": "Temos orgulho em fazer parte do Lisbon Motorcycle Film Fest 2026 e estamos felizes por receber todos os que quiserem descobrir a Iron Custom Motors, ver a Beckman ao vivo e fazer parte deste novo capítulo connosco. Se está em Lisboa neste fim de semana, venha conhecer-nos, ver uma das motas definidoras da nossa história e partilhar esta celebração da cultura motociclista juntos.",
        "s5.p2": "A Iron Custom Motors está agora em Portugal — e isto é apenas o começo.",

        "ctaEyebrow": "Depois do festival",
        "ctaTitle": "Visite a nova oficina em Cascais.",
        "ctaText": "Se nos conheceu no festival ou se quiser trazer a sua mota a uma oficina que leva engenharia a sério — passe pela Iron Custom Motors em São Domingos de Rana. Mande WhatsApp à equipa para marcar serviço ou simplesmente cumprimentar.",

        "breadHome": "Início",
        "breadNews": "Notícias",
        "h1Crumb": "Iron Custom Motors no Lisbon Motorcycle Film Fest 2026",
        "btnWA": "WhatsApp",
        "btnSend": "Enviar pedido",
        "btnBack": "Voltar às notícias",

        "img1.alt": "Equipa da Iron Custom Motors junto à mota custom ICM Beckman, campeã do mundo na classe Cafe Racer, com motor tricilíndrico construído à mão, no Lisbon Motorcycle Film Fest 2026.",
        "img1.cap": "ICM Beckman em exposição no Lisbon Motorcycle Film Fest 2026 — Campeã do Mundo na Cafe Racer Class, AMD World Championship of Custom Bike Building 2016.",
        "img2.alt": "Equipa da Iron Custom Motors com amigos e convidados do festival no Lisbon Motorcycle Film Fest 2026.",
        "img2.cap": "A conhecer riders, builders e amigos no festival em Lisboa.",
        "img3.alt": "Motas BMW custom e clássicas em exposição no Lisbon Motorcycle Film Fest 2026, com uma BMW boxer cafe racer preto mate em primeiro plano.",
        "img3.cap": "O piso do festival — builds custom da cena portuguesa e internacional.",
        "img4.alt": "Réplica BMW R100 GS Paris-Dakar em librea Marlboro, exposta no Lisbon Motorcycle Film Fest 2026.",
        "img4.cap": "Réplica BMW R100 GS Paris-Dakar — herança rally no festival.",
        "img5.alt": "Concept custom BMW R18 'Maverick' da Maverick, apresentado no Lisbon Motorcycle Film Fest 2026.",
        "img5.cap": "Concept BMW R18 'Maverick' — outra build de destaque no festival.",

        "publishedISO": "2026-05-23",
        "publishedLabel": "Publicado a 23 de maio de 2026",
    },
}

# Article metadata (slug → meta + body)
NEWS_ARTICLES = {
    "lisbon-motorcycle-film-fest-2026-beckman": {
        "publishedISO": "2026-05-23",
        "imageBase": "/photos/news/news-lmff2026",
        "imageCount": 5,
        "imageHero": 1,
        "meta": ARTICLE_LMFF_META,
        "body": ARTICLE_LMFF_BODY,
        "sectionCount": 5,
        "imageMap": [(2, 2), (4, 4), (3, 5), (5, 5)],  # (img_num, after_section) — flexible placement
    },
    "opens-new-workshop-in-cascais": {
        "publishedISO": "2026-05-02",
        "imageBase": "/photos/news/news-opening",
        "imageCount": 4,
        "imageHero": 1,
        "meta": ARTICLE_OPENING_META,
        "body": ARTICLE_OPENING_BODY,
        "sectionCount": 7,
        "imageMap": [(2, 2), (4, 3), (3, 4)],
    },
}

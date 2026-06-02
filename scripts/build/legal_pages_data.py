"""
Content for legal pages: /privacy/, /cookies/, /terms/.
Plain GDPR-compliant boilerplate adapted for Iron Custom Motors business profile.
Not lawyer-reviewed — owner should pass through a Portuguese lawyer before relying on this.
"""

LAST_UPDATED = "May 2026"
CONTROLLER = {
    "name": "Iron Custom Motors",
    "address": "R. António José da Silva 100 B, 2785-253 São Domingos de Rana, Cascais, Portugal",
    "email": "Ironcustom.office@gmail.com",
    "phone": "+351 917 961 230",
}

# ============================================================
# /privacy/  — Privacy Policy
# ============================================================
PRIVACY_HEAD = {
    "en": {
        "title": "Privacy Policy | Iron Custom Motors — Cascais",
        "description": "Iron Custom Motors privacy policy: how we collect, use and protect your data when you contact us or use this website. GDPR-compliant.",
    },
    "ru": {
        "title": "Политика конфиденциальности | Iron Custom Motors — Кашкайш",
        "description": "Политика конфиденциальности Iron Custom Motors: как мы собираем, используем и защищаем ваши данные при связи с нами и использовании сайта. Соответствие GDPR.",
    },
    "uk": {
        "title": "Політика конфіденційності | Iron Custom Motors — Кашкайш",
        "description": "Політика конфіденційності Iron Custom Motors: як ми збираємо, використовуємо та захищаємо ваші дані при зв'язку з нами та використанні сайту. GDPR.",
    },
    "pt": {
        "title": "Política de Privacidade | Iron Custom Motors — Cascais",
        "description": "Política de privacidade da Iron Custom Motors: como recolhemos, usamos e protegemos os seus dados quando nos contacta ou usa este site. RGPD.",
    },
}

PRIVACY_BODY = {
    "en": {
        "h1": "Privacy Policy",
        "intro": "This privacy policy explains how Iron Custom Motors (\"we\", \"us\") collects, uses, and protects personal data of visitors and customers. We follow the EU General Data Protection Regulation (GDPR) and applicable Portuguese data-protection law.",
        "sections": [
            ("1. Who we are", "Data controller: Iron Custom Motors. Address: " + CONTROLLER["address"] + ". Contact: " + CONTROLLER["email"] + ", " + CONTROLLER["phone"] + "."),
            ("2. What data we collect", "When you contact us by form, WhatsApp, phone, or email, we collect: name, phone number, email (optional), motorcycle details (brand, model, year), and the content of your message. When you visit this site we also collect technical data via analytics: browser type, device, country, pages viewed, referring page. Analytics data is only collected after you accept cookies."),
            ("3. Why we collect it", "We use your contact details to reply to your request, prepare estimates, book service appointments, and follow up after a job. We use analytics to understand which pages help riders find us and improve the site. We never sell your data."),
            ("4. Legal basis", "Processing of contact form data is based on your consent and on our legitimate interest in answering business enquiries. Service work and invoicing is based on the contract between us. Analytics is based on consent (cookie banner)."),
            ("5. How long we keep it", "Contact enquiries are kept for up to 24 months for follow-up and quality. Customer records (invoices, service history) are kept for the period required by Portuguese tax law (currently 10 years). Analytics data is retained for 14 months in Google Analytics."),
            ("6. Who has access", "Your data is processed by Iron Custom Motors staff. We use the following third-party processors: FormSubmit (form delivery), Google Analytics 4, Meta Pixel (only after consent), Cloudflare (security/CDN for reviews widget), Google Maps (embedded map). Each processor handles your data under their own privacy terms."),
            ("7. International transfers", "Some processors are located outside the EU/EEA (Google, Meta, Cloudflare in the US). Transfers rely on Standard Contractual Clauses (SCCs) and/or the EU-US Data Privacy Framework."),
            ("8. Your rights", "You have the right to access, rectify, delete or restrict processing of your personal data; to data portability; to object to processing; to withdraw consent at any time; and to lodge a complaint with the Portuguese supervisory authority (CNPD — Comissão Nacional de Proteção de Dados)."),
            ("9. How to contact us", "To exercise any of the above rights, email us at " + CONTROLLER["email"] + ". We will respond within 30 days."),
            ("10. Changes", "We may update this policy. The last update date is shown below."),
        ],
        "updated": "Last updated: " + LAST_UPDATED,
    },
    "ru": {
        "h1": "Политика конфиденциальности",
        "intro": "Эта политика объясняет, как Iron Custom Motors («мы») собирает, использует и защищает персональные данные посетителей и клиентов. Мы следуем общему регламенту ЕС по защите данных (GDPR) и законодательству Португалии о защите данных.",
        "sections": [
            ("1. Кто мы", "Контроллер данных: Iron Custom Motors. Адрес: " + CONTROLLER["address"] + ". Связь: " + CONTROLLER["email"] + ", " + CONTROLLER["phone"] + "."),
            ("2. Какие данные мы собираем", "Когда вы пишете нам через форму, WhatsApp, телефон или email, мы получаем: имя, номер телефона, email (необязательно), данные мотоцикла (бренд, модель, год) и текст обращения. При посещении сайта собираются технические данные через аналитику: тип браузера, устройство, страна, просмотренные страницы, источник перехода. Аналитика загружается только после принятия cookie."),
            ("3. Зачем мы это собираем", "Контактные данные — чтобы ответить вам, подготовить смету, записать на сервис и связаться после работы. Аналитика — чтобы понять, какие страницы помогают клиентам находить нас, и улучшить сайт. Мы не продаём ваши данные."),
            ("4. Правовое основание", "Обработка формы — ваше согласие и наш законный интерес ответить на коммерческое обращение. Сервис и выставление счетов — договор между нами. Аналитика — согласие через cookie-баннер."),
            ("5. Сколько мы храним", "Обращения — до 24 месяцев для последующей связи. Клиентские записи (счета, история работ) — срок, требуемый налоговым кодексом Португалии (на момент написания — 10 лет). Аналитика — 14 месяцев в Google Analytics."),
            ("6. Кто имеет доступ", "Данные обрабатывают сотрудники Iron Custom Motors. Используем сторонних процессоров: FormSubmit (доставка форм), Google Analytics 4, Meta Pixel (только после согласия), Cloudflare (безопасность/CDN виджета отзывов), Google Maps (встроенная карта). Каждый процессор обрабатывает данные по своим условиям."),
            ("7. Международная передача", "Часть процессоров расположены вне ЕС/ЕЭП (Google, Meta, Cloudflare — США). Передача основана на стандартных договорных условиях (SCC) и/или EU-US Data Privacy Framework."),
            ("8. Ваши права", "Право доступа, исправления, удаления или ограничения обработки данных; переносимости данных; возражения; отзыва согласия в любое время; обращения в надзорный орган Португалии (CNPD — Comissão Nacional de Proteção de Dados)."),
            ("9. Связь с нами", "Чтобы воспользоваться правами выше, пишите на " + CONTROLLER["email"] + ". Отвечаем в течение 30 дней."),
            ("10. Изменения", "Мы можем обновлять эту политику. Дата последнего обновления — ниже."),
        ],
        "updated": "Последнее обновление: " + LAST_UPDATED,
    },
    "uk": {
        "h1": "Політика конфіденційності",
        "intro": "Ця політика пояснює, як Iron Custom Motors («ми») збирає, використовує та захищає персональні дані відвідувачів і клієнтів. Ми дотримуємось загального регламенту ЄС про захист даних (GDPR) і португальського законодавства про захист даних.",
        "sections": [
            ("1. Хто ми", "Контролер даних: Iron Custom Motors. Адреса: " + CONTROLLER["address"] + ". Зв'язок: " + CONTROLLER["email"] + ", " + CONTROLLER["phone"] + "."),
            ("2. Які дані ми збираємо", "Коли ви пишете нам через форму, WhatsApp, телефон чи email, ми отримуємо: ім'я, номер телефону, email (необов'язково), дані мотоцикла (бренд, модель, рік) і текст звернення. Під час візиту збираються технічні дані через аналітику: тип браузера, пристрій, країна, переглянуті сторінки, джерело переходу. Аналітика завантажується лише після прийняття cookie."),
            ("3. Навіщо ми це збираємо", "Контактні дані — щоб відповісти, підготувати кошторис, записати на сервіс і зв'язатися після роботи. Аналітика — щоб зрозуміти, які сторінки допомагають клієнтам знаходити нас, і покращити сайт. Ми не продаємо ваші дані."),
            ("4. Правова підстава", "Обробка форми — ваша згода і наш законний інтерес відповісти на комерційне звернення. Сервіс і виставлення рахунків — договір між нами. Аналітика — згода через cookie-банер."),
            ("5. Скільки ми зберігаємо", "Звернення — до 24 місяців для подальшого зв'язку. Клієнтські записи (рахунки, історія робіт) — термін, потрібний податковим кодексом Португалії (наразі — 10 років). Аналітика — 14 місяців у Google Analytics."),
            ("6. Хто має доступ", "Дані обробляють співробітники Iron Custom Motors. Використовуємо сторонніх процесорів: FormSubmit (доставка форм), Google Analytics 4, Meta Pixel (тільки після згоди), Cloudflare (безпека/CDN віджета відгуків), Google Maps (вбудована мапа). Кожен процесор обробляє дані за своїми умовами."),
            ("7. Міжнародна передача", "Частина процесорів розташовані поза ЄС/ЄЕЗ (Google, Meta, Cloudflare — США). Передача базується на стандартних договірних положеннях (SCC) та/або EU-US Data Privacy Framework."),
            ("8. Ваші права", "Право доступу, виправлення, видалення або обмеження обробки даних; переносимості даних; заперечення; відкликання згоди в будь-який час; звернення до наглядового органу Португалії (CNPD — Comissão Nacional de Proteção de Dados)."),
            ("9. Зв'язок з нами", "Щоб скористатися правами вище, пишіть на " + CONTROLLER["email"] + ". Відповідаємо протягом 30 днів."),
            ("10. Зміни", "Ми можемо оновлювати цю політику. Дата останнього оновлення — нижче."),
        ],
        "updated": "Останнє оновлення: " + LAST_UPDATED,
    },
    "pt": {
        "h1": "Política de Privacidade",
        "intro": "Esta política explica como a Iron Custom Motors («nós») recolhe, usa e protege os dados pessoais dos visitantes e clientes. Seguimos o Regulamento Geral sobre a Proteção de Dados da UE (RGPD) e a legislação portuguesa aplicável.",
        "sections": [
            ("1. Quem somos", "Responsável pelo tratamento: Iron Custom Motors. Morada: " + CONTROLLER["address"] + ". Contacto: " + CONTROLLER["email"] + ", " + CONTROLLER["phone"] + "."),
            ("2. Que dados recolhemos", "Quando nos contacta por formulário, WhatsApp, telefone ou email, recolhemos: nome, telefone, email (opcional), dados da moto (marca, modelo, ano) e o conteúdo da sua mensagem. Ao visitar o site recolhemos também dados técnicos via analítica: tipo de navegador, dispositivo, país, páginas vistas, página de origem. A analítica só carrega após aceitação dos cookies."),
            ("3. Porque recolhemos", "Usamos os contactos para responder, preparar orçamentos, agendar serviço e acompanhar trabalhos. Usamos analítica para perceber que páginas ajudam os clientes a encontrar-nos e melhorar o site. Nunca vendemos os seus dados."),
            ("4. Base legal", "O tratamento de dados do formulário baseia-se no seu consentimento e no nosso interesse legítimo em responder a pedidos comerciais. Serviço e faturação baseiam-se no contrato entre as partes. A analítica baseia-se no consentimento (banner de cookies)."),
            ("5. Por quanto tempo", "Pedidos de contacto: até 24 meses para acompanhamento. Registos de cliente (faturas, histórico de serviço): período exigido pela lei fiscal portuguesa (atualmente 10 anos). Dados de analítica: 14 meses no Google Analytics."),
            ("6. Quem tem acesso", "Os dados são tratados por colaboradores da Iron Custom Motors. Usamos os seguintes subcontratantes: FormSubmit (entrega de formulários), Google Analytics 4, Meta Pixel (apenas após consentimento), Cloudflare (segurança/CDN do widget de avaliações), Google Maps (mapa incorporado). Cada um trata os dados ao abrigo das suas próprias condições."),
            ("7. Transferências internacionais", "Alguns subcontratantes estão fora da UE/EEE (Google, Meta, Cloudflare nos EUA). As transferências baseiam-se em Cláusulas Contratuais-Tipo (CCT) e/ou no EU-US Data Privacy Framework."),
            ("8. Os seus direitos", "Tem direito a aceder, retificar, apagar ou limitar o tratamento dos seus dados; à portabilidade; a opor-se ao tratamento; a retirar o consentimento a qualquer momento; e a apresentar reclamação à autoridade de controlo portuguesa (CNPD — Comissão Nacional de Proteção de Dados)."),
            ("9. Como contactar-nos", "Para exercer qualquer dos direitos acima, envie email para " + CONTROLLER["email"] + ". Respondemos em 30 dias."),
            ("10. Alterações", "Esta política pode ser atualizada. A data da última atualização aparece abaixo."),
        ],
        "updated": "Última atualização: " + LAST_UPDATED,
    },
}

# ============================================================
# /cookies/  — Cookie Policy
# ============================================================
COOKIES_HEAD = {
    "en": {"title":"Cookie Policy | Iron Custom Motors","description":"How Iron Custom Motors uses cookies and similar technologies. Manage your choices and understand which services run on this site."},
    "ru": {"title":"Политика cookie | Iron Custom Motors","description":"Как Iron Custom Motors использует cookie и аналогичные технологии. Управляйте выбором и узнайте, какие сервисы работают на сайте."},
    "uk": {"title":"Політика cookie | Iron Custom Motors","description":"Як Iron Custom Motors використовує cookie та подібні технології. Керуйте вибором і дізнайтеся, які сервіси працюють на сайті."},
    "pt": {"title":"Política de Cookies | Iron Custom Motors","description":"Como a Iron Custom Motors usa cookies e tecnologias semelhantes. Gira as suas escolhas e saiba que serviços funcionam neste site."},
}

COOKIES_BODY = {
    "en": {
        "h1": "Cookie Policy",
        "intro": "We use a minimal set of cookies and similar storage technologies. This page explains which ones, why, and how to control them. By using our site you can accept or reject non-essential cookies via the cookie banner.",
        "sections": [
            ("Essential (always active)", "Used for the cookie banner itself (localStorage key icm-consent) to remember your choice, and for the language preference. No tracking."),
            ("Analytics (only after consent)", "Google Analytics 4 (G-D15BLYEKBN) to measure site traffic and improve content. Cookies set: _ga, _gid, _ga_<id>. Retention: up to 2 years. Data is anonymised where possible."),
            ("Marketing (only after consent)", "Meta Pixel (1708697916976439) — currently inactive (kept for future ad campaigns). When active, it would set _fbp and similar cookies for ad attribution."),
            ("Reviews widget", "Our reviews block fetches Google reviews via a Cloudflare Worker (icm-reviews.vg-ab6.workers.dev). The Worker may set caching headers — no personal cookies."),
            ("Embedded Google Maps", "When you view the embedded map on the contact page, Google may set its own cookies. We have no control over these — refer to Google's own privacy policy."),
            ("How to change your choice", "Clear your browser's site data for ironcustommotors.com — the cookie banner will appear again on next visit and you can choose differently."),
        ],
        "updated": "Last updated: " + LAST_UPDATED,
    },
    "ru": {
        "h1": "Политика cookie",
        "intro": "Мы используем минимальный набор cookie и аналогичных технологий хранения. Эта страница объясняет какие, зачем и как ими управлять. Используя сайт, вы можете принять или отклонить неосновные cookie через баннер согласия.",
        "sections": [
            ("Основные (всегда активны)", "Используются самим cookie-баннером (ключ localStorage icm-consent) для запоминания выбора и для языковой настройки. Без трекинга."),
            ("Аналитика (только после согласия)", "Google Analytics 4 (G-D15BLYEKBN) для измерения трафика и улучшения сайта. Cookie: _ga, _gid, _ga_<id>. Хранятся до 2 лет. Данные анонимизированы где возможно."),
            ("Маркетинг (только после согласия)", "Meta Pixel (1708697916976439) — сейчас неактивен (оставлен для будущих кампаний). Когда активен, ставит _fbp и подобные cookie для атрибуции рекламы."),
            ("Виджет отзывов", "Блок отзывов получает Google-отзывы через Cloudflare Worker (icm-reviews.vg-ab6.workers.dev). Worker может ставить заголовки кеширования — личных cookie нет."),
            ("Встроенная Google-карта", "При просмотре встроенной карты на странице контактов Google может ставить свои cookie. Мы не контролируем их — см. политику конфиденциальности Google."),
            ("Как изменить выбор", "Очистите данные сайта ironcustommotors.com в браузере — баннер появится снова при следующем визите и вы сможете выбрать иначе."),
        ],
        "updated": "Последнее обновление: " + LAST_UPDATED,
    },
    "uk": {
        "h1": "Політика cookie",
        "intro": "Ми використовуємо мінімальний набір cookie та подібних технологій зберігання. Ця сторінка пояснює які, навіщо і як ними керувати. Використовуючи сайт, ви можете прийняти або відхилити неосновні cookie через банер.",
        "sections": [
            ("Основні (завжди активні)", "Використовуються самим cookie-банером (ключ localStorage icm-consent) для запам'ятовування вибору і для мовної настройки. Без трекінгу."),
            ("Аналітика (тільки після згоди)", "Google Analytics 4 (G-D15BLYEKBN) для вимірювання трафіку і покращення сайту. Cookie: _ga, _gid, _ga_<id>. Зберігаються до 2 років. Дані анонімізовані де можливо."),
            ("Маркетинг (тільки після згоди)", "Meta Pixel (1708697916976439) — наразі неактивний (залишений для майбутніх кампаній). Коли активний, ставить _fbp і подібні cookie для атрибуції реклами."),
            ("Віджет відгуків", "Блок відгуків отримує Google-відгуки через Cloudflare Worker (icm-reviews.vg-ab6.workers.dev). Worker може ставити заголовки кешування — особистих cookie немає."),
            ("Вбудована Google-мапа", "При перегляді вбудованої мапи на сторінці контактів Google може ставити свої cookie. Ми їх не контролюємо — див. політику конфіденційності Google."),
            ("Як змінити вибір", "Очистіть дані сайту ironcustommotors.com у браузері — банер з'явиться знову при наступному візиті і ви зможете обрати інакше."),
        ],
        "updated": "Останнє оновлення: " + LAST_UPDATED,
    },
    "pt": {
        "h1": "Política de Cookies",
        "intro": "Usamos um conjunto mínimo de cookies e tecnologias de armazenamento semelhantes. Esta página explica quais, porquê e como controlá-los. Ao usar o site pode aceitar ou rejeitar cookies não essenciais via o banner.",
        "sections": [
            ("Essenciais (sempre ativos)", "Usados pelo próprio banner de cookies (chave localStorage icm-consent) para guardar a sua escolha, e pela preferência de idioma. Sem rastreamento."),
            ("Analítica (apenas após consentimento)", "Google Analytics 4 (G-D15BLYEKBN) para medir tráfego e melhorar o conteúdo. Cookies: _ga, _gid, _ga_<id>. Retenção até 2 anos. Dados anonimizados sempre que possível."),
            ("Marketing (apenas após consentimento)", "Meta Pixel (1708697916976439) — atualmente inativo (mantido para futuras campanhas). Quando ativo, define _fbp e cookies semelhantes para atribuição de anúncios."),
            ("Widget de avaliações", "O bloco de avaliações vai buscar avaliações Google através de um Cloudflare Worker (icm-reviews.vg-ab6.workers.dev). O Worker pode definir cabeçalhos de cache — sem cookies pessoais."),
            ("Mapa Google incorporado", "Ao ver o mapa na página de contactos, a Google pode definir os seus próprios cookies. Não os controlamos — consulte a política de privacidade da Google."),
            ("Como mudar a escolha", "Limpe os dados do site ironcustommotors.com no browser — o banner aparecerá de novo na próxima visita e poderá escolher diferentemente."),
        ],
        "updated": "Última atualização: " + LAST_UPDATED,
    },
}

# ============================================================
# /terms/  — Terms of service
# ============================================================
TERMS_HEAD = {
    "en": {"title":"Terms of Service | Iron Custom Motors","description":"Terms governing the use of Iron Custom Motors website and services. Service estimates, warranty, customer obligations and limitations of liability."},
    "ru": {"title":"Условия использования | Iron Custom Motors","description":"Условия использования сайта и сервиса Iron Custom Motors. Сметы, гарантия, обязанности клиента и ограничения ответственности."},
    "uk": {"title":"Умови використання | Iron Custom Motors","description":"Умови використання сайту і сервісу Iron Custom Motors. Кошториси, гарантія, обов'язки клієнта та обмеження відповідальності."},
    "pt": {"title":"Termos de Serviço | Iron Custom Motors","description":"Termos que regem o uso do site e serviços da Iron Custom Motors. Orçamentos, garantia, obrigações do cliente e limites de responsabilidade."},
}

TERMS_BODY = {
    "en": {
        "h1": "Terms of Service",
        "intro": "These terms apply to the use of this website (ironcustommotors.com) and any service you commission from Iron Custom Motors. By contacting us or booking work you accept them.",
        "sections": [
            ("1. About us", "Iron Custom Motors is a motorcycle workshop registered in Portugal at " + CONTROLLER["address"] + ". Contact: " + CONTROLLER["email"] + " · " + CONTROLLER["phone"] + "."),
            ("2. Site content", "Information on this site is provided in good faith and for guidance only. Prices, timelines and availability published on the site can change; the binding figures are those in the written estimate we send for your specific job."),
            ("3. Service estimates and approval", "We provide written estimates before starting any work. Work begins only after you approve the estimate. We will contact you for written approval before exceeding the agreed scope."),
            ("4. Payment", "Payment is due on completion of work, before the motorcycle is collected, unless otherwise agreed in writing. We accept bank transfer, MB Way, and card payments. Portuguese VAT applies where required."),
            ("5. Warranty", "Workmanship is covered by a 90-day warranty against defects in the work performed. Parts are covered by the manufacturer's warranty (typically 12–24 months). Warranty excludes wear-and-tear items (oils, filters, brake pads, chains, tires), damage from accident, misuse, modification by third parties, or racing/track use."),
            ("6. Pre-purchase inspections", "A pre-purchase inspection is a documented opinion about the visible and testable condition of a motorcycle at the time of inspection. It is not a guarantee of future reliability and does not transfer liability for hidden defects to us. Conclusions are based on observation and standard tests in the time agreed."),
            ("7. Storage of customer motorcycles", "Motorcycles left with us are insured under our workshop insurance for the duration of work. After completion, motorcycles not collected within 30 days may incur a storage fee, communicated in advance."),
            ("8. Liability limits", "Our total liability for any claim relating to a service we performed is limited to the value of that specific service, except where higher liability is mandated by Portuguese consumer law."),
            ("9. Intellectual property", "All photos, text, designs and branding on this website are the property of Iron Custom Motors. Reuse without written permission is not allowed."),
            ("10. Governing law", "These terms are governed by Portuguese law. Disputes can be addressed through the Portuguese consumer mediation system or the competent court of Cascais."),
        ],
        "updated": "Last updated: " + LAST_UPDATED,
    },
    "ru": {
        "h1": "Условия использования",
        "intro": "Эти условия применяются к использованию сайта ironcustommotors.com и любых услуг Iron Custom Motors. Связавшись с нами или заказав работу, вы их принимаете.",
        "sections": [
            ("1. О нас", "Iron Custom Motors — мотомастерская, зарегистрированная в Португалии. Адрес: " + CONTROLLER["address"] + ". Связь: " + CONTROLLER["email"] + " · " + CONTROLLER["phone"] + "."),
            ("2. Информация на сайте", "Информация предоставляется добросовестно и для общего ориентира. Цены, сроки и наличие могут меняться; обязывающие цифры — те, что в письменной смете по вашей задаче."),
            ("3. Сметы и согласование", "Перед началом работ мы выдаём письменную смету. Работа начинается только после её одобрения. Если задача расширяется — связываемся для письменного согласования до выхода за рамки."),
            ("4. Оплата", "Оплата производится по завершении работ, до выдачи мотоцикла, если иное не оговорено письменно. Принимаем банковский перевод, MB Way и карту. НДС Португалии — где требуется."),
            ("5. Гарантия", "На выполненные работы — гарантия 90 дней от дефектов нашей работы. На запчасти — гарантия производителя (обычно 12–24 мес). Гарантия не покрывает расходники (масла, фильтры, колодки, цепи, шины), ущерб от ДТП, неправильной эксплуатации, модификации третьими лицами, гонок/треков."),
            ("6. Предпокупочная инспекция", "Инспекция — задокументированное мнение о видимом и проверяемом состоянии мотоцикла на момент осмотра. Это не гарантия будущей надёжности и не передаёт нам ответственность за скрытые дефекты. Выводы основаны на наблюдении и стандартных тестах в согласованное время."),
            ("7. Хранение клиентских мотоциклов", "Мотоциклы, оставленные у нас, застрахованы в рамках страховки мастерской на время работ. После завершения, не забранные в течение 30 дней мотоциклы могут облагаться платой за хранение, о которой сообщим заранее."),
            ("8. Ограничение ответственности", "Наша совокупная ответственность по любой претензии по конкретной услуге ограничена стоимостью этой услуги, кроме случаев, когда португальское потребительское право требует большего."),
            ("9. Интеллектуальная собственность", "Все фото, тексты, дизайн и брендинг на сайте — собственность Iron Custom Motors. Повторное использование без письменного разрешения запрещено."),
            ("10. Применимое право", "Условия регулируются правом Португалии. Споры — через систему потребительского посредничества Португалии или компетентный суд Кашкайша."),
        ],
        "updated": "Последнее обновление: " + LAST_UPDATED,
    },
    "uk": {
        "h1": "Умови використання",
        "intro": "Ці умови застосовуються до використання сайту ironcustommotors.com і будь-яких послуг Iron Custom Motors. Зв'язавшись з нами або замовивши роботу, ви їх приймаєте.",
        "sections": [
            ("1. Про нас", "Iron Custom Motors — мотомайстерня, зареєстрована в Португалії. Адреса: " + CONTROLLER["address"] + ". Зв'язок: " + CONTROLLER["email"] + " · " + CONTROLLER["phone"] + "."),
            ("2. Інформація на сайті", "Інформація надається добросовісно і для загального орієнтиру. Ціни, терміни й наявність можуть змінюватись; зобов'язуючі цифри — у письмовому кошторисі за вашою задачею."),
            ("3. Кошториси і узгодження", "Перед початком робіт ми видаємо письмовий кошторис. Робота починається лише після його затвердження. Якщо задача розширюється — зв'язуємось для письмового погодження до виходу за межі."),
            ("4. Оплата", "Оплата проводиться по завершенню робіт, до видачі мотоцикла, якщо інше не обумовлено письмово. Приймаємо банківський переказ, MB Way і картку. ПДВ Португалії — де потрібно."),
            ("5. Гарантія", "На виконані роботи — гарантія 90 днів від дефектів нашої роботи. На запчастини — гарантія виробника (зазвичай 12–24 міс). Гарантія не покриває витратники (оливи, фільтри, колодки, ланцюги, шини), пошкодження від ДТП, неправильної експлуатації, модифікації третіми особами, гонок/треків."),
            ("6. Передкупівельна інспекція", "Інспекція — задокументована думка про видимий і перевірюваний стан мотоцикла на момент огляду. Це не гарантія майбутньої надійності і не передає нам відповідальність за приховані дефекти. Висновки базуються на спостереженні та стандартних тестах у погоджений час."),
            ("7. Зберігання клієнтських мотоциклів", "Мотоцикли, залишені в нас, застраховані в межах страхування майстерні на час робіт. Після завершення, не забрані протягом 30 днів мотоцикли можуть оподатковуватись платою за зберігання, про що повідомимо заздалегідь."),
            ("8. Обмеження відповідальності", "Наша сукупна відповідальність за будь-якою претензією по конкретній послузі обмежена вартістю цієї послуги, окрім випадків, коли португальське споживче право вимагає більшого."),
            ("9. Інтелектуальна власність", "Усі фото, тексти, дизайн і брендинг на сайті — власність Iron Custom Motors. Повторне використання без письмового дозволу заборонено."),
            ("10. Застосовне право", "Умови регулюються правом Португалії. Спори — через систему споживчого посередництва Португалії або компетентний суд Кашкайша."),
        ],
        "updated": "Останнє оновлення: " + LAST_UPDATED,
    },
    "pt": {
        "h1": "Termos de Serviço",
        "intro": "Estes termos aplicam-se ao uso deste site (ironcustommotors.com) e a qualquer serviço encomendado à Iron Custom Motors. Ao contactar-nos ou agendar trabalho, aceita-os.",
        "sections": [
            ("1. Sobre nós", "A Iron Custom Motors é uma oficina registada em Portugal em " + CONTROLLER["address"] + ". Contacto: " + CONTROLLER["email"] + " · " + CONTROLLER["phone"] + "."),
            ("2. Conteúdo do site", "A informação é fornecida de boa-fé e a título orientador. Preços, prazos e disponibilidade podem mudar; os valores vinculativos são os do orçamento escrito para a sua intervenção."),
            ("3. Orçamentos e aprovação", "Fornecemos orçamento escrito antes de iniciar qualquer trabalho. O trabalho só começa após a sua aprovação. Para exceder o âmbito acordado contactaremos para nova aprovação por escrito."),
            ("4. Pagamento", "O pagamento é devido na conclusão do trabalho, antes da recolha da moto, salvo acordo escrito em contrário. Aceitamos transferência bancária, MB Way e cartão. Aplica-se IVA português quando exigido."),
            ("5. Garantia", "A mão-de-obra está coberta por garantia de 90 dias contra defeitos do trabalho realizado. As peças têm a garantia do fabricante (geralmente 12–24 meses). A garantia exclui consumíveis (óleos, filtros, pastilhas, correntes, pneus), danos por acidente, uso indevido, modificação por terceiros ou uso em corrida/pista."),
            ("6. Inspeções pré-compra", "A inspeção é um parecer documentado sobre o estado visível e testável da moto no momento da inspeção. Não é garantia de fiabilidade futura nem transfere para nós a responsabilidade por defeitos ocultos. As conclusões baseiam-se na observação e testes padrão no tempo acordado."),
            ("7. Permanência de motas dos clientes", "As motas deixadas connosco estão cobertas pelo seguro da oficina durante a intervenção. Após a conclusão, motas não recolhidas durante 30 dias podem ser sujeitas a taxa de armazenamento, comunicada com antecedência."),
            ("8. Limites de responsabilidade", "A nossa responsabilidade total por qualquer reclamação relativa a um serviço realizado limita-se ao valor desse serviço, exceto quando a lei portuguesa do consumidor obrigue a responsabilidade superior."),
            ("9. Propriedade intelectual", "Todas as fotografias, textos, designs e identidade gráfica do site são propriedade da Iron Custom Motors. A reutilização sem autorização escrita não é permitida."),
            ("10. Lei aplicável", "Estes termos regem-se pela lei portuguesa. Litígios podem ser resolvidos através do sistema português de mediação de consumo ou pelo tribunal competente de Cascais."),
        ],
        "updated": "Última atualização: " + LAST_UPDATED,
    },
}

LEGAL_PAGES = {
    "privacy": (PRIVACY_HEAD, PRIVACY_BODY),
    "cookies": (COOKIES_HEAD, COOKIES_BODY),
    "terms":   (TERMS_HEAD,   TERMS_BODY),
}

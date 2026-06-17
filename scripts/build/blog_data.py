"""
Blog section content: hub + future workshop articles.
Each future post should have full multilingual content (en, ru, uk, pt).

Post slug will be keyed in BLOG_POSTS.
"""

# ============================================================
# Hub /blog/ — title + description + heading per language
# ============================================================

BLOG_HUB_META = {
    "en": {
        "title": "Blog — Motorcycle Workshop Guides | Iron Custom Motors",
        "description": "Practical motorcycle blog from Iron Custom Motors in Cascais: workshop notes, maintenance guidance, diagnostics, parts, upgrades and used-bike advice.",
    },
    "ru": {
        "title": "Блог — полезные материалы мотомастерской | Iron Custom Motors",
        "description": "Практический мотоблог Iron Custom Motors в Кашкайше: заметки из мастерской, обслуживание, диагностика, запчасти, апгрейды и советы по покупке мотоциклов.",
    },
    "uk": {
        "title": "Блог — корисні матеріали мотомайстерні | Iron Custom Motors",
        "description": "Практичний мотоблог Iron Custom Motors у Кашкайші: нотатки з майстерні, обслуговування, діагностика, запчастини, апґрейди та поради щодо купівлі мотоциклів.",
    },
    "pt": {
        "title": "Blog — Guias de Oficina de Motas | Iron Custom Motors",
        "description": "Blog prático de motos da Iron Custom Motors em Cascais: notas de oficina, manutenção, diagnóstico, peças, upgrades e conselhos para comprar motos usadas.",
    },
}

BLOG_HUB_BODY = {
    "en": {
        "eyebrow": "Blog · Workshop knowledge",
        "h1": "Workshop notes for<br/><span class=\"accent\">real riders.</span>",
        "sub": "Useful articles from the Iron Custom Motors bench: maintenance, diagnostics, parts choices, upgrades, pre-purchase checks and the small details that keep motorcycles honest.",
        "breadHome": "Home",
        "h1Crumb": "Blog",
        "readMore": "Read the guide →",
        "noPosts": "The first workshop guide is being prepared.",
        "topicsEyebrow": "What will live here",
        "topicsTitle": "Practical articles, <em>not noise.</em>",
        "topicsLead": "The blog is for useful, searchable material: what riders ask us in the workshop, what we check before buying a bike, how we choose parts, and why some jobs should be done before they become expensive.",
        "topic1Title": "Maintenance",
        "topic1Text": "Service intervals, fluids, brakes, chains, tires and seasonal preparation for Portugal.",
        "topic2Title": "Diagnostics",
        "topic2Text": "How symptoms turn into real causes: electrical, engine, suspension and running issues.",
        "topic3Title": "Parts & upgrades",
        "topic3Text": "OEM, aftermarket and tuning choices explained from a workshop point of view.",
        "topic4Title": "Buying used",
        "topic4Text": "What to inspect before buying a motorcycle and when a cheap bike becomes expensive.",
        "topic5Title": "Workshop life",
        "topic5Text": "Stories from the bench, project decisions and the culture behind Iron Custom Motors.",
        "ctaEyebrow": "Need an answer now?",
        "ctaTitle": "Ask the workshop.",
        "ctaText": "Send your motorcycle model and question via WhatsApp. If it needs a proper check, we will tell you the next step.",
        "btnWA": "WhatsApp us",
        "btnContact": "Contact page",
    },
    "ru": {
        "eyebrow": "Блог · знания из мастерской",
        "h1": "Заметки из мастерской<br/>для <span class=\"accent\">реальных райдеров.</span>",
        "sub": "Полезные материалы от Iron Custom Motors: обслуживание, диагностика, выбор запчастей, апгрейды, предпокупочные проверки и мелочи, которые помогают мотоциклу оставаться честным.",
        "breadHome": "Главная",
        "h1Crumb": "Блог",
        "readMore": "Читать материал →",
        "noPosts": "Первый материал уже готовится.",
        "topicsEyebrow": "Что здесь будет",
        "topicsTitle": "Практические статьи, <em>а не шум.</em>",
        "topicsLead": "Блог нужен для полезных материалов, которые ищут владельцы мотоциклов: что спрашивают в мастерской, что проверять перед покупкой, как выбирать запчасти и почему некоторые работы лучше сделать до того, как они станут дорогими.",
        "topic1Title": "Обслуживание",
        "topic1Text": "Интервалы сервиса, жидкости, тормоза, цепи, шины и сезонная подготовка для Португалии.",
        "topic2Title": "Диагностика",
        "topic2Text": "Как симптомы превращаются в реальные причины: электрика, двигатель, подвеска и ходовая.",
        "topic3Title": "Запчасти и апгрейды",
        "topic3Text": "OEM, aftermarket и тюнинг-решения с точки зрения мастерской.",
        "topic4Title": "Покупка б/у",
        "topic4Text": "Что проверять перед покупкой мотоцикла и когда дешёвый байк становится дорогим.",
        "topic5Title": "Жизнь мастерской",
        "topic5Text": "Истории со стенда, решения по проектам и культура Iron Custom Motors.",
        "ctaEyebrow": "Нужен ответ сейчас?",
        "ctaTitle": "Спросите мастерскую.",
        "ctaText": "Отправьте модель мотоцикла и вопрос в WhatsApp. Если нужна проверка, подскажем следующий шаг.",
        "btnWA": "WhatsApp",
        "btnContact": "Контакты",
    },
    "uk": {
        "eyebrow": "Блог · знання з майстерні",
        "h1": "Нотатки з майстерні<br/>для <span class=\"accent\">реальних райдерів.</span>",
        "sub": "Корисні матеріали від Iron Custom Motors: обслуговування, діагностика, вибір запчастин, апґрейди, передкупівельні перевірки й дрібниці, що допомагають мотоциклу залишатися чесним.",
        "breadHome": "Головна",
        "h1Crumb": "Блог",
        "readMore": "Читати матеріал →",
        "noPosts": "Перший матеріал уже готується.",
        "topicsEyebrow": "Що тут буде",
        "topicsTitle": "Практичні статті, <em>а не шум.</em>",
        "topicsLead": "Блог потрібен для корисних матеріалів, які шукають власники мотоциклів: що запитують у майстерні, що перевіряти перед купівлею, як обирати запчастини і чому деякі роботи краще зробити до того, як вони стануть дорогими.",
        "topic1Title": "Обслуговування",
        "topic1Text": "Інтервали сервісу, рідини, гальма, ланцюги, шини та сезонна підготовка для Португалії.",
        "topic2Title": "Діагностика",
        "topic2Text": "Як симптоми перетворюються на реальні причини: електрика, двигун, підвіска та ходова.",
        "topic3Title": "Запчастини й апґрейди",
        "topic3Text": "OEM, aftermarket і тюнінг-рішення з точки зору майстерні.",
        "topic4Title": "Купівля б/в",
        "topic4Text": "Що перевіряти перед купівлею мотоцикла і коли дешевий байк стає дорогим.",
        "topic5Title": "Життя майстерні",
        "topic5Text": "Історії зі стенда, рішення щодо проєктів і культура Iron Custom Motors.",
        "ctaEyebrow": "Потрібна відповідь зараз?",
        "ctaTitle": "Запитайте майстерню.",
        "ctaText": "Надішліть модель мотоцикла і питання у WhatsApp. Якщо потрібна перевірка, підкажемо наступний крок.",
        "btnWA": "WhatsApp",
        "btnContact": "Контакти",
    },
    "pt": {
        "eyebrow": "Blog · Conhecimento de oficina",
        "h1": "Notas de oficina<br/>para <span class=\"accent\">riders reais.</span>",
        "sub": "Artigos úteis da bancada da Iron Custom Motors: manutenção, diagnóstico, escolha de peças, upgrades, inspeções pré-compra e detalhes que mantêm a moto honesta.",
        "breadHome": "Início",
        "h1Crumb": "Blog",
        "readMore": "Ler o guia →",
        "noPosts": "O primeiro guia de oficina está a ser preparado.",
        "topicsEyebrow": "O que vai viver aqui",
        "topicsTitle": "Artigos práticos, <em>não ruído.</em>",
        "topicsLead": "O blog é para material útil e pesquisável: o que os riders nos perguntam na oficina, o que verificar antes de comprar uma moto, como escolher peças e porque alguns trabalhos devem ser feitos antes de ficarem caros.",
        "topic1Title": "Manutenção",
        "topic1Text": "Intervalos de serviço, fluidos, travões, correntes, pneus e preparação sazonal em Portugal.",
        "topic2Title": "Diagnóstico",
        "topic2Text": "Como sintomas viram causas reais: elétrica, motor, suspensão e comportamento em andamento.",
        "topic3Title": "Peças e upgrades",
        "topic3Text": "OEM, aftermarket e tuning explicados do ponto de vista da oficina.",
        "topic4Title": "Comprar usada",
        "topic4Text": "O que verificar antes de comprar uma moto e quando uma moto barata fica cara.",
        "topic5Title": "Vida de oficina",
        "topic5Text": "Histórias da bancada, decisões de projeto e a cultura por trás da Iron Custom Motors.",
        "ctaEyebrow": "Precisa de resposta agora?",
        "ctaTitle": "Pergunte à oficina.",
        "ctaText": "Envie o modelo da moto e a pergunta por WhatsApp. Se precisar de uma verificação, dizemos o próximo passo.",
        "btnWA": "WhatsApp",
        "btnContact": "Contacto",
    },
}

# Blog posts. Individual posts are generated by build_blog.py.
BLOG_POSTS = {'revtech-110-oil-service-engine-gearbox-drive': {'publishedISO': '2026-06-17',
                                                  'modifiedISO': '2026-06-17',
                                                  'imageBase': '/photos/blog/blog-revtech-110-oil-service',
                                                  'imageHero': 1,
                                                  'imageCount': 1,
                                                  'imageDims': {1: (1600, 900)},
                                                  'youtubeUrl': 'https://www.youtube.com/shorts/ylsQq_bnvU0',
                                                  'youtubeEmbed': 'https://www.youtube.com/embed/ylsQq_bnvU0',
                                                  'sourceLocalizedSlugs': {'en': 'revtech-110-oil-service-engine-gearbox-drive',
                                                                           'ru': 'revtech-110-zamena-masla-dvigatel-korobka-privod',
                                                                           'pt': 'servico-oleo-revtech-110-motor-caixa-transmissao',
                                                                           'uk': 'revtech-110-zamina-olyvy-dvyhun-korobka-pryvid'},
                                                  'meta': {'en': {'title': 'RevTech 110 Oil Service: Engine, Gearbox & '
                                                                           'Drive | Iron Custom Motors',
                                                                  'description': 'Why oil service matters on RevTech '
                                                                                 '110 and similar V-twin engines: '
                                                                                 'engine, gearbox and drive '
                                                                                 'lubrication explained by Iron Custom '
                                                                                 'Motors.',
                                                                  'excerpt': 'Why oil service matters on RevTech 110 '
                                                                             'and similar V-twin engines: engine, '
                                                                             'gearbox and drive lubrication explained '
                                                                             'by Iron Custom Motors.'},
                                                           'ru': {'title': 'Сервис масла RevTech 110: двигатель, КПП и '
                                                                           'привод | Iron Custom Motors',
                                                                  'description': 'Почему замена масла важна для '
                                                                                 'RevTech 110 и похожих V-twin '
                                                                                 'моторов: двигатель, коробка и привод '
                                                                                 'глазами Iron Custom Motors.',
                                                                  'excerpt': 'Почему замена масла важна для RevTech '
                                                                             '110 и похожих V-twin моторов: двигатель, '
                                                                             'коробка и привод глазами Iron Custom '
                                                                             'Motors.'},
                                                           'pt': {'title': 'Serviço de Óleo RevTech 110: Motor, Caixa '
                                                                           'e Transmissão | Iron Custom Motors',
                                                                  'description': 'Porque o serviço de óleo é essencial '
                                                                                 'no RevTech 110 e em V-twin '
                                                                                 'semelhantes: motor, caixa e '
                                                                                 'transmissão explicados pela Iron '
                                                                                 'Custom Motors.',
                                                                  'excerpt': 'Porque o serviço de óleo é essencial no '
                                                                             'RevTech 110 e em V-twin semelhantes: '
                                                                             'motor, caixa e transmissão explicados '
                                                                             'pela Iron Custom Motors.'},
                                                           'uk': {'title': 'Сервіс оливи RevTech 110: двигун, КПП і '
                                                                           'привід | Iron Custom Motors',
                                                                  'description': 'Чому заміна оливи важлива для '
                                                                                 'RevTech 110 і схожих V-twin моторів: '
                                                                                 'двигун, коробка та привід від Iron '
                                                                                 'Custom Motors.',
                                                                  'excerpt': 'Чому заміна оливи важлива для RevTech '
                                                                             '110 і схожих V-twin моторів: двигун, '
                                                                             'коробка та привід від Iron Custom '
                                                                             'Motors.'}},
                                                  'body': {'en': {'eyebrow': 'Workshop guide · 17 June 2026',
                                                                  'publishedLabel': 'Published 17 June 2026',
                                                                  'breadHome': 'Home',
                                                                  'breadBlog': 'Blog',
                                                                  'introTitle': 'What the service includes',
                                                                  'videoEyebrow': 'Workshop video',
                                                                  'videoTitle': 'Watch the RevTech 110 oil service',
                                                                  'videoText': 'A short look at the service: engine '
                                                                               'oil, gearbox oil and drive-side '
                                                                               'lubrication checked as separate '
                                                                               'mechanical zones.',
                                                                  'videoLink': 'Open on YouTube',
                                                                  'faqTitle': 'RevTech 110 oil service FAQ',
                                                                  'ctaEyebrow': 'Need this service?',
                                                                  'ctaTitle': 'Book an oil service or inspection.',
                                                                  'btnWA': 'WhatsApp us',
                                                                  'btnBack': 'Back to blog',
                                                                  'imageAlt': 'RevTech 110 oil service cover graphic '
                                                                              'showing a custom V-twin motorcycle in '
                                                                              'the Iron Custom Motors workshop.',
                                                                  'imageCaption': 'RevTech 110 oil service at Iron '
                                                                                  'Custom Motors: engine, gearbox and '
                                                                                  'drive-side lubrication treated as '
                                                                                  'separate systems.',
                                                                  'h1': 'RevTech 110 Oil Service:<br/><span '
                                                                        'class="accent">Engine, Gearbox & Final '
                                                                        'Drive.</span>',
                                                                  'h1Crumb': 'RevTech 110 Oil Service: Engine, Gearbox '
                                                                             '& Final Drive',
                                                                  'lede': 'A big V-twin rarely fails without giving '
                                                                          'small warnings first. Sometimes the signs '
                                                                          'are obvious: rough shifting, more '
                                                                          'mechanical noise than usual, a clutch that '
                                                                          'feels different, or oil that comes out '
                                                                          'darker and thinner than expected. Sometimes '
                                                                          'there is no clear symptom at all — just a '
                                                                          'motorcycle that has been ridden, heated, '
                                                                          'cooled, stored, started again, and slowly '
                                                                          'asked to work with tired fluids.',
                                                                  'intro': {'title': 'What the service includes',
                                                                            'paragraphs': ['This short video shows an '
                                                                                           'oil service on a RevTech '
                                                                                           '110 setup: engine oil, '
                                                                                           'gearbox oil and drive-side '
                                                                                           'lubrication. For this type '
                                                                                           'of Harley-style custom '
                                                                                           'motorcycle, it is not just '
                                                                                           '“an oil change.” It is a '
                                                                                           'basic health check of '
                                                                                           'three different mechanical '
                                                                                           'zones that work under very '
                                                                                           'different loads.',
                                                                                           'The engine oil deals with '
                                                                                           'heat, combustion '
                                                                                           'by-products and internal '
                                                                                           'friction. The gearbox oil '
                                                                                           'protects loaded gears and '
                                                                                           'bearings. The primary or '
                                                                                           'drive-side lubrication, '
                                                                                           'depending on the exact '
                                                                                           'build, has to work around '
                                                                                           'chain, clutch and rotating '
                                                                                           'components. Treating all '
                                                                                           'of them as the same thing '
                                                                                           'is a common mistake.',
                                                                                           'At Iron Custom Motors, we '
                                                                                           'look at this type of '
                                                                                           'service as a system check, '
                                                                                           'not just a drain-and-fill '
                                                                                           'job.']},
                                                                  'sections': [{'title': 'Why It Matters',
                                                                                'paragraphs': ['On a '
                                                                                               'large-displacement '
                                                                                               'air-cooled or '
                                                                                               'air/oil-cooled V-twin, '
                                                                                               'oil has a difficult '
                                                                                               'life. The engine works '
                                                                                               'with big pistons, '
                                                                                               'strong pulses, high '
                                                                                               'internal loads and a '
                                                                                               'lot of heat. In city '
                                                                                               'traffic around Lisbon '
                                                                                               'or Cascais, that heat '
                                                                                               'does not disappear '
                                                                                               'quickly. Short trips, '
                                                                                               'stop-and-go riding and '
                                                                                               'coastal humidity all '
                                                                                               'make the service '
                                                                                               'environment harder '
                                                                                               'than it looks on '
                                                                                               'paper.',
                                                                                               'Fresh oil does more '
                                                                                               'than reduce friction. '
                                                                                               'It helps carry heat '
                                                                                               'away from critical '
                                                                                               'parts, suspends '
                                                                                               'contamination, '
                                                                                               'protects metal '
                                                                                               'surfaces and keeps '
                                                                                               'internal components '
                                                                                               'working with the '
                                                                                               'correct film strength. '
                                                                                               'When oil is old, '
                                                                                               'contaminated, diluted '
                                                                                               'or simply wrong for '
                                                                                               'the application, the '
                                                                                               'motorcycle may still '
                                                                                               'run — but the '
                                                                                               'protection margin '
                                                                                               'becomes smaller.',
                                                                                               'The gearbox has a '
                                                                                               'different problem. It '
                                                                                               'does not deal with '
                                                                                               'combustion, but it '
                                                                                               'sees high pressure '
                                                                                               'between gear teeth and '
                                                                                               'load changes every '
                                                                                               'time the rider opens '
                                                                                               'or closes the '
                                                                                               'throttle. Old or '
                                                                                               'incorrect gearbox oil '
                                                                                               'can make shifting feel '
                                                                                               'heavier, increase wear '
                                                                                               'on gears and bearings, '
                                                                                               'and make small '
                                                                                               'internal problems '
                                                                                               'harder to detect '
                                                                                               'early.',
                                                                                               'The drive side is '
                                                                                               'another story. On many '
                                                                                               'Harley-style '
                                                                                               'motorcycles, the belt '
                                                                                               'final drive itself is '
                                                                                               'not oil-filled. The '
                                                                                               'oil service usually '
                                                                                               'refers to the primary '
                                                                                               'drive or '
                                                                                               'transmission-related '
                                                                                               'lubricant zones. On a '
                                                                                               'custom motorcycle, '
                                                                                               'especially one built '
                                                                                               'around an aftermarket '
                                                                                               'engine such as a '
                                                                                               'RevTech, the exact '
                                                                                               'configuration must be '
                                                                                               'confirmed before '
                                                                                               'choosing oil, quantity '
                                                                                               'or procedure.']},
                                                                               {'title': 'Main Technical Explanation',
                                                                                'paragraphs': ['Engine oil is the most '
                                                                                               'obvious part of the '
                                                                                               'service, but also the '
                                                                                               'easiest to '
                                                                                               'oversimplify. In a '
                                                                                               'RevTech 110 or similar '
                                                                                               'large V-twin engine, '
                                                                                               'oil works under high '
                                                                                               'thermal and mechanical '
                                                                                               'stress. It must '
                                                                                               'protect bearings, '
                                                                                               'pistons, cylinder '
                                                                                               'walls, cam components '
                                                                                               'and other internal '
                                                                                               'parts while carrying '
                                                                                               'contamination away '
                                                                                               'from those surfaces.',
                                                                                               'Over time, oil loses '
                                                                                               'part of its protective '
                                                                                               'properties. It can '
                                                                                               'oxidize, collect fuel '
                                                                                               'dilution, hold '
                                                                                               'microscopic metal '
                                                                                               'particles and become '
                                                                                               'less stable under '
                                                                                               'heat. That is why an '
                                                                                               'engine oil service '
                                                                                               'should also include '
                                                                                               'looking at the drained '
                                                                                               'oil condition, '
                                                                                               'checking the filter '
                                                                                               'area, inspecting for '
                                                                                               'leaks, and confirming '
                                                                                               'that there are no '
                                                                                               'signs of oil '
                                                                                               'migration, overfilling '
                                                                                               'or external '
                                                                                               'contamination.',
                                                                                               'The oil level and '
                                                                                               'checking procedure can '
                                                                                               'be different depending '
                                                                                               'on the oil tank, '
                                                                                               'frame, engine '
                                                                                               'configuration and '
                                                                                               'whether the bike is '
                                                                                               'checked hot, cold, '
                                                                                               'upright or on the side '
                                                                                               'stand. There is no '
                                                                                               'universal number that '
                                                                                               'should be trusted '
                                                                                               'without the correct '
                                                                                               'manual.',
                                                                                               'The gearbox lives a '
                                                                                               'different life from '
                                                                                               'the engine. It does '
                                                                                               'not see combustion '
                                                                                               'gases, but it sees '
                                                                                               'high pressure between '
                                                                                               'gear teeth and load '
                                                                                               'changes every time the '
                                                                                               'rider opens or closes '
                                                                                               'the throttle. When '
                                                                                               'gearbox oil gets old '
                                                                                               'or contaminated, the '
                                                                                               'rider may notice '
                                                                                               'heavier shifting, more '
                                                                                               'mechanical noise, a '
                                                                                               'less precise feel '
                                                                                               'through the lever, or '
                                                                                               'difficulty finding '
                                                                                               'neutral.',
                                                                                               'The phrase “final '
                                                                                               'drive” can mean '
                                                                                               'different things '
                                                                                               'depending on the '
                                                                                               'motorcycle layout. On '
                                                                                               'many Harley-style '
                                                                                               'motorcycles, the belt '
                                                                                               'final drive itself is '
                                                                                               'not oil-filled. The '
                                                                                               'oil service usually '
                                                                                               'refers to the primary '
                                                                                               'drive or '
                                                                                               'transmission-related '
                                                                                               'lubricant zones. The '
                                                                                               'exact configuration '
                                                                                               'must be confirmed '
                                                                                               'before choosing oil, '
                                                                                               'quantity or '
                                                                                               'procedure.']},
                                                                               {'title': 'Workshop Nuances Riders '
                                                                                         'Often Miss',
                                                                                'bullets': ['Three oil zones do not '
                                                                                            'always want the same oil. '
                                                                                            'The engine, gearbox and '
                                                                                            'clutch or primary area '
                                                                                            'have different mechanical '
                                                                                            'needs. The right choice '
                                                                                            'depends on the actual '
                                                                                            'components installed on '
                                                                                            'the motorcycle.',
                                                                                            '“It starts and rides” '
                                                                                            'does not mean the oil is '
                                                                                            'healthy. A big V-twin can '
                                                                                            'still pull strongly with '
                                                                                            'old oil, but the '
                                                                                            'protection margin may '
                                                                                            'already be reduced.',
                                                                                            'Drain plug debris is '
                                                                                            'information. Fine paste '
                                                                                            'can be normal wear '
                                                                                            'residue, while chips, '
                                                                                            'flakes or heavy metal '
                                                                                            'build-up mean the service '
                                                                                            'should become an '
                                                                                            'inspection.',
                                                                                            'Coastal climate matters. '
                                                                                            'Around Cascais and '
                                                                                            'Lisbon, humidity and sea '
                                                                                            'air can accelerate '
                                                                                            'corrosion around '
                                                                                            'fasteners, electrical '
                                                                                            'connectors, exposed metal '
                                                                                            'and sealing surfaces.',
                                                                                            'Custom builds need '
                                                                                            'rechecking. A '
                                                                                            'RevTech-powered '
                                                                                            'motorcycle may combine '
                                                                                            'aftermarket engine, '
                                                                                            'frame, oil tank, hoses, '
                                                                                            'fittings, gearbox, '
                                                                                            'primary components and '
                                                                                            'exhaust layout. After '
                                                                                            'service, the bike should '
                                                                                            'be checked as a complete '
                                                                                            'system.']},
                                                                               {'title': 'Common Mistakes',
                                                                                'bullets': ['Treating a '
                                                                                            'high-displacement custom '
                                                                                            'V-twin like a generic '
                                                                                            'motorcycle.',
                                                                                            'Changing only engine oil '
                                                                                            'and forgetting the '
                                                                                            'gearbox or primary-drive '
                                                                                            'lubricant.',
                                                                                            'Using universal numbers '
                                                                                            'from the internet instead '
                                                                                            'of the correct '
                                                                                            'documentation.',
                                                                                            'Overfilling. More oil is '
                                                                                            'not automatically safer '
                                                                                            'and can cause leaks, '
                                                                                            'clutch issues or messy '
                                                                                            'breather behavior.',
                                                                                            'Ignoring small leaks '
                                                                                            'after service. A light '
                                                                                            'oil mark can be a simple '
                                                                                            'O-ring issue, but it can '
                                                                                            'also point to a sealing '
                                                                                            'surface, hose, fitting or '
                                                                                            'venting problem.']},
                                                                               {'title': 'When to Visit a Workshop',
                                                                                'paragraphs': ['Book an inspection if '
                                                                                               'shifting becomes '
                                                                                               'heavier or less '
                                                                                               'precise, neutral is '
                                                                                               'harder to find, the '
                                                                                               'clutch starts '
                                                                                               'dragging, the engine '
                                                                                               'sounds harsher than '
                                                                                               'usual, oil leaks '
                                                                                               'appear after a ride, '
                                                                                               'the oil smells burnt '
                                                                                               'or looks unusually '
                                                                                               'contaminated, there '
                                                                                               'are visible metal '
                                                                                               'particles on a drain '
                                                                                               'plug, or the '
                                                                                               'motorcycle has been '
                                                                                               'stored for a long '
                                                                                               'time.',
                                                                                               'These symptoms do not '
                                                                                               'always mean something '
                                                                                               'serious has failed. '
                                                                                               'But they are good '
                                                                                               'reasons to check the '
                                                                                               'motorcycle before a '
                                                                                               'small issue becomes a '
                                                                                               'major repair.']},
                                                                               {'title': 'What We Check at Iron Custom '
                                                                                         'Motors',
                                                                                'paragraphs': ['At Iron Custom Motors, '
                                                                                               'an oil service on a '
                                                                                               'RevTech 110 or similar '
                                                                                               'V-twin is handled as a '
                                                                                               'mechanical inspection, '
                                                                                               'not just a fluid '
                                                                                               'replacement.',
                                                                                               'We check the engine, '
                                                                                               'gearbox and drive-side '
                                                                                               'areas as separate '
                                                                                               'systems. We verify the '
                                                                                               'correct lubricant '
                                                                                               'specification for the '
                                                                                               'actual build, inspect '
                                                                                               'drain plugs and '
                                                                                               'sealing parts, look '
                                                                                               'for signs of oil '
                                                                                               'contamination, check '
                                                                                               'for leaks and make '
                                                                                               'sure the motorcycle is '
                                                                                               'clean and safe before '
                                                                                               'it leaves the '
                                                                                               'workshop.',
                                                                                               'For custom '
                                                                                               'motorcycles, we also '
                                                                                               'pay attention to oil '
                                                                                               'line routing, heat '
                                                                                               'exposure, vibration '
                                                                                               'points, fastener '
                                                                                               'condition, corrosion '
                                                                                               'signs and whether the '
                                                                                               'setup makes sense as a '
                                                                                               'complete system. A '
                                                                                               'good service is not '
                                                                                               'only fresh oil. It is '
                                                                                               'a chance to read the '
                                                                                               'motorcycle.']},
                                                                               {'title': 'Conclusion',
                                                                                'paragraphs': ['Oil service on a '
                                                                                               'RevTech 110 or similar '
                                                                                               'Harley-style V-twin is '
                                                                                               'one of the '
                                                                                               'simplest-looking jobs '
                                                                                               'on the outside and one '
                                                                                               'of the most important '
                                                                                               'maintenance routines '
                                                                                               'for long-term '
                                                                                               'reliability.',
                                                                                               'The engine, gearbox '
                                                                                               'and drive-side '
                                                                                               'components all need '
                                                                                               'the right lubricant, '
                                                                                               'the right level and '
                                                                                               'the right inspection '
                                                                                               'approach. Done '
                                                                                               'properly, this service '
                                                                                               'helps protect the '
                                                                                               'bike, improve riding '
                                                                                               'feel and catch early '
                                                                                               'signs of wear before '
                                                                                               'they become expensive '
                                                                                               'problems.']}],
                                                                  'ctaText': 'If you ride a RevTech-powered custom '
                                                                             'bike, Harley-Davidson, or another big '
                                                                             'V-twin around Cascais or Lisbon, book an '
                                                                             'oil service or inspection at Iron Custom '
                                                                             'Motors. We will check the motorcycle as '
                                                                             'a complete system and explain what needs '
                                                                             'attention, what can wait, and what is '
                                                                             'worth preventing now.',
                                                                  'faqs': [{'q': 'Is oil service on a RevTech 110 the '
                                                                                 'same as on a Harley-Davidson?',
                                                                            'a': 'It can be similar in concept, but it '
                                                                                 'should not be treated as identical '
                                                                                 'without checking the actual engine, '
                                                                                 'gearbox and primary-drive '
                                                                                 'configuration.'},
                                                                           {'q': 'Can the same oil be used for engine, '
                                                                                 'gearbox and primary?',
                                                                            'a': 'Sometimes a lubricant may be '
                                                                                 'approved for multiple zones, but '
                                                                                 'this is not universal. The correct '
                                                                                 'oil depends on the specific engine, '
                                                                                 'transmission, clutch and primary '
                                                                                 'setup.'},
                                                                           {'q': 'Why change gearbox oil if the bike '
                                                                                 'shifts normally?',
                                                                            'a': 'Because wear and oil degradation can '
                                                                                 'build slowly. Fresh, correct oil '
                                                                                 'helps protect gears and bearings and '
                                                                                 'can improve shift feel.'},
                                                                           {'q': 'What happens if the primary or '
                                                                                 'drive-side oil is wrong?',
                                                                            'a': 'Depending on the setup, incorrect '
                                                                                 'lubricant or level can affect clutch '
                                                                                 'behavior, neutral selection, chain '
                                                                                 'lubrication, sealing and component '
                                                                                 'wear.'},
                                                                           {'q': 'How often should oil be changed on a '
                                                                                 'RevTech 110?',
                                                                            'a': 'The interval depends on the engine '
                                                                                 'specification, motorcycle '
                                                                                 'configuration, oil type, riding '
                                                                                 'conditions and manufacturer '
                                                                                 'recommendations.'}]},
                                                           'ru': {'eyebrow': 'Гайд мастерской · 17 июня 2026',
                                                                  'publishedLabel': 'Опубликовано 17 июня 2026',
                                                                  'breadHome': 'Главная',
                                                                  'breadBlog': 'Блог',
                                                                  'introTitle': 'Что входит в этот сервис',
                                                                  'videoEyebrow': 'Видео из мастерской',
                                                                  'videoTitle': 'Смотрите масляный сервис RevTech 110',
                                                                  'videoText': 'Короткий взгляд на сервис: моторное '
                                                                               'масло, масло коробки передач и смазка '
                                                                               'приводной зоны проверяются как '
                                                                               'отдельные механические системы.',
                                                                  'videoLink': 'Открыть на YouTube',
                                                                  'faqTitle': 'FAQ по сервису масла RevTech 110',
                                                                  'ctaEyebrow': 'Нужен такой сервис?',
                                                                  'ctaTitle': 'Запишитесь на замену масла или '
                                                                              'инспекцию.',
                                                                  'btnWA': 'WhatsApp',
                                                                  'btnBack': 'К блогу',
                                                                  'imageAlt': 'Обложка масляного сервиса RevTech 110 с '
                                                                              'кастомным V-twin мотоциклом в '
                                                                              'мастерской Iron Custom Motors.',
                                                                  'imageCaption': 'Масляный сервис RevTech 110 в Iron '
                                                                                  'Custom Motors: двигатель, коробка и '
                                                                                  'приводная зона рассматриваются как '
                                                                                  'отдельные системы.',
                                                                  'h1': 'Сервис масла RevTech 110:<br/><span '
                                                                        'class="accent">двигатель, коробка передач и '
                                                                        'привод.</span>',
                                                                  'h1Crumb': 'Сервис масла RevTech 110: двигатель, '
                                                                             'коробка передач и привод',
                                                                  'lede': 'Большой V-twin редко выходит из строя без '
                                                                          'предупреждения. Иногда признаки заметны '
                                                                          'сразу: передачи включаются грубее, мотор '
                                                                          'звучит механически жёстче, сцепление '
                                                                          'ощущается иначе, а слитое масло выглядит '
                                                                          'темнее и жиже, чем должно. Иногда явных '
                                                                          'симптомов нет вообще — просто мотоцикл '
                                                                          'ездил, грелся, остывал, стоял, снова '
                                                                          'запускался и постепенно работал на уставших '
                                                                          'жидкостях.',
                                                                  'intro': {'title': 'Что входит в этот сервис',
                                                                            'paragraphs': ['В этом коротком видео '
                                                                                           'показан масляный сервис '
                                                                                           'RevTech 110: масло '
                                                                                           'двигателя, масло коробки '
                                                                                           'передач и смазка зоны '
                                                                                           'привода. Для Harley-style '
                                                                                           'custom motorcycle это не '
                                                                                           'просто “замена масла”. Это '
                                                                                           'базовая проверка здоровья '
                                                                                           'трёх разных механических '
                                                                                           'зон, которые работают под '
                                                                                           'разными нагрузками.',
                                                                                           'Моторное масло борется с '
                                                                                           'температурой, продуктами '
                                                                                           'сгорания и внутренним '
                                                                                           'трением. Масло в коробке '
                                                                                           'защищает нагруженные '
                                                                                           'шестерни и подшипники. '
                                                                                           'Первичный привод или зона '
                                                                                           'привода, в зависимости от '
                                                                                           'конкретной сборки, '
                                                                                           'работает с цепью, '
                                                                                           'сцеплением и вращающимися '
                                                                                           'деталями. Считать всё это '
                                                                                           'одной и той же задачей — '
                                                                                           'частая ошибка.',
                                                                                           'В Iron Custom Motors мы '
                                                                                           'относимся к такому сервису '
                                                                                           'как к проверке системы, а '
                                                                                           'не просто как к операции '
                                                                                           '“слил-залил”.']},
                                                                  'sections': [{'title': 'Почему это важно',
                                                                                'paragraphs': ['В крупнообъёмном '
                                                                                               'воздушном или '
                                                                                               'воздушно-масляном '
                                                                                               'V-twin масло живёт '
                                                                                               'тяжёлой жизнью. '
                                                                                               'Большие поршни, '
                                                                                               'сильные импульсы, '
                                                                                               'высокая внутренняя '
                                                                                               'нагрузка и много тепла '
                                                                                               '— нормальная среда для '
                                                                                               'такого мотора. В '
                                                                                               'городском трафике '
                                                                                               'Лиссабона или Кашкайша '
                                                                                               'это тепло уходит не '
                                                                                               'сразу. Короткие '
                                                                                               'поездки, пробки и '
                                                                                               'влажность у океана '
                                                                                               'делают условия работы '
                                                                                               'сложнее, чем кажется '
                                                                                               'по сухому регламенту.',
                                                                                               'Свежее масло не только '
                                                                                               'уменьшает трение. Оно '
                                                                                               'помогает отводить '
                                                                                               'тепло от важных '
                                                                                               'деталей, удерживает '
                                                                                               'загрязнения во взвеси, '
                                                                                               'защищает металл и '
                                                                                               'поддерживает '
                                                                                               'правильную масляную '
                                                                                               'плёнку. Когда масло '
                                                                                               'старое, загрязнённое, '
                                                                                               'разбавленное или '
                                                                                               'просто неподходящее, '
                                                                                               'мотоцикл может '
                                                                                               'продолжать ехать — но '
                                                                                               'запас защиты '
                                                                                               'становится меньше.',
                                                                                               'У коробки передач '
                                                                                               'другая задача. В ней '
                                                                                               'нет продуктов '
                                                                                               'сгорания, зато есть '
                                                                                               'высокое давление между '
                                                                                               'зубьями шестерён и '
                                                                                               'ударные нагрузки при '
                                                                                               'каждом открытии и '
                                                                                               'закрытии газа. Старое '
                                                                                               'или неправильное масло '
                                                                                               'может сделать '
                                                                                               'переключения тяжелее, '
                                                                                               'ускорить износ '
                                                                                               'шестерён и подшипников '
                                                                                               'и скрыть мелкую '
                                                                                               'проблему до того '
                                                                                               'момента, когда она '
                                                                                               'станет дорогой.',
                                                                                               'С зоной привода всё '
                                                                                               'ещё тоньше. На многих '
                                                                                               'Harley-style '
                                                                                               'мотоциклах ременной '
                                                                                               'final drive сам по '
                                                                                               'себе не заполнен '
                                                                                               'маслом. Обычно '
                                                                                               'масляный сервис '
                                                                                               'касается primary drive '
                                                                                               'или трансмиссионных '
                                                                                               'зон, связанных со '
                                                                                               'смазкой. На кастомном '
                                                                                               'мотоцикле, особенно с '
                                                                                               'aftermarket engine '
                                                                                               'вроде RevTech, '
                                                                                               'конкретную '
                                                                                               'конфигурацию нужно '
                                                                                               'подтвердить до выбора '
                                                                                               'масла, объёма и '
                                                                                               'процедуры.']},
                                                                               {'title': 'Основное техническое '
                                                                                         'объяснение',
                                                                                'paragraphs': ['Моторное масло — самая '
                                                                                               'очевидная часть '
                                                                                               'сервиса, но именно её '
                                                                                               'часто упрощают слишком '
                                                                                               'сильно. В RevTech 110 '
                                                                                               'или похожем большом '
                                                                                               'V-twin масло работает '
                                                                                               'при высокой '
                                                                                               'температурной и '
                                                                                               'механической нагрузке. '
                                                                                               'Оно защищает '
                                                                                               'подшипники, поршни, '
                                                                                               'стенки цилиндров, '
                                                                                               'компоненты ГРМ и '
                                                                                               'другие внутренние '
                                                                                               'детали, одновременно '
                                                                                               'уводя загрязнения от '
                                                                                               'рабочих поверхностей.',
                                                                                               'Со временем масло '
                                                                                               'теряет часть защитных '
                                                                                               'свойств. Оно '
                                                                                               'окисляется, может '
                                                                                               'накапливать следы '
                                                                                               'топлива, удерживать '
                                                                                               'микроскопические '
                                                                                               'металлические частицы '
                                                                                               'и хуже переносить '
                                                                                               'высокую температуру. '
                                                                                               'Поэтому сервис '
                                                                                               'двигателя — это не '
                                                                                               'только свежее масло. '
                                                                                               'Нужно оценить '
                                                                                               'состояние слитого '
                                                                                               'масла, проверить зону '
                                                                                               'фильтра, осмотреть '
                                                                                               'возможные подтёки и '
                                                                                               'убедиться, что нет '
                                                                                               'признаков миграции '
                                                                                               'масла, перелива или '
                                                                                               'внешнего загрязнения.',
                                                                                               'Процедура проверки '
                                                                                               'уровня зависит от '
                                                                                               'маслобака, рамы, '
                                                                                               'конфигурации двигателя '
                                                                                               'и даже от того, '
                                                                                               'проверяется ли '
                                                                                               'мотоцикл горячим или '
                                                                                               'холодным, вертикально '
                                                                                               'или на боковой '
                                                                                               'подножке. '
                                                                                               'Универсальных цифр '
                                                                                               'здесь быть не должно: '
                                                                                               'нужен правильный '
                                                                                               'manual под конкретную '
                                                                                               'сборку.',
                                                                                               'Коробка передач живёт '
                                                                                               'иначе, чем двигатель. '
                                                                                               'Она не видит продуктов '
                                                                                               'сгорания, но постоянно '
                                                                                               'работает с давлением '
                                                                                               'между зубьями шестерён '
                                                                                               'и нагрузками при смене '
                                                                                               'тяги. Когда масло в '
                                                                                               'коробке старое или '
                                                                                               'загрязнённое, райдер '
                                                                                               'может почувствовать '
                                                                                               'более тяжёлое '
                                                                                               'переключение, лишний '
                                                                                               'механический шум, '
                                                                                               'менее точный ход лапки '
                                                                                               'или трудности с '
                                                                                               'поиском нейтрали.',
                                                                                               'Фраза “final drive” '
                                                                                               'зависит от конструкции '
                                                                                               'мотоцикла. На многих '
                                                                                               'Harley-style байках '
                                                                                               'ременной финальный '
                                                                                               'привод не имеет '
                                                                                               'масляной ванны. Чаще '
                                                                                               'речь идёт о primary '
                                                                                               'drive или смазке '
                                                                                               'отдельных '
                                                                                               'трансмиссионных зон. '
                                                                                               'Поэтому перед сервисом '
                                                                                               'нужно понимать, что '
                                                                                               'именно установлено на '
                                                                                               'конкретном '
                                                                                               'мотоцикле.']},
                                                                               {'title': 'Нюансы мастерской, которые '
                                                                                         'часто пропускают',
                                                                                'bullets': ['Три масляные зоны не '
                                                                                            'всегда требуют одного и '
                                                                                            'того же масла. Двигатель, '
                                                                                            'коробка и зона сцепления '
                                                                                            'или primary имеют разные '
                                                                                            'механические задачи. '
                                                                                            'Правильный выбор зависит '
                                                                                            'от реально установленных '
                                                                                            'компонентов.',
                                                                                            '“Заводится и едет” не '
                                                                                            'означает, что масло ещё '
                                                                                            'здоровое. Большой V-twin '
                                                                                            'может уверенно тянуть '
                                                                                            'даже на старом масле, но '
                                                                                            'запас защиты уже может '
                                                                                            'быть снижен.',
                                                                                            'Состояние сливной пробки '
                                                                                            '— это информация. Лёгкая '
                                                                                            'металлическая паста может '
                                                                                            'быть обычным следом '
                                                                                            'износа. Стружка, хлопья '
                                                                                            'или необычно большое '
                                                                                            'количество металла — '
                                                                                            'повод превратить замену '
                                                                                            'масла в диагностику.',
                                                                                            'Климат побережья имеет '
                                                                                            'значение. В Кашкайше и '
                                                                                            'Лиссабоне влажность и '
                                                                                            'морской воздух ускоряют '
                                                                                            'коррозию крепежа, '
                                                                                            'контактов, открытого '
                                                                                            'металла и уплотнительных '
                                                                                            'поверхностей.',
                                                                                            'Кастомные сборки нужно '
                                                                                            'перепроверять. Мотоцикл с '
                                                                                            'RevTech может объединять '
                                                                                            'aftermarket двигатель, '
                                                                                            'раму, маслобак, шланги, '
                                                                                            'фитинги, коробку, '
                                                                                            'primary-компоненты и '
                                                                                            'нестандартный выхлоп. '
                                                                                            'После сервиса такой байк '
                                                                                            'нужно смотреть как единую '
                                                                                            'систему.']},
                                                                               {'title': 'Типичные ошибки',
                                                                                'bullets': ['Относиться к крупному '
                                                                                            'кастомному V-twin как к '
                                                                                            'обычному универсальному '
                                                                                            'мотоциклу.',
                                                                                            'Менять только моторное '
                                                                                            'масло и забывать про '
                                                                                            'коробку или primary-drive '
                                                                                            'lubricant.',
                                                                                            'Брать универсальные цифры '
                                                                                            'из интернета вместо '
                                                                                            'документации по '
                                                                                            'конкретному двигателю и '
                                                                                            'компонентам.',
                                                                                            'Переливать масло. Больше '
                                                                                            'масла — не значит '
                                                                                            'безопаснее. В некоторых '
                                                                                            'узлах это приводит к '
                                                                                            'подтёкам, проблемам '
                                                                                            'сцепления или грязной '
                                                                                            'работе вентиляции.',
                                                                                            'Игнорировать небольшие '
                                                                                            'следы масла после '
                                                                                            'сервиса. Маленькое пятно '
                                                                                            'может быть простой '
                                                                                            'проблемой O-ring, а может '
                                                                                            'указывать на '
                                                                                            'уплотнительную '
                                                                                            'поверхность, шланг, '
                                                                                            'фитинг или вентиляцию.']},
                                                                               {'title': 'Когда стоит обратиться в '
                                                                                         'мастерскую',
                                                                                'paragraphs': ['Запишитесь на '
                                                                                               'проверку, если '
                                                                                               'передачи стали '
                                                                                               'включаться тяжелее или '
                                                                                               'менее точно, нейтраль '
                                                                                               'ищется хуже, сцепление '
                                                                                               'начало “тянуть”, мотор '
                                                                                               'звучит жёстче '
                                                                                               'обычного, после '
                                                                                               'поездки появились '
                                                                                               'подтёки, масло пахнет '
                                                                                               'горелым или выглядит '
                                                                                               'необычно загрязнённым, '
                                                                                               'на сливной пробке '
                                                                                               'видны металлические '
                                                                                               'частицы, или мотоцикл '
                                                                                               'долго стоял без '
                                                                                               'обслуживания.',
                                                                                               'Эти признаки не всегда '
                                                                                               'означают серьёзную '
                                                                                               'поломку. Но это '
                                                                                               'хороший повод '
                                                                                               'проверить мотоцикл до '
                                                                                               'того, как маленькая '
                                                                                               'проблема станет '
                                                                                               'большим ремонтом.']},
                                                                               {'title': 'Что мы проверяем в Iron '
                                                                                         'Custom Motors',
                                                                                'paragraphs': ['В Iron Custom Motors '
                                                                                               'масляный сервис '
                                                                                               'RevTech 110 или '
                                                                                               'похожего V-twin — это '
                                                                                               'механическая '
                                                                                               'инспекция, а не просто '
                                                                                               'замена жидкостей.',
                                                                                               'Мы рассматриваем '
                                                                                               'двигатель, коробку и '
                                                                                               'приводную зону как '
                                                                                               'отдельные системы. '
                                                                                               'Проверяем правильную '
                                                                                               'спецификацию масла для '
                                                                                               'конкретной сборки, '
                                                                                               'осматриваем сливные '
                                                                                               'пробки и уплотнения, '
                                                                                               'ищем признаки '
                                                                                               'загрязнения, проверяем '
                                                                                               'подтёки и убеждаемся, '
                                                                                               'что мотоцикл чистый и '
                                                                                               'безопасный перед '
                                                                                               'выдачей.',
                                                                                               'Для кастомных '
                                                                                               'мотоциклов мы также '
                                                                                               'смотрим прокладку '
                                                                                               'масляных линий, зоны '
                                                                                               'нагрева, точки '
                                                                                               'вибрации, состояние '
                                                                                               'крепежа, признаки '
                                                                                               'коррозии и общую '
                                                                                               'логику сборки. Хороший '
                                                                                               'сервис — это не только '
                                                                                               'свежее масло. Это '
                                                                                               'возможность прочитать '
                                                                                               'мотоцикл.']},
                                                                               {'title': 'Вывод',
                                                                                'paragraphs': ['Масляный сервис '
                                                                                               'RevTech 110 или '
                                                                                               'похожего Harley-style '
                                                                                               'V-twin снаружи '
                                                                                               'выглядит простой '
                                                                                               'работой, но для долгой '
                                                                                               'и надёжной жизни '
                                                                                               'мотоцикла это одна из '
                                                                                               'ключевых процедур.',
                                                                                               'Двигатель, коробка и '
                                                                                               'зона привода требуют '
                                                                                               'правильной смазки, '
                                                                                               'правильного уровня и '
                                                                                               'правильного подхода к '
                                                                                               'осмотру. Если всё '
                                                                                               'сделано грамотно, '
                                                                                               'сервис помогает '
                                                                                               'защитить мотоцикл, '
                                                                                               'улучшить ощущение от '
                                                                                               'езды и поймать ранние '
                                                                                               'признаки износа до '
                                                                                               'дорогого ремонта.']}],
                                                                  'ctaText': 'Если вы ездите на кастомном мотоцикле с '
                                                                             'RevTech, Harley-Davidson или другом '
                                                                             'большом V-twin в районе Cascais или '
                                                                             'Lisbon, запишитесь на масляный сервис '
                                                                             'или инспекцию в Iron Custom Motors. Мы '
                                                                             'проверим мотоцикл как систему и спокойно '
                                                                             'объясним, что требует внимания, что '
                                                                             'может подождать, а что лучше '
                                                                             'предотвратить сейчас.',
                                                                  'faqs': [{'q': 'Замена масла на RevTech 110 такая '
                                                                                 'же, как на Harley-Davidson?',
                                                                            'a': 'По логике она может быть похожей, но '
                                                                                 'не должна считаться идентичной без '
                                                                                 'проверки двигателя, коробки и '
                                                                                 'primary-drive конфигурации '
                                                                                 'конкретного мотоцикла.'},
                                                                           {'q': 'Можно ли использовать одно масло для '
                                                                                 'двигателя, коробки и primary?',
                                                                            'a': 'Иногда продукт может быть допущен '
                                                                                 'для нескольких зон, но это не '
                                                                                 'универсальное правило. Всё зависит '
                                                                                 'от двигателя, коробки, сцепления и '
                                                                                 'primary setup.'},
                                                                           {'q': 'Зачем менять масло в коробке, если '
                                                                                 'передачи включаются нормально?',
                                                                            'a': 'Потому что износ и деградация масла '
                                                                                 'накапливаются постепенно. Свежее '
                                                                                 'правильное масло помогает защищать '
                                                                                 'шестерни и подшипники и может '
                                                                                 'улучшить ощущение переключений.'},
                                                                           {'q': 'Что будет, если в primary или зоне '
                                                                                 'привода неправильное масло?',
                                                                            'a': 'В зависимости от конструкции это '
                                                                                 'может повлиять на работу сцепления, '
                                                                                 'поиск нейтрали, смазку цепи, '
                                                                                 'уплотнения и износ деталей.'},
                                                                           {'q': 'Как часто менять масло на RevTech '
                                                                                 '110?',
                                                                            'a': 'Интервал зависит от спецификации '
                                                                                 'двигателя, конфигурации мотоцикла, '
                                                                                 'типа масла, условий езды и '
                                                                                 'рекомендаций производителя.'}]},
                                                           'pt': {'eyebrow': 'Guia da oficina · 17 de junho de 2026',
                                                                  'publishedLabel': 'Publicado em 17 de junho de 2026',
                                                                  'breadHome': 'Início',
                                                                  'breadBlog': 'Blog',
                                                                  'introTitle': 'O que este serviço inclui',
                                                                  'videoEyebrow': 'Vídeo da oficina',
                                                                  'videoTitle': 'Veja o serviço de óleo RevTech 110',
                                                                  'videoText': 'Um olhar curto sobre o serviço: óleo '
                                                                               'do motor, óleo da caixa e lubrificação '
                                                                               'da zona de transmissão verificados '
                                                                               'como sistemas mecânicos separados.',
                                                                  'videoLink': 'Abrir no YouTube',
                                                                  'faqTitle': 'FAQ sobre serviço de óleo RevTech 110',
                                                                  'ctaEyebrow': 'Precisa deste serviço?',
                                                                  'ctaTitle': 'Marque um serviço de óleo ou inspeção.',
                                                                  'btnWA': 'WhatsApp',
                                                                  'btnBack': 'Voltar ao blog',
                                                                  'imageAlt': 'Imagem de capa do serviço de óleo '
                                                                              'RevTech 110 com uma moto custom V-twin '
                                                                              'na oficina Iron Custom Motors.',
                                                                  'imageCaption': 'Serviço de óleo RevTech 110 na Iron '
                                                                                  'Custom Motors: motor, caixa e zona '
                                                                                  'de transmissão tratados como '
                                                                                  'sistemas separados.',
                                                                  'h1': 'Serviço de Óleo RevTech 110:<br/><span '
                                                                        'class="accent">Motor, Caixa de Velocidades e '
                                                                        'Transmissão.</span>',
                                                                  'h1Crumb': 'Serviço de Óleo RevTech 110: Motor, '
                                                                             'Caixa de Velocidades e Transmissão',
                                                                  'lede': 'Um grande V-twin raramente falha sem dar '
                                                                          'pequenos avisos primeiro. Às vezes os '
                                                                          'sinais são claros: mudanças mais duras, '
                                                                          'mais ruído mecânico do que o normal, uma '
                                                                          'embraiagem com sensação diferente, ou óleo '
                                                                          'que sai mais escuro e mais fino do que '
                                                                          'deveria. Outras vezes não há um sintoma '
                                                                          'evidente — apenas uma moto que rodou, '
                                                                          'aqueceu, arrefeceu, ficou parada, voltou a '
                                                                          'arrancar e continuou a trabalhar com '
                                                                          'fluidos já cansados.',
                                                                  'intro': {'title': 'O que este serviço inclui',
                                                                            'paragraphs': ['Este vídeo curto mostra um '
                                                                                           'serviço de óleo num '
                                                                                           'conjunto RevTech 110: óleo '
                                                                                           'do motor, óleo da caixa de '
                                                                                           'velocidades e lubrificação '
                                                                                           'da zona de transmissão. '
                                                                                           'Neste tipo de custom '
                                                                                           'motorcycle ao estilo '
                                                                                           'Harley, isto não é apenas '
                                                                                           '“mudar o óleo”. É uma '
                                                                                           'verificação básica da '
                                                                                           'saúde de três zonas '
                                                                                           'mecânicas diferentes, que '
                                                                                           'trabalham sob cargas muito '
                                                                                           'diferentes.',
                                                                                           'O óleo do motor lida com '
                                                                                           'calor, subprodutos da '
                                                                                           'combustão e atrito '
                                                                                           'interno. O óleo da caixa '
                                                                                           'protege engrenagens e '
                                                                                           'rolamentos sob carga. A '
                                                                                           'lubrificação da primária '
                                                                                           'ou da zona de transmissão, '
                                                                                           'dependendo da configuração '
                                                                                           'exata, pode trabalhar com '
                                                                                           'corrente, embraiagem e '
                                                                                           'componentes em rotação. '
                                                                                           'Tratar tudo como se fosse '
                                                                                           'a mesma coisa é um erro '
                                                                                           'comum.',
                                                                                           'Na Iron Custom Motors, '
                                                                                           'olhamos para este serviço '
                                                                                           'como uma verificação de '
                                                                                           'sistema — não apenas como '
                                                                                           'um simples “drenar e '
                                                                                           'encher”.']},
                                                                  'sections': [{'title': 'Porque é importante',
                                                                                'paragraphs': ['Num V-twin de grande '
                                                                                               'cilindrada, arrefecido '
                                                                                               'a ar ou a ar/óleo, o '
                                                                                               'óleo tem uma vida '
                                                                                               'difícil. O motor '
                                                                                               'trabalha com pistões '
                                                                                               'grandes, pulsações '
                                                                                               'fortes, cargas '
                                                                                               'internas elevadas e '
                                                                                               'muito calor. No '
                                                                                               'trânsito urbano de '
                                                                                               'Lisboa ou Cascais, '
                                                                                               'esse calor não '
                                                                                               'desaparece '
                                                                                               'rapidamente. Percursos '
                                                                                               'curtos, para-arranca e '
                                                                                               'humidade costeira '
                                                                                               'tornam o ambiente de '
                                                                                               'serviço mais exigente '
                                                                                               'do que parece no '
                                                                                               'papel.',
                                                                                               'O óleo novo faz mais '
                                                                                               'do que reduzir atrito. '
                                                                                               'Ajuda a remover calor '
                                                                                               'de zonas críticas, '
                                                                                               'mantém contaminantes '
                                                                                               'em suspensão, protege '
                                                                                               'superfícies metálicas '
                                                                                               'e conserva a película '
                                                                                               'lubrificante correta. '
                                                                                               'Quando o óleo está '
                                                                                               'velho, contaminado, '
                                                                                               'diluído ou '
                                                                                               'simplesmente errado '
                                                                                               'para a aplicação, a '
                                                                                               'moto pode continuar a '
                                                                                               'funcionar — mas a '
                                                                                               'margem de proteção '
                                                                                               'fica menor.',
                                                                                               'A caixa de velocidades '
                                                                                               'tem outro tipo de '
                                                                                               'esforço. Não lida com '
                                                                                               'combustão, mas lida '
                                                                                               'com alta pressão entre '
                                                                                               'dentes de engrenagens '
                                                                                               'e cargas de choque '
                                                                                               'sempre que o piloto '
                                                                                               'abre ou fecha o '
                                                                                               'acelerador. Óleo velho '
                                                                                               'ou incorreto na caixa '
                                                                                               'pode tornar as '
                                                                                               'mudanças mais pesadas, '
                                                                                               'aumentar o desgaste de '
                                                                                               'engrenagens e '
                                                                                               'rolamentos e tornar '
                                                                                               'pequenos problemas '
                                                                                               'internos mais difíceis '
                                                                                               'de detetar cedo.',
                                                                                               'A zona de transmissão '
                                                                                               'exige ainda mais '
                                                                                               'atenção. Em muitas '
                                                                                               'motos ao estilo '
                                                                                               'Harley, a transmissão '
                                                                                               'final por correia não '
                                                                                               'tem banho de óleo. '
                                                                                               'Normalmente, o serviço '
                                                                                               'de óleo refere-se à '
                                                                                               'transmissão primária '
                                                                                               'ou a zonas '
                                                                                               'lubrificadas '
                                                                                               'relacionadas com a '
                                                                                               'transmissão. Numa moto '
                                                                                               'custom, especialmente '
                                                                                               'com um motor '
                                                                                               'aftermarket como o '
                                                                                               'RevTech, a '
                                                                                               'configuração exata '
                                                                                               'deve ser confirmada '
                                                                                               'antes de escolher '
                                                                                               'óleo, quantidade ou '
                                                                                               'procedimento.']},
                                                                               {'title': 'Explicação técnica principal',
                                                                                'paragraphs': ['O óleo do motor é a '
                                                                                               'parte mais evidente do '
                                                                                               'serviço, mas também a '
                                                                                               'mais fácil de '
                                                                                               'simplificar em '
                                                                                               'excesso. Num RevTech '
                                                                                               '110 ou num V-twin '
                                                                                               'grande semelhante, o '
                                                                                               'óleo trabalha sob '
                                                                                               'elevada carga térmica '
                                                                                               'e mecânica. Tem de '
                                                                                               'proteger rolamentos, '
                                                                                               'pistões, paredes dos '
                                                                                               'cilindros, componentes '
                                                                                               'de comando e outras '
                                                                                               'peças internas, ao '
                                                                                               'mesmo tempo que '
                                                                                               'transporta '
                                                                                               'contaminantes para '
                                                                                               'longe das superfícies '
                                                                                               'de trabalho.',
                                                                                               'Com o tempo, o óleo '
                                                                                               'perde parte das suas '
                                                                                               'propriedades de '
                                                                                               'proteção. Pode oxidar, '
                                                                                               'acumular diluição por '
                                                                                               'combustível, reter '
                                                                                               'partículas metálicas '
                                                                                               'microscópicas e '
                                                                                               'tornar-se menos '
                                                                                               'estável com o calor. '
                                                                                               'Por isso, um serviço '
                                                                                               'de óleo do motor deve '
                                                                                               'incluir também a '
                                                                                               'observação do óleo '
                                                                                               'drenado, a verificação '
                                                                                               'da zona do filtro, a '
                                                                                               'inspeção de fugas e a '
                                                                                               'confirmação de que não '
                                                                                               'existem sinais de '
                                                                                               'migração de óleo, '
                                                                                               'excesso de enchimento '
                                                                                               'ou contaminação '
                                                                                               'externa.',
                                                                                               'O nível de óleo e o '
                                                                                               'procedimento de '
                                                                                               'verificação podem '
                                                                                               'mudar conforme o '
                                                                                               'depósito de óleo, '
                                                                                               'quadro, configuração '
                                                                                               'do motor e se a moto é '
                                                                                               'verificada quente, '
                                                                                               'fria, na vertical ou '
                                                                                               'apoiada no descanso '
                                                                                               'lateral. Não existe um '
                                                                                               'número universal que '
                                                                                               'deva ser seguido sem o '
                                                                                               'manual correto.',
                                                                                               'A caixa de velocidades '
                                                                                               'vive uma realidade '
                                                                                               'diferente da do motor. '
                                                                                               'Não recebe gases de '
                                                                                               'combustão, mas suporta '
                                                                                               'alta pressão entre '
                                                                                               'engrenagens e '
                                                                                               'variações de carga '
                                                                                               'sempre que o piloto '
                                                                                               'altera a entrega de '
                                                                                               'potência. Quando o '
                                                                                               'óleo da caixa '
                                                                                               'envelhece ou fica '
                                                                                               'contaminado, o piloto '
                                                                                               'pode notar mudanças '
                                                                                               'mais duras, mais ruído '
                                                                                               'mecânico, menos '
                                                                                               'precisão na alavanca '
                                                                                               'ou dificuldade em '
                                                                                               'encontrar o '
                                                                                               'ponto-morto.',
                                                                                               'A expressão '
                                                                                               '“transmissão final” '
                                                                                               'pode significar coisas '
                                                                                               'diferentes conforme a '
                                                                                               'construção da moto. Em '
                                                                                               'muitas motos ao estilo '
                                                                                               'Harley, a correia '
                                                                                               'final não é '
                                                                                               'lubrificada por óleo. '
                                                                                               'Normalmente fala-se da '
                                                                                               'primária ou de zonas '
                                                                                               'lubrificadas da '
                                                                                               'transmissão. A '
                                                                                               'configuração real tem '
                                                                                               'de ser confirmada '
                                                                                               'antes de decidir óleo, '
                                                                                               'quantidade ou '
                                                                                               'procedimento.']},
                                                                               {'title': 'Nuances de oficina que '
                                                                                         'muitos pilotos não veem',
                                                                                'bullets': ['Três zonas de óleo nem '
                                                                                            'sempre pedem o mesmo '
                                                                                            'lubrificante. Motor, '
                                                                                            'caixa e zona da '
                                                                                            'embraiagem ou primária '
                                                                                            'têm necessidades '
                                                                                            'mecânicas diferentes. A '
                                                                                            'escolha correta depende '
                                                                                            'dos componentes realmente '
                                                                                            'instalados na moto.',
                                                                                            '“Arranca e anda” não '
                                                                                            'significa que o óleo '
                                                                                            'esteja saudável. Um '
                                                                                            'grande V-twin pode '
                                                                                            'continuar a puxar bem com '
                                                                                            'óleo velho, mas a margem '
                                                                                            'de proteção pode já estar '
                                                                                            'reduzida.',
                                                                                            'Os resíduos no bujão de '
                                                                                            'drenagem são informação. '
                                                                                            'Uma pasta metálica fina '
                                                                                            'pode ser desgaste normal. '
                                                                                            'Limalhas, flocos ou '
                                                                                            'excesso de metal '
                                                                                            'significam que o serviço '
                                                                                            'deve passar a inspeção.',
                                                                                            'O clima costeiro importa. '
                                                                                            'Em Cascais e Lisboa, a '
                                                                                            'humidade e o ar marítimo '
                                                                                            'aceleram a corrosão em '
                                                                                            'parafusos, fichas '
                                                                                            'elétricas, metal exposto '
                                                                                            'e superfícies de vedação.',
                                                                                            'As motos custom precisam '
                                                                                            'de nova verificação. Uma '
                                                                                            'moto com motor RevTech '
                                                                                            'pode combinar motor, '
                                                                                            'quadro, depósito de óleo, '
                                                                                            'mangueiras, ligações, '
                                                                                            'caixa, primária e escape '
                                                                                            'aftermarket. Depois do '
                                                                                            'serviço, a moto deve ser '
                                                                                            'verificada como um '
                                                                                            'sistema completo.']},
                                                                               {'title': 'Erros comuns',
                                                                                'bullets': ['Tratar um V-twin custom '
                                                                                            'de grande cilindrada como '
                                                                                            'se fosse uma moto '
                                                                                            'genérica.',
                                                                                            'Mudar apenas o óleo do '
                                                                                            'motor e esquecer o óleo '
                                                                                            'da caixa ou da primária.',
                                                                                            'Usar números universais '
                                                                                            'encontrados na internet '
                                                                                            'em vez da documentação '
                                                                                            'correta.',
                                                                                            'Encher óleo em excesso. '
                                                                                            'Mais óleo não é '
                                                                                            'automaticamente mais '
                                                                                            'seguro e pode causar '
                                                                                            'fugas, problemas de '
                                                                                            'embraiagem ou '
                                                                                            'comportamento sujo da '
                                                                                            'ventilação.',
                                                                                            'Ignorar pequenas fugas '
                                                                                            'depois do serviço. Uma '
                                                                                            'pequena marca de óleo '
                                                                                            'pode ser apenas um '
                                                                                            'O-ring, mas também pode '
                                                                                            'indicar uma superfície de '
                                                                                            'vedação, mangueira, '
                                                                                            'ligação ou ventilação que '
                                                                                            'precisa de atenção.']},
                                                                               {'title': 'Quando visitar uma oficina',
                                                                                'paragraphs': ['Marque uma inspeção se '
                                                                                               'as mudanças ficarem '
                                                                                               'mais pesadas ou menos '
                                                                                               'precisas, se for mais '
                                                                                               'difícil encontrar '
                                                                                               'ponto-morto, se a '
                                                                                               'embraiagem começar a '
                                                                                               'arrastar, se o motor '
                                                                                               'soar mais áspero do '
                                                                                               'que o normal, se '
                                                                                               'aparecerem fugas de '
                                                                                               'óleo depois de rodar, '
                                                                                               'se o óleo cheirar a '
                                                                                               'queimado ou parecer '
                                                                                               'muito contaminado, se '
                                                                                               'houver partículas '
                                                                                               'metálicas visíveis no '
                                                                                               'bujão, ou se a moto '
                                                                                               'esteve parada durante '
                                                                                               'muito tempo.',
                                                                                               'Estes sintomas nem '
                                                                                               'sempre significam uma '
                                                                                               'avaria grave. Mas são '
                                                                                               'boas razões para '
                                                                                               'verificar a moto antes '
                                                                                               'de um pequeno problema '
                                                                                               'se tornar uma '
                                                                                               'reparação cara.']},
                                                                               {'title': 'O que verificamos na Iron '
                                                                                         'Custom Motors',
                                                                                'paragraphs': ['Na Iron Custom Motors, '
                                                                                               'um serviço de óleo num '
                                                                                               'RevTech 110 ou num '
                                                                                               'V-twin semelhante é '
                                                                                               'tratado como uma '
                                                                                               'inspeção mecânica, não '
                                                                                               'apenas como '
                                                                                               'substituição de '
                                                                                               'fluido.',
                                                                                               'Verificamos motor, '
                                                                                               'caixa e zona de '
                                                                                               'transmissão como '
                                                                                               'sistemas separados. '
                                                                                               'Confirmamos a '
                                                                                               'especificação correta '
                                                                                               'de lubrificante para a '
                                                                                               'configuração real, '
                                                                                               'inspecionamos bujões e '
                                                                                               'vedantes, procuramos '
                                                                                               'sinais de '
                                                                                               'contaminação, '
                                                                                               'verificamos fugas e '
                                                                                               'garantimos que a moto '
                                                                                               'sai limpa e segura da '
                                                                                               'oficina.',
                                                                                               'Em motos custom, '
                                                                                               'também observamos '
                                                                                               'passagem das linhas de '
                                                                                               'óleo, exposição ao '
                                                                                               'calor, pontos de '
                                                                                               'vibração, estado dos '
                                                                                               'fixadores, sinais de '
                                                                                               'corrosão e se o '
                                                                                               'conjunto faz sentido '
                                                                                               'como sistema completo. '
                                                                                               'Um bom serviço não é '
                                                                                               'só óleo novo. É uma '
                                                                                               'oportunidade para ler '
                                                                                               'a moto.']},
                                                                               {'title': 'Conclusão',
                                                                                'paragraphs': ['O serviço de óleo num '
                                                                                               'RevTech 110 ou num '
                                                                                               'V-twin ao estilo '
                                                                                               'Harley parece uma '
                                                                                               'tarefa simples por '
                                                                                               'fora, mas é uma das '
                                                                                               'rotinas mais '
                                                                                               'importantes para a '
                                                                                               'fiabilidade a longo '
                                                                                               'prazo.',
                                                                                               'Motor, caixa e zonas '
                                                                                               'de transmissão '
                                                                                               'precisam do '
                                                                                               'lubrificante certo, do '
                                                                                               'nível certo e da '
                                                                                               'abordagem correta de '
                                                                                               'inspeção. Quando feito '
                                                                                               'corretamente, este '
                                                                                               'serviço protege a '
                                                                                               'moto, melhora a '
                                                                                               'sensação de condução e '
                                                                                               'ajuda a detetar sinais '
                                                                                               'iniciais de desgaste '
                                                                                               'antes de se tornarem '
                                                                                               'problemas caros.']}],
                                                                  'ctaText': 'Se conduz uma custom com motor RevTech, '
                                                                             'uma Harley-Davidson ou outro grande '
                                                                             'V-twin em Cascais ou Lisboa, marque um '
                                                                             'serviço de óleo ou uma inspeção na Iron '
                                                                             'Custom Motors. Vamos verificar a moto '
                                                                             'como um sistema completo e explicar o '
                                                                             'que precisa de atenção, o que pode '
                                                                             'esperar e o que vale a pena prevenir '
                                                                             'agora.',
                                                                  'faqs': [{'q': 'O serviço de óleo num RevTech 110 é '
                                                                                 'igual ao de uma Harley-Davidson?',
                                                                            'a': 'Pode ser semelhante no conceito, mas '
                                                                                 'não deve ser tratado como idêntico '
                                                                                 'sem verificar motor, caixa e '
                                                                                 'configuração da primária da moto '
                                                                                 'específica.'},
                                                                           {'q': 'Pode usar-se o mesmo óleo no motor, '
                                                                                 'caixa e primária?',
                                                                            'a': 'Às vezes um lubrificante pode ser '
                                                                                 'aprovado para várias zonas, mas isso '
                                                                                 'não é uma regra universal. Depende '
                                                                                 'do motor, transmissão, embraiagem e '
                                                                                 'configuração da primária.'},
                                                                           {'q': 'Porque mudar o óleo da caixa se as '
                                                                                 'mudanças entram normalmente?',
                                                                            'a': 'Porque o desgaste e a degradação do '
                                                                                 'óleo acumulam-se gradualmente. Óleo '
                                                                                 'correto e novo ajuda a proteger '
                                                                                 'engrenagens e rolamentos e pode '
                                                                                 'melhorar a sensação das mudanças.'},
                                                                           {'q': 'O que acontece se o óleo da primária '
                                                                                 'ou da transmissão estiver errado?',
                                                                            'a': 'Dependendo da configuração, pode '
                                                                                 'afetar a embraiagem, a seleção do '
                                                                                 'ponto-morto, a lubrificação da '
                                                                                 'corrente, vedantes e desgaste de '
                                                                                 'componentes.'},
                                                                           {'q': 'Com que frequência deve ser mudado o '
                                                                                 'óleo num RevTech 110?',
                                                                            'a': 'O intervalo depende da especificação '
                                                                                 'do motor, configuração da moto, tipo '
                                                                                 'de óleo, condições de condução e '
                                                                                 'recomendações do fabricante.'}]},
                                                           'uk': {'eyebrow': 'Гайд майстерні · 17 червня 2026',
                                                                  'publishedLabel': 'Опубліковано 17 червня 2026',
                                                                  'breadHome': 'Головна',
                                                                  'breadBlog': 'Блог',
                                                                  'introTitle': 'Що входить у цей сервіс',
                                                                  'videoEyebrow': 'Відео з майстерні',
                                                                  'videoTitle': 'Дивіться сервіс оливи RevTech 110',
                                                                  'videoText': 'Короткий погляд на сервіс: моторна '
                                                                               'олива, олива коробки передач і '
                                                                               'змащення зони приводу перевіряються як '
                                                                               'окремі механічні системи.',
                                                                  'videoLink': 'Відкрити на YouTube',
                                                                  'faqTitle': 'FAQ щодо сервісу оливи RevTech 110',
                                                                  'ctaEyebrow': 'Потрібен такий сервіс?',
                                                                  'ctaTitle': 'Запишіться на сервіс оливи або '
                                                                              'інспекцію.',
                                                                  'btnWA': 'WhatsApp',
                                                                  'btnBack': 'До блогу',
                                                                  'imageAlt': 'Обкладинка сервісу оливи RevTech 110 з '
                                                                              'кастомним V-twin мотоциклом у майстерні '
                                                                              'Iron Custom Motors.',
                                                                  'imageCaption': 'Сервіс оливи RevTech 110 в Iron '
                                                                                  'Custom Motors: двигун, коробка та '
                                                                                  'зона приводу розглядаються як '
                                                                                  'окремі системи.',
                                                                  'h1': 'Сервіс оливи RevTech 110:<br/><span '
                                                                        'class="accent">двигун, коробка передач і '
                                                                        'привід.</span>',
                                                                  'h1Crumb': 'Сервіс оливи RevTech 110: двигун, '
                                                                             'коробка передач і привід',
                                                                  'lede': 'Великий V-twin рідко виходить з ладу без '
                                                                          'попереджень. Іноді ознаки очевидні: '
                                                                          'передачі вмикаються грубіше, мотор звучить '
                                                                          'механічно жорсткіше, зчеплення відчувається '
                                                                          'інакше, а злита олива темніша й рідша, ніж '
                                                                          'очікувалося. Інколи явного симптому немає — '
                                                                          'просто мотоцикл їздив, нагрівався, '
                                                                          'охолоджувався, стояв, знову запускався і '
                                                                          'поступово працював на втомлених рідинах.',
                                                                  'intro': {'title': 'Що входить у цей сервіс',
                                                                            'paragraphs': ['У цьому короткому відео '
                                                                                           'показано сервіс оливи на '
                                                                                           'RevTech 110: моторна '
                                                                                           'олива, олива коробки '
                                                                                           'передач і змащення зони '
                                                                                           'приводу. Для Harley-style '
                                                                                           'custom motorcycle це не '
                                                                                           'просто “заміна оливи”. Це '
                                                                                           'базова перевірка стану '
                                                                                           'трьох різних механічних '
                                                                                           'зон, які працюють під '
                                                                                           'різними навантаженнями.',
                                                                                           'Моторна олива працює з '
                                                                                           'температурою, продуктами '
                                                                                           'згоряння та внутрішнім '
                                                                                           'тертям. Олива в коробці '
                                                                                           'захищає навантажені '
                                                                                           'шестерні та підшипники. '
                                                                                           'Первинний привід або зона '
                                                                                           'приводу, залежно від '
                                                                                           'конкретної збірки, може '
                                                                                           'працювати з ланцюгом, '
                                                                                           'зчепленням і деталями, що '
                                                                                           'обертаються. Сприймати все '
                                                                                           'це як одну й ту саму '
                                                                                           'операцію — поширена '
                                                                                           'помилка.',
                                                                                           'В Iron Custom Motors ми '
                                                                                           'дивимося на такий сервіс '
                                                                                           'як на перевірку системи, а '
                                                                                           'не просто як на процедуру '
                                                                                           '“злив-залив”.']},
                                                                  'sections': [{'title': 'Чому це важливо',
                                                                                'paragraphs': ['У великооб’ємному '
                                                                                               'повітряному або '
                                                                                               'повітряно-оливному '
                                                                                               'V-twin олива має '
                                                                                               'непросте життя. Двигун '
                                                                                               'працює з великими '
                                                                                               'поршнями, сильними '
                                                                                               'імпульсами, високими '
                                                                                               'внутрішніми '
                                                                                               'навантаженнями та '
                                                                                               'значною температурою. '
                                                                                               'У міському трафіку '
                                                                                               'Лісабона чи Кашкайша '
                                                                                               'це тепло не зникає '
                                                                                               'швидко. Короткі '
                                                                                               'поїздки, затори та '
                                                                                               'вологість біля океану '
                                                                                               'роблять умови '
                                                                                               'експлуатації важчими, '
                                                                                               'ніж здається за '
                                                                                               'регламентом.',
                                                                                               'Свіжа олива не лише '
                                                                                               'зменшує тертя. Вона '
                                                                                               'допомагає відводити '
                                                                                               'тепло від критичних '
                                                                                               'деталей, утримує '
                                                                                               'забруднення у '
                                                                                               'зваженому стані, '
                                                                                               'захищає металеві '
                                                                                               'поверхні й підтримує '
                                                                                               'правильну оливну '
                                                                                               'плівку. Коли олива '
                                                                                               'стара, забруднена, '
                                                                                               'розбавлена або просто '
                                                                                               'не підходить для '
                                                                                               'конкретного вузла, '
                                                                                               'мотоцикл може їхати — '
                                                                                               'але запас захисту вже '
                                                                                               'менший.',
                                                                                               'Коробка передач має '
                                                                                               'інше завдання. У ній '
                                                                                               'немає продуктів '
                                                                                               'згоряння, зате є '
                                                                                               'високий тиск між '
                                                                                               'зубцями шестерень і '
                                                                                               'ударні навантаження '
                                                                                               'кожного разу, коли '
                                                                                               'райдер відкриває або '
                                                                                               'закриває газ. Стара чи '
                                                                                               'неправильна олива в '
                                                                                               'коробці може зробити '
                                                                                               'перемикання важчим, '
                                                                                               'прискорити знос '
                                                                                               'шестерень і '
                                                                                               'підшипників та '
                                                                                               'приховати дрібну '
                                                                                               'проблему до моменту, '
                                                                                               'коли вона стане '
                                                                                               'дорогою.',
                                                                                               'Зона приводу потребує '
                                                                                               'окремої уваги. На '
                                                                                               'багатьох Harley-style '
                                                                                               'мотоциклах ремінний '
                                                                                               'final drive сам по '
                                                                                               'собі не заповнений '
                                                                                               'оливою. Зазвичай '
                                                                                               'оливний сервіс '
                                                                                               'стосується primary '
                                                                                               'drive або змащуваних '
                                                                                               'зон трансмісії. На '
                                                                                               'кастомному мотоциклі, '
                                                                                               'особливо з aftermarket '
                                                                                               'engine на кшталт '
                                                                                               'RevTech, точну '
                                                                                               'конфігурацію потрібно '
                                                                                               'підтвердити до вибору '
                                                                                               'оливи, кількості та '
                                                                                               'процедури.']},
                                                                               {'title': 'Основне технічне пояснення',
                                                                                'paragraphs': ['Моторна олива — '
                                                                                               'найочевидніша частина '
                                                                                               'сервісу, але саме її '
                                                                                               'найчастіше надто '
                                                                                               'спрощують. У RevTech '
                                                                                               '110 або схожому '
                                                                                               'великому V-twin олива '
                                                                                               'працює під високим '
                                                                                               'тепловим і механічним '
                                                                                               'навантаженням. Вона '
                                                                                               'має захищати '
                                                                                               'підшипники, поршні, '
                                                                                               'стінки циліндрів, '
                                                                                               'компоненти ГРМ та інші '
                                                                                               'внутрішні деталі, '
                                                                                               'одночасно відводячи '
                                                                                               'забруднення від '
                                                                                               'робочих поверхонь.',
                                                                                               'З часом олива втрачає '
                                                                                               'частину захисних '
                                                                                               'властивостей. Вона '
                                                                                               'може окислюватися, '
                                                                                               'накопичувати сліди '
                                                                                               'палива, утримувати '
                                                                                               'мікроскопічні металеві '
                                                                                               'частинки й гірше '
                                                                                               'переносити високу '
                                                                                               'температуру. Тому '
                                                                                               'сервіс моторної оливи '
                                                                                               'має включати не тільки '
                                                                                               'заміну, а й оцінку '
                                                                                               'стану злитої оливи, '
                                                                                               'перевірку зони '
                                                                                               'фільтра, огляд на '
                                                                                               'підтікання та '
                                                                                               'підтвердження, що '
                                                                                               'немає ознак міграції '
                                                                                               'оливи, переливу або '
                                                                                               'зовнішнього '
                                                                                               'забруднення.',
                                                                                               'Рівень оливи та '
                                                                                               'процедура перевірки '
                                                                                               'можуть відрізнятися '
                                                                                               'залежно від оливного '
                                                                                               'бака, рами, '
                                                                                               'конфігурації двигуна і '
                                                                                               'навіть від того, чи '
                                                                                               'перевіряється мотоцикл '
                                                                                               'гарячим, холодним, '
                                                                                               'вертикально або на '
                                                                                               'боковій підніжці. '
                                                                                               'Універсальним цифрам '
                                                                                               'без правильного manual '
                                                                                               'довіряти не можна.',
                                                                                               'Коробка передач живе '
                                                                                               'інакше, ніж двигун. '
                                                                                               'Вона не бачить газів '
                                                                                               'згоряння, але постійно '
                                                                                               'працює з тиском між '
                                                                                               'шестернями та зміною '
                                                                                               'навантажень. Коли '
                                                                                               'олива в коробці стара '
                                                                                               'або забруднена, райдер '
                                                                                               'може відчути важче '
                                                                                               'перемикання, зайвий '
                                                                                               'механічний шум, менш '
                                                                                               'точний хід лапки або '
                                                                                               'складніший пошук '
                                                                                               'нейтралі.',
                                                                                               'Фраза “final drive” '
                                                                                               'може означати різні '
                                                                                               'речі залежно від '
                                                                                               'конструкції мотоцикла. '
                                                                                               'На багатьох '
                                                                                               'Harley-style байках '
                                                                                               'ремінний фінальний '
                                                                                               'привід не має оливної '
                                                                                               'ванни. Найчастіше '
                                                                                               'йдеться про primary '
                                                                                               'drive або окремі '
                                                                                               'змащувані зони '
                                                                                               'трансмісії. Реальну '
                                                                                               'конфігурацію потрібно '
                                                                                               'підтвердити перед '
                                                                                               'вибором оливи, '
                                                                                               'кількості чи '
                                                                                               'процедури.']},
                                                                               {'title': 'Нюанси майстерні, які часто '
                                                                                         'не помічають',
                                                                                'bullets': ['Три оливні зони не завжди '
                                                                                            'потребують однієї й тієї '
                                                                                            'самої оливи. Двигун, '
                                                                                            'коробка та зона зчеплення '
                                                                                            'або primary мають різні '
                                                                                            'механічні потреби. '
                                                                                            'Правильний вибір залежить '
                                                                                            'від фактично встановлених '
                                                                                            'компонентів.',
                                                                                            '“Заводиться і їде” не '
                                                                                            'означає, що олива '
                                                                                            'здорова. Великий V-twin '
                                                                                            'може впевнено тягнути '
                                                                                            'навіть зі старою оливою, '
                                                                                            'але запас захисту вже '
                                                                                            'може бути зменшений.',
                                                                                            'Сміття на зливній пробці '
                                                                                            '— це інформація. Легка '
                                                                                            'металева паста може бути '
                                                                                            'нормальним слідом зносу. '
                                                                                            'Стружка, пластівці або '
                                                                                            'надмірна кількість металу '
                                                                                            'означають, що сервіс має '
                                                                                            'перейти в інспекцію.',
                                                                                            'Клімат узбережжя має '
                                                                                            'значення. У Кашкайші та '
                                                                                            'Лісабоні вологість і '
                                                                                            'морське повітря '
                                                                                            'прискорюють корозію '
                                                                                            'кріплення, електричних '
                                                                                            'контактів, відкритого '
                                                                                            'металу та ущільнювальних '
                                                                                            'поверхонь.',
                                                                                            'Кастомні збірки потрібно '
                                                                                            'перевіряти повторно. '
                                                                                            'Мотоцикл із RevTech може '
                                                                                            'поєднувати aftermarket '
                                                                                            'двигун, раму, оливний '
                                                                                            'бак, шланги, фітинги, '
                                                                                            'коробку, '
                                                                                            'primary-компоненти та '
                                                                                            'нестандартний вихлоп. '
                                                                                            'Після сервісу такий байк '
                                                                                            'треба дивитися як єдину '
                                                                                            'систему.']},
                                                                               {'title': 'Типові помилки',
                                                                                'bullets': ['Ставитися до великого '
                                                                                            'кастомного V-twin як до '
                                                                                            'звичайного універсального '
                                                                                            'мотоцикла.',
                                                                                            'Міняти тільки моторну '
                                                                                            'оливу й забувати про '
                                                                                            'коробку або primary-drive '
                                                                                            'lubricant.',
                                                                                            'Використовувати '
                                                                                            'універсальні цифри з '
                                                                                            'інтернету замість '
                                                                                            'документації для '
                                                                                            'конкретного двигуна та '
                                                                                            'компонентів.',
                                                                                            'Переливати оливу. Більше '
                                                                                            'оливи — не означає '
                                                                                            'безпечніше. У деяких '
                                                                                            'вузлах це може спричинити '
                                                                                            'підтікання, проблеми зі '
                                                                                            'зчепленням або брудну '
                                                                                            'роботу вентиляції.',
                                                                                            'Ігнорувати невеликі сліди '
                                                                                            'оливи після сервісу. '
                                                                                            'Маленька пляма може бути '
                                                                                            'просто проблемою O-ring, '
                                                                                            'але також може вказувати '
                                                                                            'на ущільнювальну '
                                                                                            'поверхню, шланг, фітинг '
                                                                                            'або вентиляцію.']},
                                                                               {'title': 'Коли варто звернутися до '
                                                                                         'майстерні',
                                                                                'paragraphs': ['Запишіться на '
                                                                                               'перевірку, якщо '
                                                                                               'передачі стали '
                                                                                               'вмикатися важче або '
                                                                                               'менш точно, нейтраль '
                                                                                               'знайти складніше, '
                                                                                               'зчеплення почало '
                                                                                               '“тягнути”, двигун '
                                                                                               'звучить жорсткіше, ніж '
                                                                                               'зазвичай, після '
                                                                                               'поїздки з’явилися '
                                                                                               'підтікання, олива '
                                                                                               'пахне горілим або '
                                                                                               'виглядає надто '
                                                                                               'забрудненою, на '
                                                                                               'зливній пробці видно '
                                                                                               'металеві частинки, або '
                                                                                               'мотоцикл довго стояв '
                                                                                               'без сервісу.',
                                                                                               'Ці симптоми не завжди '
                                                                                               'означають серйозну '
                                                                                               'поломку. Але це вагомі '
                                                                                               'причини перевірити '
                                                                                               'мотоцикл до того, як '
                                                                                               'маленька проблема '
                                                                                               'перетвориться на '
                                                                                               'великий ремонт.']},
                                                                               {'title': 'Що ми перевіряємо в Iron '
                                                                                         'Custom Motors',
                                                                                'paragraphs': ['В Iron Custom Motors '
                                                                                               'сервіс оливи на '
                                                                                               'RevTech 110 або '
                                                                                               'схожому V-twin — це '
                                                                                               'механічна інспекція, а '
                                                                                               'не просто заміна '
                                                                                               'рідин.',
                                                                                               'Ми перевіряємо двигун, '
                                                                                               'коробку та зону '
                                                                                               'приводу як окремі '
                                                                                               'системи. Підтверджуємо '
                                                                                               'правильну специфікацію '
                                                                                               'оливи для конкретної '
                                                                                               'збірки, оглядаємо '
                                                                                               'зливні пробки та '
                                                                                               'ущільнення, шукаємо '
                                                                                               'ознаки забруднення, '
                                                                                               'перевіряємо підтікання '
                                                                                               'і переконуємося, що '
                                                                                               'мотоцикл чистий та '
                                                                                               'безпечний перед '
                                                                                               'видачею.',
                                                                                               'Для кастомних '
                                                                                               'мотоциклів ми також '
                                                                                               'дивимося прокладання '
                                                                                               'оливних ліній, зони '
                                                                                               'нагріву, точки '
                                                                                               'вібрації, стан '
                                                                                               'кріплення, ознаки '
                                                                                               'корозії та загальну '
                                                                                               'логіку збірки. Хороший '
                                                                                               'сервіс — це не тільки '
                                                                                               'свіжа олива. Це '
                                                                                               'можливість прочитати '
                                                                                               'мотоцикл.']},
                                                                               {'title': 'Висновок',
                                                                                'paragraphs': ['Сервіс оливи на '
                                                                                               'RevTech 110 або '
                                                                                               'схожому Harley-style '
                                                                                               'V-twin зовні виглядає '
                                                                                               'простою роботою, але '
                                                                                               'для довгої надійної '
                                                                                               'служби мотоцикла це '
                                                                                               'одна з ключових '
                                                                                               'процедур.',
                                                                                               'Двигун, коробка та '
                                                                                               'зона приводу '
                                                                                               'потребують правильної '
                                                                                               'оливи, правильного '
                                                                                               'рівня й правильного '
                                                                                               'підходу до огляду. '
                                                                                               'Якщо все зроблено '
                                                                                               'грамотно, сервіс '
                                                                                               'допомагає захистити '
                                                                                               'мотоцикл, покращити '
                                                                                               'відчуття від їзди й '
                                                                                               'упіймати ранні ознаки '
                                                                                               'зносу до дорогого '
                                                                                               'ремонту.']}],
                                                                  'ctaText': 'Якщо ви їздите на кастомному мотоциклі з '
                                                                             'RevTech, Harley-Davidson або іншому '
                                                                             'великому V-twin у районі Cascais чи '
                                                                             'Lisbon, запишіться на сервіс оливи або '
                                                                             'інспекцію в Iron Custom Motors. Ми '
                                                                             'перевіримо мотоцикл як систему й '
                                                                             'спокійно пояснимо, що потребує уваги, що '
                                                                             'може зачекати, а що краще попередити вже '
                                                                             'зараз.',
                                                                  'faqs': [{'q': 'Сервіс оливи на RevTech 110 такий '
                                                                                 'самий, як на Harley-Davidson?',
                                                                            'a': 'За логікою він може бути схожим, але '
                                                                                 'не має вважатися ідентичним без '
                                                                                 'перевірки двигуна, коробки та '
                                                                                 'primary-drive конфігурації '
                                                                                 'конкретного мотоцикла.'},
                                                                           {'q': 'Чи можна використовувати одну оливу '
                                                                                 'для двигуна, коробки та primary?',
                                                                            'a': 'Іноді мастило може бути дозволене '
                                                                                 'для кількох зон, але це не '
                                                                                 'універсальне правило. Усе залежить '
                                                                                 'від двигуна, коробки, зчеплення та '
                                                                                 'primary setup.'},
                                                                           {'q': 'Навіщо міняти оливу в коробці, якщо '
                                                                                 'передачі вмикаються нормально?',
                                                                            'a': 'Тому що знос і деградація оливи '
                                                                                 'накопичуються поступово. Свіжа '
                                                                                 'правильна олива допомагає захищати '
                                                                                 'шестерні та підшипники й може '
                                                                                 'покращити відчуття перемикання.'},
                                                                           {'q': 'Що буде, якщо в primary або зоні '
                                                                                 'приводу неправильна олива?',
                                                                            'a': 'Залежно від конструкції це може '
                                                                                 'вплинути на роботу зчеплення, пошук '
                                                                                 'нейтралі, змащення ланцюга, '
                                                                                 'ущільнення та знос компонентів.'},
                                                                           {'q': 'Як часто міняти оливу на RevTech '
                                                                                 '110?',
                                                                            'a': 'Інтервал залежить від специфікації '
                                                                                 'двигуна, конфігурації мотоцикла, '
                                                                                 'типу оливи, умов їзди та '
                                                                                 'рекомендацій виробника.'}]}},
                                                  'keywords': {'en': ['RevTech 110 oil service',
                                                                      'Harley-style V-twin maintenance',
                                                                      'engine oil',
                                                                      'gearbox oil',
                                                                      'primary drive service',
                                                                      'motorcycle service Cascais'],
                                                               'ru': ['сервис масла RevTech 110',
                                                                      'обслуживание V-twin',
                                                                      'моторное масло',
                                                                      'масло коробки передач',
                                                                      'primary drive',
                                                                      'мотосервис Кашкайш'],
                                                               'uk': ['сервіс оливи RevTech 110',
                                                                      'обслуговування V-twin',
                                                                      'моторна олива',
                                                                      'олива коробки передач',
                                                                      'primary drive',
                                                                      'мотосервіс Кашкайш'],
                                                               'pt': ['serviço de óleo RevTech 110',
                                                                      'manutenção V-twin',
                                                                      'óleo do motor',
                                                                      'óleo da caixa',
                                                                      'primária',
                                                                      'serviço de motos Cascais']}}}

#!/usr/bin/env python3
"""Add reusable highlights, significance and related links to project pages."""

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup, FeatureNotFound

SITE_ROOT = Path(__file__).resolve().parents[2]
BUILD_DIR = Path(__file__).resolve().parent
TARGET_LANGS = ["en", "ru", "uk", "pt"]
PROJECTS = [
    "inspirium",
    "beckman",
    "unbreakable",
    "quanta-r",
    "burly",
    "sturmvogel",
    "geometric",
    "joker",
    "hellboy",
    "true-religion",
]

try:
    BeautifulSoup("", "lxml")
    HTML_PARSER = "lxml"
except FeatureNotFound:
    HTML_PARSER = "html.parser"

GLOBAL_I18N = json.loads((BUILD_DIR / "i18n.json").read_text(encoding="utf-8"))

COMMON_I18N = {
    "en": {
        "projx.highlightsEyebrow": "Project highlights",
        "projx.highlightsTitle": "What this build <em>proves.</em>",
        "projx.highlightsLead": "Each project is documented as an engineering and brand reference, not just a gallery item.",
        "projx.h1t": "Achievement",
        "projx.h1d": "The public result or recognition attached to this motorcycle.",
        "projx.h2t": "Category",
        "projx.h2d": "The technical or cultural class this project belongs to.",
        "projx.h3t": "Context",
        "projx.h3d": "Where the project lived, competed, was shown or became part of the Iron Custom Motors story.",
        "projx.whyEyebrow": "Why it matters",
        "projx.whyTitle": "A reference point for the <em>current workshop.</em>",
        "projx.whyText": "This build explains the standard behind the Cascais workshop today: disciplined engineering, visual taste, documentation and the ability to solve unusual motorcycle problems.",
        "projx.relatedEyebrow": "Next steps",
        "projx.relatedTitle": "From project story to <em>workshop action.</em>",
        "projx.relatedLead": "Explore the portfolio, discuss a custom idea, or connect this experience to service, parts and upgrades.",
        "projx.relatedText": "Open the related page for service context, booking options or the broader Iron Custom Motors story.",
    },
    "ru": {
        "projx.highlightsEyebrow": "Ключевые акценты",
        "projx.highlightsTitle": "Что эта сборка <em>доказывает.</em>",
        "projx.highlightsLead": "Каждый проект описан как инженерный и брендовый ориентир, а не просто пункт галереи.",
        "projx.h1t": "Достижение",
        "projx.h1d": "Публичный результат или признание, связанное с этим мотоциклом.",
        "projx.h2t": "Категория",
        "projx.h2d": "Технический или культурный класс, к которому относится проект.",
        "projx.h3t": "Контекст",
        "projx.h3d": "Где проект жил, выступал, показывался или стал частью истории Iron Custom Motors.",
        "projx.whyEyebrow": "Почему это важно",
        "projx.whyTitle": "Ориентир для <em>нынешней мастерской.</em>",
        "projx.whyText": "Эта сборка объясняет стандарт мастерской в Cascais сегодня: дисциплинированная инженерия, визуальный вкус, документация и способность решать нестандартные мотоциклетные задачи.",
        "projx.relatedEyebrow": "Следующие шаги",
        "projx.relatedTitle": "От истории проекта к <em>действию в мастерской.</em>",
        "projx.relatedLead": "Посмотрите портфолио, обсудите кастомную идею или свяжите этот опыт с сервисом, запчастями и апгрейдами.",
        "projx.relatedText": "Откройте связанную страницу для сервисного контекста, вариантов записи или широкой истории Iron Custom Motors.",
    },
    "uk": {
        "projx.highlightsEyebrow": "Ключові акценти",
        "projx.highlightsTitle": "Що ця збірка <em>доводить.</em>",
        "projx.highlightsLead": "Кожен проєкт описано як інженерний і брендовий орієнтир, а не просто пункт галереї.",
        "projx.h1t": "Досягнення",
        "projx.h1d": "Публічний результат або визнання, пов'язане з цим мотоциклом.",
        "projx.h2t": "Категорія",
        "projx.h2d": "Технічний або культурний клас, до якого належить проєкт.",
        "projx.h3t": "Контекст",
        "projx.h3d": "Де проєкт жив, виступав, показувався або став частиною історії Iron Custom Motors.",
        "projx.whyEyebrow": "Чому це важливо",
        "projx.whyTitle": "Орієнтир для <em>нинішньої майстерні.</em>",
        "projx.whyText": "Ця збірка пояснює стандарт майстерні у Cascais сьогодні: дисциплінована інженерія, візуальний смак, документація і здатність вирішувати нестандартні мотоциклетні задачі.",
        "projx.relatedEyebrow": "Наступні кроки",
        "projx.relatedTitle": "Від історії проєкту до <em>дії в майстерні.</em>",
        "projx.relatedLead": "Подивіться портфоліо, обговоріть кастомну ідею або зв'яжіть цей досвід із сервісом, запчастинами й апґрейдами.",
        "projx.relatedText": "Відкрийте пов'язану сторінку для сервісного контексту, варіантів запису або ширшої історії Iron Custom Motors.",
    },
    "pt": {
        "projx.highlightsEyebrow": "Destaques do projeto",
        "projx.highlightsTitle": "O que este build <em>prova.</em>",
        "projx.highlightsLead": "Cada projeto é documentado como referência de engenharia e marca, não apenas como item de galeria.",
        "projx.h1t": "Conquista",
        "projx.h1d": "O resultado público ou reconhecimento ligado a esta moto.",
        "projx.h2t": "Categoria",
        "projx.h2d": "A classe técnica ou cultural a que este projeto pertence.",
        "projx.h3t": "Contexto",
        "projx.h3d": "Onde o projeto viveu, competiu, foi mostrado ou se tornou parte da história da Iron Custom Motors.",
        "projx.whyEyebrow": "Porque importa",
        "projx.whyTitle": "Uma referência para a <em>oficina atual.</em>",
        "projx.whyText": "Este build explica o padrão por trás da oficina de Cascais hoje: engenharia disciplinada, gosto visual, documentação e capacidade de resolver problemas invulgares em motos.",
        "projx.relatedEyebrow": "Próximos passos",
        "projx.relatedTitle": "Da história do projeto à <em>ação na oficina.</em>",
        "projx.relatedLead": "Explore o portfólio, discuta uma ideia custom ou ligue esta experiência a serviço, peças e upgrades.",
        "projx.relatedText": "Abra a página relacionada para contexto de serviço, opções de marcação ou a história mais ampla da Iron Custom Motors.",
    },
}

RELATED = [
    ("nav.projects", "/projects/", "Projects"),
    ("services.s4.title", "/custom/", "Custom & special projects"),
    ("nav.community", "/community/", "Community"),
    ("nav.contact", "/contact/", "Contact"),
]


def parse_html(markup: str) -> BeautifulSoup:
    return BeautifulSoup(markup, HTML_PARSER)


def replace_html(el, html: str):
    fragment = parse_html(html)
    container = fragment.body or fragment
    el.clear()
    for child in list(container.children):
        el.append(child)


def load_inline_i18n(soup) -> tuple[dict, object]:
    for script in soup.find_all("script"):
        text = script.string or ""
        match = re.search(r"window\.ICM_I18N_PAGE\s*=\s*(\{.*?\});", text, re.DOTALL)
        if not match:
            continue
        return json.loads(match.group(1)), script
    raise RuntimeError("Project page has no ICM_I18N_PAGE block")


def merge_i18n(page_i18n: dict):
    for lang in TARGET_LANGS:
        page_i18n.setdefault(lang, {})
        page_i18n[lang].update(COMMON_I18N[lang])


def sync_en_text(soup):
    full = {**GLOBAL_I18N["en"], **COMMON_I18N["en"]}
    for el in soup.find_all(attrs={"data-i18n": True}):
        key = el["data-i18n"]
        if key in full:
            replace_html(el, full[key])


def related_rows():
    rows = []
    for idx, (key, href, fallback) in enumerate(RELATED, start=1):
        label = GLOBAL_I18N["en"].get(key, fallback)
        rows.append(f'''<article class="project-enhance-row">
<span class="num">{idx:02d}</span>
<div>
<h4><a data-i18n="{key}" href="{href}">{label}</a></h4>
<p data-i18n="projx.relatedText">{COMMON_I18N["en"]["projx.relatedText"]}</p>
</div>
</article>''')
    return "\n".join(rows)


def insert_css(soup):
    style = soup.find("style")
    if style is None or "project-enhance-grid" in (style.string or ""):
        return
    style.string = (style.string or "") + """
.project-enhance-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:30px}
.project-enhance-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);padding:26px 24px}
.project-enhance-card .num{font-family:'Saira Condensed',sans-serif;font-weight:800;color:var(--accent);font-size:30px;line-height:1;margin-bottom:12px}
.project-enhance-card h3{font-family:'Saira Condensed',sans-serif;font-weight:800;text-transform:uppercase;font-size:22px;color:#fff;margin-bottom:8px}
.project-enhance-card p{font-size:15px;color:var(--text-dim);line-height:1.55}
.project-enhance-card .value{font-family:'Saira',sans-serif;font-weight:600;color:#fff;margin-bottom:12px}
.project-enhance-row{display:grid;grid-template-columns:70px 1fr;gap:24px;padding:22px 0;border-bottom:1px solid var(--border);align-items:start}
.project-enhance-row .num{font-family:'Saira Condensed',sans-serif;font-weight:800;font-size:28px;color:var(--accent);line-height:1}
.project-enhance-row h4{margin-bottom:6px;color:#fff;font-size:clamp(16px,1.4vw,20px)}
.project-enhance-row h4 a{color:#fff;text-decoration:none}
.project-enhance-row h4 a:hover{color:var(--accent)}
.project-enhance-row p{font-size:14px;color:var(--text-dim);max-width:60ch}
@media (max-width:900px){.project-enhance-grid{grid-template-columns:1fr}.project-enhance-row{grid-template-columns:50px 1fr;gap:18px}}
"""


def enhancement_html(slug: str):
    badge_key = f"proj.{slug}.badge"
    cat_key = f"proj.{slug}.cat"
    where_key = f"proj.{slug}.where"
    en = GLOBAL_I18N["en"]
    return f'''<section class="sub-section" data-enhancement="project-highlights">
<div class="container">
<div class="heading reveal">
<span class="h-eyebrow" data-i18n="projx.highlightsEyebrow">{COMMON_I18N["en"]["projx.highlightsEyebrow"]}</span>
<div>
<h2 data-i18n="projx.highlightsTitle">{COMMON_I18N["en"]["projx.highlightsTitle"]}</h2>
<p class="lead" data-i18n="projx.highlightsLead">{COMMON_I18N["en"]["projx.highlightsLead"]}</p>
</div>
</div>
<div class="project-enhance-grid reveal-stagger">
<article class="project-enhance-card">
<div class="num">01</div>
<h3 data-i18n="projx.h1t">{COMMON_I18N["en"]["projx.h1t"]}</h3>
<p class="value" data-i18n="{badge_key}">{en.get(badge_key, "")}</p>
<p data-i18n="projx.h1d">{COMMON_I18N["en"]["projx.h1d"]}</p>
</article>
<article class="project-enhance-card">
<div class="num">02</div>
<h3 data-i18n="projx.h2t">{COMMON_I18N["en"]["projx.h2t"]}</h3>
<p class="value" data-i18n="{cat_key}">{en.get(cat_key, "")}</p>
<p data-i18n="projx.h2d">{COMMON_I18N["en"]["projx.h2d"]}</p>
</article>
<article class="project-enhance-card">
<div class="num">03</div>
<h3 data-i18n="projx.h3t">{COMMON_I18N["en"]["projx.h3t"]}</h3>
<p class="value" data-i18n="{where_key}">{en.get(where_key, "")}</p>
<p data-i18n="projx.h3d">{COMMON_I18N["en"]["projx.h3d"]}</p>
</article>
</div>
</div>
</section>
<section class="sub-section" data-enhancement="project-related">
<div class="container">
<div class="heading reveal">
<span class="h-eyebrow" data-i18n="projx.whyEyebrow">{COMMON_I18N["en"]["projx.whyEyebrow"]}</span>
<div>
<h2 data-i18n="projx.whyTitle">{COMMON_I18N["en"]["projx.whyTitle"]}</h2>
<p class="lead" data-i18n="projx.whyText">{COMMON_I18N["en"]["projx.whyText"]}</p>
</div>
</div>
<div class="heading reveal" style="margin-top:50px">
<span class="h-eyebrow" data-i18n="projx.relatedEyebrow">{COMMON_I18N["en"]["projx.relatedEyebrow"]}</span>
<div>
<h2 data-i18n="projx.relatedTitle">{COMMON_I18N["en"]["projx.relatedTitle"]}</h2>
<p class="lead" data-i18n="projx.relatedLead">{COMMON_I18N["en"]["projx.relatedLead"]}</p>
</div>
</div>
<div class="reveal-stagger" style="max-width:900px">
{related_rows()}
</div>
</div>
</section>'''


def process_project(slug: str) -> bool:
    path = SITE_ROOT / "projects" / slug / "index.html"
    if not path.exists():
        print(f"  SKIP missing: projects/{slug}/index.html")
        return False
    soup = parse_html(path.read_text(encoding="utf-8"))
    for old in soup.find_all(attrs={"data-enhancement": re.compile(r"^project-")}):
        old.decompose()

    insert_css(soup)
    page_i18n, script = load_inline_i18n(soup)
    merge_i18n(page_i18n)
    script.string = f"window.ICM_I18N_PAGE = {json.dumps(page_i18n, ensure_ascii=False)};"

    target = soup.find("section", class_="cta-back")
    if target is None:
        print(f"  SKIP no insertion point: projects/{slug}/index.html")
        return False
    fragment = parse_html(enhancement_html(slug))
    sections = [child for child in (fragment.body or fragment).children if getattr(child, "name", None)]
    for section in reversed(sections):
        target.insert_before(section)

    sync_en_text(soup)
    path.write_text(str(soup), encoding="utf-8")
    print(f"  enhanced: projects/{slug}/index.html")
    return True


def main():
    changed = 0
    for slug in PROJECTS:
        if process_project(slug):
            changed += 1
    print(f"\nDone. {changed}/{len(PROJECTS)} project pages enhanced.")


if __name__ == "__main__":
    main()

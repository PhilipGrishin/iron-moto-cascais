#!/usr/bin/env python3
"""Generate downloadable multilingual pricing PDFs from pricing_data.py.

The HTML pricing pages and the downloadable PDFs must stay in sync. Edit
pricing_data.py first, then run this script to refresh all four PDF files.
"""

from __future__ import annotations

import re
from io import BytesIO
from html import unescape
from pathlib import Path
from typing import Any

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from pypdf import PdfReader

from pricing_data import LABELS, LANGS, SECTIONS


SITE_ROOT = Path(__file__).resolve().parents[2]
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_ITALIC = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"
DOMAIN = "ironcustommotors.com"

COLORS = {
    "ink": colors.HexColor("#111111"),
    "muted": colors.HexColor("#5a5a5f"),
    "soft": colors.HexColor("#f4f4f5"),
    "line": colors.HexColor("#d9d9de"),
    "dark": colors.HexColor("#0b0b0d"),
    "panel": colors.HexColor("#17171d"),
    "accent": colors.HexColor("#ff5722"),
    "white": colors.white,
}


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("ICMRegular", FONT_REGULAR))
    pdfmetrics.registerFont(TTFont("ICMBold", FONT_BOLD))
    pdfmetrics.registerFont(TTFont("ICMItalic", FONT_ITALIC))


def plain(value: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", value, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    return unescape(text).strip()


def t(value: Any, lang: str) -> str:
    if isinstance(value, dict):
        return plain(str(value[lang]))
    return plain(str(value))


def price_text(item: dict[str, Any], lang: str) -> str:
    bits = []
    if item.get("price_from"):
        bits.append(LABELS[lang]["from"])
    bits.append(item["price"])
    if item.get("price_suffix") == "per_hour":
        bits.append(LABELS[lang]["per_hour"])
    return " ".join(bits)


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "coverTitle": ParagraphStyle(
            "coverTitle",
            parent=base["Title"],
            fontName="ICMBold",
            fontSize=34,
            leading=36,
            textColor=COLORS["white"],
            spaceAfter=18,
        ),
        "coverLead": ParagraphStyle(
            "coverLead",
            parent=base["BodyText"],
            fontName="ICMRegular",
            fontSize=11,
            leading=17,
            textColor=colors.HexColor("#d7d7dc"),
            spaceAfter=24,
        ),
        "coverMeta": ParagraphStyle(
            "coverMeta",
            parent=base["BodyText"],
            fontName="ICMBold",
            fontSize=9,
            leading=12,
            textColor=COLORS["accent"],
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName="ICMBold",
            fontSize=20,
            leading=23,
            textColor=COLORS["ink"],
            spaceBefore=8,
            spaceAfter=8,
        ),
        "intro": ParagraphStyle(
            "intro",
            parent=base["BodyText"],
            fontName="ICMRegular",
            fontSize=10,
            leading=15,
            textColor=COLORS["muted"],
            spaceAfter=10,
        ),
        "sectionMeta": ParagraphStyle(
            "sectionMeta",
            parent=base["BodyText"],
            fontName="ICMBold",
            fontSize=8,
            leading=10,
            textColor=COLORS["accent"],
            spaceBefore=10,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["BodyText"],
            fontName="ICMRegular",
            fontSize=9,
            leading=13,
            textColor=COLORS["ink"],
        ),
        "muted": ParagraphStyle(
            "muted",
            parent=base["BodyText"],
            fontName="ICMItalic",
            fontSize=8,
            leading=12,
            textColor=COLORS["muted"],
            spaceBefore=6,
            spaceAfter=8,
        ),
        "cell": ParagraphStyle(
            "cell",
            parent=base["BodyText"],
            fontName="ICMRegular",
            fontSize=8,
            leading=10,
            textColor=COLORS["ink"],
        ),
        "cellBold": ParagraphStyle(
            "cellBold",
            parent=base["BodyText"],
            fontName="ICMBold",
            fontSize=8,
            leading=10,
            textColor=COLORS["ink"],
        ),
        "cellPrice": ParagraphStyle(
            "cellPrice",
            parent=base["BodyText"],
            fontName="ICMBold",
            fontSize=9,
            leading=11,
            textColor=COLORS["accent"],
            alignment=TA_RIGHT,
        ),
        "cardTitle": ParagraphStyle(
            "cardTitle",
            parent=base["BodyText"],
            fontName="ICMBold",
            fontSize=10,
            leading=12,
            textColor=COLORS["ink"],
        ),
        "cardPrice": ParagraphStyle(
            "cardPrice",
            parent=base["BodyText"],
            fontName="ICMBold",
            fontSize=11,
            leading=12,
            textColor=COLORS["accent"],
            alignment=TA_RIGHT,
        ),
        "disclaimer": ParagraphStyle(
            "disclaimer",
            parent=base["BodyText"],
            fontName="ICMRegular",
            fontSize=7.5,
            leading=10.5,
            textColor=COLORS["muted"],
        ),
    }


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text.replace("\n", "<br/>"), style)


def section_header(section: dict[str, Any], lang: str, styles: dict[str, ParagraphStyle]) -> list[Any]:
    return [
        p(f"{section['num']} - {t(section['title'], lang)}", styles["sectionMeta"]),
        p(t(section["h2"], lang), styles["h2"]),
        p(t(section["intro"], lang), styles["intro"]),
    ]


def simple_card_table(rows: list[list[Any]], widths: list[float]) -> Table:
    table = Table(rows, colWidths=widths, hAlign="LEFT", repeatRows=0)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), COLORS["soft"]),
                ("BOX", (0, 0), (-1, -1), 0.7, COLORS["line"]),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, COLORS["line"]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def price_cards(section: dict[str, Any], lang: str, styles: dict[str, ParagraphStyle]) -> list[Any]:
    flow: list[Any] = []
    for card in section["cards"]:
        tags = card.get("tags", {}).get(lang, [])
        tags_text = "<br/>".join(f"- {plain(tag)}" for tag in tags)
        desc = t(card["desc"], lang)
        body = desc if not tags_text else f"{desc}<br/><br/>{tags_text}"
        flow.append(
            simple_card_table(
                [
                    [
                        p(t(card["name"], lang), styles["cardTitle"]),
                        p(price_text(card, lang), styles["cardPrice"]),
                    ],
                    [p(body, styles["cell"]), ""],
                ],
                [125 * mm, 45 * mm],
            )
        )
        flow.append(Spacer(1, 5))
    if "note" in section:
        flow.append(p(t(section["note"], lang), styles["muted"]))
    return flow


def scheduled_section(section: dict[str, Any], lang: str, styles: dict[str, ParagraphStyle]) -> list[Any]:
    flow: list[Any] = [
        simple_card_table(
            [[p(t(section["consumables_label"], lang), styles["cardTitle"]), p(t(section["consumables_text"], lang), styles["cell"])]],
            [42 * mm, 128 * mm],
        ),
        Spacer(1, 8),
    ]
    for group in section["groups"]:
        checklist = "<br/>".join(f"- {plain(item)}" for item in group["checklist"][lang])
        flow.append(
            simple_card_table(
                [
                    [
                        p(t(group["name"], lang), styles["cardTitle"]),
                        p(price_text(group, lang), styles["cardPrice"]),
                    ],
                    [p(checklist, styles["cell"]), ""],
                ],
                [125 * mm, 45 * mm],
            )
        )
        flow.append(Spacer(1, 5))
    flow.append(p(t(section["note"], lang), styles["muted"]))
    return flow


def list_section(section: dict[str, Any], lang: str, styles: dict[str, ParagraphStyle]) -> list[Any]:
    flow: list[Any] = []
    for subgroup in section["subgroups"]:
        flow.append(p(t(subgroup["label"], lang), styles["sectionMeta"]))
        rows = []
        for item in subgroup["items"]:
            desc = item.get("desc", {}).get(lang, "")
            name = t(item["name"], lang)
            text = name if not desc else f"{name}<br/><font color='#5a5a5f'>{plain(desc)}</font>"
            rows.append([p(text, styles["cellBold"]), p(price_text(item, lang), styles["cellPrice"])])
        flow.append(simple_card_table(rows, [125 * mm, 45 * mm]))
        flow.append(Spacer(1, 7))
    return flow


def data_table(headers: list[str], rows: list[list[str]], styles: dict[str, ParagraphStyle]) -> Table:
    data = [[p(header, styles["cellBold"]) for header in headers]]
    for row in rows:
        data.append(
            [
                p(cell, styles["cellBold"] if idx == 0 else styles["cellPrice"],)
                for idx, cell in enumerate(row)
            ]
        )
    col_count = len(headers)
    first_width = 58 * mm
    rest = (170 * mm - first_width) / (col_count - 1)
    table = Table(data, colWidths=[first_width] + [rest] * (col_count - 1), hAlign="LEFT", repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f0f0f2")),
                ("BOX", (0, 0), (-1, -1), 0.7, COLORS["line"]),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, COLORS["line"]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def valves_wheels_section(section: dict[str, Any], lang: str, styles: dict[str, ParagraphStyle]) -> list[Any]:
    flow: list[Any] = []
    valve = section["valve_table"]
    flow.extend(
        [
            p(t(valve["title"], lang), styles["sectionMeta"]),
            data_table(valve["cols"][lang], [[plain(str(cell)) for cell in row] for row in valve["rows"]], styles),
            p(t(valve["note"], lang), styles["muted"]),
        ]
    )

    tyre = section["tyre_table"]
    tyre_rows = []
    for row in tyre["rows"]:
        tyre_rows.append([t(row[0], lang), *[plain(str(cell)) for cell in row[1:]]])
    flow.extend(
        [
            p(t(tyre["title"], lang), styles["sectionMeta"]),
            data_table(tyre["cols"][lang], tyre_rows, styles),
            p(t(tyre["note"], lang), styles["muted"]),
        ]
    )

    for service in section.get("additional_services", []):
        flow.append(
            simple_card_table(
                [[p(t(service["name"], lang), styles["cardTitle"]), p(t(service["price"], lang), styles["cardPrice"])]],
                [125 * mm, 45 * mm],
            )
        )

    chain = section["chain"]
    flow.extend(
        [
            simple_card_table(
                [
                    [p(t(chain["name"], lang), styles["cardTitle"]), p(chain["price"], styles["cardPrice"])],
                    [p(t(chain["desc"], lang), styles["cell"]), ""],
                ],
                [125 * mm, 45 * mm],
            ),
            p(t(chain["note"], lang), styles["muted"]),
        ]
    )
    return flow


def accessories_section(section: dict[str, Any], lang: str, styles: dict[str, ParagraphStyle]) -> list[Any]:
    rows = []
    for column in section["columns"]:
        items = "<br/>".join(f"{t(name, lang)} - {price}" for name, price in column["items"])
        rows.append([p(t(column["label"], lang), styles["cardTitle"]), p(items, styles["cell"])])
    return [
        simple_card_table(rows, [45 * mm, 125 * mm]),
        p(t(section["note_install"], lang), styles["muted"]),
        p(t(section["note_sourcing"], lang), styles["muted"]),
    ]


def custom_section(section: dict[str, Any], lang: str, styles: dict[str, ParagraphStyle]) -> list[Any]:
    rows = [
        [p(t(section["custom_title"], lang), styles["cardTitle"]), p(t(section["custom_body"], lang), styles["cell"])]
    ]
    for item in section["community"]:
        rows.append([p(t(item["title"], lang), styles["cardTitle"]), p(t(item["body"], lang), styles["cell"])])
    return [
        simple_card_table(rows, [45 * mm, 125 * mm]),
        p(t(section["slogan"], lang), styles["muted"]),
    ]


def build_story(lang: str, styles: dict[str, ParagraphStyle]) -> list[Any]:
    labels = LABELS[lang]
    flow: list[Any] = [
        Spacer(1, 58 * mm),
        p("IRON CUSTOM MOTORS", styles["coverMeta"]),
        p(plain(labels["h1"]).upper(), styles["coverTitle"]),
        p(labels["lead"], styles["coverLead"]),
        p(labels["eyebrow"], styles["coverMeta"]),
        p(labels["all_prices_include"], styles["coverLead"]),
        PageBreak(),
    ]

    for index, section in enumerate(SECTIONS):
        if index:
            flow.append(Spacer(1, 4))
        flow.extend(section_header(section, lang, styles))
        if section["num"] in {"01", "06"}:
            flow.extend(price_cards(section, lang, styles))
        elif section["num"] == "02":
            flow.extend(scheduled_section(section, lang, styles))
        elif section["num"] == "03":
            flow.extend(list_section(section, lang, styles))
        elif section["num"] == "04":
            flow.extend(valves_wheels_section(section, lang, styles))
        elif section["num"] == "05":
            flow.extend(accessories_section(section, lang, styles))
        elif section["num"] == "07":
            flow.extend(custom_section(section, lang, styles))

    flow.extend(
        [
            Spacer(1, 12),
            p(labels["disclaimer_title"], styles["sectionMeta"]),
            p(labels["disclaimer"], styles["disclaimer"]),
        ]
    )
    return flow


def draw_page(canvas, doc, lang: str) -> None:
    width, height = A4
    page = canvas.getPageNumber()
    if page == 1:
        canvas.saveState()
        canvas.setFillColor(COLORS["dark"])
        canvas.rect(0, 0, width, height, stroke=0, fill=1)
        canvas.setFillColor(COLORS["panel"])
        canvas.rect(0, 0, width, 74 * mm, stroke=0, fill=1)
        canvas.setFillColor(COLORS["accent"])
        canvas.rect(0, height - 14 * mm, width, 5 * mm, stroke=0, fill=1)
        canvas.setFont("ICMBold", 10)
        canvas.setFillColor(COLORS["white"])
        canvas.drawString(20 * mm, 24 * mm, DOMAIN)
        canvas.setFont("ICMRegular", 8)
        canvas.setFillColor(colors.HexColor("#d7d7dc"))
        canvas.drawString(20 * mm, 18 * mm, "Cascais / Lisbon")
        canvas.restoreState()
        return

    canvas.saveState()
    canvas.setFont("ICMBold", 8)
    canvas.setFillColor(COLORS["muted"])
    canvas.drawString(20 * mm, height - 12 * mm, "IRON CUSTOM MOTORS")
    canvas.setFillColor(COLORS["accent"])
    canvas.drawRightString(width - 20 * mm, height - 12 * mm, LABELS[lang]["eyebrow"])
    canvas.setStrokeColor(COLORS["line"])
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, height - 15 * mm, width - 20 * mm, height - 15 * mm)
    canvas.setFont("ICMRegular", 7)
    canvas.setFillColor(COLORS["muted"])
    canvas.drawString(20 * mm, 12 * mm, DOMAIN)
    canvas.drawRightString(width - 20 * mm, 12 * mm, str(page))
    canvas.restoreState()


def output_path(lang: str) -> Path:
    pdf_filename = LABELS[lang]["pdf_filename"].lstrip("/")
    return SITE_ROOT / pdf_filename


def pdf_semantics(payload: bytes) -> tuple:
    reader = PdfReader(BytesIO(payload))
    return tuple(
        (
            round(float(page.mediabox.width), 3),
            round(float(page.mediabox.height), 3),
            re.sub(r"\s+", " ", page.extract_text() or "").strip(),
        )
        for page in reader.pages
    )


def build_pdf(lang: str) -> Path:
    styles = make_styles()
    out = output_path(lang)
    out.parent.mkdir(parents=True, exist_ok=True)
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=22 * mm,
        bottomMargin=18 * mm,
        title=LABELS[lang]["page_title"],
        author="Iron Custom Motors",
        subject=LABELS[lang]["page_description"],
    )
    doc.build(
        build_story(lang, styles),
        onFirstPage=lambda canvas, doc: draw_page(canvas, doc, lang),
        onLaterPages=lambda canvas, doc: draw_page(canvas, doc, lang),
        canvasmaker=lambda *args, **kwargs: Canvas(
            *args, **{**kwargs, "invariant": 1}
        ),
    )
    generated = buffer.getvalue()
    if not out.exists() or pdf_semantics(out.read_bytes()) != pdf_semantics(generated):
        out.write_bytes(generated)
    return out


def main() -> None:
    register_fonts()
    for lang in LANGS:
        out = build_pdf(lang)
        print(f"wrote {out.relative_to(SITE_ROOT)}")


if __name__ == "__main__":
    main()

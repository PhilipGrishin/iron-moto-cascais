#!/usr/bin/env python3
"""Fetch anonymous lead counters and save a local checkup report."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


SITE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATS_URL = "https://icm-leads.vg-ab6.workers.dev/stats"
SECRET_FILE = SITE_ROOT / ".secrets" / "leads.env"
OUTPUT_DIR = SITE_ROOT / "data" / "leads"
EVENT_TYPES = ("whatsapp", "tel", "form_submit", "form_view")


def read_secret_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def settings() -> tuple[str, str]:
    local = read_secret_file(SECRET_FILE)
    url = os.environ.get("ICM_LEADS_STATS_URL") or local.get(
        "ICM_LEADS_STATS_URL", DEFAULT_STATS_URL
    )
    token = os.environ.get("ICM_LEADS_STATS_TOKEN") or local.get(
        "ICM_LEADS_STATS_TOKEN", ""
    )
    if not token:
        raise RuntimeError(
            "ICM_LEADS_STATS_TOKEN is missing; set it in the environment "
            "or .secrets/leads.env"
        )
    return url, token


def fetch_stats(url: str, token: str, days: int) -> dict:
    separator = "&" if "?" in url else "?"
    query = urlencode({
        'days': days,
        'includeTests': 0,
        'token': token,
    })
    request_url = f"{url}{separator}{query}"
    request = Request(
        request_url,
        headers={"accept": "application/json", "user-agent": "icm-leads-report/1.0"},
    )
    try:
        with urlopen(request, timeout=20) as response:
            payload = json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"Lead stats returned HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"Could not reach lead stats endpoint: {exc.reason}") from exc
    if (
        not isinstance(payload, dict)
        or payload.get("days") != days
        or payload.get("includeTests") is not False
    ):
        raise RuntimeError(f"Lead stats returned an invalid {days}-day response")
    return payload


def table(headers: tuple[str, ...], rows: list[tuple[object, ...]]) -> str:
    rendered = [[str(cell) for cell in headers], *[[str(cell) for cell in row] for row in rows]]
    widths = [max(len(row[index]) for row in rendered) for index in range(len(headers))]
    lines = ["  ".join(cell.ljust(widths[index]) for index, cell in enumerate(rendered[0]))]
    lines.append("  ".join("-" * width for width in widths))
    lines.extend("  ".join(cell.ljust(widths[index]) for index, cell in enumerate(row)) for row in rendered[1:])
    return "\n".join(lines)


def print_period(stats: dict) -> None:
    days = stats["days"]
    totals = stats.get("totals", {})
    print(f"\nLEADS — {days} DAYS ({stats.get('from')} to {stats.get('to')})")
    print(table(
        ("Type", "Count"),
        [(event_type, totals.get(event_type, 0)) for event_type in EVENT_TYPES],
    ))

    page_rows = []
    for row in stats.get("pages", [])[:10]:
        by_type = row.get("byType", {})
        page_rows.append((
            row.get("page", ""),
            row.get("lang", ""),
            row.get("total", 0),
            by_type.get("whatsapp", 0),
            by_type.get("tel", 0),
            by_type.get("form_submit", 0),
            by_type.get("form_view", 0),
        ))
    print("\nTop pages")
    print(table(
        ("Page", "Lang", "Total", "WA", "Tel", "Submit", "View"),
        page_rows or [("—", "—", 0, 0, 0, 0, 0)],
    ))

    language_rows = []
    for row in stats.get("languages", []):
        by_type = row.get("byType", {})
        language_rows.append((
            row.get("lang", ""),
            row.get("total", 0),
            by_type.get("whatsapp", 0),
            by_type.get("tel", 0),
            by_type.get("form_submit", 0),
            by_type.get("form_view", 0),
        ))
    print("\nLanguages")
    print(table(
        ("Lang", "Total", "WA", "Tel", "Submit", "View"),
        language_rows or [("—", 0, 0, 0, 0, 0)],
    ))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch 7/28-day anonymous lead statistics from icm-leads."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help="Local JSON output directory (default: data/leads)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        url, token = settings()
        periods = {str(days): fetch_stats(url, token, days) for days in (7, 28)}
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    report = {
        "generatedAt": datetime.now().astimezone().isoformat(timespec="seconds"),
        "source": url,
        "periods": periods,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / f"{datetime.now().astimezone().date().isoformat()}_leads.json"
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for days in (7, 28):
        print_period(periods[str(days)])
    print(f"\nSaved JSON: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import json
import re
from datetime import datetime
import requests
from bs4 import BeautifulSoup

LCA_URL = "https://www.hermesairports.com/flight-info/arrivals-and-departures-lca"
PFO_URL = "https://www.hermesairports.com/flight-info/arrivals-and-departures-pfo"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def fetch_page(url):
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()
    return response.text


def count_keywords(text, keywords):
    total = 0
    for word in keywords:
        total += len(re.findall(word, text, flags=re.IGNORECASE))
    return total


def parse_hermes_page(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(" ", strip=True)

    cancelled = count_keywords(text, [r"cancelled", r"canceled"])
    delayed = count_keywords(text, [r"delayed", r"late", r"estimated"])
    diverted = count_keywords(text, [r"diverted"])

    return {
        "cancelled": cancelled,
        "delayed": delayed,
        "diverted": diverted,
        "raw_text_size": len(text)
    }


def build_hermes_status(total_cancelled, total_delayed):
    if total_cancelled >= 10 or total_delayed >= 40:
        return "disrupted", "high", "заметные сбои по аэропортам"
    elif total_cancelled >= 3 or total_delayed >= 15:
        return "stressed", "medium", "есть заметные задержки и отдельные отмены"
    else:
        return "normal", "low", "массовых сбоев не видно"


def update_today_json():
    lca_html = fetch_page(LCA_URL)
    pfo_html = fetch_page(PFO_URL)

    lca = parse_hermes_page(lca_html)
    pfo = parse_hermes_page(pfo_html)

    total_cancelled = lca["cancelled"] + pfo["cancelled"]
    total_delayed = lca["delayed"] + pfo["delayed"]

    airport_status, disruption_level, note = build_hermes_status(
        total_cancelled,
        total_delayed
    )

    today_data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "eurocontrol": {
            "traffic_status": "n/a",
            "traffic_change_pct": 0,
            "pressure_level": "n/a",
            "note": "EUROCONTROL пока не подключен"
        },
        "hermes": {
            "airport_status": airport_status,
            "cancelled_flights": total_cancelled,
            "delayed_flights": total_delayed,
            "disruption_level": disruption_level,
            "note": note
        },
        "summary": {
            "risk_level": "yellow" if disruption_level == "medium" else ("red" if disruption_level == "high" else "green"),
            "message": (
                "Есть заметные сбои по Hermes"
                if disruption_level == "high"
                else "Есть отдельные проблемы по Hermes"
                if disruption_level == "medium"
                else "По Hermes массовых сбоев не видно"
            )
        }
    }

    with open("today_data.json", "w", encoding="utf-8") as f:
        json.dump(today_data, f, ensure_ascii=False, indent=2)

    print("today_data.json updated successfully")


if __name__ == "__main__":
    update_today_json()

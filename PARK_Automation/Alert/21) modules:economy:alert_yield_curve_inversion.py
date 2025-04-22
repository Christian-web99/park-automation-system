# modules/economy/alert_yield_curve_inversion.py

import requests
from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message
from config import FRED_API_KEY

FRED_SERIES = {
    "10Y": "GS10",
    "2Y": "GS2",
    "3M": "TB3MS"
}

def fetch_rate(series_id):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()["observations"]
        for obs in reversed(data):
            if obs["value"] != ".":
                return float(obs["value"])
    except:
        return None

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")

    r_10y = fetch_rate(FRED_SERIES["10Y"])
    r_2y = fetch_rate(FRED_SERIES["2Y"])
    r_3m = fetch_rate(FRED_SERIES["3M"])

    if None in (r_10y, r_2y, r_3m):
        if daily:
            send_telegram_message(f"[PARK 시스템 – 21번 항목] {now}\n금리 데이터 수집 실패")
        return

    spread_10y_2y = r_10y - r_2y
    spread_10y_3m = r_10y - r_3m

    msg = f"""[PARK 시스템 – 21번 항목]
📉 <b>장단기 금리차 역전 감지</b> ({now})

• 🇺🇸 10Y – 2Y: {spread_10y_2y:+.2f}% {'⚠️ 역전' if spread_10y_2y < 0 else ''}
• 🇺🇸 10Y – 3M: {spread_10y_3m:+.2f}% {'⚠️ 역전' if spread_10y_3m < 0 else ''}

✅ 기준: 금리차 < 0% → 역전 인식
✅ 주기: 오전 7시 요약
"""
    send_telegram_message(msg)
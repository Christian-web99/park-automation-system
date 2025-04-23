# modules/flows/alert_short_selling.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

# 🔽 실제로는 한국거래소 공매도 통계 또는 증권사 API 연동 필요
def fetch_short_selling_summary():
    return {
        "KOSPI": {
            "외국인": 245_000_000_00,
            "기관": 312_000_000_00,
            "개인": 58_000_000_00
        },
        "KOSDAQ": {
            "외국인": 122_000_000_00,
            "기관": 145_000_000_00,
            "개인": 35_000_000_00
        }
    }

def format_amount(value):
    unit = "억 원"
    return f"{int(value / 100_000_000):,}{unit}"

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    data = fetch_short_selling_summary()

    if not data:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 7번 항목] {now}\n공매도 요약 데이터 없음")
        return

    msg = f"""[PARK 시스템 – 7번 항목]
📊 <b>공매도 요약</b> ({now})

"""

    for market in ["KOSPI", "KOSDAQ"]:
        msg += f"• {market} 공매도\n"
        for entity in ["외국인", "기관", "개인"]:
            amount = format_amount(data[market][entity])
            msg += f"  - {entity}: {amount}\n"
        msg += "\n"

    msg += "✅ 주기: 종가 후 + 다음날 오전 7시\n✅ 기준: 외국인/기관/개인 공매도 총액 요약"
    send_telegram_message(msg)
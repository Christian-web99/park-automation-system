# modules/flows/alert_weekly_options.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

# 실전에서는 한국거래소(KRX), 증권사 API, 또는 DB 연동
def fetch_weekly_option_summary():
    # 예시 데이터 (실제는 수집기에서 업데이트됨)
    return {
        "KOSPI": {
            "외국인": {"콜": 2315, "풋": -1108},
            "기관": {"콜": -943, "풋": 756},
            "개인": {"콜": -1372, "풋": 352}
        },
        "KOSDAQ": {
            "외국인": {"콜": 122, "풋": -34},
            "기관": {"콜": -85, "풋": 60},
            "개인": {"콜": -37, "풋": -26}
        }
    }

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    data = fetch_weekly_option_summary()

    if not data:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 6번 항목] {now}\n위클리 옵션 요약 데이터 없음")
        return

    def format_side(name, side):
        val = side[name]
        sign = "+" if val >= 0 else "–"
        return f"{sign}{abs(val):,}계약"

    msg = f"""[PARK 시스템 – 6번 항목]
📊 <b>국내 위클리 옵션 포지션 요약</b> ({now})

"""

    for market in ["KOSPI", "KOSDAQ"]:
        msg += f"• {market} 위클리 옵션\n"
        for entity in ["외국인", "기관", "개인"]:
            summary = f"{entity}: 콜 {format_side(entity, data[market])} / 풋 {format_side(entity, data[market]['풋'])}"
            msg += f"  - {summary}\n"
        msg += "\n"

    msg += "✅ 주기: 종가 후 + 다음날 오전 7시\n✅ 기준: 위클리 옵션 순매매 요약"
    send_telegram_message(msg)
# modules/macro/alert_earnings_report.py

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

# 감시 대상 기업
EARNINGS_WATCHLIST = {
    "AAPL": "애플",
    "TSLA": "테슬라",
    "MSFT": "마이크로소프트",
    "005930.KS": "삼성전자",
    "000660.KS": "SK하이닉스"
}

# ✅ 수동 입력 일정 예시 (실전에서는 DB or 크롤링 필요)
EARNINGS_SCHEDULE = {
    "2025-04-23": ["TSLA", "MSFT"],
    "2025-04-25": ["AAPL", "005930.KS"],
    "2025-04-26": ["000660.KS"]
}

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul"))
    today_str = now.strftime("%Y-%m-%d")
    tomorrow_str = (now + timedelta(days=1)).strftime("%Y-%m-%d")

    msg_list = []

    for date_key, ticker_list in EARNINGS_SCHEDULE.items():
        if date_key in [today_str, tomorrow_str]:
            for tkr in ticker_list:
                kr_name = EARNINGS_WATCHLIST.get(tkr, tkr)
                dtag = "오늘" if date_key == today_str else "내일"
                msg_list.append(f"• {kr_name}({tkr}) → {dtag} 실적 발표 예정")

    if msg_list:
        msg = f"""[PARK 시스템 – 16번 항목]
📢 <b>주요 기업 실적 발표 감지</b> ({now.strftime('%Y-%m-%d %H:%M')})

{chr(10).join(msg_list)}

✅ 주기: 실적 발표 전 + 오전 7시 요약
✅ 대상: 주요 글로벌/국내 기업
"""
        send_telegram_message(msg)
    elif daily:
        send_telegram_message(f"[PARK 시스템 – 16번 항목] {now.strftime('%Y-%m-%d %H:%M')}\n오늘~내일 실적 발표 예정 기업 없음")
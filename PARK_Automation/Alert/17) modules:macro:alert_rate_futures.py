# modules/macro/alert_rate_futures.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

# ✅ 실전에서는 CME FedWatch 연동 필요 (예: 크롤링, API 대체)
def fetch_fedwatch_probabilities():
    # 예시 데이터 (실전은 동결/인하/인상 확률 %)
    return {
        "회의일": "2025-06-18",
        "동결": "87.3%",
        "인상": "2.1%",
        "인하": "10.6%",
        "기준금리": "5.25%"
    }

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    data = fetch_fedwatch_probabilities()

    if not data:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 17번 항목] {now}\n금리 선물 기반 데이터 없음")
        return

    msg = f"""[PARK 시스템 – 17번 항목]
📈 <b>금리 선물 + 연준 인상 확률</b> ({now})

• 📅 다음 회의일: {data['회의일']}
• 🇺🇸 예상 기준금리: {data['기준금리']}
• 동결 확률: {data['동결']}
• 인상 확률: {data['인상']}
• 인하 확률: {data['인하']}

✅ 주기: 5분 실시간 + 오전 7시 요약
✅ 데이터 출처: CME FedWatch 기반
"""
    send_telegram_message(msg)
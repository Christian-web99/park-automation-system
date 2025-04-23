# modules/flows/alert_kospi200_futures.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

# 실전에서는 API 또는 크롤링 자동 수집 필요
def fetch_kospi200_futures_change():
    # 예시 값: +0.42% 상승
    return "+0.42%"

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    change = fetch_kospi200_futures_change()

    if not change:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 8번 항목] {now}\nKOSPI200 야간선물 데이터 없음")
        return

    msg = f"""[PARK 시스템 – 8번 항목]
📊 <b>KOSPI200 야간선물 변동률</b> ({now})

• 전일 대비 변동률: {change}

✅ 주기: 매일 오전 7시
✅ 기준: 야간선물 종가 대비 등락률 (%) 기준
"""
    send_telegram_message(msg)
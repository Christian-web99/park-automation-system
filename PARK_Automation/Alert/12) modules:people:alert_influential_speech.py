# modules/people/alert_influential_speech.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message
from config import KEY_PEOPLE_REALTIME, KEY_PEOPLE_HOURLY

# 실전에서는 Twitter API, Google News API, RSS Feed, 크롤러 연동
def fetch_latest_statements(person_list, level="realtime"):
    # 🔽 예시 응답
    if level == "realtime":
        return [
            {"name": "Jerome Powell", "content": "We are closely watching inflation...", "source": "Twitter"},
            {"name": "ECB President", "content": "Further rate hikes may not be necessary", "source": "Google News"}
        ]
    else:
        return [
            {"name": "Nancy Pelosi", "content": "The market needs clarity on debt ceiling", "source": "News"}
        ]

def run(level="realtime", daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")

    people_list = KEY_PEOPLE_REALTIME if level == "realtime" else KEY_PEOPLE_HOURLY
    statements = fetch_latest_statements(people_list, level)

    if not statements:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 12번 항목] {now}\n실시간 발언 감지 없음")
        return

    msg = f"""[PARK 시스템 – 12번 항목]
🎙 <b>영향력 인물 발언 감지</b> ({now})

"""

    for s in statements:
        msg += f"• {s['name']}: \"{s['content']}\" ({s['source']})\n"

    msg += f"""
✅ 주기: 1분 실시간 (일반), 1시간 감지 (의회)
✅ 오전 7시 요약 포함
"""
    send_telegram_message(msg)
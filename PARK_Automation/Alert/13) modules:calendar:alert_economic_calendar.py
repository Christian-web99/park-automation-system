# modules/calendar/alert_economic_calendar.py

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

def fetch_calendar_events(weekly=False):
    today = datetime.now(ZoneInfo("Asia/Seoul")).date()
    if weekly:
        events = [
            {"date": today + timedelta(days=1), "time": "21:30", "event": "🇺🇸 미국 CPI 발표"},
            {"date": today + timedelta(days=2), "time": "23:00", "event": "🇪🇺 ECB 금리 결정"},
            {"date": today + timedelta(days=4), "time": "21:30", "event": "🇺🇸 미국 고용지표 발표"},
        ]
    else:
        events = [
            {"date": today, "time": "21:30", "event": "🇺🇸 미국 CPI 발표"},
            {"date": today, "time": "23:00", "event": "🇪🇺 ECB 금리 결정"}
        ]
    return events

def run(weekly=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    events = fetch_calendar_events(weekly=weekly)

    if not events:
        return

    title = "[PARK 시스템 – 13번 항목]\n📆 <b>경제 캘린더 알림</b>"
    subtitle = "🗓 이번 주 주요 일정" if weekly else "🗓 오늘의 주요 일정"

    msg = f"""{title} ({now})
{subtitle}\n"""

    for event in events:
        msg += f"• {event['date'].strftime('%m/%d')} {event['time']} → {event['event']}\n"

    msg += "\n✅ 주기: 매일 오전 7시 + 매주 월요일 주간 일정"
    send_telegram_message(msg)
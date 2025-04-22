# modules/crisis/alert_global_crisis.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message
from config import CRISIS_KEYWORDS

# 실전: Twitter(X) API, News API, RSS Feed 연동
def fetch_recent_news():
    # 예시 응답
    return [
        {"headline": "북한이 미사일을 발사했다", "source": "Yonhap", "url": "https://..."},
        {"headline": "러시아-우크라 전쟁 격화", "source": "CNN", "url": "https://..."},
        {"headline": "ECB 긴급 회의 소집", "source": "Bloomberg", "url": "https://..."},
    ]

def filter_crisis_news(news_list):
    alerts = []
    for article in news_list:
        for keyword in CRISIS_KEYWORDS:
            if keyword in article["headline"]:
                alerts.append(f"{article['headline']} ({article['source']})\n🔗 {article['url']}")
                break
    return alerts

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    news = fetch_recent_news()
    crisis_items = filter_crisis_news(news)

    if crisis_items:
        msg = f"""[PARK 시스템 – 14번 항목]
⚠️ <b>글로벌 위기 이벤트 감지</b> ({now})

• 주요 감지 항목:
{chr(10).join(crisis_items)}

✅ 감지 키워드: {', '.join(CRISIS_KEYWORDS[:5])} 외
✅ 주기: 1분 실시간 + 오전 7시 요약
"""
        send_telegram_message(msg)
    elif daily:
        send_telegram_message(f"[PARK 시스템 – 14번 항목] {now}\n감지된 글로벌 위기 이벤트 없음")
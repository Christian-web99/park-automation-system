# modules/economy/alert_pmi_release.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

PMI_KEYWORDS = [
    "미국 PMI", "중국 PMI", "유럽 PMI",
    "ISM 제조업", "Caixin 제조업", "Eurozone PMI",
    "Manufacturing PMI", "PMI 발표", "제조업 지수"
]

# 예시: 뉴스 또는 캘린더 API 응답
def fetch_pmi_headlines():
    return [
        {"headline": "미국 ISM 제조업 PMI 48.5… 예상 하회", "source": "Bloomberg", "url": "https://..."},
        {"headline": "중국 Caixin 제조업 PMI 51.2… 경기 확장세", "source": "Reuters", "url": "https://..."}
    ]

def filter_pmi_news(news_list):
    matched = []
    for news in news_list:
        for keyword in PMI_KEYWORDS:
            if keyword in news["headline"]:
                matched.append(f"{news['headline']} ({news['source']})\n🔗 {news['url']}")
                break
    return matched

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    news = fetch_pmi_headlines()
    alerts = filter_pmi_news(news)

    if alerts:
        msg = f"""[PARK 시스템 – 25번 항목]
🏭 <b>미국/중국/유럽 제조업 PMI 감지</b> ({now})

• 감지된 항목:
{chr(10).join(alerts)}

✅ 주기: 5분 실시간 + 오전 7시 요약
✅ 필터 키워드: {', '.join(PMI_KEYWORDS[:3])} 외
"""
        send_telegram_message(msg)
    elif daily:
        send_telegram_message(f"[PARK 시스템 – 25번 항목] {now}\n감지된 PMI 뉴스 없음")
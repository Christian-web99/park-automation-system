# modules/economy/alert_gdp_release.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

GDP_KEYWORDS = [
    "미국 GDP", "미국 경제성장률", "US GDP", "US growth",
    "중국 GDP", "China GDP", "중국 경제성장률",
    "일본 GDP", "Japan GDP", "일본 경제성장률"
]

# 실전 연동: Google News API, 뉴스 크롤러, 또는 정기 캘린더 크롤링
def fetch_recent_gdp_news():
    # 예시 응답
    return [
        {"headline": "미국 1분기 GDP 전년 대비 2.5% 성장", "source": "Bloomberg", "url": "https://..."},
        {"headline": "중국 GDP 예상치 상회… 경기 반등 신호", "source": "Reuters", "url": "https://..."}
    ]

def filter_gdp_news(news_list):
    filtered = []
    for news in news_list:
        for kw in GDP_KEYWORDS:
            if kw in news["headline"]:
                filtered.append(f"{news['headline']} ({news['source']})\n🔗 {news['url']}")
                break
    return filtered

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    news = fetch_recent_gdp_news()
    gdp_news = filter_gdp_news(news)

    if gdp_news:
        msg = f"""[PARK 시스템 – 20번 항목]
📊 <b>미국·중국·일본 GDP 발표 감지</b> ({now})

• 감지 항목:
{chr(10).join(gdp_news)}

✅ 키워드: {', '.join(GDP_KEYWORDS[:3])} 외
✅ 주기: 5분 실시간 + 오전 7시 요약
"""
        send_telegram_message(msg)
    elif daily:
        send_telegram_message(f"[PARK 시스템 – 20번 항목] {now}\n감지된 GDP 뉴스 없음")
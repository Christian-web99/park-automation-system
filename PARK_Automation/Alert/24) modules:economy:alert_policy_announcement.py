# modules/economy/alert_policy_announcement.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

POLICY_KEYWORDS = [
    "통화 개입", "국채 발행", "긴급 정책", "시장 안정 조치",
    "유동성 공급", "예산 수정안", "환율 방어", "지급준비율",
    "BOJ 개입", "PBOC 긴급", "ECB 특별 회의", "Fed 긴급", "기축통화 스왑"
]

# 예시: Google News / Twitter API 등에서 수집한 헤드라인 리스트
def fetch_policy_headlines():
    return [
        {"headline": "일본 BOJ, 3조엔 규모 통화 개입 단행", "source": "Nikkei", "url": "https://..."},
        {"headline": "중국, 위안화 방어 위해 긴급 유동성 공급", "source": "Reuters", "url": "https://..."}
    ]

def filter_policy_alerts(news_list):
    alerts = []
    for news in news_list:
        for keyword in POLICY_KEYWORDS:
            if keyword in news["headline"]:
                alerts.append(f"{news['headline']} ({news['source']})\n🔗 {news['url']}")
                break
    return alerts

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    news = fetch_policy_headlines()
    alerts = filter_policy_alerts(news)

    if alerts:
        msg = f"""[PARK 시스템 – 24번 항목]
🚨 <b>각국 긴급 정책 발표 감지</b> ({now})

• 감지된 내용:
{chr(10).join(alerts)}

✅ 주기: 1분 실시간 + 오전 7시 요약
✅ 필터 키워드: {', '.join(POLICY_KEYWORDS[:3])} 외
"""
        send_telegram_message(msg)
    elif daily:
        send_telegram_message(f"[PARK 시스템 – 24번 항목] {now}\n감지된 긴급 정책 발표 없음")
# modules/sentiment/alert_market_sentiment.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

def fetch_market_sentiment_data():
    # ✅ 실전은 API or 크롤링 기반 자동 수집
    return {
        "cnn_index": 82,
        "cnn_status": "Extreme Greed",
        "korea_index": 48,
        "korea_status": "Neutral",
        "buffett_ratio": 152.0,  # 시총/GDP (%)
        "buffett_status": "고평가",
        "mmf_balance": "6.03조 달러",
        "real_estate_kb": "+0.4%",
        "real_estate_cs": "-0.2%"
    }

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    data = fetch_market_sentiment_data()

    if not data:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 27번 항목] {now}\n시장 체온 지표 데이터 수집 실패")
        return

    msg = f"""[PARK 시스템 – 27번 항목]
🌡️ <b>시장 체온 요약</b> ({now})

• 🧠 CNN Fear & Greed Index: {data['cnn_index']} ({data['cnn_status']})
• 🇰🇷 Korea Fear & Greed Index: {data['korea_index']} ({data['korea_status']})
• 🪙 버핏지수 (시총/GDP): {data['buffett_ratio']}% ({data['buffett_status']})
• 💵 MMF 잔고: {data['mmf_balance']}
• 🏠 KB 부동산: {data['real_estate_kb']}
• 🏠 Case-Shiller: {data['real_estate_cs']}

✅ 해석:
- 미국 투자심리: {data['cnn_status']}
- 한국 투자심리: {data['korea_status']}
- 장기 밸류에이션: {data['buffett_status']}

✅ 주기: 오전 7시 요약
"""
    send_telegram_message(msg)
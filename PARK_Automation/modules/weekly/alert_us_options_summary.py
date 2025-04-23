# modules/weekly/alert_us_options_summary.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

def fetch_us_option_summary():
    return "미국 옵션: 콜 옵션 강세, 풋/콜 비율 0.78 (중립)"

def fetch_index_weekly_returns():
    return {
        "KOSPI": "+0.35%",
        "KOSDAQ": "+0.52%",
        "NASDAQ": "+1.20%",
        "S&P500": "+0.85%",
        "DOW": "+0.42%"
    }

def fetch_btc_etf_flow():
    return "+2,000억 원 순유입"

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul"))
    if now.weekday() != 0 and daily:
        return  # 월요일이 아닐 경우 요약 생략

    us_options = fetch_us_option_summary()
    returns = fetch_index_weekly_returns()
    btc_etf_flow = fetch_btc_etf_flow()

    msg = f"""[PARK 시스템 – 9번 항목]
📊 <b>미국 옵션 + BTC ETF + 주간 수익률 요약</b> ({now.strftime('%Y-%m-%d %H:%M')})

✅ 미국 옵션 포지션 요약
• {us_options}

✅ 주간 주요 지수 수익률
• KOSPI: {returns['KOSPI']}
• KOSDAQ: {returns['KOSDAQ']}
• NASDAQ: {returns['NASDAQ']}
• S&P500: {returns['S&P500']}
• DOW: {returns['DOW']}

✅ BTC 현물 ETF 흐름
• {btc_etf_flow}

🕘 주기: 매주 월요일 오전 7시
"""
    send_telegram_message(msg)
# modules/macro/alert_commodities.py

import yfinance as yf
from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

# 추적 대상 티커
COMMODITY_TICKERS = {
    "WTI 원유": "CL=F",
    "금": "GC=F",
    "구리": "HG=F",
    "천연가스": "NG=F"
}

def fetch_commodity_prices():
    data = {}
    for name, ticker in COMMODITY_TICKERS.items():
        try:
            df = yf.download(ticker, period="2d", interval="1d", progress=False)
            if len(df) >= 2:
                prev = df['Close'].iloc[-2]
                curr = df['Close'].iloc[-1]
                pct = (curr - prev) / prev * 100
                data[name] = {
                    "현재가": round(curr, 2),
                    "등락률": f"{pct:+.2f}%"
                }
        except Exception as e:
            data[name] = {"현재가": "N/A", "등락률": "N/A"}
    return data

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    prices = fetch_commodity_prices()

    if not prices:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 15번 항목] {now}\n원자재 데이터 없음")
        return

    msg = f"""[PARK 시스템 – 15번 항목]
🛢 <b>원자재 가격 추적</b> ({now})

"""

    for name, val in prices.items():
        msg += f"• {name}: ${val['현재가']} ({val['등락률']})\n"

    msg += "\n✅ 주기: 5분 실시간 + 오전 7시 요약"
    send_telegram_message(msg)
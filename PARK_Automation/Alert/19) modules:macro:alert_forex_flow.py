# modules/macro/alert_forex_flow.py

import yfinance as yf
from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

CURRENCY_TICKERS = {
    "달러인덱스(DXY)": "DX-Y.NYB",
    "유로/달러": "EURUSD=X",
    "달러/엔화": "JPY=X",
    "달러/위안": "CNY=X"
}

def fetch_forex_data():
    result = {}
    for name, ticker in CURRENCY_TICKERS.items():
        try:
            df = yf.download(ticker, period="2d", interval="1d", progress=False)
            if len(df) >= 2:
                prev = df["Close"].iloc[-2]
                curr = df["Close"].iloc[-1]
                pct = (curr - prev) / prev * 100
                result[name] = {
                    "현재가": round(curr, 4),
                    "등락률": f"{pct:+.2f}%"
                }
        except:
            result[name] = {"현재가": "N/A", "등락률": "N/A"}
    return result

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    data = fetch_forex_data()

    if not data:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 19번 항목] {now}\n외환시장 데이터 없음")
        return

    msg = f"""[PARK 시스템 – 19번 항목]
💱 <b>외환시장 자금 흐름 감지</b> ({now})

"""

    for name, info in data.items():
        msg += f"• {name}: {info['현재가']} ({info['등락률']})\n"

    msg += "\n✅ 주기: 5분 실시간 + 오전 7시 요약"
    send_telegram_message(msg)
# modules/ema/alert_ema_cross.py

import pandas as pd
import yfinance as yf
from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

from config import KOSPI_TOP_50, KOSDAQ_TOP_50, CRYPTO_TOP_10

def fetch_price_data(ticker, interval="1d", period="200d"):
    try:
        df = yf.download(ticker, interval=interval, period=period, progress=False)
        return df
    except:
        return None

def analyze_ema_signals(ticker):
    df = fetch_price_data(ticker)
    if df is None or len(df) < 200:
        return None

    df["EMA50"] = df["Close"].ewm(span=50).mean()
    df["EMA200"] = df["Close"].ewm(span=200).mean()

    current_price = df["Close"].iloc[-1]
    ema50 = df["EMA50"].iloc[-1]
    ema200 = df["EMA200"].iloc[-1]

    deviation = (current_price - ema50) / ema50 * 100
    signal = None

    # ✅ 괴리율 ±13%
    if deviation >= 13:
        signal = f"📈 실시간 +13% 이상 (괴리율 {deviation:.2f}%)"
    elif deviation <= -13:
        signal = f"📉 실시간 -13% 이하 (괴리율 {deviation:.2f}%)"

    # ✅ 크로스 확인
    ema50_yesterday = df["EMA50"].iloc[-2]
    ema200_yesterday = df["EMA200"].iloc[-2]

    if ema50 > ema200 and ema50_yesterday <= ema200_yesterday:
        signal = "📈 골든크로스"
    elif ema50 < ema200 and ema50_yesterday >= ema200_yesterday:
        signal = "📉 데드크로스"

    return signal

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    targets = KOSPI50_TICKERS + KOSDAQ50_TICKERS + CRYPTO_TICKERS
    triggered = []

    for ticker in targets:
        signal = analyze_ema_signals(ticker)
        if signal:
            triggered.append(f"{ticker} → {signal}")

    if triggered:
        message = f"""[PARK 시스템 – 3번 항목]
📊 <b>EMA50 괴리율 + 크로스 감지</b> ({now})

• 조건 충족 종목 ({len(triggered)}개):
{chr(10).join(triggered)}

✅ 조건:
- 실시간가 EMA50 ±13% 이상
- EMA50이 EMA200 상향/하향 돌파 시 골든/데드크로스
- 주기: 5분 실시간 + 오전 7시 요약
"""
        send_telegram_message(message)
    elif daily:
        send_telegram_message(f"[PARK 시스템 – 3번 항목] {now} 기준 조건 충족 종목 없음")
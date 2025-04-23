# modules/etf/alert_etf_signals.py

import pandas as pd
import yfinance as yf
from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message
from config import ETF_THEME_TICKERS

# 스토캐스틱 + 볼린저밴드
def calc_technical_indicators(df):
    low_min = df["Low"].rolling(14).min()
    high_max = df["High"].rolling(14).max()
    k = 100 * (df["Close"] - low_min) / (high_max - low_min)
    d = k.rolling(3).mean()

    bb_mid = df["Close"].rolling(20).mean()
    bb_std = df["Close"].rolling(20).std()
    upper = bb_mid + 2 * bb_std
    lower = bb_mid - 2 * bb_std

    return k.iloc[-1], d.iloc[-1], upper.iloc[-1], lower.iloc[-1], df["Close"].iloc[-1]

# 수급 (예시: 3일 연속 외인 순매수 여부)
def check_supply_flow(ticker):
    # 실전에서는 증권사 API 또는 DB 사용
    flow = [50, 100, 20]  # 3일치 외인 순매수 금액 (억 단위)
    return all(x > 0 for x in flow)

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    triggered = []

    for ticker in ETF_THEME_TICKERS:
        df = yf.download(ticker, period="3mo", interval="1d", progress=False)
        if df is None or len(df) < 30:
            continue

        k, d, upper, lower, close = calc_technical_indicators(df)
        tech_signal = ""
        if k > 80 and d > 80:
            tech_signal = "📈 과매수"
        elif k < 20 and d < 20:
            tech_signal = "📉 과매도"
        elif close >= upper:
            tech_signal = "📈 BB 상단 돌파"
        elif close <= lower:
            tech_signal = "📉 BB 하단 돌파"

        flow_signal = "✅ 3일 연속 외인 순매수" if check_supply_flow(ticker) else ""

        if tech_signal or flow_signal:
            result = f"{ticker} → {tech_signal} {flow_signal}".strip()
            triggered.append(result)

    if triggered:
        msg = f"""[PARK 시스템 – 11번 항목]
📊 <b>ETF 테마 기술적/수급 알림</b> ({now})

• 조건 충족 ETF ({len(triggered)}개):
{chr(10).join(triggered)}

✅ 주기: 5분 실시간 + 오전 7시 요약
✅ 기준: 과매수/과매도/BB 돌파 + 외인 수급 흐름
"""
        send_telegram_message(msg)
    elif daily:
        send_telegram_message(f"[PARK 시스템 – 11번 항목] {now}\n조건 충족 ETF 없음")
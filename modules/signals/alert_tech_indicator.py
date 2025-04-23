# modules/signals/alert_tech_indicator.py

import pandas as pd
import yfinance as yf
from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

from config import KOSPI_TOP_50, KOSDAQ_TOP_50, CRYPTO_TOP_10

def fetch_price_data(ticker, interval="1d", period="90d"):
    try:
        df = yf.download(ticker, interval=interval, period=period, progress=False)
        return df
    except:
        return None

def calculate_stochastic(df, k_period, d_period, smooth_k):
    low_min = df['Low'].rolling(window=k_period).min()
    high_max = df['High'].rolling(window=k_period).max()
    k_fast = 100 * (df['Close'] - low_min) / (high_max - low_min)
    k_slow = k_fast.rolling(window=smooth_k).mean()
    d = k_slow.rolling(window=d_period).mean()
    return k_slow, d

def calculate_bollinger(df, window=20):
    ma = df['Close'].rolling(window).mean()
    std = df['Close'].rolling(window).std()
    upper = ma + (2 * std)
    lower = ma - (2 * std)
    return upper, lower

def analyze_indicator(ticker):
    daily = fetch_price_data(ticker, interval="1d", period="90d")
    weekly = fetch_price_data(ticker, interval="1wk", period="2y")

    if daily is None or len(daily) < 60 or weekly is None or len(weekly) < 30:
        return None

    # ✅ 일봉 분석
    st_k1_d, st_d1_d = calculate_stochastic(daily, 5, 3, 3)
    st_k2_d, st_d2_d = calculate_stochastic(daily, 10, 6, 6)
    upper, lower = calculate_bollinger(daily)

    close = daily["Close"].iloc[-1]
    overbought_d = (st_k1_d.iloc[-1] > 80 and st_d1_d.iloc[-1] > 80 and
                    st_k2_d.iloc[-1] > 80 and st_d2_d.iloc[-1] > 80)
    oversold_d = (st_k1_d.iloc[-1] < 20 and st_d1_d.iloc[-1] < 20 and
                  st_k2_d.iloc[-1] < 20 and st_d2_d.iloc[-1] < 20)
    bb_upper_touch = close >= upper.iloc[-1]
    bb_lower_touch = close <= lower.iloc[-1]

    daily_signal = None
    if overbought_d:
        daily_signal = "📈 일봉 과매수"
    elif oversold_d:
        daily_signal = "📉 일봉 과매도"
    elif bb_upper_touch:
        daily_signal = "📈 볼린저 상단 돌파"
    elif bb_lower_touch:
        daily_signal = "📉 볼린저 하단 돌파"

    # ✅ 주봉 분석
    st_k1_w, st_d1_w = calculate_stochastic(weekly, 5, 3, 3)
    last_k_w = st_k1_w.iloc[-1]
    last_d_w = st_d1_w.iloc[-1]
    weekly_signal = None
    if last_k_w > 80 and last_d_w > 80:
        weekly_signal = "📈 주봉 과매수"
    elif last_k_w < 20 and last_d_w < 20:
        weekly_signal = "📉 주봉 과매도"

    signals = []
    if daily_signal:
        signals.append(daily_signal)
    if weekly_signal:
        signals.append(weekly_signal)

    return ", ".join(signals) if signals else None

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    targets = KOSPI_TOP_50 + KOSDAQ_TOP_50 + CRYPTO_TOP_10
    triggered = []

    for ticker in targets:
        signal = analyze_indicator(ticker)
        if signal:
            triggered.append(f"{ticker} → {signal}")

    if triggered:
        message = f"""[PARK 시스템 – 2번 항목]
📊 <b>보조지표 기반 시그널 감지</b> ({now})

• 조건 충족 종목 ({len(triggered)}개):
{chr(10).join(triggered)}

✅ 기준:
- 일봉: Stochastic(5,3,3) AND (10,6,6) OR 볼린저밴드
- 주봉: Stochastic(5,3,3)
- 주기: 5분 실시간 + 오전 7시 요약
"""
        send_telegram_message(message)
    elif daily:
        send_telegram_message(f"[PARK 시스템 – 2번 항목] {now} 기준 조건 충족 종목 없음")
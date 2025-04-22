# modules/flows/alert_fi_five_day.py

import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message
from config import KOSPI50_TICKERS, KOSDAQ50_TICKERS

# 🔽 실제로는 DB 또는 API 연동 필요. 예시로 DataFrame 구조 가정
def fetch_fi_data(ticker):
    # 예시 데이터프레임 (실전에서는 최근 5일 외인/기관 수급 데이터 수집)
    return pd.DataFrame({
        "date": pd.date_range(end=datetime.now(), periods=5),
        "foreigner": [100, 200, -150, 300, 400],  # + 순매수 / - 순매도
        "institution": [50, 100, 30, 20, 10]
    })

def check_consecutive_flow(df, col):
    values = df[col].tolist()
    return all(v > 0 for v in values), all(v < 0 for v in values)

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    targets = KOSPI50_TICKERS + KOSDAQ50_TICKERS
    alerts = []

    for ticker in targets:
        df = fetch_fi_data(ticker)
        if df is None or len(df) < 5:
            continue

        f_buy, f_sell = check_consecutive_flow(df, "foreigner")
        i_buy, i_sell = check_consecutive_flow(df, "institution")

        signals = []
        if f_buy:
            signals.append("🔴 외국인 5일 순매수")
        elif f_sell:
            signals.append("🔵 외국인 5일 순매도")
        if i_buy:
            signals.append("🔴 기관 5일 순매수")
        elif i_sell:
            signals.append("🔵 기관 5일 순매도")

        if signals:
            alerts.append(f"{ticker} → {' / '.join(signals)}")

    if alerts:
        msg = f"""[PARK 시스템 – 5번 항목]
📊 <b>외국인/기관 5일 연속 수급 종목</b> ({now})

• 조건 충족 종목:
{chr(10).join(alerts)}

✅ 조건: 외국인/기관 순매수 or 순매도 5일 연속
✅ 대상: KOSPI50 + KOSDAQ50
✅ 주기: 종가 후 + 다음날 오전 7시
"""
        send_telegram_message(msg)
    elif daily:
        send_telegram_message(f"[PARK 시스템 – 5번 항목] {now} 기준 조건 충족 종목 없음")
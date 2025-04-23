# modules/economy/alert_vix_volatility.py

import yfinance as yf
from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message


def fetch_vix_value():
    """
    ✅ VIX 변동성 지수 데이터를 yfinance로부터 수집
    """
    try:
        df = yf.download("^VIX", period="2d", interval="1d", progress=False)
        if not df.empty and len(df) >= 2:
            return float(df["Close"].iloc[-1])
        return None
    except Exception as e:
        print(f"[❌ VIX 데이터 수집 오류] {e}")
        return None


def run(daily=False):
    """
    ✅ VIX가 25 초과 또는 15 미만일 경우 알림 발송
    :param daily: True일 경우, 데이터 수집 실패 시에도 알림
    """
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    vix = fetch_vix_value()

    if vix is None:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 18번 항목] {now}\n⚠️ VIX 데이터 수집 실패")
        return

    # 상태 분류
    if vix > 25:
        status = "📈 급등 (공포 증가)"
    elif vix < 15:
        status = "📉 급락 (과열 or 낙관)"
    else:
        status = "🔎 안정적 구간"

    # 텔레그램 메시지
    msg = f"""[PARK 시스템 – 18번 항목]
📊 <b>VIX 변동성 지수</b> ({now} 기준)

• 현재 VIX: <b>{vix:.2f}</b>
• 상태: {status}

✅ 기준: VIX > 25 or < 15
🕖 주기: 오전 7시 요약
"""
    send_telegram_message(msg)
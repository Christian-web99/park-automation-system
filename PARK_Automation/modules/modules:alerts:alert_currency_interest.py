# modules/alerts/alert_currency_interest.py

from datetime import datetime
from zoneinfo import ZoneInfo
import requests

from config import FRED_API_KEY
from telegram_handler import send_telegram_message
from services.fetch_market_data import (
    get_usdkrw_exchange_rate,
    get_bond_yields,
    get_btc_price_from_okx
)

def get_fred_series_latest(series_id):
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": 1
    }
    try:
        res = requests.get(url, params=params, timeout=5).json()
        return float(res["observations"][0]["value"])
    except Exception as e:
        print(f"[❗FRED 오류] {series_id} – {e}")
        return None

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")

    usdkrw = get_usdkrw_exchange_rate()
    us_yield, kr_yield = get_bond_yields()
    btc = get_btc_price_from_okx()

    us_base = get_fred_series_latest("DFEDTARU")
    kr_base = get_fred_series_latest("INTDSRKRM193N")
    kr_call = get_fred_series_latest("IRSTCI01KRA156N")

    # ✅ 수동 입력 항목
    cme_prob = "동결 87% / 인하 13%"
    kospi200_fut = "+0.42%"

    if None in [usdkrw, us_base, kr_base, us_yield, kr_yield, kr_call, btc]:
        send_telegram_message(f"[PARK 시스템] ❗1번 알림 실패 – {now}\n데이터 수집 누락")
        return

    msg = f"""[PARK 시스템 – 1번 항목]
📊 <b>환율·시장금리 요약</b> ({now} 기준)

• 원/달러 환율: {usdkrw:,.2f}원  
• 미국 기준금리: {us_base:.2f}%  
• 한국 기준금리: {kr_base:.2f}%  
• 미국 10년물 금리: {us_yield:.2f}%  
• 한국 10년물 금리: {kr_yield:.2f}%  
• 한국 콜금리: {kr_call:.2f}%  
• CME 금리 인상 확률: {cme_prob}  
• 비트코인 시세: ${btc:,.0f}  
• KOSPI200 야간선물: {kospi200_fut}

🔁 오전 7시 요약 자동 알림
"""
    send_telegram_message(msg)
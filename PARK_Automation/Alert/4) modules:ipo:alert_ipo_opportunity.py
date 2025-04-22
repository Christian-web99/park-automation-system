# modules/ipo/alert_ipo_opportunity.py

import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

from telegram_handler import send_telegram_message
from services.fetch_ipo_list import fetch_recent_ipos


def check_basic_undervaluation(row):
    """
    ✅ 기본 조건:
    PER ≤ 13, PBR ≤ 1.5, DIV ≥ 6%, 고점 대비 -50% 이하
    → 1개 이상 충족 시 통과
    """
    return (
        row.get("PER", 99) <= 13 or
        row.get("PBR", 99) <= 1.5 or
        row.get("DIV", 0) >= 6 or
        row.get("DROP_PCT", 0) <= -50
    )


def check_park_a1_logic(row):
    """
    ✅ PARK A1 전략 (4개 중 2개 이상 충족)
    ① -60% ~ -40% 과대낙폭
    ② 거래량 급등 + 최근 고가 돌파 + 양봉
    ③ 공모가 이하 + PER ≤ 10 or PBR ≤ 1.5 + 시총 < 1000억 + 유통비율 30%↓
    ④ 외국인/기관 순매수 전환
    """
    conds = 0

    # ① 과대낙폭
    if -60 <= row.get("DROP_PCT", 0) <= -40:
        conds += 1
    # ② 기술적 조건
    if row.get("VOLUME_SURGE") and row.get("BREAKOUT") and row.get("BULLISH_CANDLE"):
        conds += 1
    # ③ 공모가 이하 + 재무 + 시총 + 유통
    if (
        row.get("IPO_PRICE", 0) > row.get("CURRENT_PRICE", 0) and
        (row.get("PER", 99) <= 10 or row.get("PBR", 99) <= 1.5) and
        row.get("MARKET_CAP", 9999) < 1000 and
        row.get("FLOAT_RATIO", 100) <= 30
    ):
        conds += 1
    # ④ 외인/기관 순매수 전환
    if row.get("NET_BUY"):
        conds += 1

    return conds >= 2


def run(daily=False):
    """
    🔁 매 5분 실시간 or 매주 월요일 오전 7시 요약
    """
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    ipo_data = fetch_recent_ipos()

    if not ipo_data:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 4번 알림]\n{now}\n📭 조건 충족 신규상장주 없음")
        return

    df = pd.DataFrame(ipo_data)

    basic_hits = df[df.apply(check_basic_undervaluation, axis=1)]
    park_hits = df[df.apply(check_park_a1_logic, axis=1)]

    if basic_hits.empty and park_hits.empty:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 4번 알림]\n{now}\n📭 조건 충족 신규상장주 없음")
        return

    message = f"""📢 <b>[PARK 시스템 – 4번 신규상장 알림]</b>
📊 <b>저평가 신규상장주 + PARK A1 전략</b>
🕘 {now}

✅ 기본 조건 충족 <b>({len(basic_hits)}개)</b>
{chr(10).join(basic_hits['TICKER'].astype(str).tolist()) if not basic_hits.empty else '없음'}

✅ PARK A1 전략 충족 <b>({len(park_hits)}개)</b>
{chr(10).join(park_hits['TICKER'].astype(str).tolist()) if not park_hits.empty else '없음'}

🕘 주기: 5분 실시간 + 매주 월요일 오전 7시
📌 기준: PER≤13, PBR≤1.5, 배당≥6%, –50%↓ or PARK A1(2개 이상)
"""
    send_telegram_message(message)
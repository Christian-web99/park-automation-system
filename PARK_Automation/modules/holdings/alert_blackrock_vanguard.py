# modules/holdings/alert_blackrock_vanguard.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

from config import KOSPI50_TICKERS, KOSDAQ50_TICKERS

# ✅ 실전에서는 DB 또는 정기 수집 CSV 대비 비교
def fetch_current_holdings():
    # 실전에서는 DART, ETF 보고서, 데이터 크롤링 연동
    return {
        "BlackRock": {"005930.KS": 300000, "000660.KS": 250000},
        "Vanguard": {"005930.KS": 200000},
        "NPS": {"035420.KQ": 180000}  # 국민연금
    }

def fetch_previous_holdings():
    return {
        "BlackRock": {"005930.KS": 200000},
        "Vanguard": {},
        "NPS": {"035420.KQ": 180000}  # 변동 없음
    }

def compare_holdings(current, previous):
    results = []
    for inst in current:
        for ticker, cur_amt in current[inst].items():
            prev_amt = previous.get(inst, {}).get(ticker, 0)
            if cur_amt > prev_amt:
                if prev_amt == 0:
                    status = "🆕 신규 매집"
                else:
                    status = f"⬆️ 보유 증가 (+{cur_amt - prev_amt:,}주)"
                results.append(f"{inst} → {ticker}: {status}")
    return results

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    current = fetch_current_holdings()
    previous = fetch_previous_holdings()

    results = compare_holdings(current, previous)

    if results:
        msg = f"""[PARK 시스템 – 10번 항목]
📊 <b>기관 보유 종목 변화 감지</b> ({now})

• 조건 충족 항목 ({len(results)}개):
{chr(10).join(results)}

✅ 기준: 블랙록 / 뱅가드 / 국민연금 보유 비중 증가 or 신규 매입
✅ 주기: 5분 실시간 + 오전 7시 요약
"""
        send_telegram_message(msg)
    elif daily:
        send_telegram_message(f"[PARK 시스템 – 10번 항목] {now}\n조건 충족 변화 없음")
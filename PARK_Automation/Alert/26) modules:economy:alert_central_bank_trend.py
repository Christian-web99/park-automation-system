# modules/economy/alert_central_bank_trend.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

def fetch_central_bank_trends():
    return [
        {"기관": "Fed (미국)", "요약": "6월 FOMC에서 기준금리 동결 가능성 높음. 일부 위원은 1회 인하 전망"},
        {"기관": "ECB (유럽)", "요약": "6월부터 금리 인하 논의 시작될 것으로 예상"},
        {"기관": "BOJ (일본)", "요약": "YCC(수익률 곡선 제어) 정책 유지, 엔화 약세 대응 논의"},
        {"기관": "PBoC (중국)", "요약": "지급준비율 인하 가능성 시사, 유동성 공급 확대 전망"},
        {"기관": "BOE (영국)", "요약": "물가 상승세 둔화 확인, 1분기 내 첫 인하 가능성 언급"}
    ]

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    trends = fetch_central_bank_trends()

    if not trends:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 26번 항목] {now}\n중앙은행 동향 데이터 없음")
        return

    msg = f"""[PARK 시스템 – 26번 항목]
🏦 <b>5대 중앙은행 동향 요약</b> ({now})

"""
    for item in trends:
        msg += f"• {item['기관']}: {item['요약']}\n"

    msg += "\n✅ 대상: Fed, ECB, BOJ, PBoC, BOE\n✅ 주기: 오전 7시 요약"
    send_telegram_message(msg)
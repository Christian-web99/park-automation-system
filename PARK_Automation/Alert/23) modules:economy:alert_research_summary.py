# modules/economy/alert_research_summary.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

def fetch_latest_research():
    # 예시 기반 수동 or 추후 자동화 가능
    return [
        {
            "기관": "블랙록",
            "코멘트": "중국 기술주 비중 확대를 권고하며, 향후 반등 가능성 언급",
        },
        {
            "기관": "JP모건",
            "코멘트": "S&P500은 과매수 구간 진입, 단기 조정 경고",
        },
        {
            "기관": "골드만삭스",
            "코멘트": "미국 10년물 금리 4.7% 이상 지속시 성장주 부담 예상"
        }
    ]

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    research_list = fetch_latest_research()

    if not research_list:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 23번 항목] {now}\n주요 기관 리서치 요약 없음")
        return

    msg = f"""[PARK 시스템 – 23번 항목]
📑 <b>주요 기관 리서치 요약</b> ({now})

"""

    for item in research_list:
        msg += f"• {item['기관']}: {item['코멘트']}\n"

    msg += "\n✅ 주기: 오전 7시 요약"
    send_telegram_message(msg)
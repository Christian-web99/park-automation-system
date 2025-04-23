# modules/economy/alert_cds_spike.py

from datetime import datetime
from zoneinfo import ZoneInfo
from telegram_handler import send_telegram_message

# 예시용 수동 데이터 – 실전은 RapidAPI, Investing, 또는 정부 통계 크롤링 필요
CDS_SAMPLE = {
    "Korea": {"현재": 121.3, "전일": 105.2},
    "Japan": {"현재": 54.8, "전일": 52.0},
    "USA": {"현재": 25.1, "전일": 24.9}
}

def detect_cds_spike():
    results = []
    for country, values in CDS_SAMPLE.items():
        curr = values["현재"]
        prev = values["전일"]
        pct = ((curr - prev) / prev) * 100
        alert = ""

        if pct > 10:
            alert += "🚨 급등"
        elif curr > 200:
            alert += "⚠️ 위험 수준"
        elif curr > 100:
            alert += "⚠️ 경계"

        results.append({
            "국가": country,
            "현재": curr,
            "전일": prev,
            "등락률": f"{pct:+.2f}%",
            "상태": alert
        })
    return results

def run(daily=False):
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    cds_data = detect_cds_spike()

    if not cds_data:
        if daily:
            send_telegram_message(f"[PARK 시스템 – 22번 항목] {now}\nCDS 데이터 없음")
        return

    msg = f"""[PARK 시스템 – 22번 항목]
💥 <b>CDS 프리미엄 급등 감지</b> ({now})

"""

    for item in cds_data:
        msg += f"• {item['국가']}: {item['현재']}bp ({item['등락률']}) {item['상태']}\n"

    msg += "\n✅ 기준: +10% 이상 급등 or 100bp/200bp 경계선 이상\n✅ 주기: 5분 실시간 + 오전 7시 요약"
    send_telegram_message(msg)
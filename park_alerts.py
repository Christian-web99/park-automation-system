import schedule
import time
import requests
import os
from telegram import send_message

# ✅ 기준 환율 (전일 종가 기준 수동 설정, 향후 자동화 가능)
BASE_USDKRW = 1417.0

def run_park_alerts():
    # ✅ 오전 7시 요약 알림
    def morning_summary():
        message = (
            "🌅 PARK 자동화 시스템 – 오전 7시 요약 알림입니다.\n"
            "1. 환율/금리\n"
            "2. 기술적 분석 (보조지표, EMA)\n"
            "3. 신규상장주/PARK A1\n"
            "4. 외국인/기관 수급\n"
            "5. 옵션/공매도 요약\n"
            "6. ETF/인물 발언/캘린더\n"
            "7. 거시지표/정책감지\n"
            "8. 시장 심리 요약"
        )
        send_message(message)

    # ✅ 실시간 환율 급등/급락 감지
    def realtime_alerts():
        try:
            url = "https://api.exchangerate.host/latest?base=USD&symbols=KRW"
            response = requests.get(url)
            data = response.json()
            usdkrw = data['rates']['KRW']
            change = round(usdkrw - BASE_USDKRW, 2)

            if abs(change) >= 3:
                emoji = "📈" if change > 0 else "📉"
                direction = "상승" if change > 0 else "하락"
                message = (
                    f"{emoji} 환율 실시간 감지\n"
                    f"USD/KRW {direction} 감지!\n"
                    f"현재 환율: {usdkrw:.2f}원\n"
                    f"기준 대비 {change:+.2f}원"
                )
                send_message(message)
        except Exception as e:
            print(f"❌ 환율 API 오류: {e}")

    # ✅ 종가 후 요약
    def end_of_day_summary():
        message = "📊 종가 후 요약 알림 – 외국인 수급, 옵션, 공매도 등"
        send_message(message)

    # 알림 스케줄 등록
    schedule.every().day.at("07:00").do(morning_summary)       # 오전 7시 요약
    schedule.every(1).minutes.do(realtime_alerts)              # 실시간 감지
    schedule.every().day.at("15:45").do(end_of_day_summary)    # 종가 후 요약

    print("✅ PARK 시스템 작동 시작 (오전 7시 요약 + 실시간 환율 감지 + 종가 후 요약)")

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as e:
            print(f"🔥 오류 발생: {e}")
            time.sleep(10)

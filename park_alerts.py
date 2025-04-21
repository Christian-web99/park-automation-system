import schedule
import time
from telegram import send_message


def run_park_alerts():
    # 오전 7시 알림 예시
    def morning_summary():
        message = "🌅 PARK 자동화 시스템 – 오전 7시 요약 알림 테스트입니다."
        send_message(message)

    # 테스트용: 매 1분마다 실행되도록 설정 (실제 환경에서는 07:00으로 변경)
    schedule.every(1).minutes.do(morning_summary)

    print("✅ run_park_alerts() started")

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as e:
            print(f"🔥 오류 발생: {e}")
            time.sleep(10)

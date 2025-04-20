import time
import schedule
from park_alerts import run_park_alerts
from telegram import send_message

def send_morning_summary():
    send_message("☀️ 오전 7시 요약 알림 준비 중...")
    run_park_alerts()

# 오전 7시에 알림 실행 예약
schedule.every().day.at("07:00").do(send_morning_summary)

print("✅ PARK Automation System is running...")

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        time.sleep(10)

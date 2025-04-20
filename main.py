import time
import schedule
from park_alerts import get_summary_message
from telegram import send_message

def send_morning_summary():
    message = get_summary_message()
    send_message(message)

schedule.every().day.at("07:00").do(send_morning_summary)

print("✅ PARK Automation System is running...")

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        time.sleep(10)

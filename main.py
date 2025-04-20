import schedule
import time
from telegram import send_message
from modules.park_alerts import run_all_7am_tasks

schedule.every().day.at("07:00").do(run_all_7am_tasks)

print("✅ PARK 자동화 시스템 실행 중...")

while True:
    schedule.run_pending()
    time.sleep(1)
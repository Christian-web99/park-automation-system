import schedule
import time
from telegram import send_message  # ← telegram.py에 있는 함수

def send_morning_summary():
    message = "📊 오전 7시 요약 알림입니다! (테스트 알림)"
    send_message(message)

# 매일 오전 7시에 실행될 작업 등록
schedule.every().day.at("07:00").do(send_morning_summary)

print("✅ PARK Automation System Running...")

# 무한 루프로 매 분마다 작업 확인 및 실행
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print(f"❗ 오류 발생: {e}")
        time.sleep(10)

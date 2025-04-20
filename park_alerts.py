from datetime import datetime
from telegram import send_message

def run_park_alerts():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"📡 PARK 자동화 시스템이 정상 작동 중입니다.\n현재 시각: {now}"
    send_message(message)

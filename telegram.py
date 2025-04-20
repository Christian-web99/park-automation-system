import os
import requests

def send_message(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("❌ TELEGRAM_TOKEN 또는 TELEGRAM_CHAT_ID 환경변수가 없습니다.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("✅ 메시지 전송 성공")
    except Exception as e:
        print(f"❌ 메시지 전송 실패: {e}")

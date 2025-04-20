import os
import requests

def send_message(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_ids = os.getenv("TELEGRAM_CHAT_ID").split(",")

    for chat_id in chat_ids:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id.strip(),
            "text": message
        }
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            print(f"✅ 메시지 전송 성공 → {chat_id}")
        except Exception as e:
            print(f"❌ 메시지 전송 실패 → {chat_id}: {e}")

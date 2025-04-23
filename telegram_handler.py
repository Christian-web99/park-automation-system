# telegram_handler.py

import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_IDS

def send_telegram_message(message: str, parse_mode: str = "HTML") -> None:
    """
    텔레그램 메시지를 설정된 모든 사용자에게 전송합니다.
    :param message: 전송할 메시지 문자열
    :param parse_mode: 메시지 포맷 ("HTML" 또는 "Markdown")
    """
    for chat_id in TELEGRAM_CHAT_IDS:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": message,
                "parse_mode": parse_mode
            }
            response = requests.post(url, data=payload, timeout=10)

            if response.status_code == 200:
                print(f"[✅] 메시지 전송 성공 → {chat_id}")
            else:
                print(f"[❌] 메시지 전송 실패 → {chat_id}: {response.status_code}, {response.text}")

        except Exception as e:
            print(f"[🚨] 텔레그램 예외 발생 → {chat_id}: {str(e)}")
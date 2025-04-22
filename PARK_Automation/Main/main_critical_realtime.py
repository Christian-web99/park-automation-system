import time
from park_alerts import (
    alert_12_influential_speech,
    alert_14_crisis_event,
    alert_24_policy_announcement,
)

def run_every(interval_seconds, func):
    while True:
        try:
            func()
        except Exception as e:
            print(f"[❗] Error in {func.__name__}: {e}")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    from threading import Thread

    print("[🔔] Starting main_critical_realtime.py – 초실시간 감시 시작 (1분 간격)")

    Thread(target=run_every, args=(60, alert_12_influential_speech)).start()   # 12번: 인물 발언
    Thread(target=run_every, args=(60, alert_14_crisis_event)).start()          # 14번: 글로벌 위기
    Thread(target=run_every, args=(60, alert_24_policy_announcement)).start()   # 24번: 각국 정책 발표

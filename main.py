import time
from park_alerts import run_park_alerts

print("✅ PARK 자동화 시스템 실행 중...")

while True:
    try:
        run_park_alerts()
        time.sleep(60)
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        time.sleep(60)

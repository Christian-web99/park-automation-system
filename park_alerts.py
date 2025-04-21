# Alert logic for 26 features

from modules import config
from modules import technical_indicators, supply_demand, exchange_rate, global_events
from modules.telegram import send_message

import schedule
import time

def run_park_alerts():
    print("✅ PARK 자동화 시스템 시작됨!")

    # 기술적 분석 기반
    technical_indicators.check_indicators()
    
    # 수급 기반
    supply_demand.check_supply_demand()
    
    # 환율 및 금리
    exchange_rate.check_exchange_rate()

    # 글로벌 이벤트
    global_events.check_global_events()

# 테스트용 즉시 실행
if __name__ == "__main__":
    run_park_alerts()
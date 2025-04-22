import time
from park_alerts import (
    run_tech_signal_alert,
    run_ema_cross_alert,
    run_ipo_alert,
    run_blackrock_alert,
    run_etf_signal_alert,
    run_commodity_alert,
    run_rate_futures_alert,
    run_forex_flow_alert,
    run_gdp_release_alert,
    run_cds_spike_alert,
    run_policy_announcement_alert,
    run_pmi_alert,
)

INTERVAL_MINUTES = 5

if __name__ == "__main__":
    while True:
        print("\n[PARK 실시간 시스템 – main_realtime.py] 5분 간격 실행 중...")

        # 기술적 분석 기반
        run_tech_signal_alert(realtime=True)
        run_ema_cross_alert(realtime=True)
        run_ipo_alert(realtime=True)  # 신규상장주 감지 (PARK A1 포함)

        # 수급 기반
        run_blackrock_alert(realtime=True)
        run_etf_signal_alert(realtime=True)

        # 거시지표 확장
        run_commodity_alert(realtime=True)
        run_rate_futures_alert(realtime=True)
        run_forex_flow_alert(realtime=True)

        # 전문가형 확장
        run_gdp_release_alert(realtime=True)
        run_cds_spike_alert(realtime=True)
        run_pmi_alert(realtime=True)

        print(f"[대기] {INTERVAL_MINUTES}분 후 다음 실행...\n")
        time.sleep(INTERVAL_MINUTES * 60)

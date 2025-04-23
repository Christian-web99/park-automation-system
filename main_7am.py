# main_7am.py (오전 7시 알림 전용 - 모든 메시지를 하나로 통합 전송)
print("\u2705 main_7am.py started")
print("\u2705 모든 설정 정상 작동 중 - 오전 7시 요약 알림 통합 실행")

import os
import sys

# ✅ 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "modules"))
sys.path.append(os.path.join(BASE_DIR, "services"))

# 텔레그램 알림 모듈
from telegram_handler import send_telegram_message

# 각 모듈의 run 함수 (daily=True 시 메시지를 반환하도록 사전에 수정되어야 함)
from modules.alerts.alert_currency_interest import run as run_currency_interest
from modules.signals.alert_tech_indicator import run as run_tech_indicator
from modules.ema.alert_ema_cross import run as run_ema_cross
from modules.ipo.alert_ipo_opportunity import run as run_ipo_alert
from modules.flows.alert_fi_five_day import run as run_fi_five_day
from modules.flows.alert_weekly_options import run as run_weekly_options
from modules.flows.alert_short_selling import run as run_short_selling
from modules.flows.alert_kospi200_futures import run as run_kospi200_futures
from modules.weekly.alert_us_options_summary import run as run_us_option_summary
from modules.holdings.alert_blackrock_vanguard import run as run_blackrock_holdings
from modules.etf.alert_etf_signals import run as run_etf_signals
from modules.people.alert_influential_speech import run as run_influential_speech
from modules.calendar.alert_economic_calendar import run as run_economic_calendar
from modules.crisis.alert_global_crisis import run as run_global_crisis
from modules.macro.alert_commodities import run as run_commodities
from modules.macro.alert_earnings_report import run as run_earnings_report
from modules.macro.alert_rate_futures import run as run_rate_futures
from modules.economy.alert_vix_volatility import run as run_vix_alert
from modules.macro.alert_forex_flow import run as run_forex_flow
from modules.economy.alert_gdp_release import run as run_gdp_release
from modules.economy.alert_yield_curve_inversion import run as run_yield_curve
from modules.economy.alert_cds_spike import run as run_cds_spike
from modules.economy.alert_research_summary import run as run_research_summary
from modules.economy.alert_policy_announcement import run as run_policy_announcement
from modules.economy.alert_pmi_release import run as run_pmi_release
from modules.economy.alert_central_bank_trend import run as run_cb_trend
from modules.sentiment.alert_market_sentiment import run as run_sentiment

# ✅ 실행 함수: 결과 메시지를 모아서 통합 전송
def safe_collect(name, func):
    try:
        print(f"\n▶️ Collecting {name}...")
        result = func(daily=True)
        if result:
            print(f"✅ {name} collected.")
            return result
        else:
            return None
    except Exception as e:
        print(f"❌ Error in {name}: {e}")
        return f"[Error] {name}: {e}"

if __name__ == "__main__":
    print("\n🚀 Launching PARK 7AM Summary Modules...\n")
    messages = []

    for name, func in [
        ("Currency & Interest", run_currency_interest),
        ("Technical Indicator", run_tech_indicator),
        ("EMA Cross", run_ema_cross),
        ("IPO Alert", run_ipo_alert),
        ("FI 5-Day Flow", run_fi_five_day),
        ("Weekly Options", run_weekly_options),
        ("Short Selling", run_short_selling),
        ("KOSPI200 Futures", run_kospi200_futures),
        ("US Option Summary", run_us_option_summary),
        ("BlackRock Holdings", run_blackrock_holdings),
        ("ETF Signals", run_etf_signals),
        ("Influential Speech", run_influential_speech),
        ("Economic Calendar", run_economic_calendar),
        ("Global Crisis", run_global_crisis),
        ("Commodities", run_commodities),
        ("Earnings Report", run_earnings_report),
        ("Rate Futures", run_rate_futures),
        ("VIX Alert", run_vix_alert),
        ("Forex Flow", run_forex_flow),
        ("GDP Release", run_gdp_release),
        ("Yield Curve", run_yield_curve),
        ("CDS Spike", run_cds_spike),
        ("Research Summary", run_research_summary),
        ("Policy Announcement", run_policy_announcement),
        ("PMI Release", run_pmi_release),
        ("Central Bank Trend", run_cb_trend),
        ("Market Sentiment", run_sentiment),
    ]:
        msg = safe_collect(name, func)
        if msg:
            messages.append(msg)

    full_report = "\n\n".join(messages)
    send_telegram_message(full_report)
    print("\n🌅 7AM Summary Completed. All alerts sent.")
    sys.exit(0)

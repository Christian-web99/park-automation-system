print("\u2705 main.py started")
print("\u2705 모든 설정 정상 작동 중 - 테스트 로그 출력")

import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

# ✅ 핵심: PYTHONPATH에 현재 디렉토리 + 하위 모듈 경로 추가
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "modules"))
sys.path.append(os.path.join(BASE_DIR, "services"))

from telegram_handler import send_telegram_message

# ✅ 모듈별 run 함수 임포트
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

# ✅ 메시지를 모아서 한 번에 전송하기 위한 리스트
messages = []

def safe_run(name, func):
    try:
        print(f"\n▶️ Running {name}...")
        result = func(daily=True) if 'daily' in func.__code__.co_varnames else func()
        if isinstance(result, str):
            messages.append(result)
        print(f"✅ {name} completed successfully.")
    except Exception as e:
        print(f"❌ Error in {name}: {e}")

if __name__ == "__main__":
    print("\U0001F680 Launching PARK Automation Modules...\n")

    # ✅ 주요 모듈 실행
    safe_run("Currency & Interest", run_currency_interest)
    safe_run("Technical Indicator", run_tech_indicator)
    safe_run("EMA Cross", run_ema_cross)
    safe_run("IPO Alert", run_ipo_alert)
    safe_run("FI 5-Day Flow", run_fi_five_day)
    safe_run("Weekly Options", run_weekly_options)
    safe_run("Short Selling", run_short_selling)
    safe_run("KOSPI200 Futures", run_kospi200_futures)
    safe_run("US Option Summary", run_us_option_summary)
    safe_run("BlackRock Holdings", run_blackrock_holdings)
    safe_run("ETF Signals", run_etf_signals)
    safe_run("Influential Speech", run_influential_speech)
    safe_run("Economic Calendar", run_economic_calendar)
    safe_run("Global Crisis", run_global_crisis)
    safe_run("Commodities", run_commodities)
    safe_run("Earnings Report", run_earnings_report)
    safe_run("Rate Futures", run_rate_futures)
    safe_run("VIX Alert", run_vix_alert)
    safe_run("Forex Flow", run_forex_flow)
    safe_run("GDP Release", run_gdp_release)
    safe_run("Yield Curve", run_yield_curve)
    safe_run("CDS Spike", run_cds_spike)
    safe_run("Research Summary", run_research_summary)
    safe_run("Policy Announcement", run_policy_announcement)
    safe_run("PMI Release", run_pmi_release)
    safe_run("Central Bank Trend", run_cb_trend)
    safe_run("Market Sentiment", run_sentiment)

    # ✅ 모든 메시지를 하나로 묶어 전송
    now = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M")
    full_message = f"<b>\U0001F4E2 PARK 시스템 오전 7시 요약 ({now})</b>\n\n" + "\n\n".join(messages)
    send_telegram_message(full_message)

    print("\n\U0001F31F 평가: All modules executed.")
    sys.exit(0)

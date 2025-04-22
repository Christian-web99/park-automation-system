# main.py (완전 실전용)

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
from modules.macro.alert_vix_volatility import run as run_vix_alert
from modules.macro.alert_forex_flow import run as run_forex_flow
from modules.economy.alert_gdp_release import run as run_gdp_release
from modules.economy.alert_yield_curve_inversion import run as run_yield_curve
from modules.economy.alert_cds_spike import run as run_cds_spike
from modules.economy.alert_research_summary import run as run_research_summary
from modules.economy.alert_policy_announcement import run as run_policy_announcement
from modules.economy.alert_pmi_release import run as run_pmi_release
from modules.economy.alert_central_bank_trend import run as run_cb_trend
from modules.sentiment.alert_market_sentiment import run as run_sentiment

# 알림 실행
run_currency_interest()
run_tech_indicator()
run_ema_cross()
run_ipo_alert()  # 기본값 daily=False → 실시간용
run_fi_five_day()
run_weekly_options()
run_short_selling()
run_kospi200_futures()
run_us_option_summary()
run_blackrock_holdings()
run_etf_signals()
run_influential_speech()
run_economic_calendar()
run_global_crisis()
run_commodities()
run_earnings_report()
run_rate_futures()
run_vix_alert()
run_forex_flow()
run_gdp_release()
run_yield_curve()
run_cds_spike()
run_research_summary()
run_policy_announcement()
run_pmi_release()
run_cb_trend()
run_sentiment()

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


def safe_run(name, func):
    try:
        print(f"✅ Running {name}...")
        func()
    except Exception as e:
        print(f"❌ Error in {name}: {e}")


# 안전하게 실행
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
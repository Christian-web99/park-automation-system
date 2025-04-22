import asyncio

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

async def main():
    await asyncio.gather(
        asyncio.to_thread(run_currency_interest),
        asyncio.to_thread(run_tech_indicator),
        asyncio.to_thread(run_ema_cross),
        asyncio.to_thread(run_ipo_alert),
        asyncio.to_thread(run_fi_five_day),
        asyncio.to_thread(run_weekly_options),
        asyncio.to_thread(run_short_selling),
        asyncio.to_thread(run_kospi200_futures),
        asyncio.to_thread(run_us_option_summary),
        asyncio.to_thread(run_blackrock_holdings),
        asyncio.to_thread(run_etf_signals),
        asyncio.to_thread(run_influential_speech),
        asyncio.to_thread(run_economic_calendar),
        asyncio.to_thread(run_global_crisis),
        asyncio.to_thread(run_commodities),
        asyncio.to_thread(run_earnings_report),
        asyncio.to_thread(run_rate_futures),
        asyncio.to_thread(run_vix_alert),
        asyncio.to_thread(run_forex_flow),
        asyncio.to_thread(run_gdp_release),
        asyncio.to_thread(run_yield_curve),
        asyncio.to_thread(run_cds_spike),
        asyncio.to_thread(run_research_summary),
        asyncio.to_thread(run_policy_announcement),
        asyncio.to_thread(run_pmi_release),
        asyncio.to_thread(run_cb_trend),
        asyncio.to_thread(run_sentiment),
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        import traceback
        print("\n🚨 CRITICAL ERROR 발생:", e)
        traceback.print_exc()

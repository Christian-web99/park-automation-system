# park_alerts.py - 실전용 (27개 항목 완전 연결)

from modules.alerts.alert_currency_interest import run as alert_01
from modules.signals.alert_tech_indicator import run as alert_02
from modules.ema.alert_ema_cross import run as alert_03
from modules.ipo.alert_ipo_opportunity import run as alert_04
from modules.flows.alert_fi_five_day import run as alert_05
from modules.flows.alert_weekly_options import run as alert_06
from modules.flows.alert_short_selling import run as alert_07
from modules.flows.alert_kospi200_futures import run as alert_08
from modules.weekly.alert_us_options_summary import run as alert_09
from modules.holdings.alert_blackrock_vanguard import run as alert_10
from modules.etf.alert_etf_signals import run as alert_11
from modules.people.alert_influential_speech import run as alert_12
from modules.calendar.alert_economic_calendar import run as alert_13
from modules.crisis.alert_global_crisis import run as alert_14
from modules.macro.alert_commodities import run as alert_15
from modules.macro.alert_earnings_report import run as alert_16
from modules.macro.alert_rate_futures import run as alert_17
from modules.macro.alert_vix_volatility import run as alert_18
from modules.macro.alert_forex_flow import run as alert_19
from modules.economy.alert_gdp_release import run as alert_20
from modules.economy.alert_yield_curve_inversion import run as alert_21
from modules.economy.alert_cds_spike import run as alert_22
from modules.economy.alert_research_summary import run as alert_23
from modules.economy.alert_policy_announcement import run as alert_24
from modules.economy.alert_pmi_release import run as alert_25
from modules.economy.alert_central_bank_trend import run as alert_26
from modules.sentiment.alert_market_sentiment import run as alert_27

# 오전 7시 요약 알림 전용 실행 함수
def run_all_alerts_7am():
    alert_01(daily=True)
    alert_02(daily=True)
    alert_03(daily=True)
    alert_04(daily=True)
    alert_05(daily=True)
    alert_06(daily=True)
    alert_07(daily=True)
    alert_08(daily=True)
    alert_09(daily=True)
    alert_10(daily=True)
    alert_11(daily=True)
    alert_12(daily=True)
    alert_13(daily=True)
    alert_14(daily=True)
    alert_15(daily=True)
    alert_16(daily=True)
    alert_17(daily=True)
    alert_18(daily=True)
    alert_19(daily=True)
    alert_20(daily=True)
    alert_21(daily=True)
    alert_22(daily=True)
    alert_23(daily=True)
    alert_24(daily=True)
    alert_25(daily=True)
    alert_26(daily=True)
    alert_27(daily=True)

# 실시간 전용 실행 함수 (5분 단위 또는 1분 단위에서 선택적으로 호출)
def run_all_alerts_realtime():
    alert_02()
    alert_03()
    alert_04()
    alert_10()
    alert_11()
    alert_12()
    alert_14()
    alert_15()
    alert_16()
    alert_17()
    alert_19()
    alert_20()
    alert_22()
    alert_24()
    alert_25()

# 1분 실시간 감시 대상만 따로 호출 (critical)
def run_critical_realtime():
    alert_12()
    alert_14()
    alert_24()

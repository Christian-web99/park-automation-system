# config.py

# ✅ 텔레그램 설정
TELEGRAM_BOT_TOKEN = "7662927522:AAGb5ak46iXEcMXxNrT_icJuHrmNjt88Uk4"
TELEGRAM_CHAT_IDS = ["7889848921", "7807026817"]

# ✅ 외부 API 키 (사용자 직접 입력)
DART_API_KEY = "0e3762c7f376d646d543a159dc513198931b7eaa"
IPO_CSV_PATH = "data/ipo_master_list.csv"
FRED_API_KEY = "318cd5891dd8d0769101adced05ad33e"
ALPHA_VANTAGE_API_KEY = "YGMU8WFG84X8QK3L"
COINMARKETCAP_API_KEY = "8da67d27-992a-4874-b42e-7e3eb040e9cd"
NEWS_API_KEY = "b5980a99b1ff4d67937cf35e0f766f06"
TWITTER_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAAAo0wEAAAAAJnfI%2B6rS479H3BtwFIh8ySnFpCg%3DEFSTJrXjGF9vUSkSG7tx7ZFYyyEpRN6TDZ25VaEIz4ygHkuNxw"
INVESTING_API_KEY = "64e6fa6494mshdb9ff9cefe17d6dp1615c6jsn655bb94a209e"
OKX_API_KEY = "c6a9abc7-29e7-4df0-90dd-8753d85b01ae"
OKX_SECRET_KEY = "F4B34C9E2F56777DCC2897A5C3DB2CD3"
OKX_PASSPHRASE = "Qwerty123$"
OPENWEATHER_API_KEY = "71b684f7898a1659f2ed38fcdfda36ed"

# ✅ 기술적 분석용 종목 리스트
KOSPI_TOP_50 = [
    "005930.KS", "000660.KS", "035420.KS", "207940.KS", "051910.KS", "068270.KS", "028260.KS", "005935.KS", "012330.KS", "055550.KS",
    "006400.KS", "035720.KS", "105560.KS", "032830.KS", "003550.KS", "096770.KS", "034730.KS", "066570.KS", "017670.KS", "015760.KS",
    "018260.KS", "003670.KS", "047050.KS", "030200.KS", "032640.KS", "024110.KS", "000270.KS", "033780.KS", "010950.KS", "009150.KS",
    "086790.KS", "023530.KS", "036570.KS", "034020.KS", "011170.KS", "138040.KS", "012450.KS", "009540.KS", "042660.KS", "035250.KS",
    "034220.KS", "000100.KS", "000810.KS", "000880.KS", "090430.KS", "021240.KS", "010130.KS", "010140.KS", "002790.KS", "001040.KS"
]

KOSDAQ_TOP_50 = [
    "035760.KS", "041510.KS", "091990.KS", "263750.KS", "196300.KS", "066970.KS", "005290.KS", "086900.KS", "032500.KS", "078600.KS",
    "241820.KS", "054050.KS", "222080.KS", "142760.KS", "067160.KS", "026890.KS", "230240.KS", "039030.KS", "131970.KS", "035600.KS",
    "033640.KS", "092190.KS", "052260.KS", "058470.KS", "214150.KS", "083310.KS", "036930.KS", "058630.KS", "046890.KS", "039130.KS",
    "115480.KS", "090460.KS", "052400.KS", "104460.KS", "079370.KS", "109080.KS", "121600.KS", "044180.KS", "196170.KS", "100090.KS",
    "195940.KS", "237690.KS", "048260.KS", "090710.KS", "145020.KS", "078340.KS", "050890.KS", "060150.KS", "036810.KS", "080530.KS"
]

CRYPTO_TOP_10 = [
    "BTC/USDT", "ETH/USDT", "XRP/USDT", "SOL/USDT", "BNB/USDT", "DOGE/USDT", "ADA/USDT", "AVAX/USDT", "DOT/USDT", "TRX/USDT"
]

# ✅ alias (모든 모듈에서 이 이름으로 불러옵니다)
KOSPI50_TICKERS = KOSPI_TOP_50
KOSDAQ50_TICKERS = KOSDAQ_TOP_50
CRYPTO_TICKERS = CRYPTO_TOP_10

# ✅ 주요 테마 ETF 티커 리스트 (기술적/수급 분석용)
ETF_THEME_TICKERS = [
    "TIGER AI코리아", "KODEX 2차전지산업", "TIGER 반도체", "KODEX 반도체", "TIGER 미국S&P500", "KODEX 미국나스닥100",
    "TIGER 미국필라델피아반도체", "KODEX 미국S&P에너지", "TIGER MSCI리튬&배터리", "TIGER 미국테크TOP10 INDXX"
]

# ✅ 감시 대상 인물 (상하원 의원 제외 전 세계 영향력자 포함)
KEY_PEOPLE = {
    # 미국 영향력 있는 투자자 (현재 기준)
    "warren_buffett": "@WarrenBuffett",
    "cathie_wood": "@CathieDWood",
    "david_tepper": "@DavidTepper",
    "ken_griffin": "@Citadel",
    "jim_simons": "@renaissance",
    "ray_dalio": "@RayDalio",
    "bill_ackman": "@BillAckman",
    "michael_burry": "@michaeljburry",
    "daniel_loeb": "@DanielSLoeb1",
    "paul_tudor_jones": "@ptj_official",

    # 전설적인 투자자
    "ben_graham": "@valueinvestor",
    "peter_lynch": "@PeterLynchFund",
    "george_soros": "@georgesoros",
    "charlie_munger": "@munger_daily",
    "john_bogle": "@jackbogle",
    "carl_icahn": "@Carl_C_Icahn",
    "philip_fisher": "@PhilFisher1939",
    "jesse_livermore": "@JesseLivermore",
    "john_templeton": "@TempletonTrust",
    "stanley_druckenmiller": "@stanleyDrucken",

    # 미국 상위 기업가
    "elon_musk": "@elonmusk",
    "jeff_bezos": "@JeffBezos",
    "bill_gates": "@BillGates",
    "mark_zuckerberg": "@finkd",
    "steve_jobs": "@steve_jobs_daily",
    "oprah": "@Oprah",
    "sam_walton": "@WalmartInc",
    "charles_schwab": "@CharlesSchwab",
    "tom_love": "@Love_s_Travel",
    "john_johnson": "@JJHoldings",

    # 미국 정치 및 중앙은행
    "Donald Trump": "@realDonaldTrump",
    "Scott Bessent": "@SecScottBessent",
    "janet_yellen": "@SecYellen",
    "neel_kashkari": "@neelkashkari",
    "jerome_powell": "@federalreserve",
    "lael_brainard": "@laelbrainard",

    # 유럽/일본/중국/국제기구
    "christine_lagarde": "@Lagarde",
    "ecb": "@ecb",
    "andrew_bailey": "@bankofengland",
    "pboC": "@PBOC_CN",
    "boj": "@Bank_of_Japan_en",
    "china_embassy": "@ChinaEmbTokyo",
    "imf": "@IMFNews",
    "worldbank": "@WorldBank",
    "bis": "@BIS_org",

    # 주요 금융기관
    "blackrock": "@blackrock",
    "vanguard": "@Vanguard_Group",
    "goldman_sachs": "@GoldmanSachs",
    "jp_morgan": "@jpmorgan",
    "morgan_stanley": "@MorganStanley",
    "bofa": "@BankofAmerica",
    "citi": "@Citi",
    "hsbc": "@HSBC",
    "ubs": "@UBS",
    "credit_suisse": "@CreditSuisse",

    # 한국
    "yoon_suk_yeol": "@President_KR",
    "bank_of_korea": "@bankofkorea",

    # 중동 석유 수장
    "opec": "@OPECSecretariat",
    "saudi_energy": "@MoEnergy_Saudi",
    "uae_energy": "@UAE_MOE",

    # 블룸버그 & CNBC 앵커/이코노미스트
    "bloomberg": "@business",
    "cnbc": "@CNBC",
    "krugman": "@paulkrugman",
    "roubini": "@Nouriel",
    "elerian": "@elerianm",
    "shiller": "@RobertJShiller",
    "larry_summers": "@LHSummers",
    "stiglitz": "@JosephEStiglitz",
    "rogoff": "@krogoff"
}

# ✅ KEY_PEOPLE에서 시간 단위 요약 감시할 대상
KEY_PEOPLE_HOURLY = [
    "warren_buffett", "ray_dalio", "stanley_druckenmiller", "larry_summers", "shiller",
    "worldbank", "vanguard", "boj", "pboC", "bank_of_korea", "saudi_energy", "uae_energy"
]
    # ✅ KEY_PEOPLE에서 실시간 감시할 대상 (예: 트위터 알림 대상)
KEY_PEOPLE_REALTIME = [
    "elon_musk", "jeff_bezos", "bill_ackman", "michael_burry", "janet_yellen", "jerome_powell",
    "christine_lagarde", "blackrock", "goldman_sachs", "imf", "cnbc", "bloomberg"
]

# ✅ 실시간 감지 키워드
REALTIME_KEYWORDS = [
    "전쟁", "계엄", "테러", "대재난", "금융위기", "시장 붕괴", 
    "긴급 발표", "긴급 회의", "원유 공급 중단", "전염병", "북한 핵", "북한 미사일", "아포칼립스", "이상기후", "비상사태", "금융 시스템 위기", "대지진"
]

# config.py 맨 하단쯤에 추가해줘
CRISIS_KEYWORDS = REALTIME_KEYWORDS

# ✅ 주기 설정 (초 단위)
INTERVALS = {
    "7am_summary": 86400,        # 매일 오전 7시
    "realtime_check": 300,       # 5분 주기
    "critical_realtime": 60      # 초실시간 감시 (60초)
}

# ✅ 기타 경로
IPO_CSV_PATH = "Data/data:ipo_master_list.csv"
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
    "005930", "000660", "035420", "207940", "051910", "068270", "028260", "005935", "012330", "055550",
    "006400", "035720", "105560", "032830", "003550", "096770", "034730", "066570", "017670", "015760",
    "018260", "003670", "047050", "030200", "032640", "024110", "000270", "033780", "010950", "009150",
    "086790", "023530", "036570", "034020", "011170", "138040", "012450", "009540", "042660", "035250",
    "034220", "000100", "000810", "000880", "090430", "021240", "010130", "010140", "002790", "001040"
]

KOSDAQ_TOP_50 = [
    "035760", "041510", "091990", "263750", "196300", "066970", "005290", "086900", "032500", "078600",
    "241820", "054050", "222080", "142760", "067160", "026890", "230240", "039030", "131970", "035600",
    "033640", "092190", "052260", "058470", "214150", "083310", "036930", "058630", "046890", "039130",
    "115480", "090460", "052400", "104460", "079370", "109080", "121600", "044180", "196170", "100090",
    "195940", "237690", "048260", "090710", "145020", "078340", "050890", "060150", "036810", "080530"
]

CRYPTO_TOP_10 = [
    "BTC", "ETH", "XRP", "SOL", "BNB", "DOGE", "ADA", "AVAX", "DOT", "TRX"
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
    "Scott Bessent": "@SecScottBessent"
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

# ✅ 실시간 감지 키워드
REALTIME_KEYWORDS = [
    "전쟁", "계엄", "테러", "대재난", "금융위기", "시장 붕괴", 
    "긴급 발표", "긴급 회의", "원유 공급 중단", "전염병", "북한 핵", "북한 미사일", "아포칼립스", "이상기후", "비상사태", "금융 시스템 위기", "대지진"
]

# ✅ 주기 설정 (초 단위)
INTERVALS = {
    "7am_summary": 86400,        # 매일 오전 7시
    "realtime_check": 300,       # 5분 주기
    "critical_realtime": 60      # 초실시간 감시 (60초)
}
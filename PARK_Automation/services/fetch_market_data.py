# services/fetch_market_data.py

import requests
from config import (
    FRED_API_KEY
    ALPHA_VANTAGE_API_KEY,
    COINMARKETCAP_API_KEY,
    NEWS_API_KEY,
    TWITTER_BEARER_TOKEN,
    INVESTING_API_KEY,
    OKX_API_KEY, OKX_SECRET_KEY, OKX_PASSPHRASE,
    OPENWEATHER_API_KEY
)

### 1. USD/KRW 환율
def get_usdkrw_exchange_rate():
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=KRW&apikey={ALPHA_VANTAGE_API_KEY}"
    try:
        response = requests.get(url, timeout=5).json()
        rate = float(response['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        return rate
    except:
        return None

### 2. 미국/한국 10년물 금리 (FRED)
def get_bond_yields():
    try:
        us_10y = f"https://api.stlouisfed.org/fred/series/observations?series_id=GS10&api_key={FRED_API_KEY}&file_type=json"
        kr_10y = f"https://api.stlouisfed.org/fred/series/observations?series_id=IRLTLT01KRM156N&api_key={FRED_API_KEY}&file_type=json"
        us_yield = float(requests.get(us_10y).json()['observations'][-1]['value'])
        kr_yield = float(requests.get(kr_10y).json()['observations'][-1]['value'])
        return us_yield, kr_yield
    except:
        return None, None

### 3. 미국 기준금리 (FRED)
def get_us_base_rate():
    try:
        url = f"https://api.stlouisfed.org/fred/series/observations?series_id=DFEDTARU&api_key={FRED_API_KEY}&file_type=json"
        value = float(requests.get(url).json()['observations'][-1]['value'])
        return value
    except:
        return None

### 4. 한국 기준금리 (FRED)
def get_kr_base_rate():
    try:
        url = f"https://api.stlouisfed.org/fred/series/observations?series_id=IRTOTL01KRM156N&api_key={FRED_API_KEY}&file_type=json"
        value = float(requests.get(url).json()['observations'][-1]['value'])
        return value
    except:
        return None

### 5. 한국 콜금리 (FRED)
def get_kr_call_rate():
    try:
        url = f"https://api.stlouisfed.org/fred/series/observations?series_id=IR3TIB01KRM156N&api_key={FRED_API_KEY}&file_type=json"
        value = float(requests.get(url).json()['observations'][-1]['value'])
        return value
    except:
        return None

### 6. CME 금리 인상 확률 (데이터 수동 입력 or 향후 웹스크래핑)
def get_cme_fedwatch_summary():
    return "동결 87% / 인하 13%"  # 수동 입력 or 별도 구현 예정

### 7. 비트코인 시세 (OKX)
def get_btc_price():
    try:
        url = "https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT"
        data = requests.get(url).json()
        return float(data["data"][0]["last"])
    except:
        return None

### 8. KOSPI200 야간선물 등락률 (RapidAPI 필요 or 수동)
def get_kospi200_futures_change():
    return "+0.42%"  # 향후 연동 가능 (ex. Kiwoom API, Investing 등)

### 9. VIX 지수
def get_vix_index():
    url = "https://investing-cryptocurrency-markets.p.rapidapi.com/quotes/get-summary"
    headers = {
        "X-RapidAPI-Key": INVESTING_API_KEY,
        "X-RapidAPI-Host": "investing-cryptocurrency-markets.p.rapidapi.com"
    }
    params = {"pair_ID": "44336", "smlID": "1159963", "lang_ID": "1", "currency": "12"}
    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        return float(response.json()["data"]["last"])
    except:
        return None

### 10. 이상기후 (OpenWeather)
def get_weather(city="Seoul"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        res = requests.get(url).json()
        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]
        return f"{city}: {temp}℃, {desc}"
    except:
        return None

### 11. BTC ETF 순유입/순유출 (수동 요약 또는 프리미엄 데이터)
def get_btc_etf_flow():
    return "2,000억 순유입"  # 향후 크롤링 자동화 가능

### 12. CNN Fear & Greed Index (웹스크래핑 필요)
def get_cnn_fgi_index():
    return {"score": 82, "label": "Extreme Greed"}  # 크롤링 대체 가능

### 13. Korea Fear & Greed Index
def get_korea_fgi_index():
    return {"score": 65, "label": "Greed"}  # 향후 구현 가능
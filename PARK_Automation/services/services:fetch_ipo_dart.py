# services/fetch_ipo_dart.py

import requests
import pandas as pd
from datetime import datetime, timedelta
from config import DART_API_KEY

def fetch_dart_ipos(start_date=None, end_date=None):
    """
    ✅ 최근 2년 이내 신규상장 공시(A001)를 DART API를 통해 수집
    :param start_date: 조회 시작일 (YYYYMMDD)
    :param end_date: 조회 종료일 (YYYYMMDD)
    :return: 신규상장 공시 데이터프레임 (corp_name, corp_code, rcept_dt, report_nm)
    """

    # 기본 기간: 최근 2년
    if not start_date:
        start_date = (datetime.now() - timedelta(days=730)).strftime("%Y%m%d")
    if not end_date:
        end_date = datetime.now().strftime("%Y%m%d")

    url = "https://opendart.fss.or.kr/api/list.json"
    params = {
        "crtfc_key": DART_API_KEY,
        "bgn_de": start_date,
        "end_de": end_date,
        "pblntf_detail_ty": "A001",  # A001 = 신규상장 관련 공시
        "page_no": "1",
        "page_count": "100"
    }

    try:
        print(f"[DART] 신규상장 공시 요청 중: {start_date} ~ {end_date}")
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        # 응답 검증
        if data.get("status") != "000":
            print(f"[⚠️] DART 응답 오류: {data.get('message', 'Unknown error')}")
            return pd.DataFrame()

        items = data.get("list", [])
        if not items:
            print("[📭] 신규상장 공시 없음")
            return pd.DataFrame()

        df = pd.DataFrame(items)
        df["rcept_dt"] = pd.to_datetime(df["rcept_dt"])

        return df[["corp_name", "corp_code", "rcept_dt", "report_nm"]]

    except Exception as e:
        print(f"[❌] DART API 예외 발생: {e}")
        return pd.DataFrame()
# services/fetch_ipo_list.py

import os
import pandas as pd
from datetime import datetime
from config import IPO_CSV_PATH
from services.fetch_ipo_dart import fetch_dart_ipos

def fetch_recent_ipos():
    """
    ✅ 최근 2년 이내 신규상장 기업을 DART에서 조회 → CSV 저장 → 리스트 반환
    이 데이터는 alert_ipo_opportunity.py에서 조건 필터링에 사용됨.
    """

    print("[📡] DART 신규상장 공시 수집 중...")
    df = fetch_dart_ipos()

    if df is None or df.empty:
        print("[🚫] 신규상장 공시 없음 또는 API 오류")
        return []

    df.rename(columns={
        "corp_name": "NAME",
        "corp_code": "TICKER",
        "rcept_dt": "LISTED_DATE",
        "report_nm": "REPORT"
    }, inplace=True)

    # 기본 예시 재무 데이터 및 조건 컬럼 채워넣기 (향후 실데이터로 교체 가능)
    df["IPO_PRICE"] = 10000                         # 공모가
    df["CURRENT_PRICE"] = 9200                      # 현재가
    df["PER"] = 10.0                                # PER
    df["PBR"] = 1.2                                 # PBR
    df["DIV"] = 6.5                                 # 배당수익률 %
    df["DROP_PCT"] = -54.0                          # 고점 대비 낙폭 %
    df["VOLUME_SURGE"] = True                       # 거래량 급등 여부
    df["BREAKOUT"] = True                           # 최근 3~5일 고가 돌파 여부
    df["BULLISH_CANDLE"] = True                    # 시가 대비 양봉 마감 여부
    df["MARKET_CAP"] = 870                          # 시총 (억원 기준)
    df["FLOAT_RATIO"] = 28                          # 유통물량 비율 %
    df["NET_BUY"] = True                            # 외국인/기관 순매수 전환 여부

    # ✅ CSV 저장
    os.makedirs(os.path.dirname(IPO_CSV_PATH), exist_ok=True)
    df.to_csv(IPO_CSV_PATH, index=False, encoding="utf-8-sig")
    print(f"[✅] 신규상장 종목 CSV 저장 완료 → {IPO_CSV_PATH}")

    # ✅ 리스트(dict) 반환
    return df.to_dict("records")

# services/fetch_ipo_list.py

import pandas as pd
from datetime import datetime, timedelta

def fetch_recent_ipos(file_path="data/data:ipo_master_list.csv", days=30):
    """
    최근 상장된 기업을 불러오는 함수
    - file_path: CSV 파일 경로
    - days: 최근 몇 일 내 상장 기업을 가져올지 (기본 30일)
    """
    try:
        df = pd.read_csv(file_path)
        df["상장일"] = pd.to_datetime(df["상장일"], errors="coerce")
        cutoff = datetime.today() - timedelta(days=days)
        recent = df[df["상장일"] >= cutoff].copy()
        return recent.sort_values(by="상장일", ascending=False)
    except Exception as e:
        print(f"[❗IPO 로딩 오류]: {e}")
        return pd.DataFrame()

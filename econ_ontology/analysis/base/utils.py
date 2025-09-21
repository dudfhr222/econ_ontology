# 공용 함수 (결측치 처리, 윈도우 계산 등)

import pandas as pd
from typing import List

def align_and_fill(frames: List[pd.DataFrame]) -> pd.DataFrame:
    """
    여러 시계열 DataFrame을 합치고, 결측치 보간
    """
    if not frames:
        return pd.DataFrame()
    df = pd.concat(frames, axis=1)
    df = df.sort_index()
    df = df.ffill().bfill()  # 앞/뒤로 결측치 채움
    return df

def normalize_series(s: pd.Series) -> pd.Series:
    """0~1 정규화"""
    return (s - s.min()) / (s.max() - s.min())

def drop_missing(ts: pd.DataFrame) -> pd.DataFrame:
    """결측치 제거"""
    return ts.dropna()

# 상관계수, 회귀 등 기초 통계

import pandas as pd
import numpy as np
from typing import Tuple

def cross_correlation_best_lag(ts: pd.DataFrame, col1: str, col2: str, max_lag: int = 7) -> Tuple[int, float]:
    """
    두 시계열 간 cross-correlation을 계산해서
    가장 높은 상관을 보이는 시차(lag)를 반환
    """
    if col1 not in ts.columns or col2 not in ts.columns:
        return 0, np.nan

    s1 = ts[col1].pct_change().dropna()
    s2 = ts[col2].pct_change().dropna()
    common_idx = s1.index.intersection(s2.index)
    s1, s2 = s1.loc[common_idx], s2.loc[common_idx]

    best_lag, best_corr = 0, -2  # -1~1 밖으로 초기화
    for lag in range(-max_lag, max_lag + 1):
        if lag < 0:
            shifted = s1.shift(-lag)
            corr = shifted.corr(s2)
        elif lag > 0:
            shifted = s2.shift(lag)
            corr = s1.corr(shifted)
        else:
            corr = s1.corr(s2)

        if corr is not None and corr > best_corr:
            best_corr = corr
            best_lag = lag

    return best_lag, best_corr

def correlation_matrix(ts: pd.DataFrame) -> pd.DataFrame:
    """시계열 상관계수 행렬"""
    return ts.corr(numeric_only=True)

def rolling_mean(ts: pd.Series, window: int = 20) -> pd.Series:
    """이동평균"""
    return ts.rolling(window).mean()

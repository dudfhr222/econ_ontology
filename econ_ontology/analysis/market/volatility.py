# 변동성 분석

import pandas as pd

def realized_volatility(ts: pd.Series, window: int = 30) -> float:
    """최근 window일 변동성 (표준편차 기반)"""
    return ts.pct_change().dropna().rolling(window).std().iloc[-1]

# 추세 분석 (이동평균, 모멘텀 등)

import pandas as pd

def momentum(ts: pd.Series, window: int = 14) -> float:
    """단기 모멘텀 (현재가 / n일 전)"""
    if len(ts) < window:
        return None
    return ts.iloc[-1] / ts.iloc[-window] - 1

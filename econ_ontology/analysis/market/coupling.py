# 코인/자산 커플링 분석

import pandas as pd

def compute_coupling(ts: pd.DataFrame, src: str, dst: str, window: int = 30) -> float | None:
    """두 자산 간 이동 상관계수 (커플링 정도)"""
    if src not in ts.columns or dst not in ts.columns:
        return None
    return ts[src].pct_change().rolling(window).corr(ts[dst].pct_change()).iloc[-1]

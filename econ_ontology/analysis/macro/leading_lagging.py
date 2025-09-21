# 선행/후행 지표 분석
import pandas as pd

def compute_lagged_corr(ts: pd.DataFrame, lead: str, lag: str, max_lag: int = 5):
    """선행/후행 관계 탐색: lead 변수가 lag 변수에 얼마나 앞서는지"""
    results = {}
    for i in range(1, max_lag+1):
        shifted = ts[lead].shift(i)
        corr = ts[[lag]].join(shifted.rename(f"{lead}_lag{i}")).corr().iloc[0,1]
        results[f"lag_{i}"] = corr
    return results

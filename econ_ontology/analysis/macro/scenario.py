# 금리 시나리오 (Hike/Hold/Cut)
import pandas as pd

def rate_scenario_summary(ts: pd.DataFrame) -> pd.DataFrame:
    """금리 변동 시나리오별 평균 S&P500 반응"""
    if "Fed_Funds_Rate" not in ts or "SP500_Index" not in ts:
        return pd.DataFrame()
    rate_change = ts["Fed_Funds_Rate"].diff()
    sp_ret = ts["SP500_Index"].pct_change() * 100
    key = rate_change.apply(lambda x: "Hold" if x == 0 else ("Hike" if x > 0 else "Cut"))
    return pd.DataFrame({"SP500_%Change": sp_ret}).groupby(key).mean()

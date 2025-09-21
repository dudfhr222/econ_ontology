#  상관관계 분석

import pandas as pd

def pair_correlation(ts: pd.DataFrame, col1: str, col2: str) -> float | None:
    if col1 not in ts.columns or col2 not in ts.columns:
        return None
    return ts[[col1, col2]].corr().iloc[0, 1]

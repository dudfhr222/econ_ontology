# 이상치 탐지 (AI 기반 리스크)

import pandas as pd

def detect_anomalies(ts: pd.Series, z_thresh: float = 3.0):
    """간단한 Z-score 기반 이상치 탐지"""
    z = (ts - ts.mean()) / ts.std()
    return ts[z.abs() > z_thresh]

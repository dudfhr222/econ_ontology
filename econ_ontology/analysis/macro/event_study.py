# 이벤트 스터디 (FOMC, CPI 발표 등)
import pandas as pd

def event_study(ts: pd.DataFrame, events: pd.DataFrame, target: str, window: int = 3):
    """이벤트 전후 수익률 분석"""
    s = ts[target]
    pct = s.pct_change().fillna(0.0)
    out = []
    for _, row in events.iterrows():
        t = row["Date"]
        idx = ts.index.get_indexer([t], method="nearest")[0]
        rng = range(-window, window + 1)
        for k in rng:
            p = idx + k
            if 0 <= p < len(pct):
                out.append((row["Event"], k, pct.iloc[p]))
    df = pd.DataFrame(out, columns=["event", "k", "ret"])
    avg = df.groupby("k")["ret"].mean()
    return df, avg.to_frame("avg_ret"), avg.cumsum().to_frame("cum_%")

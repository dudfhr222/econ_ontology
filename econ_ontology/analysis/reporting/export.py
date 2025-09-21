# JSON/CSV 변환 등

import pandas as pd

def to_json(df: pd.DataFrame, path: str):
    df.to_json(path, orient="records", indent=2, force_ascii=False)

def to_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)

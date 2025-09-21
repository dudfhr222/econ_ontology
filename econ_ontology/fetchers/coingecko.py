import requests
import pandas as pd
from typing import List

import time, requests

BASE_URL = "https://api.coingecko.com/api/v3"

def fetch_many(coin_ids: List[str], vs_currency: str = "usd", days: int = 180) -> pd.DataFrame:
    """
    여러 코인 시계열 한 번에 가져오기 (rate limit 고려 → sleep 추가)
    """
    frames = []
    for cid in coin_ids:
        frames.append(fetch_coin_history(cid, vs_currency, days))
        time.sleep(1.5)  # ✅ CoinGecko rate limit 보호 (1.5초 대기)
    return pd.concat(frames, axis=1).sort_index()


def safe_request(url, params, retries=5, delay=5):
    for i in range(retries):
        r = requests.get(url, params=params, timeout=60)
        if r.status_code == 429:  # rate limit
            wait = delay * (i+1)
            print(f"Rate limit hit. Waiting {wait}s...")
            time.sleep(wait)
            continue
        r.raise_for_status()
        return r
    raise Exception("Failed after retries (429 too many requests)")


def fetch_coin_history(coin_id: str, vs_currency: str = "usd", days: int = 180) -> pd.DataFrame:
    url = f"{BASE_URL}/coins/{coin_id}/market_chart"
    params = {"vs_currency": vs_currency, "days": days}
    r = safe_request(url, params)
    data = r.json()
    prices = data.get("prices", [])
    if not prices:
        raise ValueError(f"No price data returned for {coin_id}")
    df = pd.DataFrame(prices, columns=["timestamp", coin_id.upper()])
    df["Date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("Date", inplace=True)
    df.drop(columns=["timestamp"], inplace=True)
    return df

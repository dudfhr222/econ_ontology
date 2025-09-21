import requests
import pandas as pd

BASE_URL = "https://api.coingecko.com/api/v3"

def fetch_coin_history(coin_id="bitcoin", vs_currency="usd", days=30):
    url = f"{BASE_URL}/coins/{coin_id}/market_chart"
    params = {"vs_currency": vs_currency, "days": days}
    res = requests.get(url, params=params)
    res.raise_for_status()
    data = res.json()
    prices = data["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["Date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("Date", inplace=True)
    df.drop(columns=["timestamp"], inplace=True)
    return df

import pandas as pd
import yfinance as yf
from typing import List

def fetch_yahoo_close(tickers: List[str], period: str = "6mo", interval: str = "1d") -> pd.DataFrame:
    """
    Yahoo Finance에서 종가 데이터 가져오기
    - tickers: ["^GSPC", "^IXIC"] 같은 리스트
    - period: "1mo", "6mo", "1y", "5y", "max"
    - interval: "1d", "1wk", "1mo"
    """
    data = yf.download(tickers=tickers, period=period, interval=interval, auto_adjust=True, threads=True, progress=False)

    if isinstance(data.columns, pd.MultiIndex):
        data = data["Close"]  # 여러 티커일 경우
    else:
        data = data.rename(columns={"Close": tickers[0]})
        data = data[[tickers[0]]]

    data.index.name = "Date"
    return data

from econ_ontology.core.entity import Entity

BITCOIN = Entity(
    id="BTC_USD",
    type="Asset",
    name="Bitcoin",
    desc="Bitcoin price in USD",
    category="Cryptocurrency",
    source="CoinGecko",
    unit="USD",
    frequency="Daily",
    timezone="UTC",
    status="active",
    currency="USD",
    market="Crypto",
    sector="Digital Asset",
    region="Global",
    ticker="BTC",
    asset_class="Crypto",
    exchange="Binance/Coinbase",
    risk_level="High",
    volatility=None,  # 분석 모듈에서 자동 채워질 수 있음
    provider="CoinGecko",
    definition="Bitcoin is a decentralized digital currency without a central bank or single administrator.",
    historical_range="2010-07-01 ~ Present",
    tags=["store-of-value", "crypto", "digital-gold"]
)

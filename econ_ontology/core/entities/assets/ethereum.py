from econ_ontology.core.entity import Entity

ETHEREUM = Entity(
    id="ETH_USD",
    type="Asset",
    name="Ethereum",
    desc="Ethereum price in USD",
    category="Cryptocurrency",
    source="CoinGecko",
    unit="USD",
    frequency="Daily",
    timezone="UTC",
    status="active",
    currency="USD",
    market="Crypto",
    sector="Smart Contracts",
    region="Global",
    ticker="ETH",
    asset_class="Crypto",
    exchange="Binance/Coinbase/Kraken",
    risk_level="High",
    volatility=None,  # 분석 모듈에서 계산
    provider="CoinGecko",
    definition="Ethereum is a decentralized blockchain platform with smart contract functionality.",
    historical_range="2015-08-07 ~ Present",
    tags=["smart-contract", "layer1", "crypto"]
)

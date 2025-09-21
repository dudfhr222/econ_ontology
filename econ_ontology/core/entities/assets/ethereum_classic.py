from econ_ontology.core.entity import Entity

ETHEREUM_CLASSIC = Entity(
    id="ETC_USD",
    type="Asset",
    name="Ethereum Classic",
    desc="Ethereum Classic price in USD",
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
    ticker="ETC",
    asset_class="Crypto",
    exchange="Binance/Coinbase/Kraken",
    risk_level="High",
    volatility=None,
    provider="CoinGecko",
    definition="Ethereum Classic is the original Ethereum blockchain that continued on the legacy chain after the DAO hard fork.",
    historical_range="2016-07-24 ~ Present",
    tags=["smart-contract", "layer1", "crypto"]
)

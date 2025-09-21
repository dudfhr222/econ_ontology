from econ_ontology.core.relationship import Relationship

REL_BTC_NASDAQ = Relationship(
    src="BTC_USD",
    dst="NASDAQ_Index",
    rel=["correlated_with", "influences"],
    weight=0.72,
    lag=1,
    evidence="2023~2025 CoinGecko/Bloomberg 시계열 분석",
    source="CoinGecko",
    confidence=0.9
)

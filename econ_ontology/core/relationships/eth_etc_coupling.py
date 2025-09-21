from econ_ontology.core.relationship import Relationship

REL_ETH_ETC_COUPLING = Relationship(
    src="ETH_USD",
    dst="ETC_USD",
    rel=["correlated_with", "originated_from"],
    weight=None,  # 실제 시계열 분석 후 자동 주입 (상관계수 등)
    lag=0,
    evidence="Ethereum Classic originated from Ethereum hard fork (DAO hack, 2016). Price movements remain historically coupled.",
    source="CoinGecko / Historical blockchain events",
    confidence=0.85
)

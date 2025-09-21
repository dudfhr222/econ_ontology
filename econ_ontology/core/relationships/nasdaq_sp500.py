from econ_ontology.core.relationship import Relationship

REL_NASDAQ_SP500 = Relationship(
    src="NASDAQ_Index",
    dst="SP500_Index",
    rel="correlated_with"
)

import pandas as pd
from econ_ontology.core.entities.indices import INDICES
from econ_ontology.core.entities.assets import ASSETS
# from econ_ontology.core.entities.macros import MACROS
from econ_ontology.core.relationships.btc_nasdaq import REL_BTC_NASDAQ
from econ_ontology.core.relationships.nasdaq_sp500 import REL_NASDAQ_SP500
from econ_ontology.core.ontology import EconOntology

# 전체 엔티티 그룹 모으기
ALL_ENTITIES = INDICES + ASSETS
# ALL_ENTITIES = INDICES + ASSETS + MACROS

def build_default_ontology(ts: pd.DataFrame) -> EconOntology:
    nodes = pd.DataFrame([
        {"id": e.id, "type": e.type, "desc": e.desc} 
        for e in ALL_ENTITIES
    ])
    # nodes = pd.DataFrame([
    #     {"id": SP500.id, "type": SP500.type, "desc": SP500.desc},
    #     {"id": NASDAQ.id, "type": NASDAQ.type, "desc": NASDAQ.desc},
    #     {"id": BITCOIN.id, "type": BITCOIN.type, "desc": BITCOIN.desc},
    # ])

    rels = pd.DataFrame([
        REL_BTC_NASDAQ.__dict__,
        REL_NASDAQ_SP500.__dict__
    ])
    # rels = pd.DataFrame([
    #     {"src": REL_BTC_NASDAQ.src, "dst": REL_BTC_NASDAQ.dst, "rel": REL_BTC_NASDAQ.rel},
    #     {"src": REL_NASDAQ_SP500.src, "dst": REL_NASDAQ_SP500.dst, "rel": REL_NASDAQ_SP500.rel},
    # ])

    return EconOntology(nodes, rels, ts)

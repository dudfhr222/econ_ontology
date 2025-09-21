import pandas as pd, json
from pathlib import Path
from econ_ontology.fetchers.coingecko import fetch_many
from econ_ontology.fetchers.yahoo import fetch_yahoo_close
from econ_ontology.core.ontology import EconOntology
from econ_ontology.core.relationships.nl_parser import parse_many
from econ_ontology.analysis.base.utils import align_and_fill
from econ_ontology.analysis.base.stats import cross_correlation_best_lag
from econ_ontology.analysis.ai.explain import generate_evidence   # ✅ 추가

DATA_DIR = Path("data")

def load_entities_config():
    with open(DATA_DIR / "entities_config.json","r",encoding="utf-8") as f:
        return json.load(f)

def fetch_timeseries(cfg, days=180):
    frames = []; nodes=[]
    # CoinGecko
    ids = [m["coin_id"] for _, m in cfg["assets"].items() if m["source"]=="coingecko"]
    if ids:
        df_cg = fetch_many(ids, days=days)
        rename_map = {m["coin_id"].upper(): eid for eid,m in cfg["assets"].items() if m["source"]=="coingecko"}
        df_cg.rename(columns=rename_map, inplace=True)
        frames.append(df_cg)
        nodes += [{"id": eid,"type": m["type"],"desc": m["name"]} for eid,m in cfg["assets"].items()]
    # Yahoo
    tickers = [m["ticker"] for _, m in cfg["indices"].items() if m["source"]=="yahoo"]
    if tickers:
        df_y = fetch_yahoo_close(tickers)
        df_y.rename(columns={m["ticker"]:eid for eid,m in cfg["indices"].items()}, inplace=True)
        frames.append(df_y)
        nodes += [{"id": eid,"type": m["type"],"desc": m["name"]} for eid,m in cfg["indices"].items()]
    ts = align_and_fill(frames)
    return ts, pd.DataFrame(nodes)

def build_relationships(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    return parse_many(lines)

def auto_fill_weights(ts, rels_df):
    filled = rels_df.copy()
    for i,row in filled.iterrows():
        lag,corr = cross_correlation_best_lag(ts,row["src"],row["dst"],7)
        filled.at[i,"lag"]=lag
        filled.at[i,"weight"]=None if corr is None else round(float(corr),3)
        # ✅ Ollama evidence 자동 생성
        filled.at[i,"evidence"]=generate_evidence(
            row["src"], row["dst"], row["rel"].split(","), filled.at[i,"weight"], lag
        )
    return filled

def run():
    cfg = load_entities_config()
    ts,nodes = fetch_timeseries(cfg)
    rels = build_relationships(DATA_DIR/"relationships_nl.txt")
    rels_df = pd.DataFrame([r.to_row() for r in rels])
    rels_df = auto_fill_weights(ts, rels_df)
    ont = EconOntology(nodes, rels_df, ts)
    
    print("Nodes:"); print(nodes)
    print("\nRelationships:"); print(rels_df)
    print("\nPath BTC->SP500:", ont.has_path("BTC_USD","SP500_Index"))

if __name__=="__main__":
    run()

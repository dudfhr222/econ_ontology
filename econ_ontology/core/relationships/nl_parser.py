import re
from typing import List
from econ_ontology.core.relationship import Relationship
from econ_ontology.analysis.ai.ollama_client import turn_nl_to_json

_SIMPLE = re.compile(r"^(?P<src>\S+)\s*->\s*(?P<dst>\S+)\s*:\s*(?P<rels>[\w_,\- ]+)(?:;\s*lag\s*=\s*(?P<lag>-?\d+))?(?:;\s*weight\s*=\s*(?P<weight>[-+]?\d*\.?\d+|auto))?", re.IGNORECASE)

def parse_line(line: str) -> dict:
    line = line.strip()
    if not line or line.startswith("#"):
        return {}
    m = _SIMPLE.match(line)
    if m:
        d = m.groupdict()
        rels = [r.strip() for r in d["rels"].split(",") if r.strip()]
        lag = int(d["lag"]) if d.get("lag") else 0
        w = d.get("weight")
        weight = None if (w is None or w == "auto") else float(w)
        return {"src": d["src"], "dst": d["dst"], "rel": rels, "lag": lag, "weight": weight, "notes": "regex"}
    # 정규식 안 맞으면 LLM에 위임
    return turn_nl_to_json(line)

def parse_many(lines: List[str]) -> list[Relationship]:
    rels: list[Relationship] = []
    for ln in lines:
        spec = parse_line(ln)
        if not spec: continue
        rel = Relationship(
            src=spec.get("src",""),
            dst=spec.get("dst",""),
            rel=spec.get("rel",["related_to"]),
            weight=spec.get("weight"),
            lag=int(spec.get("lag", 0)) if spec.get("lag") not in (None,"auto") else 0,
            evidence=spec.get("notes",""),
            source="NL"
        )
        rels.append(rel)
    return rels

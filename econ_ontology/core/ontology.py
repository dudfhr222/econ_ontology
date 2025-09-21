import pandas as pd
from collections import deque

class EconOntology:
    def __init__(self, nodes: pd.DataFrame, rels: pd.DataFrame, ts: pd.DataFrame):
        self.nodes = nodes.set_index("id")
        self.rels = rels
        self.ts = ts

    def neighbors(self, node_id: str, rel_type: str|None=None):
        df = self.rels[self.rels["src"] == node_id]
        if rel_type:
            df = df[df["rel"] == rel_type]
        return df["dst"].tolist()

    def has_path(self, src: str, dst: str, max_depth: int = 3):
        q = deque([(src, 0)])
        visited = {src}
        while q:
            cur, depth = q.popleft()
            if cur == dst:
                return True
            if depth >= max_depth:
                continue
            for n in self.rels[self.rels["src"] == cur]["dst"]:
                if n not in visited:
                    visited.add(n)
                    q.append((n, depth + 1))
        return False

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(nodes_path="data/econ_nodes.csv", rels_path="data/econ_relationships.csv"):
    nodes = pd.read_csv(nodes_path)
    rels = pd.read_csv(rels_path)
    G = nx.DiGraph()
    for _, row in nodes.iterrows():
        G.add_node(row["id"], type=row["type"], desc=row["desc"])
    for _, row in rels.iterrows():
        G.add_edge(row["src"], row["dst"], rel=row["rel"])
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8,6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v):d["rel"] for u,v,d in G.edges(data=True)})
    plt.title("Economic Ontology Graph")
    plt.tight_layout()
    plt.show()

import networkx as nx
import matplotlib.pyplot as plt
from random import sample, randint

DEFAULT = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "g"]


def create_graph(gr=None):
    g = nx.Graph()
    g.add_nodes_from(list(gr.keys()))
    for a in gr:
        for b in gr[a]:
            g.add_weighted_edges_from([(a, b, randint(0,10))])
    return g


def create_adj():
    return sample(DEFAULT, randint(0, len(DEFAULT)))


if __name__ == '__main__':
    graph = {}
    print("=== Start ===")
    for node in DEFAULT[:8]:
        graph[node] = create_adj()

    # Example of generated grapth
    # graph = {"a": ["c", "g"],
    #          "b": ["c", "e"],
    #          "c": ["a", "b", "d", "e"],
    #          "d": ["c"],
    #          "e": ["c", "b", "g"],
    #          "f": [],
    #          "g": ["a", "e"]
    #          }

    G = create_graph(graph)
    print("Nodes", G.nodes(), "\nEdges", G.edges.data())

    nx.draw(G, with_labels=True)
    plt.savefig("graph.png")
    plt.show()
    print("=== End ===")

import networkx as nx
import matplotlib.pyplot as plt
import random


def create_graph(gr=None):
    g = nx.Graph()
    g.add_nodes_from(list(gr.keys()))
    for a in gr:
        for b in gr[a]:
            g.add_weighted_edges_from([(a, b, random.random())])
    return g


if __name__ == '__main__':
    print("start")

    graph = {"a": ["c", "g"],
             "b": ["c", "e"],
             "c": ["a", "b", "d", "e"],
             "d": ["c"],
             "e": ["c", "b", "g"],
             "f": [],
             "g": ["a", "e"]
             }

    G = create_graph(graph)
    print("Nodes", G.nodes(), "Edges", G.edges.data())

    nx.draw(G, with_labels=True)
    plt.savefig("graph.png")
    plt.show()
    print("end")

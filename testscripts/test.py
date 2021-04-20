import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.spatial import KDTree


def main():
    g = nx.Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(4, 7)
    g.add_edge(5, 7)
    g.add_edge(6, 7)

    print(list(nx.node_disjoint_paths(g, 0, 7)))
    print(list(nx.edge_disjoint_paths(g, 0, 7)))

    g2 = g.to_directed()
    print(list(nx.node_disjoint_paths(g2, 0, 7)))
    vertex_disjoint_paths = list(nx.node_disjoint_paths(g2, 0, 7))
    for path in vertex_disjoint_paths:
        i = 0
        while i < len(path) - 1:
            g2.remove_edge(path[i], path[i + 1])
            i = i+1

    # print(list(nx.node_disjoint_paths(g2, 0, 7)))
    nx.draw_networkx(g2, edge_color='black')
    plt.draw()
    plt.show()

if __name__ == '__main__':
    main()

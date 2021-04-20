import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.spatial import KDTree


def covert(data):
    print("test")


def main():
    k = 4
    s = (5, 21.5)
    t = (6, -1.5)
    points = [
        (3, 0.0), (3, 5.0), (3, 10.0), (3, 15.0), (3, 20.0), (5.5, 0.0), (5.5, 5.0), (5.5, 10.0), (5.5, 15.0),
        (5.5, 20.0), (8.0, 0.0), (8.0, 5.0), (8.0, 10.0), (8.0, 15.0), (8.0, 20.0), (10.5, 2.0), (10.5, 5.0),
        (10.5, 7.0), (10.5, 10.0), (10.5, 12.0), (10.5, 15.0), (10.5, 17.0), (10.5, 18.0)]

    pointArr = np.array(points)
    print(len(pointArr))
    tree = KDTree(pointArr)
    tree.query((3, 0.0))
    print(tree.query_ball_point([5, 21.5], 4))
    print(tree.query_ball_point([3, 0.0], 6))
    G = nx.Graph()
    G.add_nodes_from(np.arange(len(pointArr)))
    index = 0
    for a in pointArr:
        neighbors = tree.query_ball_point(a, r=k)
        print(neighbors)
        for n in neighbors:
            G.add_edge(index, n)
        index = index + 1
    # nx.draw_networkx_edges(G, pos=nx.spring_layout(G))
    nx.draw_networkx(G, edge_color='black')
    plt.draw()
    plt.show()

    Gprime = nx.DiGraph()
    Gprime.add_nodes_from(np.arange(len(pointArr) + 2))

    index = 0
    for a in pointArr:
        neighbors = tree.query_ball_point(a, r=k)
        print(str(index) + ":" + str(neighbors))
        for n in neighbors:
            Gprime.add_edge(index, n)
        index = index + 1

    sn = len(pointArr) + 1
    tn = len(pointArr) + 2
    neighbors = tree.query_ball_point(s, r=k)
    print(neighbors)
    for n in neighbors:
        Gprime.add_edge(sn - 1, n)

    neighbors = tree.query_ball_point(t, r=k)
    print(neighbors)
    for n in neighbors:
        Gprime.add_edge(tn - 1, n)

    nx.draw_networkx(Gprime, edge_color='black')
    plt.draw()
    plt.show()


if __name__ == '__main__':
    main()

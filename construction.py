import networkx as nx
import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

def covert(data):
    print("test")


def main():
    points = [
        (3, 0.0), (3, 5.0), (3, 10.0), (3, 15.0), (3, 20.0), (5.5, 0.0), (5.5, 5.0), (5.5, 10.0), (5.5, 15.0),
        (5.5, 20.0), (8.0, 0.0), (8.0, 5.0), (8.0, 10.0), (8.0, 15.0), (8.0, 20.0), (10.5, 2.0), (10.5, 5.0),
        (10.5, 7.0), (10.5, 10.0), (10.5, 12.0), (10.5, 15.0), (10.5, 17.0), (10.5, 18.0)]

    pointArr = np.array(points)
    print(len(pointArr))
    tree = KDTree(pointArr)
    tree.query((3,0.0))
    print(tree.query_ball_point([3,0.0], 6))
    G = nx.Graph()
    G.add_nodes_from(np.arange(len(pointArr)))
    index = 0
    for a in pointArr:
        neighbors = tree.query_ball_point(a, r=4)
        print(neighbors)
        for n in neighbors:
            G.add_edge(index, n)
        index = index + 1
    # nx.draw_networkx_edges(G, pos=nx.spring_layout(G))
    nx.draw_networkx(G, edge_color='black')
    plt.draw()
    plt.show()

if __name__ == '__main__':
    main()

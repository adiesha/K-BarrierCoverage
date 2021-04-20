import networkx as nx
import numpy as np
from scipy.spatial import KDTree


class ResidualGraph:
    def __init__(self, data, s, t, k):
        self.data = data
        self.s = s
        self.t = t
        self.k = k
        self.G = nx.Graph()
        self.Gp = nx.DiGraph()
        self.residualG = nx.DiGraph()
        self.tree = None
        self.initialize()

    def initialize(self):
        self.tree = KDTree(self.data)

        # G prime construction
        self.Gp.add_nodes_from(np.arange(2 * len(self.data) + 2))

        index = 0
        for a in self.data:
            # connect vin and vout
            self.Gp.add_edge(index, len(self.data) + index)

            neighbors = self.tree.query_ball_point(a, r=self.k)
            # print(str(index) + ":" + str(neighbors))
            for n in neighbors:
                self.Gp.add_edge(len(self.data) + index, n)
            index = index + 1

        sn = 2 * len(self.data) + 2 - 1 - 1
        tn = 2 * len(self.data) + 2 - 1
        neighbors = self.tree.query_ball_point(self.s, r=self.k)
        # print(neighbors)
        for n in neighbors:
            self.Gp.add_edge(sn, n)

        neighbors = self.tree.query_ball_point(self.t, r=self.k)
        # print(neighbors)
        for n in neighbors:
            self.Gp.add_edge(len(self.data) + n, tn)

        # nx.draw_networkx(self.Gp, edge_color='black')
        # plt.draw()
        # plt.show()

        self.residualG = self.Gp.copy()
        # print(list(nx.node_disjoint_paths(self.Gp, sn, tn)))
        # print(len(list(nx.node_disjoint_paths(self.Gp, sn, tn))))

        vertex_disjoint_paths = list(nx.node_disjoint_paths(self.Gp, sn, tn))
        for path in vertex_disjoint_paths:
            i = 0
            while i < len(path) - 1:
                self.Gp.remove_edge(path[i], path[i + 1])
                i = i + 1

    def getResidualGraph(self):
        return self.residualG

    def getgprime(self):
        return self.Gp

def main():
    k = 4
    s = (5, 21.5)
    t = (6, -1.5)
    points = [
        (3, 0.0), (3, 5.0), (3, 10.0), (3, 15.0), (3, 20.0), (5.5, 0.0), (5.5, 5.0), (5.5, 10.0), (5.5, 15.0),
        (5.5, 20.0), (8.0, 0.0), (8.0, 5.0), (8.0, 10.0), (8.0, 15.0), (8.0, 20.0), (10.5, 2.0), (10.5, 5.0),
        (10.5, 7.0), (10.5, 10.0), (10.5, 12.0), (10.5, 15.0), (10.5, 17.0), (10.5, 18.0)]
    r1 = ResidualGraph(points, s, t, k)


if __name__ == '__main__':
    main()

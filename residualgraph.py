import networkx as nx
import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt


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

        un = 2 * len(self.data) + 2 - 1 - 1
        vn = 2 * len(self.data) + 2 - 1

        # neighbors = self.tree.query_ball_point(self.s, r=self.k)
        index = 0
        for p in self.data:
            if p[0] - self.s <= self.k / 2:
                print(p)
                self.Gp.add_edge(un, index)

            if self.t - p[0] <= self.k / 2:
                print(p)
                self.Gp.add_edge(len(self.data) + index, vn)
            index = index + 1

        self.residualG = self.Gp.copy()
        # print(list(nx.node_disjoint_paths(self.Gp, un, vn)))
        # print(len(list(nx.node_disjoint_paths(self.Gp, un, vn))))

        vertex_disjoint_paths = list(nx.node_disjoint_paths(self.Gp, un, vn))
        print("Vertex Disjoint Paths: " + str(len(vertex_disjoint_paths)))
        for path in vertex_disjoint_paths:
            i = 0
            while i < len(path) - 1:
                self.residualG.remove_edge(path[i], path[i + 1])
                self.residualG.add_edge(path[i + 1], path[i])
                i = i + 1

    def getResidualGraph(self):
        return self.residualG

    def getgprime(self):
        return self.Gp

    def getUindex(self):
        return 2 * len(self.data) + 2 - 1 - 1

    def getVindex(self):
        return 2 * len(self.data) + 2 - 1

    def getOutVertexIndex(self, index):
        return len(self.data) + index

# def main():
#     k = 4
#     s = 1
#     t = 12
#     points = [
#         (3, 0.0), (3, 5.0), (3, 10.0), (3, 15.0), (3, 20.0), (5.5, 0.0), (5.5, 5.0), (5.5, 10.0), (5.5, 15.0),
#         (5.5, 20.0), (8.0, 0.0), (8.0, 5.0), (8.0, 10.0), (8.0, 15.0), (8.0, 20.0), (10.5, 2.0), (10.5, 5.0),
#         (10.5, 7.0), (10.5, 10.0), (10.5, 12.0), (10.5, 15.0), (10.5, 17.0), (10.5, 18.0)]
#     r1 = ResidualGraph(points, s, t, k)
#     # print(r1.getUindex())
#     # print(r1.getVindex())
#     # print(r1.getOutVertexIndex(5))
#     # nx.draw_networkx(r1.getResidualGraph(), edge_color='black')
#     # plt.draw()
#     # plt.show()
#     # print(list(nx.node_disjoint_paths(r1.getResidualGraph(), r1.getUindex(), r1.getVindex())))
#     # print(r1.getResidualGraph().out_edges(46))
#     # print(r1.getResidualGraph().in_edges(47))

#     # print("------------------")
#     # for i in range(23):
#     #     print(r1.getResidualGraph().in_edges(i))

#     # print("++++++++++")
#     # print(r1.getResidualGraph().in_edges(0))
#
#     print(len(minimum_st_node_cut(r1.getResidualGraph(), 46, 47)))
#     print(minimum_st_node_cut(r1.getResidualGraph(), 46, 47))
#
#     print(len(minimum_st_node_cut(r1.getgprime(), 46, 47)))
#     print(minimum_st_node_cut(r1.getgprime(), 46, 47))


# if __name__ == '__main__':
#     main()

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph


class visualize:
    def __init__(self):
        pass

    def visualizeCircles(self, circles, belts, unitDistance):
        fig, ax = plt.subplots()
        # draw circles
        for circle in circles:
            print(circle)
            ax.add_patch(plt.Circle((circle[0], circle[1]), unitDistance, color='b', fill=False))
        # draw belts
        ax.add_patch(plt.Rectangle(belts[0][0], belts[0][1], belts[0][2], color='r'))
        ax.add_patch(plt.Rectangle(belts[1][0], belts[1][1], belts[1][2], color='r'))
        ax.margins(0.5, 0.5)
        plt.show()

    def visualizeGraph(self, residualGraph, vertex_disjoint_paths, start, end):
        A = to_agraph(residualGraph)
        A.node_attr['style']='filled'

        # iterate over vertex disjoint paths
        for path in vertex_disjoint_paths:
                i = 0
                while i < len(path) - 1:
                    n = A.get_node(path[i])
                    n.attr['fillcolor']="#6445d6"
                    n = A.get_edge(path[i], path[i + 1])
                    n.attr['fillcolor']="#6445d6"
                    i = i + 1
                # fill starting and ending node
        n = A.get_node(start)
        n.attr['fillcolor']="#d64945"
        n = A.get_node(end)
        n.attr['fillcolor']="#d64945"
        A.layout('dot')
        A.draw('graph.png')
        img = mpimg.imread('graph.png')
        imgplot = plt.imshow(img)
        plt.show()

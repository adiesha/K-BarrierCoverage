import matplotlib.pyplot as plt
import networkx as nx

# import networkx as nx
# import pylab as plt
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph
import pygraphviz as pgv
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

	def visualizeGraph(self, residualGraph):
		A = to_agraph(residualGraph)
		A.layout('dot')
		A.draw('graph.png')
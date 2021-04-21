import matplotlib.pyplot as plt
import networkx as nx
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
		nx.draw_networkx(residualGraph, edge_color='black')
		plt.draw()
		plt.show()

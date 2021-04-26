from DS import DS
from generateDisks import generateDisks
from visualize import visualize
from residualgraph import ResidualGraph
import networkx as nx
def run1():
    gd = generateDisks()
    vis = visualize()
    unitDistance = 2
    s = 1
    t = 12
    belts = (s, t)
    k = 2
    # generate optimal k-coverage disk set
    disks = gd.generateUnitDisks(k, belts, unitDistance)
    # generate belt rectangles
    beltRectangles = gd.getBeltRegions(k, belts, unitDistance)

    # visualize circles
    vis.visualizeCircles(disks, beltRectangles, unitDistance)

    # create residual graph
    r1 = ResidualGraph(disks, s, t, unitDistance * 2)
    # starting vertex
    start = r1.getUindex()
    # ending vertex
    end = r1.getVindex()
    print(r1.getUindexofG, r1.getVindexOfG)
    print(list(nx.node_disjoint_paths(r1.G, r1.getUindexofG, r1.getVindexOfG)))
    # visualize G graph
    vis.visualizeGraph(r1.G, list(nx.node_disjoint_paths(r1.G, r1.getUindexofG, r1.getVindexOfG)), r1.getUindexofG, r1.getVindexOfG)

    # visualize G' graph
    vis.visualizeGraph(r1.Gp, r1.disjoint_paths, start, end)

    # retrieve residual graph
    r_Graph = r1.getResidualGraph()

    # visualize residual graph
    vis.visualizeGraph(r_Graph, [], start, end)

    

run1()
# generate d random unit disks
# d = 20
# disks = gd.generateRandomUnitDisks(d, belts, unitDistance)






# vis.visualizeGraph(r1.G)
# print(list(r1.G.successors(8)))

# ds = DS(r1.G, [r1.getUindexofG(), 9])
# print(ds.IN)
# print(ds.OUT)

# print(ds.query(4))
# print(ds.query(4))

# print(ds.IN)
# print(ds.OUT)

# ds.remove(3)

# print(ds.IN)
# print(ds.OUT)

# print(ds.query(1))

# print(r1.disjoint_paths)
# p, v = r1.preprocessEdgedisjointpaths(r1.disjoint_paths, r1.getUindex(), r1.getVindex())
# print(p)
# print(v)

from DS import DS
from generateDisks import generateDisks
from visualize import visualize
from residualgraph import ResidualGraph

gd = generateDisks()
vis = visualize()
unitDistance = 2
s = 1
t = 12
belts = (s, t)
k = 2
# generate optimal k-coverage disk set
disks = gd.generateUnitDisks(k, belts, unitDistance)

# generate d random unit disks
# d = 20
# disks = gd.generateRandomUnitDisks(d, belts, unitDistance)

# generate belt rectangles
beltRectangles = gd.getBeltRegions(k, belts, unitDistance)

# visualize circles
vis.visualizeCircles(disks, beltRectangles, unitDistance)

# create residual graph
r1 = ResidualGraph(disks, s, t, unitDistance * 2)

# retrieve residual graph
r_Graph = r1.getResidualGraph()

# visualize residual graph
# vis.visualizeGraph(r_Graph)

# vis.visualizeGraph(r1.G)
print(list(r1.G.successors(8)))

ds = DS(r1.G, r1.getUindexofG())
print(ds.IN)
print(ds.OUT)

print(ds.query(4))
print(ds.query(4))

print(ds.IN)
print(ds.OUT)

ds.remove(3)

print(ds.IN)
print(ds.OUT)

print(ds.query(1))
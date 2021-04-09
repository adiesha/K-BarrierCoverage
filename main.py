from generateDisks import generateDisks
from visualize import visualize
gd = generateDisks()
vis = visualize()
unitDistance = 2
belts = (1,12)
k = 5
disks = gd.generateUnitDisks(k, belts, unitDistance)
beltRectangles = gd.getBeltRegions(k, belts, unitDistance)
vis.visualizeCircles(disks, beltRectangles, unitDistance)

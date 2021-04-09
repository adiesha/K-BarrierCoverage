class generateDisks:
	def __init__(self):
		self.disks = None
		self.belt = None
		self.k = None
	
	# generate a set of k-barrier covered intersecting disks
	# k - specify the k coverage of the set of disks
	# belt - tuple representing the placement x-coordinate of the two parallel belts
	# unitDistance = unit distance of disks
	def generateUnitDisks(self, k, belt, unitDistance):
		self.k = k
		self.belt = belt
		disks = [] 
		x = belt[0]  + unitDistance
		while x <= belt[1]:
			for y in range(k):
				if belt[1] - x < unitDistance * 1.25 and k > 1:	
					if y == 0:
						disks.append((x, y * unitDistance * 2.5 + unitDistance))
					elif y == k-1:
						disks.append((x, y * unitDistance * 2.5 - unitDistance))
					else:
						disks.append((x, y * unitDistance * 2.5))
						# add extra code to add one more
						if y < k-1:
							disks.append((x, y * unitDistance * 2.5 + unitDistance))
				else:
					disks.append((x, y * unitDistance * 2.5))
			x += unitDistance * 1.25
		self.disks = disks
		return disks

	# generate a belt regions
	# k - specify the k coverage of the set of disks
	# belt - tuple representing the placement x-coordinate of the two parallel belts
	# unitDistance = unit distance of disks	
	def getBeltRegions(self, k, belt, unitDistance):
		leftBelt = ((belt[0], -unitDistance * 2), -1 * unitDistance/2, k * unitDistance * 3)
		rightBelt = ((belt[1], -unitDistance * 2), 1 * unitDistance/2, k * unitDistance * 3)
		return (leftBelt, rightBelt)
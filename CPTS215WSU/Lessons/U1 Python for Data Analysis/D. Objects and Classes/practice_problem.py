class Point:
	"""
	CLass about Point in 2D.
	"""
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		return "%d %d" %(self.x,self.y)

	def __eq__(self,other_point):
		if (other_point.x == self.x) and (other_point.y == self.y):
			return True
		else:
			return False

def main():
	"""
	Main program
	"""
	a = Point(4,5)
	print(a)
	b = Point(5,6)
	c = Point(4,5)
	print(a == c)
	print(a == b)

main()
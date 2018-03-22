#this program writes class Point, circle and cylinder using composition instead of inheritance. 
import math

class Point:
	"""Class that represents a geometric point"""

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(%d, %d)" % (self.x, self.y)



class Circle:
	"""class representing a circle"""

	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.Radius = float(radius)
		self.P1 = Point(x,y)


	def __str__(self):
		return "center = %s , radius = %.2f" % (self.P1.__str__(), self.Radius)


	def area(self):
		return math.pi * self.Radius ** 2




class Cylinder:
	"""class representing a cylinder"""

	def __init__(self, x, y, radius, height):
		self.x = x
		self.y = y
		self.Radius = float(radius)
		self.Height = float(height)
		self.P1 = Point(x,y)
		self.C1 = Circle(x,y, radius)


	def __str__(self):
		return "Center: %s; Raduis = %.2f: Height = %.2f" % (self.P1.__str__(), self.Radius, self.Height)

	def volume(self):
		return self.C1.area() * self.Height

	def area(self):
		"""calculating surface area of cylinder"""
		return  2 * self.C1.area() * self.Height + 2 * math.pi * self.Radius * self.Height




#main program
def main():
	cylinder = Cylinder(12,23,2.5,5.7)
	circle = Circle(12,23,2.5)

	# print Cylinder attributes and methods
	print "\nPrinting cylinder cordinates"
	print cylinder
	print "The area of cylinder is: %.2f" % cylinder.area()
	print "The volume of cylinder is: %.2f" % cylinder.volume()
	

	print "\n\n printing circle cordinates"
	print circle
	print "The area of circle is :", circle.area()
	
	



if __name__ == "__main__":
	main()





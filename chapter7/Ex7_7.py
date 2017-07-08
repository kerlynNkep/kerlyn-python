
class Rectangle: 

	def __init__(self, x=1.0, y=1.0):

		self.setParameter(x, y)

	def setParameter(self, x , y):
		if x>y:
			self.setLength(x)
			self.setWidth(y)
		else:
			self.setWidth(x)
			self.setLength(y)

	def setLength(self,x):
		if 0.0<x<20.0:
			self.__length = x
		else:
			raise ValueError, "Invalid width value: %.1f" % x


	def setWidth(self,y):
		if 0.0<y<20.0:
			self.__width = y
		else:
			raise ValueError, "Invalid width value: %.1f" % y

	def getLength(self):
		return self.__length

	def getWidth(self):
		return self.__width

	def Perimeter(self):
		return 2*(self.__length + self.__width)
		
	def area(self):
		return (self.__length * self.__width)

	def isSquare(self):
		if self.__length==self.__width:
			return "Your length and width are equal hence : you have a square"


x = int(raw_input("Input your x cordinate: "))
y = int(raw_input("Input your y cordinate: "))

rectangle1 = Rectangle(x,y)

print "your length is, ", rectangle1._Rectangle__length

print "your width is, ", rectangle1._Rectangle__width

print "The perimeter of your rectangle is:",
print Rectangle.Perimeter(rectangle1)

print "The area of your rectangle is: ",
print Rectangle.area(rectangle1)

print Rectangle.isSquare(rectangle1)


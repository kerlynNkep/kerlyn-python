
class Rectangle:


	def __init__(self, length=1.0, width=1.0):
		self.__length = length
		self.__width = width

	def setWidth(self,width):
		if 0.0 < width < 20.0:
			self.__width = width
		else:
			raise ValueError, "Invalid width value: %.1f" % width

	def setLength(self,length):
		if 0.0<length<20.0:
			self.__length = length
		else:
			raise ValueError, "Invalid width value: %.1f" % length

	def getWidth(self):
		return self.__width

	def getLength(self):
		return self.__length

	def Perimeter(self):
		return 2*(self.__length + self.__width)
		
	def area(self):
		return (self.__length * self.__width)




length = int(raw_input("Input your length: "))
width = int(raw_input("Input width: "))

rectangle1 = Rectangle(length,width)

print "The perimeter of your rectangle is:",
print Rectangle.Perimeter(rectangle1)

print "The area of your rectangle is: ",
print Rectangle.area(rectangle1)













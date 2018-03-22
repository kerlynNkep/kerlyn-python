#this program designs class Quadrilatral(base class) with other fourside figures as derived classes
#Quadrilateral is an absrtact class

import math


class Quadrilateral:
	"""Base class quadrilateral"""

	def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
		self.X1 = x1
		self.Y1 = y1
		self.X2 = x2
		self.Y2 = y2
		self.X3 = x3
		self.Y3 = y3
		self.X4 = x4
		self.Y4 = y4


	def __str__(self):
		return "point A:(%d,%d); point B:(%d,%d); point C:(%d,%d); point D:(%d,%d);" \
		 		% (self.X1,self.Y1,self.X2,self.Y2,self.X3,self.Y3,self.X4,self.Y4)	


	def getDistance(self, X1,Y1, X2, Y2):
		return math.sqrt((self.X2-self.X1)**2 + (self.Y2-self.Y1)**2)



class Parallelogram(Quadrilateral):
	"""Class representing parallelogram"""

	def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
		Quadrilateral.__init__(self,x1,y1,x2,y2,x3,y3,x4,y4)


	def __str__(self):
		return Quadrilateral.__str__(self)


	def getPerimeter(self):
		A = Quadrilateral.getDistance(self, self.X1,self.Y1, self.X2, self.Y2)
		B = Quadrilateral.getDistance(self, self.X2,self.Y2, self.X3, self.Y3)
		C = Quadrilateral.getDistance(self, self.X3,self.Y3, self.X4, self.Y4)
		D = Quadrilateral.getDistance(self, self.X4,self.Y4, self.X1, self.Y1)
		return (A+B+C+D)



class Rectangle(Quadrilateral):
    
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        Quadrilateral.__init__(self,x1,y1,x2,y2,x3,y3,x4,y4)


    def getArea(self):
        return (self.getDistance(self.X1,self.Y1,self.X2,self.Y2) * \
        		self.getDistance(self.X2,self.Y2,self.X3,self.Y3 ))    
   

    def getPerimeter(self):
        return 2 *(self.getDistance(self.X1,self.Y1,self.X2,self.Y2) + \
        			self.getDistance(self.X2,self.Y2,self.X3,self.Y3 )) 


    def __str__(self):
        return "for a Rectangle: %s" % Quadrilateral.__str__(self)




class Square(Quadrilateral):

    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        Quadrilateral.__init__(self,x1,y1,x2,y2,x3,y3,x4,y4)


    def getPerimeter(self):
        return (self.getDistance(self.X1, self.Y1, self.X2, self.Y2))* 4

    def getArea(self):
        return (self.getDistance(self.X1,self.Y1,self.X2,self.Y2)) ** 2

    def __str__(self):
		return "for a Square: %s" % Quadrilateral.__str__(self)



class Trapezoid(Quadrilateral):

	def __init__(self, x1,y1,x2,y2,x3,y3,x4,y4,height):
		Quadrilateral.__init__(self,x1,y1,x2,y2,x3,y3,x4,y4)
		self.Height = height
	

	def getPerimeter(self):
		A = Quadrilateral.getDistance(self, self.X1, self.Y1, self.X2, self.Y2)
		B = Quadrilateral.getDistance(self, self.X2, self.Y2, self.X3, self.Y3)
		C = Quadrilateral.getDistance(self, self.X3, self.Y3, self.X4, self.Y4)
		D = Quadrilateral.getDistance(self, self.X4, self.Y4, self.X1, self.Y1)
		return (A+B+C+D)


	def getArea(self):
		A = Quadrilateral.getDistance(self, self.X1,self.Y1, self.X2, self.Y2)
		B = Quadrilateral.getDistance(self, self.X2,self.Y2, self.X3, self.Y3)
		C = Quadrilateral.getDistance(self, self.X3,self.Y3, self.X4, self.Y4)
		D = Quadrilateral.getDistance(self, self.X4,self.Y4, self.X1, self.Y1)
		return ((A+C)/2) * self.Height


	def __str__(self):
		return "for a Trapezuim: %s with height: %d" % (Quadrilateral.__str__(self), self.Height)






def main():

	trapezuim = Trapezoid(2,2,3,3,4,4,5,5,6)
	parallelogram = Parallelogram(2,2,3,3,4,4,5,5)
	square = Square(2,2,3,3,3,3,2,2)
	rectangle = Rectangle(2,2,3,3,4,4,5,5)

	print "\n"
	print trapezuim
	print "Area of trapezuim is:", trapezuim.getArea()
	print "perimeter of trapezuim is:", trapezuim.getPerimeter()

	print "\n"
	print parallelogram
	print "perimeter of parallelogram is:", parallelogram.getPerimeter()

	print "\n"
	print square
	print "Area of Square is:", square.getArea()
	print "perimeter of Square is:", square.getPerimeter()

	print "\n"
	print rectangle
	print "Area of rectangle is:", rectangle.getArea()
	print "perimeter of rectangle is:", rectangle.getPerimeter()



if __name__ == "__main__":
	main()

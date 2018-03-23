

class Square:
	
	def __init__(self, x, y):
		try:
			self.X = x
			self.Y = y

			assert self.X == self.Y

		except AssertionError:
			print "x and y value have to be same for a square"

	
	def __str__(self):
		return "square coordinates are: (%d,%d)" % (self.X, self.Y)

	def getArea(self):
		return "area of square is", self.X * self.Y



def main():
	square1 = Square(2,2)
	print square1
	print square1.getArea()
	print "\n"
	square2 = Square(4,5)
	print square2
	print square2.getArea()


if __name__ == "__main__":
	main()
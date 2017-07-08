
class RationalNumber:
	""" performs arithmetic with fractions"""

	def __init__(self, num = 0, den = 1):
		self.num = num
		self.den = den

	def printNumber(self):
		print "%d/%d" % (self.num, self.den)

	def printFloatFormat(self):
		print "%.1f/%.1f" % (self.num, self.den)

	def addNumber(self, other):
		addNum = (self.num * other.den + other.num* self.den)
		addDen = self.den * other.den 
		print "%d/%d" % (addNum,addDen)


	def subNumber(self, other):
		subNum = (self.num * other.den - other.num* self.den)
		subDen = self.den * other.den 
		print "%d/%d" % (subNum,subDen)

	def MultiNumber(self, other):
		multiNum = self.num * other.num
		multiDen = self.den * other.den 
		print "%d/%d" % (multiNum,multiDen)

	def DivisionNumber(self, other):
		divNum = self.num * other.den
		divDen = self.den * other.num 
		print "%d/%d" % (divNum,divDen)



fraction1 = RationalNumber(1,2)
fraction2 = RationalNumber(2,3)

print "\nThe first fraction is ",
fraction1.printNumber()

print "The second fraction is ",
fraction2.printNumber()

print "The first fraction in float format is ",
fraction1.printFloatFormat()

print "The second fraction in float format is ",
fraction2.printFloatFormat()

print "The sum of the two fractions is",
RationalNumber.addNumber(fraction1,fraction2)

print "Subtracting these two fractions is",
RationalNumber.subNumber(fraction1, fraction2)

print "Multiplication of fraction one and two is",
RationalNumber.MultiNumber(fraction1, fraction2)

print "Division of fraction one and two is: ",
RationalNumber.DivisionNumber(fraction1, fraction2)


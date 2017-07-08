
class Complex:
	"""Performing arithmetic with complex numbers"""

	def __init__(self, realpart=0.0, imaginary=0.0):
		self.realpart = realpart
		self.imaginary = imaginary

	def printComplex(self):
		print "%.1f + %.1fi" % (self.realpart, self.imaginary)
		
		
	def addComplex(self, other):
		sumReal = self.realpart + other.realpart
		sumImg  = self.imaginary + other.imaginary
		print "%.1f + %.1fi" % (sumReal, sumImg)
		

	def subComplex(self, other):
		subReal = self.realpart - other.realpart
		subImg  = self.imaginary - other.imaginary
		print "%.1f + %.1fi" % (subReal, subImg)


	


complexe1 = Complex(1,4)	
complexe2 = Complex(2,3)

print "\nThe first complex number is : ",
complexe1.printComplex()
print "The second complex number is:  ", 
complexe2.printComplex()
print "Sum of the two complex number is : ", 
Complex.addComplex(complexe1,complexe2)
print "Subtracting the two complex number gives: ", 
Complex.subComplex(complexe1,complexe2)
		



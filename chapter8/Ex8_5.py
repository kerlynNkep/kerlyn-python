#Definition of class Rational

def gcd(x,y):
	"""computes the greatest common dividor of two values"""
	while y:
		z = x
		x = y
		y = z % y
	return x
	
class Rational:
	"""Representation of rational number"""
	
	def __init__(self,top = 1,bottom = 1):
		"""initialses rational instance"""

		if bottom == 0:
			raise ZeroDivisionError,"cannot have 0 at denominator"

		
		self.numerator = abs(top)			
		self.denominator = abs(bottom)
		self.sign = (top * bottom) / (self.numerator *self.denominator)

		self.simplify() #Rational representation in reduced form

	
	# class interface method
	def simplify(self):
		"""simplifies a Rational number"""
		common = gcd(self.numerator,self.denominator)
		self.numerator /= common
		self.denominator /= common

    # overloaded unary operator
	def __neg__(self):
		"""overloaded negation operator"""
		return Rational(-self.sign*self.numerator,self.denominator)
	
	
	#overloaded binary arithmetic operators
	
	def __add__(self,other):
		"""overloaded addition operator"""
		return Rational(self.sign*self.numerator*other.denominator +
		 other.sign *other.numerator * self.denominator,self.denominator * other.denominator)

	def __radd__(self,other):
		"""overload right-hand addition """

		return Rational(self.sign*self.numerator*other.denominator +
		 other.sign *other.numerator * self.denominator,self.denominator * other.denominator)


	def __sub__(self,other):
		"""overload subtraction operator"""
		return self + (-other)

	def __rsub__(self,other):
		"""overload right-hand subtraction"""
		return self + (-other)
	

	def __mul__(self,other):
		"""overloaded multiplication method"""
		return Rational(self.numerator * other.numerator,self.sign
    		*self.denominator * other.sign *other.denominator)	


	def __rmul__(self,other):
		"""overload right-hand  multiplication"""
		return Rational(self.numerator * other.numerator,self.sign
    		*self.denominator * other.sign *other.denominator)



	def __div__(self,other):
		"""overloaded / division operator"""
		return Rational(self.numerator * self.denominator,
    		self.sign *self.denominator*other.sign * other.numerator)

	def __rdiv__(self,other):
		"""overloaded / division operator"""
		return Rational(self.numerator * self.denominator,
    		self.sign *self.denominator*other.sign * other.numerator)

	def __rfloordiv__(self,other):
		"""overloaded // division operator"""
		return Rational(self.numerator * self.denominator,
    		self.sign *self.denominator*other.sign * other.numerator)		


	def __truediv__(self,other):
		"""overloaded / division operator,(for use with python
     version(>=2.2)that contain the // opeartor )"""
		return self.__div__(other)

	def __str__(self):
		"""string representation"""
		#determine sign dispaly
		if self.sign == -1:
			signString = "-"
		else:
			signString = ""

		if self.numerator == 0:
			return "0"
		elif self.denominator == 1:
			return "%s%d" %(signString,self.numerator)
		else:
			return "%s%d/%d" %(signString,self.numerator,self.denominator)

#overloaded coercion capability
	def __int__(self):
		"""overloaded integer representation"""
		return self.sign * divmod(self.numerator,self.denominator)[0]

	def __coerce__(self,other):
		"""overloaded coercion.can only coerce int to Rational"""
		if type(other) == type(1):
			return(self,Rational(other))
		else:
			return None		


#driver program for the Rational class

# create objects of class Rational
rational1 = Rational() #1/1
rational2 = Rational(10,30) # 10/30 reducesd to 1/3
rational3 = Rational(-7,14) # -7/14 reduced to -1/2

# prints objects of class rational
print "rational1",rational1
print "rational2 ", rational2
print "rational3",rational3
print 

# test mathematical operators
print rational1, "/", rational2, "=", rational1 / rational2
print rational3, "-", rational2, "=", rational3 - rational2
print rational2, "*", rational3, "-", rational1, "=", \
rational2 * rational3 - rational1

# overloading + implicitly overloads +=
rational1 += rational2 * rational3
print "\nrational1 after adding rational2 * rational3:", rational1
print

# test coercion
print rational2, "as an integer is:", int( rational2 )
print rational2, "+ 1 =", rational2 + 1

# when user defined class is used as the right-hand value of an operator

add = 1 + Rational(3,4)
print "when using addition", add

sub = 1 - Rational(3,4)
print "for subtraction", sub

multi = 1 * Rational(3,4)
print "for multiplication" ,multi

div = 1 / Rational(3,4)
print "for division", div

truediv = 1 // Rational(3,4)
print "for true division", truediv
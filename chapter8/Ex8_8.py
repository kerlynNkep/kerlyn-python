# class polynomial : exponent=key,coefficient = value

import math

class Polynomial:
	"""class to make a polynomial behave like a dictionary"""
	
	def __init__(self,exponent = 0 ,coefficient = 0):
		
		self.__dict__[exponent] = coefficient
	
	
	#mapping special methods
	
	def __getitem__(self,exponent):
		"""overloaded key-value access"""
		
		if not self.__dict__[exponent]:
			return 0
		return self.__dict__[exponent]

	def __setitem__(self,exponent,coefficient):
		"""overloaded key-value assignment/creation"""
		
		self.__dict__[exponent] = coefficient

	
	def __str__(self):
		"""overloaded string representation"""
		
		return str(self.__dict__)

	
	def keys(self):
		"""return list of keys in dictionary"""
		
		return self.__dict__.keys()

	
	def values(self):
		
		return self.__dict__.values()

	def __len__(self):
		"""return length of dictionary"""
		
		self.length = self.keys()
		return max(self.length)



#driver program


polynomial1 = Polynomial()
polynomial2 = Polynomial(4,5)
print "empty dictionary", polynomial1

#add values to polynomial 1(calls simple.setitem)
polynomial1 [1] = 2
polynomial1 [3] = 4
polynomial1 [5] = 6
 
polynomial2 [2] = 6
polynomial2 [3] = 5
polynomial2 [4] = 2

print "dict after adding values to polynomial 1 :",polynomial1
print "dict after adding values to polynimial 2 :",polynomial2

print "length is from the highest exponent:",len(polynomial2)
print "coffiecient with exponent 5 is :",polynomial1[5]
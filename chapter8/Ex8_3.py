# Definition of class SimpleDictionary.

class SimpleDictionary:
	"""Class to make an instance behave like a dictionary"""

	# mapping special methods
	
	def __getitem__( self, key ):
		"""Overloaded key-value access"""

		return self.__dict__[ key ]

	
	def __setitem__( self, key, value ):
		"""Overloaded key-value assignment/creation"""

		self.__dict__[ key ] = value


	def __delitem__( self, key ):
		"""Overloaded key-value deletion"""

		del self.__dict__[ key ]


	def __str__( self ):
		"""Overloaded string representation"""

		return str( self.__dict__ )


# common mapping methods
	
	def keys( self ):
		"""Returns list of keys in dictionary"""

		return self.__dict__.keys()

	
	def values( self ):
		"""Returns list of values in dictionary"""

		return self.__dict__.values()


	def items( self ):
		"""Returns list of items in dictionary"""

		return self.__dict__.items()

	def clear(self):
		"""Returns empty dictionary"""

		return self.__dict__.clear()

	def copy(self):
		"""Returns a shallow copy of the dictionary"""

		return self.__dict__.copy()

	def has_key(self, number):
		"""determines if mapping contains key"""

		for key in self.keys():

			if key == number :
				return "The key %d was found" % (number)
			else:
				return "key %d was not found" % (number)

	def get(self):
		"""Returns values of keys in mapping"""

		for key in self.keys():
			return self.__dict__.values()

	
	def update(self,other):
		"""overloaded update method"""
	
		return self.__dict__.update(other)



simple = SimpleDictionary()
print "The empty dictionary:"

# add values to simple (invokes simple.__setitem__)
simple[ 1 ] = "one"
simple[ 2 ] = "two"
simple[ 3 ] = "three"
print "\nThe dic after adding values:", simple

del simple[ 1 ] # remove a value
print "The dict after removing a value:", simple

# use mapping methods

print "\nDict keys:", simple.keys()

print "\nDict values:", simple.values()

print  "\nDic items:", simple.items()

simple2 = simple.copy()
print "\nA copy of dictionary:", simple2

print "\nChecking for a key :" , simple.has_key(2)

print "\nValues of dictionary keys:", simple.get()

simple.clear()
print "\n Dict after clearing:",simple 
print "checking the copied version:", simple2

dic = {4:"four",5: "five",6:"six",7:"seven"}
simple.update(dic)
print "\nDict after updating", simple
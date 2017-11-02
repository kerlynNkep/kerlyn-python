# Editing class SingleList.

class SingleList:

	def __init__( self, initialList = None ):
		"""Initializes SingleList instance"""

		self.__list = []  # internal list, contains no duplicates
		
		# process list passed to __init__, if necessary

		if initialList:

			for value in initialList:

				if value not in self.__list:
					self.__list.append( value )		# add original value


	# string representation method
	
	def __str__( self ):
		"""Overloaded string representation"""

		tempString = ""
		i = 0


		# build output string
		for i in range( len( self ) ):

			tempString += "%12d" % self.__list[ i ]

			if ( i + 1 ) % 4 == 0:
				
				tempString += "\n"	# 4 numbers per row of output


		if i % 4 != 0: # add newline, if necessary
			tempString += "\n"

		return tempString


	# overloaded sequence methods

	def __len__( self ):
		"""Overloaded length of the list"""
		
		return len( self.__list )


	def __getitem__( self, index ):
		"""Overloaded sequence element access"""

		return self.__list[ index ]

	def __setitem__( self, index, value ):
		"""Overloaded sequence element assignment"""

		if value in self.__list:
		
			raise ValueError, "List already contains value %s" % str( value )

		self.__list[ index ] = value
		
	
	# overloaded equality operators
	def __eq__( self, other ):
		"""Overloaded == operator"""

		if len( self ) != len( other ):
			return 0                          # lists of different sizes

		for i in range( 0, len( self ) ):
			
			if self.__list[ i ] != other.__list[ i ]:
				return 0       # lists are not equal

		return 1	# lists are equal


	def __ne__( self, other ):
		"""Overloaded != and <> operators"""

		return not ( self == other )


	#overloading list methods

	def append(self,elt):

		return self.__list.append(elt)

	
	def count(self, elt):

		count =  self.__list.count(elt)
		return count

	
	def index(self, elt):

		return self.__list.index(elt)

	
	def insert(self, index, item):

		return self.__list.insert(index, item)

	
	def pop(self):

		return self.__list.pop()

	
	def remove(self,elt):

		if elt not in self.__list:
			raise ValueError, "Value not in the list"
		return self.__list.remove(elt)

	
	def reverse(self):

		return self.__list.reverse()


	def sort(self):
		 return self.__list.sort()


	def __delitem__(self,item):
		del self.__list[item]
		return self.__list


	def __contains__(self, elt):

		for elt in self.__list:
			return "%d in list" % (elt)
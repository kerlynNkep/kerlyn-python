# Driver for simple class SingleList.

from Ex8_4 import SingleList


def getIntegers():

	size = int( raw_input( "List size: " ) )
	
	returnList = [] # create an empty list

	for i in range( size ):
		returnList.append( int( raw_input( "Integer %d: " % ( i + 1 ) ) ) )

	return returnList


# input and create integers1 and integers2
print "Creating integers1..."
integers1 = SingleList( getIntegers() )

print "Creating integers2..."
integers2 = SingleList( getIntegers() )


# print integers1 size and contents
print "List:\n", integers1
print "\nSize of list integers1 is", len( integers1 )



# print integers2 size and contents
print "List:\n", integers2
print "\nSize of list integers2 is", len( integers2 )




#add value to a list
integers1.append(2)
print "\nAfter adding 2 to integer 1:", integers1 

print "number of 2 in list:", integers1.count(2)

print "\nindex of 2:", integers1.index(2)

integers1.insert(2,4)
print "\ninsert value 4 at position 2:", integers1

integers1.append(2)
print "\nAfter adding 2 to integer 1:", integers1 

print "\nremoving and returning the last elt in integers1:", integers1.pop()

integers1.remove(2)
print "\nRemoving the first occurance of 2 in integers1:", integers1 

integers1.reverse()
print "\nReversing intergers1:", integers1

integers1.sort()
print "\nSorting the list:", integers1
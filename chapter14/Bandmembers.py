
import sys, cPickle

class BandMembers:
	"""Represent a Band member"""

	def __init__(self, name, instrument):
		self.name = name
		self.instrument = instrument

	def __str__(self):
		return "%s %s \n" % ( self.name, self.instrument )



try:
	file = open("users.dat", "w")

except IOError:
	print >> sys.stderr, "file couldnt open"
	sys.exit(1)

#member1 = BandMembers("John Doe", "Guitar")
#member2 = BandMembers("Sue Hannah", "Flute")
#member3 = BandMembers("Joe Praise","Piano")
#member4 = BandMembers("Lilian Scott", "Flute")

print "**Enter the first two names and the instrument. You can enter 0 to end program***"
inputList = []
while 1:
	try:
		inputValue = raw_input( "first two names? " )
		inputValue2 = raw_input( "Instrument? " )


	except EOFError:
		break
	
	else:
		if inputValue == "0" or inputValue2 == "0":
			break
		else:
			member1 = BandMembers(inputValue,inputValue2)
			person1 = member1.__str__()
			inputList.append(person1.split())


cPickle.dump(inputList, file)


file.close()
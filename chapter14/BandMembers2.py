
import sys, cPickle


#open file
try:
	file = open("users.dat", "r")

except IOError:
	print >> sys.stderr, "file couldnt be open"
	sys.exit(1)

records = cPickle.load(file) #retrieve list of lines in file



print "Firstname".ljust(10),
print "LastName".ljust(20),
print "Instrument".ljust(20)

for record in records:
	print record[0].ljust(10),
	print record[1].ljust(20),
	print record[2].ljust(20)


file.close()
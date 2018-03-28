#substantial transaction process to achieve instant access

import sys
import shelve

#function to list output
def output(number, aList):
	print number.ljust(15),
	print aList[0].ljust(25),
	print aList[1].ljust(15),
	print aList[2].rjust(10)


def main():
	try:
		ShelveFile = shelve.open("hardware.dat")

	except IOError:
		print >> stderr, "couldnt open file"

	print "Please enter a record number for hardware tool or 0 to end input"

	while 1:
		print "\nRecord number"
		recordNum = int(raw_input("?"))

		if recordNum >0:
			recordValues = raw_input("input Toolname, Quantity and cost\n?")
			aList = recordValues.split()

			#send data to shelve file
			ShelveFile[str(recordNum)] = aList


		elif recordNum ==0:
			break


	#print header outline:

	print "Record_Number".ljust(10),
	print "Tool_Name".ljust(20),
	print "Quantity".ljust(20),
	print "Cost".rjust(10)

	#calling function output
	for recordNumber in ShelveFile.keys():
		output(recordNumber, ShelveFile[recordNumber])

	ShelveFile.close()


if __name__ == "__main__":
	main()


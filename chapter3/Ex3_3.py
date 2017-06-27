
#initialization
milesPerGalon = 0
totalmiles = 0
totalgallons = 0


gallons = raw_input("Enter the gallons used (-1 to end):")  #collecting first input for gallon-used
gallons = float(gallons) 


while gallons != -1:
	miles = raw_input("Enter miles driven:") #collecting input for miles driven
	miles = int(miles)

	milesPerGalon = miles / float(gallons)  		#computing miles per gallon
	totalmiles = int(totalmiles) + miles    		
	totalgallons = float(totalgallons) + gallons

	print "miles per gallon for this tank was %.3f\n" % (milesPerGalon)

	gallons = raw_input("Enter the gallons used (-1 to end):")
	gallons = float(gallons)


if totalgallons != 0:
	print "\nThe overall average miles/gallon was: %.4f\n" % (totalmiles / totalgallons)

else:
	print "\nNo entry was made\n"

	


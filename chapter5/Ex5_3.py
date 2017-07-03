

List = []
print "Pls input 20 numbers"

for i in range(20):
	value = int(raw_input("enter %d integer" % (i+1)))
	if value not in List:
		List.append(value)
		print value
	
	
print "\n\n your list of values without duplicate is :",List 	

#initialization of variables
total = 1
total2 = 1

x = raw_input("\nyou are about to get the value of e^x. what would you like your value of x to be:")

for counter in range(1,11,1):   #getting 10 sums

		x = int(x)

		#getting factorials
		if counter==0:
			a=1

		elif counter==1:
			a=1

		else:
			a=counter

		total = total * a

		#estimating the value of e using the formula
		u = (x**counter) /float(total)
		total2 = total2 + u 
		

print "e =", total2        #getting output
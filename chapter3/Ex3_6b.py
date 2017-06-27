
#initialization of variables
total = 1
total2 = 1

for counter in range(1,11,1):   #getting 10 sums

		#getting factorials
		if counter==0:
			a=1

		elif counter==1:
			a=1

		else:
			a=counter

		total = total * a

		#estimating the value of e using the formula
		u = 1 /float(total)
		total2 = total2 + u 
		

print "e =", total2        #getting output
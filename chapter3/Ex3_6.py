
 #initialization of variable
total = 1

n = raw_input("input a positive integer to check its factorial of:")
#n = int(n)


while n>=0:
	n = int(n)

	if n==0:
		a=1

	elif n==1:
		a=1

	else:
		a=n

	total = total * a
	n = n-1


#if n>=0:
print "\nits factorial is", total

#else:
	#print "invalid number"
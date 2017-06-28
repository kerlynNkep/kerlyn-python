
#to determine if a number is a prime number

#function for prime
def prime(c):

	if c<2:
		print "%d is not a prime number" % (c)

	else:
		
		if c==2:
			print "%d is a prime number" % (c)

		else:
			for i in range(2,c):
				if c%i== 0 :
					print "%d is not a prime number" % (c)
					return
			print "%d is a prime number" % (c)


num = raw_input("pls enter a number")
num = int(num)
prime(num)










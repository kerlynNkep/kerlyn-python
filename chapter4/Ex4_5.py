#determining perfect squares and also displaying perfect squares between 1 and 100 inclusive


def perfect(num,c=0):
		
		if num==1:
			print "\n%d is a perfect square" % (num)

		else:

			for i in range(1,num):

				if num%i==0:
					c = c+i
					continue

			if c==num:
				print "%d is a perfect square" % (num)



for number in range(1,1001):
	perfect(number)
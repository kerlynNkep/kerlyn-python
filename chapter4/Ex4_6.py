#trigerring multiplication

import random

#function to generate the random numbers
def generation():
	
	num1 = int(random.randrange(1,20))
	num2 = int(random.randrange(1,20))
	product= num1 * num2
	print "how much is %d times %d: " % (num1,num2)
	return product

question = generation()
ans = int(raw_input())


while 1:
	
	if (ans==question):
		print "Very Good" 
		question = generation()
		ans = int(raw_input())

	else:
		print "No pls try again"
		ans = int(raw_input())


"""illustrating reraising"""

import math

class NegativeNumberError(ArithmeticError):
	"""Attempt imporper operations on negative number"""

	pass

def SquareRoot (number):
	"""Compute square root of number. Raise NegativeNumberError if number is less than 0"""

	if number < 0:
		raise NegativeNumberError, "Square root of a negative number not permitted"

	return math.sqrt(number)


while 1:
	#get user to enter-entered number and compute square root
	
	try:
		userValue = float (raw_input("Pls enter value"))
		print SquareRoot(userValue)

	#float raises value error if number isnt numerical
	except ValueError:
		print "the value entered isnt a number"

	except NegativeNumberError, exception:
		print exception

	#successful execution: terminate while loop
	else:
		break

number1 = raw_input( "Enter numerator: " )
number2 = raw_input( "Enter denominator: " )

try:
	number1 = float( number1 )
	number2 = float( number2 )
	result = number1 / number2

# float raises a ValueError exception
except ValueError:
	print "You must enter two numbers"

# division by zero raises a ZeroDivisionError exception
except ZeroDivisionError:
	print "Attempted to divide by zero"

# else clause's suite executes if try suite raises no exceptions
else:
	print "%.3f / %.3f = %.3f" % ( number1, number2, result )
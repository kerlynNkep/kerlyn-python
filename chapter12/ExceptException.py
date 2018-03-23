#exercise 12.4 .
# programing illustrating the use of 'except Exceptions, exception

import traceback

def function1():
	function2()

def function2():
	function3()

def function3():
# raise exception, catch exception, reraise exception

	try:
		raise Exception, "An exception has occurred"

	except Exception:
		print "Caught exception in function3. Reraising....\n"
		raise   # reraises most recent exception


# call function1, any Exception it generates will be
# caught by the except clause that follows

try:
	function1()

except Exception, exception:
	print "Exception caught in main program."
	print "\nException arguments:", exception.args
	print "\nException message:", exception
	print "\nTraceback:", traceback.print_exc()
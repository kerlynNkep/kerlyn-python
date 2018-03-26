import re


string = raw_input("Enter your digit")
expression = r"^\d+(.?)\d+$"

if re.search(expression,string):
	print "the number is valid"

else:
	print "the number is not valid"
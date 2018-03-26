import re


string = raw_input("enter you xhtml string")
expression = r"^(http://)(\w+).(com|net|org|cm)$"

if re.search(expression, string):
	print "the urml is correct"

else:
	print "the urml is not correct"
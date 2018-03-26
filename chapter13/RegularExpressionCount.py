
import re

import re

string = raw_input("pls enter a string")
counter1, counter2, counter3= 0,0,0

for x in string:
	if re.match(r"\d",x):
		counter1+=1
	elif re.match(r"\w",x):
		counter2+=1
	elif re.match(r"\s",x):
		counter3+=1
	

print "Number of digits in the string :", counter1
print "Number of words in the string :", counter2
print "Number of white spaces in the string :", counter3

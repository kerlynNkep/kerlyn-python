import re

string = raw_input("pls enter a string")

if re.search(r'[\s+]',string):
	string = re.sub(r'[\s]','space',string)
	print "the word without extra spaces is:", string

else:
	print "the word is :", string
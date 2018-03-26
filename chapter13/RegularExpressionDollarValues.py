import re

def convertion(value):
	value2 = [ ]
	
	for x in value :
		
		x = int(re.sub(r'\$', '', x))
		pound = str(0.667 * x) +'pounds'
		value2.append(pound)
	
	print(value2)

value = ['12$','15$','18$','79$','85$','100$','200$']

convertion(value)
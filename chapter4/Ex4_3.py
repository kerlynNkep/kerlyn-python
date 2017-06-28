#write a program that prints a chart showing the Fahrenheit equivalents of all 
#Celsius temperatures 0–100 degrees.

def farenheit(c):
	F = float((9.0/5)*c + 32)
	return F

print "celsius%13s" % "Farenheit"

for i in range(0,101):
		print "%.4f     %.4f" % (i,farenheit(i))


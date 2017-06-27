#Write a program that reads in two integers and determines and prints whether the first is a
#multiple of the second.

print "Welcome to know if a number is a multiple of another:\n"

Interger1 = raw_input("input the first number:\n")
Interger1 = int(Interger1)

Interger2 = raw_input("input the second number:\n")
Interger2 = int(Interger2)

if (Interger2 % Interger1) == 0:
	print "%d is a multiple of %d" % (Interger1, Interger2) 

else:
	print "%d is not a multiple of %d" % (Interger1, Interger2)
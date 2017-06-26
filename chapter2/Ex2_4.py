#Write a program that requests the user to enter two numbers and prints the sum, product, 
#difference and quotient of the two numbers

print "\nTo get the sum, product, difference and quotient of two numbers:\n"

Interger1 = raw_input("Input first number:\n")
Interger1 = int (Interger1)

Interger2 = raw_input("Input second number\n")
Interger2 = int (Interger2)

Sum = Interger1 + Interger2
difference = Interger1 - Interger2
Quotient = Interger1 / Interger2
Product = Interger1 * Interger2 

#printing output
print "*******************************************************"
print " the sum of %d and %d is %d\n" % (Interger1, Interger2, Sum)
print " the difference between %d and %d is %d\n" % (Interger1, Interger2, difference)
print " the Quotient of %d and %d is %d\n" % (Interger1, Interger2, Quotient)
print " the Product of %d and %d is %d\n" % (Interger1, Interger2, Product)
print "*******************************************************"
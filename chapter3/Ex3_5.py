
value = raw_input("input a  5 digit binary number:")   #getting in binary value
value = int(value)

#seperating the value into its seperate integers

a = value/10
num1 = value%10

b = a/10
num2 = a%10

c = b/10
num3 = b%10

d = c/10
num4 = c%10

e = d/10
num5 = d%10

#checking if the number inputed is binary
if (num1==1 or num1==0)and(num2==1 or num2==0)and(num3==1 or num3==0) and(num4==1 or num4==0)and(num5==1 or num5==0):

	decimal = (num5 *1) + (num4* 2) + (num3*4) + (num2*8) + (num1 * 32)


	print "\ndecimal equivalent of %d is: %d" % (value, decimal)

else:
	print "\ninvalid entry pls enter a binary number comprising of '1' and '0'\n"


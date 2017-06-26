
number = raw_input("\ninput a five digit integer")
number = int(number)

#deriving first digit
a = number / 10
first = number % 10

#deriving second digit
b = a/10
second = a%10

#deriving third digit
c = b/10
third = b%10

#deriving fourth digit
d = c/10
fourth = c%10

#deriving fifth digit 
e = d/10
fifth = d%10

#checking for palindrome
if first==fifth and second==fourth :
	print "\n%d is a palindrome\n" % (number)

else:
	print "\n%d is not a palindrome\n" % (number)

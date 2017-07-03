
#function to perform bubblesort
def binarysearch(a,*str):
	str1 = list(str)
	str1.sort()
	upper = len(str1)
	lower = 0

#program 
	while lower<upper:
		x = lower + (upper-lower)//2 	#midpoint of list
		value = str1[x]				#indexes list using midpoint and assigns value to variable value
		if a == value:				#check if the target value a is same as the value
			return x 				# if true return the numbers index
		elif a<value:				#if target value(a) is less than value,
			upper = x				#assign midpt number to the upperlimit
		elif a>value:
			if lower == x:			#if the midpt is same as the lower pt 
				break				#stop loop
			lower = x				#if target value is > midpt assign midpt to lower 
		else:
			return -1

print binarysearch(6,2,3,4,5,6,7)
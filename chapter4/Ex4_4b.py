
def prime(c):
	if c<2:
		return
	else:
		if c==2:
			return c
		else:
			for i in range(2,c):
				if c%i== 0 :
					return ""
			return c;


for i in range(2,1001):
	print prime(i),  


#printing the pythagorean triple that satisfy the pythagoras theorem within the range 1 to 20

for h in range(1,21):
	for a in range(1,21):
		for b in range(1,21):
				c= (a**2) + (b**2)
				c = int(c)
				d= h**2
				d = int(d)

				if(c==d):
					print "adjacent, base, hypothenus:%d,%d,%d" % (a,b,h)
				

import random
List = []
#dictionary = {1:20, 2:10, 3:20}
dictionary = {i: random.randrange(1,99) for i in range(5)}
u = sorted(dictionary.itervalues())

for i in range(len(u)-1):
	if u[i] == u[i+1]:
		print "duplicate"
	



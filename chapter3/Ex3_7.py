
#printing four star shapes

#print first figure
print "(a)"
for i in range(1,11):
	print "*" * i

print "\n\n" 

#printing second figure
print "(b)"
for i in range(11,0, -1):
	print "*" * i

print "\n\n"

#printing third figure
print "(c)"
for i in range(1,11):
	print " " *(10-i) + "*" * i
	
print "\n\n"

#printing fourth figure
print "(d)"
for i in range(11, 0, -1):
	print " " *(11-i) + "*" * i
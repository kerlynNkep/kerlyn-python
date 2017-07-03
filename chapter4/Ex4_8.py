#The tower of Hanoi
#n number of disks to be moved
#1 peg in which threads are initially threaded
#3 peg in which threads are supposed to be moved to
#2 peg to be used as temporal holding area


def hanoi(n):
	if n<0:
		pass
	elif n==1:
		print "1-3"
	else:
		print "1-2"
		print "1-3" 
		#print "2-1" 
		#print "2-3"
		hanoi(n-1)



#print "there are %d disks in peg1 to be transfered to peg3"% n
hanoi(3)

def bubblesort(List):
	for numbers in range(len(List)-1,0,-1):
		for i in range(numbers):
			if List[i]>List[i+1]:
				temp = List[i]
				List[i]=List[i+1]
				List[i+1]=temp


List=[]
print "pls enter 10 values"

for i in range(10):
	value = int(raw_input( ""))
	List.append(value)

#print output
print "List before bubblesort",List
bubblesort(List)
print "List after bubble sort",List 


import sys
import shelve

def output(record, aList):
	print record.ljust(15),
	print aList[0].ljust(25),
	print aList[1].ljust(15),
	print aList[2].rjust(10)


def enterChoice():
	print "\nEnter your choice"
	print "1 - update an account"
	print "2 - delete an account"
	print "3 - end program"

	while 1:
		enterChoice = int( raw_input( "? " ) )
		if not 1 <= enterChoice <= 4:
			print >> sys.stderr, "Incorrect choice"
		else:
			break
	
	return enterChoice


def getAccount(prompt):
	while 1:
		account = int(raw_input(prompt +":"))

		if account > 0 :
			break

	return account


def updateRecord(updateFile):
	account = getAccount("Enter account to update")

	if updateFile.has_key(account):

		output(account, updateFile[account])
		choice = int(raw_input("Enter 1 for new Quantity and 2 for new Cost\n? "))
		
		if choice == 1:  #updating quantity of tool

			transaction = raw_input("\nEnter newlyadded(+) or sold(-):\n?")

			#create temporary record to alter data
			tempRecord = updateFile[account]
			tempQuantity = int(tempRecord[1])
			tempQuantity += int(transaction)
			tempRecord[1] = tempQuantity

			#update record in shelve
			del updateFile[account]   #removing old record first
			updateFile[account] = tempRecord 
			output(account, updateFile[account])

		elif choice == 2: #updating cost of tool

			transaction = raw_input("\nEnter new cost:\n?")
			
			#create temporary record to alter data
			tempRecord = updateFile[account]
			tempCost = int(transaction)
			tempRecord[2] = tempCost
			
			#update record in shelve
			del updateFile[account]   #removing old record first
			updateFile[account] = tempRecord 
			output(account, updateFile[account])

		else:
			print "wrong input"


	else:
		print >> sys.stdErr, "Account #", account, "doesnt exist"



#deleting a record
def deleteRecord(deletefromFile):
	account = getAccount("Enter account to update")

	if deletefromFile.has_key(account):
		del deletefromFile[account]
		print "account #", account, "has been deleted"

	else:
		print >> sys.stderr, "account doesnt exist"



# list of functions that correspond to user options
#options = [ updateRecord, deleteRecord ]

try:	
	inventoryfile = shelve.open("hardware.dat")

except IOError:
	print >> sys.stderr, "file couldnt open"
	sys.exit(1)


#process user command
while 1:
	choice = enterChoice()

	if choice == 3:
		break

	elif choice == 1:
		updateRecord(inventoryfile)

	elif choice == 2:
		deleteRecord(inventoryfile)
	

inventoryfile.close()





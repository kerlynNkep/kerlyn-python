import MySQLdb
import sys

try:
	db = MySQLdb.connect(host="localhost", user="root", passwd="N1k2m3n4", db="Books")
	cursor = db.cursor()

except MySQLdb.OperationError:
	print "database couldnt open"
	sys.exit(1)


query1 = "INSERT INTO Authors (AuthorID, FirstName, LastName) VALUES (11, 'Teddy', 'Daniels')"
query2 = "INSERT INTO Publisher (PublisherID, PublisherName) VALUES (3, 'Thompson James')"
query3 = "INSERT INTO AuthorISBN (AuthorID, ISBN) VALUES (11, 139823489)"
query4 = """INSERT INTO  Titles (ISBN,Title,EditionNumber,PublisherID,copyright,imagefile,prices) 
			VALUES (139823489, 'Childrens day out', 1, 1, 2016, 'imge.jpg', 234.9)"""


value = cursor.execute(query1)

if value == 1:
	print "Values inserted into Author table.  0 Errors"
else:
	print "Insertion Error"


#executing next query
value2 = cursor.execute(query2)

if value2 == 1:
	print "Values inserted into Publisher table.  0 Errors"
else:
	print "Insertion Error"


#executing next query
cursor.execute(query3)
value3 = cursor.execute(query4)

if value3 == 1:
	print "Values inserted into Titles table.  0 Errors"
else:
	print "Insertion Error"
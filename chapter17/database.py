import MySQLdb
import sys


try:
	db = MySQLdb.connect(host="localhost", user="root", passwd="N1k2m3n4", db="Books")
	cursor = db.cursor()

except MySQLdb.OperationalError, message:
	print "Error", message
	sys.exit(1)

query1 = "SELECT * FROM Authors"
query2 = "SELECT * FROM Publisher"
query3 = """SELECT AuthorID,PublisherID,copyright,Title
			FROM Titles 
			INNER JOIN AuthorISBN ON Titles.ISBN = AuthorISBN.ISBN 
			WHERE AuthorID=1 ORDER BY Title ASC"""

query4 = """SELECT PublisherName,Title,copyright,ISBN 
			FROM Titles 
			INNER JOIN Publisher ON Publisher.PublisherID = Titles.PublisherID 
			WHERE Titles.PublisherID=1 ORDER BY Title ASC"""

cursor.execute(query1)
allFields = cursor.description #get fields name
allRecords = cursor.fetchall() #get records

#Display in table form
print "\n<table border='1' cellpadding='3> <tr bgcolor='silver'>  "

#print output results in a table
for field in allFields:
	print "<td>%s</td>" % field[0]

print "</tr>"

# display each record as a row
for name in allRecords:
	print "<tr>"
	for item in name:
		print "<td>%s</td>" % item
	print "</tr>"
print "</table>"

print "\n\n\n" 

#execution of next query

cursor.execute(query2)
allFields = cursor.description #get fields name
allRecords = cursor.fetchall() #get records

print "\n<table border='1' cellpadding='3><tr bgcolor='silver'>"

for field in allFields:
	print "<td>%s</td>" % field[0]
print "</tr>"

# display each record as a row
for name in allRecords:
	print "<tr>"
	for item in name:
		print "<td>%s</td>" % item
	print "</tr>"
print "</table>"

print "\n\n\n" 

#execution of next query

cursor.execute(query3)
allFields = cursor.description #get fields name
allRecords = cursor.fetchall() #get records

print "\n<table border='1' cellpadding='3><tr bgcolor='silver'>"

for field in allFields:
	print "<td>%s</td>" % field[0]
print "</tr>"

# display each record as a row
for name in allRecords:
	print "<tr>"
	for item in name:
		print "<td>%s</td>" % item
	print "</tr>"
print "</table>"

print "\n\n\n" 

#execution of next query

cursor.execute(query4)
allFields = cursor.description #get fields name
allRecords = cursor.fetchall() #get records

print "\n<table border='1' cellpadding='3><tr bgcolor='silver'>"

for field in allFields:
	print "<td>%s</td>" % field[0]
print "</tr>"

# display each record as a row
for name in allRecords:
	print "<tr>"
	for item in name:
		print "<td>%s</td>" % item
	print "</tr>"
print "</table>"


cursor.close()
db.close()

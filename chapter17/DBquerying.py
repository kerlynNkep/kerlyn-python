import MySQLdb
import cgi
import sys

try:
	db = MySQLdb.connect(host="localhost", user="root", passwd="N1k2m3n4", db="test")

except MySQLdb.OperationalError, error:
	print "Error:", error
	sys.exit(1)

else:
	cursor = db.cursor() # you must create a Cursor object. 

# Querrying database
cursor.execute("SELECT * FROM signup")

allFields = cursor.description #get fields name
allRecords = cursor.fetchall() #get records
print "****", allFields

#close cursor and database
cursor.close()
db.close()


print """\n<table border='1' cellpadding='3> <tr bgcolor='silver'>  """

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



#trying to make use of composition

import datetime
date=datetime.date.today()
month = date.month

class Date:

	def __init__(self, day, month, year):
		self.Day = day
		self.Month = month
		self.Year = year


	def __str__(self):
		return "birthday %d-%d-%d" % (self.Day, self.Month, self.Year) 



class Employee:

	def __init__(self, fname, lname, code):
		self.firstname = fname
		self.lastname = lname
		self.deptcode = code


	def __str__(self):
		return "Employee:%s %s with dept code %d" % (self.firstname,self.lastname, self.deptcode)


class Boss:

	def __init__(self,fname,lname, code, day, month, year, salary):
		self.firstname = fname
		self.lastname = lname
		self.deptcode = code
		self.Day = day
		self.Month = month
		self.Year = year
		self.Salary = salary
		self.E = Employee(fname,lname, code)
		self.D = Date(day, month, year)


	def __str__(self):
		return "%s is a boss worker and has %s" % (self.E.__str__(), self.D.__str__())  


	def earnings(self):
		if month == self.Month:
			return self.Salary + 1000
		else:
			return self.Salary


class CommissionWorker:

	def __init__(self,fname,lname,code,day,month,year,salary,commission,quantity):
		self.firstname = fname
		self.lastname = lname
		self.deptcode = code
		self.Day = day
		self.Month = month
		self.Year = year
		self.Salary = salary
		self.Commission = commission
		self.Quantity = quantity
		self.E = Employee(fname,lname, code)
		self.D = Date(day, month, year)


	def __str__(self):
		return "%s is a commision worker and has %s" % (self.E.__str__(), self.D.__str__())  


	def earnings(self):
		if month == self.Month:
			return self.Salary + self.Commission + self.Quantity + 1000
		else:
			return self.Salary + self.Commission + self.Quantity


class PeiceWorker:

	def __init__(self,fname,lname,code,day,month,year,wage,quantity):
		self.firstname = fname
		self.lastname = lname
		self.deptcode = code
		self.Day = day
		self.Month = month
		self.Year = year
		self.Wage = wage
		self.Quantity = quantity
		self.E = Employee(fname,lname, code)
		self.D = Date(day, month, year)


	def __str__(self):
		return "%s is a piece worker and has %s" % (self.E.__str__(), self.D.__str__())  


	def earnings(self):
		if month == self.Month:
			return self.Wage * self.Quantity + 1000
		else:
			return self.Wage * self.Quantity




def main():

	employeesList = [ Boss( "John", "Smith",02, 3,11,2012,2345),
    				  CommissionWorker( "Sue", "Jones",23, 10, 9,1978, 10000, 300, 150 ),
    				  PeiceWorker( "Loe", "Greece",02, 22,05,2018, 45,100 ),
    				]    

	for employee in employeesList:
		print "\n %s earned $%.2f" % ( employee.__str__(), employee.earnings() )




if __name__ == "__main__":
	main()


class Time:
	"""Class Time with default constructor"""

	def __init__( self, hour = 0, minute = 0, second = 0 ):
		"""Time constructor initializes each data member to zero"""
		self.setTime( hour, minute, second )

	def setTime( self, hour, minute, second ):
		"""Set values of hour, minute, and second"""
		self.setHour( hour )
		self.setMinute( minute )
		self.setSecond( second )
	
	def setHour( self, hour ):
		"""Set hour value"""
		if 0 <= hour < 24:
			self.__hour = hour
		else:
			raise ValueError, "Invalid hour value: %d" % hour

	def setMinute( self, minute ):
		"""Set minute value"""
		if 0 <= minute < 60:
			self.__minute = minute
		else:
			raise ValueError, "Invalid minute value: %d" % minute

	def setSecond( self, second ):
		"""Set second value"""
		if 0 <= second < 60:
			self.__second = second
		else:
			raise ValueError, "Invalid second value: %d" % second

	def getHour( self ):
		"""Get hour value"""
		return self.__hour
	
	def getMinute( self ):
		"""Get minute value"""
		return self.__minute
	
	def getSecond( self ):
		"""Get second value"""
		return self.__second

	def tickMethod(self):
		
		if self.__hour==23 and self.__minute==59 and self.__second==59:
			self.__second = 00
			self.__minute = 00
			self.__hour = 0
			print "Another day"
		
		else:
			self.__second += 1
			if self.__second == 60:
				self.__minute +=1
			if self.__minute == 60:
				self.__hour += 1
		
			print "%.2d:%.2d:%.2d" %(self.__hour,self.__minute,self.__second)
	

	
	def printMilitary( self ):
		"""Prints Time object in military format"""
		print "%.2d:%.2d:%.2d" % ( self.__hour, self.__minute, self.__second ),

	def printStandard( self ):
		"""Prints Time object in standard format"""
		standardTime = ""
		
		if self.__hour == 0 or self.__hour == 12:
			standardTime += "12:"
		else:
			standardTime += "%d:" % ( self.__hour % 12 )
			standardTime += "%.2d:%.2d" % ( self.__minute, self.__second )
		
		if self.__hour < 12:
			standardTime += " AM"
		else:
			standardTime += " PM"
			print standardTime,



time = Time(23,59,59)

Time.tickMethod(time)


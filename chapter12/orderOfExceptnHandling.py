
class Point:
"""Class that represents a geometric point"""
   
    def __init__( self, xValue = 0, yValue = 0 ):
        self.x = xValue
        self.y = yValue
    
    def __str__( self ):
        return "( %d, %d )" % ( self.x, self.y )
    
   


class Circle( Point ):
    """Class that represents a circle"""
    

    def __init__( self, x = 0, y = 0, radiusValue = 0.0 ):
        
        Point.__init__( self, x, y ) # call base-class constructor
        self.radius = float( radiusValue )
   

    def area( self ):
        return math.pi * self.radius ** 2
    
    def __str__( self ):
        return "Center = %s Radius = %f" % ( Point.__str__( self ), self.radius )
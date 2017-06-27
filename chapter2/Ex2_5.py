
print "welcome"
radius =  raw_input("Input the radius of your circle:\n")
radius = float(radius)

print "***********************************************************"
print "the diameter of your circle is:(%.3f x 2) = %.3f  \n" % (radius, radius * 2)
print "the circumference of your circle is:(2 X 3.14159 X %.3f) = %.3f \n" % (radius, 2 * 3.14159 * radius)
print "the area of your circle is: (3.14159 X %.3f X %.3f) =%.3f \n" % (radius, radius, 3.14159 * radius ** 2)
print "***********************************************************"
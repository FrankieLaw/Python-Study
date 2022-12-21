'''
    Question 2.20
    
    (Diameter, Circumference and Area of a Circle) Write a program that reads in the radius of
    a circle as an integer and prints the circle’s diameter, circumference and area. Use the constant value
    3.14159 for π. Do all calculations in output statements.
'''

radius = int( input( "Enter a radius: " ) )

# Diameter (2r) Calculation
print( "Diameter: %d" %( radius * 2 ) )

# Circumference (2πr) Calculation
print( "Circumference: %d" %( 2 * 3.14159 * radius ) )

# Area (πr2) Calculation
print( "Area %d" %( 3.14159 * ( radius * radius ) ) )
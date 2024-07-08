# CH2-Ex2.5.py
"""
Chapter 2 - Exercise 2.5 - Circle Area, Diameter and Circumference
"""

radius:int = 3
pie:float  = 3.14159
print( '\n\n')
print( f'Radius: { radius } ')

# Diameter
diameter:float = 2 * radius
print( f'The Diameter is { diameter }' )

# Circumference
circumference:float = 2 * pie * radius
print( f'The circumference is { circumference}' )

# Area
area:float = pie * ( radius ** 2 )
print( f'The area of a circle is { area }' )
print( '\n\n')
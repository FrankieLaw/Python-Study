# Ex3.19.py
"""
    Brute Force Pythagorean Triples
"""

import math

for h in range( 1, 21 ):
    for x in range( 1, 21 ):
        for y in range( 1, 21 ):
            if( ( x * x ) + ( y * y ) == ( h * h ) ):
                print( f"{x}, {y}, {h} >> {x*x} + {y*y} = {h*h}" )
# Ex3.3.py
"""
    Walkthrough: What is the expected output?
"""

for row in range( 10 ):
    for column in range( 10 ):
        print( '<' if row % 2 == 1 else '>', end=' ' )
    print( )
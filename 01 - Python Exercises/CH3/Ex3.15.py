# Ex3.15.py
"""
    Approximate Constant e

    e = 1 + 1/1! + 1/2!
"""

factorial:int = 1       # Denominator value
e:float       = 1       # Constant e

for x in range( 1, 10 ):
    e += 1 / ( factorial * x )
    factorial *= x
    print( f'1 / {factorial} = {e:>.50}' )



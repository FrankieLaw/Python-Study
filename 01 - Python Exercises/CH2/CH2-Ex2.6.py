# CH2-Ex2.6.py
"""
    Use if statements to determine whether an integer is odd or even.
"""


# Get a user input of a number
# If numerator % denominator == 0, then is odd else even
print( "\n\n" )

numerator:float   = float( input( "Input a number > " ) )

if( numerator % 2 == 0 ):
    print( f'{ numerator } is an Even number' )
else:
    print( f'{ numerator } is an Odd number' )

print( "\n\n" )
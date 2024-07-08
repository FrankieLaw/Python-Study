# CH2-Ex2.7.py
"""
    Multiples between Numerator and Denominator
    Use if statement to determine that.
"""

print( "\n\n" )

nu:float   = float( input( "Input a numerator >> " ) )
de:float   = float( input( "Input a denominator >> " ) )

if( nu % de == 0 ):
    print( f'{ nu } is multiple of { de }' )
else:
    print( f'{ nu } is not multiple of { de }' )

print( "\n\n" )
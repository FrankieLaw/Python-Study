# CH2-Ex2.15.py
"""
    Sort in Ascending Order
"""

print( '\n\n' )

a:float = float( input( 'Enter first number: ' ) )
b:float = float( input( 'Enter second number: ' ) )
c:float = float( input( 'Enter third number: ' ) )

output:str = ''

# 12, 23, 34    a b c
# 12, 34, 23    a c b
# 23, 12, 34    b a c
# 23, 34, 12    b c a
# 34, 12, 23    c a b
# 34, 23, 12    c b a

if ( a == b ):
    if ( a == c ):
        output += str( a ) + ', ' + str( b ) + ', ' + str( c )


if ( a > b ):
    if ( a > c ):
        output += str( a ) + ', '

        if ( b > c ):
            output += str( b ) + ', ' + str( c )
        else:
            output += str( c ) + ', ' + str( b )


if ( b > a ):
    if ( b > c ):
        output += str( b ) + ', '

        if ( a > c ):
            output += str( a ) + ', ' + str( c )
        else:
            output += str( c ) + ', ' + str( a )


if ( c > a ):
    if ( c > b ):
        output += str( c ) + ', '
    
        if( a > b ):
            output += str( a ) + ', ' + str( b )
        else:
            output += str( b ) + ', ' + str( a )

print( f'{output}' )
print( '\n\n' )
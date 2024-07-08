# CH2-Ex2.12.py
"""
    7% Investment Return
"""

# a = p( 1 + r )^n

print( "\n\n" )

p:float = float( input( 'Principal: ' ) )
r:float = float( input( 'Rate: ' ) )
n:int   = int( input( 'Term: ' ) )

a:float = p * ( ( 1 + ( r / 100 ) ) ** n )

print( f'Your investment ${p} at the rate of {r}% over {n} years is: ${a:.2f}.' )
print( '${:.2f}'.format( a ) )
print( '${:10.2f}'.format( a ) )


print( "\n\n" )
# Ex3.10.py
"""
    7% Investment Return
    a = p( 1 + r )^n
"""

print( "\n\n" )

p:float = float( input( 'Principal: ' ) )
r:float = float( input( 'Rate: ' ) )
n:int   = int( input( 'Term: ' ) )


for term in range( n ):
    a:float = p * ( ( 1 + ( r / 100 ) ) ** ( term + 1 ) );
    print( f'Year {term + 1}: ${a:.2f}' )


print( "\n\n" )
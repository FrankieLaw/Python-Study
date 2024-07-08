# Ec3.17.py
# Ec3.17.py
"""
    Print out triangles
"""

for x in range( 1, 12 ):
    for y in range( 1, x ):
        print( '*', end='' )
    print( )


print( '\n' )
for x in range( 10, 0, -1 ):
    for y in range( 0, x ):
        print( '*', end='' )
    print( )


print( '\n' )
for x in range( 10, 0, -1 ):
    output:str = ""

    for y in range( 0, x ):
        output += '*'
    
    print( f'{output:>10}' )


print( '\n' )
for x in range( 1, 12 ):
    output:str = ""

    for y in range( 1, x ):
        output += '*'

    print( f'{output:>10}' )


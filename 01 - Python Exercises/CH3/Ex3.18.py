# Ex.3.18.py
"""
    Print all 4 Triangles in one straight line
"""

o = ['*'] * 1
i = ['*'] * 10

for _ in range( 10 ):
    print( 
        f'{"".join( o ):<10}', "   ", 
        f'{"".join( i ):>10}', "   ", 
        f'{"".join( i ):<10}', "   ", 
        f'{"".join( o ):>10}' 
    )

    o.append( "*" )
    i.pop( )
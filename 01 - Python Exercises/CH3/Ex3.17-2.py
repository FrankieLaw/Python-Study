# Ec3.17.py
# Ec3.17.py
"""
    Print out triangles
"""

line:list = []

for x in range( 10 ):
    line.append( "*" )
    print( *line, sep="" )

print( '\n' )

for x in range( 10 ):
    print( *line, sep="" )
    line.pop( )
    
print( '\n' )

for x in range( 10 ):
    line.append( "*" )
    print( f'{"".join(line):>10}' )

print( '\n' )

for x in range( 10 ):
    print( f'{"".join(line):>10}' )
    line.pop( )
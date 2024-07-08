# CH2-Ex2.8.py
"""
    Table of Squares and Cube
"""

print( "\n\n" )

a:int = 1
b:int = 2
c:int = 3
d:int = 4
e:int = 5

print( 'number\tsquare\tcube')
print( f'{a}\t{a*a}\t{a**3}' )
print( f'{b}\t{b*b}\t{b**3}' )
print( f'{c}\t{c*c}\t{c**3}' )
print( f'{d}\t{d*d}\t{d**3}' )
print( f'{e}\t{e*e}\t{e**3}' )

print( "\n\n" )

print( 'number\tsquare\tcube')
print( str( a ).rjust( 6 ), "\t", str( a*a ).rjust( 5 ), "\t", str( a**3 ).rjust( 3 )  )
print( str( b ).rjust( 6 ), "\t", str( b*b ).rjust( 5 ), "\t", str( b**3 ).rjust( 3 )  )
print( str( c ).rjust( 6 ), "\t", str( c*c ).rjust( 5 ), "\t", str( c**3 ).rjust( 3 )  )
print( str( d ).rjust( 6 ), "\t", str( d*d ).rjust( 5 ), "\t", str( d**3 ).rjust( 3 )  )
print( str( e ).rjust( 6 ), "\t", str( e*e ).rjust( 5 ), "\t", str( e**3 ).rjust( 3 )  )

print( "\n\n" )

print( 'number\tsquare\tcube')
print( f'{a:>6}\t{a*a:>6}\t{a**3:>4}' )
print( f'{b:>6}\t{b*b:>6}\t{b**3:>4}' )
print( f'{c:>6}\t{c*c:>6}\t{c**3:>4}' )
print( f'{d:>6}\t{d*d:>6}\t{d**3:>4}' )
print( f'{e:>6}\t{e*e:>6}\t{e**3:>4}' )

print( "\n\n" )

print( 'number\tsquare\tcube')
print( f'{a:^6}\t{a*a:^6}\t{a**3:^4}' )
print( f'{b:^6}\t{b*b:^6}\t{b**3:^4}' )
print( f'{c:^6}\t{c*c:^6}\t{c**3:^4}' )
print( f'{d:^6}\t{d*d:^6}\t{d**3:^4}' )
print( f'{e:^6}\t{e*e:^6}\t{e**3:^4}' )

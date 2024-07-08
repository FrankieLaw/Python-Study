# Ex3.9.py
"""
    Separate the Digits in an Integer
"""

print( "\n\n" )

a:int      = int( input( "Enter any digit number to be separated: " ) );
denom:int  = 10 ** ( len( str( a ) ) - 1 );
output:str = "";

for _ in range( len( str( a ) ) ):
    output += str( a // denom ) + " ";
    a %= denom;

    denom //= 10;

print( output )

print( "\n\n" )
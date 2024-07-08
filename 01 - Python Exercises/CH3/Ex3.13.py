# Ex3.13.py
"""
    Factorial
"""
import sys
sys.set_int_max_str_digits( 8000 );


print( '\n' )

term:int = int( input( 'Enter a number for factorial: ' ) )
result:int = 1;

for x in range( term, 0, -1 ):
    result *= x;

print( f'{term}! is {result}' )
print( '\n' )


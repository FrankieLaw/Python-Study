# CH2-Ex2.11.py
"""
    Separate the Digits in an Integer
"""

print( "\n\n" )

a:int      = int( input( "Enter a 5-digit number to be separated: " ) )
output:str = ""

output += str( a // 10000 ) + " "
a %= 10000

output += str( a // 1000 ) + " "
a %= 1000

output += str( a // 100 ) + " "
a %= 100

output += str( a // 10 ) + " "
a %= 10

output += str( a )

print( output )

print( "\n\n" )
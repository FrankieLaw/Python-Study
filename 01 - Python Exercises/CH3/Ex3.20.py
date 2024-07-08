# Ex3.20.py
"""
    Binary to Decimal
"""

# SETUP
binary:str = input( "Enter a binary string: " )
decimal:int = 0


# BINARY SETUP
binary = [ _b for _b in binary ]
maxBinaryValue = 1 if len( binary ) == 1 else 2 ** ( len( binary ) - 1 )


# CALCULATE BINARY TO DECIMAL EQUIVALENT
for i in binary:
    decimal += int( i ) * maxBinaryValue
    maxBinaryValue //= 2


print( decimal )
# Ex4.9.py
# Temperature Conversion
#
# Implement a fahrenheit function that returns the Fahrenheit equivalent of a 
# Celsius temperature.  Use the following formula:
#   F = ( 9 / 5 ) * C + 32
#   C = ( F - 32 ) / ( 9 / 5 )
#
# Use this function to print a chart showing the Fahrenheit equivalents of 
# all Celsius temperatures in the range 0-100 degrees.  Use one digit of 
# precision for the results.  Print the outputs in a near tabular format.

def toFahrenheit( c ):
    return ( 9 / 5 ) * c + 32

def toCelcius( f ):
    return ( f - 32 ) / ( 9 / 5 )

# print( toFahrenheit( 0 ) )
# print( toCelcius( 32 ) )

print( f"{'Celcius':<10}{'Fahrenheit':<11}" )
for c in range( 0, 101 ):
    print( f"{c:<10}{round( toFahrenheit(c) ):<11}" )

# Ex4.8.py
# (Rounding Numbers) Investigate built-in function round.
# Then use it to round the float value 13.56449 to the nearest integer, tenths, hundredths and thousandths positions.

x:float = 13.56449

print( )

print( f"{'Nearest Integer:':<20}{round( x )}" )
print( f"{'Nearest Tenth:':<20}{round( x, 2 )}" )
print( f"{'Nearest Hundred:':<20}{round( x, 3 )}" )
print( f"{'Nearest Thousand:':<20}{round( x, 4 )}" )

print( )
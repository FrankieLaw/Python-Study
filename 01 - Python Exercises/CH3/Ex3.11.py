# Ex3.11.py
"""
    Miles per gallon calculator
"""

thisGallon:float = 0.0;
thisMiles:float  = 0.0;

gallon:float     = 0.0;
miles:float      = 0.0;

print( '\n\n' )

while( thisGallon != -1 ):
    thisGallon = float( input( 'Enter the gallons used (-1 to end): ' ) )

    if( thisGallon == -1 ):
        print( f'The overall average miles/gallon was: {miles/gallon:.2f}' )
        break;
    else:
        thisMiles  = float( input( 'Enter the miles driven: ') )
        print( f'The miles/gallon for this tank was: {thisMiles/thisGallon:.2f}\n' )

    gallon += thisGallon;
    miles  += thisMiles;

print( '\n\n' )

    
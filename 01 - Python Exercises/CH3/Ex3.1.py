# Ex3.3.py
"""
    Create a sentinel program
"""

passes:int   = 0;
failures:int = 0;
result:int   = -1;  # initial response


for student in range( 10 ):
    while( result != 1 and result != 2 ):
        result = int( input( 'Enter result (1=pass, 2=fail): ') );

    if( result == 1 ):
        passes += 1;
    else:
        failures += 1;

    result = -1; # Reset Result


print( f'Passes:   {passes}' )
print( f'Failures: {failures}' )
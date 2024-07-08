# Ex3.6.py
"""
    Simple Intelligence Test
"""

print( '\n\n' );

print( 'What is your problem?' );
input( ">> " );

print( );
print( 'Have you had this problem before (yes or no)?' );
response:str = input( '>> ' );


print( );
if( response == 'yes' ):
    print( "Well, you have it again" );

if( response == 'no' ):
    print( 'Well, you have it now' );

if( response != 'yes' and response != 'no' ):
    print( "It looks like you are not well enough to answer" )
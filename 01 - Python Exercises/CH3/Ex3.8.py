# Ex3.8.py
"""
    Smallest and Largest
"""

import statistics
import numpy

print( "\n\n" )

myList:list = [];

for _ in range( 4 ):
    myList.append( int( input( f'Enter Element-{_+1} >> ' ) ) )

print( myList )
print( )

# sum
print( f'The sum is { sum(myList) }' )

# average
print( f'The average is { statistics.mean( myList ) }' )

# product
print( f'The product is { numpy.prod( myList ) }' )

# smallest
print( f'The smallest is { min( myList ) }' )

# largest
print( f'The largest is { max( myList ) }' )


print( "\n\n" )
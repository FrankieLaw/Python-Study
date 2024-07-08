# TUPLE DECLARATION
sampleTuple1:tuple = ( 1, 2, 3, 4 )
sampleTuple2:tuple = ( "Frankie", 2, 3, 4 )

try:
    print( sampleTuple1 > sampleTuple2 )
except TypeError as err:
    print( "==================================")
    print( "sampleTuple1 > sampleTuple2" )
    print( "Cannot compare \'int\' and \'str\'")
    print( "==================================")
    print( "\n\n" )


# TUPLE COMPARISON
data1:tuple = ( 1, 1, 5 )
data2:tuple = ( 3, 2 )
data3:tuple = ( 5, 0, 3 )

print( data1 > data2 )
print( 1 > 0 )
print( 1 > 2 )

print( data1 > data3 )



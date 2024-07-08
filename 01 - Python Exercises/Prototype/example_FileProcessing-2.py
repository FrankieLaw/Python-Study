test = open( "ProductName.txt", "r" )
dictionary = { }

while True:
    result = test.readline( )
    result = result.split( "\n" )[0]

    if( result == '' ):
        print( "End of File" )
        break

    else:
        if( dictionary.get( result ) ):
            dictionary[result] = int(dictionary[result]) + 1
        else:
            dictionary[result] = 1
test.close( )



check = open( "checker.txt", "w" )
total_product:int = 0

for key in dictionary.keys( ):
    total_product = total_product + int(dictionary[key])
    check.writelines( "%s %s\n" %( key, dictionary[key] ) )

check.writelines( "Total Product: %d" %( total_product ) )
print( len(dictionary.keys( ) ) ) 

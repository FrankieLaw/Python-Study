'''
    This is the basic codes to extract text from a CSV file.
    CSV is a "COMMA DELIMITED" file.

    The output you get from this file an array of values:
        ['Hello,World\n', '1,A\n', '2,B\n', '3,C\n', '4,D\n', '5,E\n', '6,F\n', '7,G\n', '8,H\n', '9,I\n', '10,J\n']

    Each element is a record (row)
    The column is separated by a comma delimiter.

    To visualize the above array in table format.
    'Hello,World\n'  would be the heading

        Hello   World
        1       A
        2       B
        3       C
        4       D
        5       E
        6       F
        7       G
        8       H
        9       I
        10      J
'''
filePtr = open( "Prototype/TextSamples/Book1.csv", "r" )

myRecord = filePtr.readlines( )

print( f"ColumnA\t\tColumnB")

for values in myRecord:
    rowData = values.split( "," )
    rowData[1] = rowData[1].replace( "\n", "" )
    
    print( "%s\t\t%s" %(rowData[0], rowData[1]) )
    #print( f"{rowData[0]}\t\t{rowData[1]}" )

filePtr.close( )

import glob

listOfFilesPtr = glob.glob( "Prototype/TextSamples/*.csv" )

for path in listOfFilesPtr:
    file = open( path, "r" )
    myRecords = file.readlines( )

    print( myRecords )


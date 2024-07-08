'''
    This is the basic codes to write text to files.
    By default (Based on my observation) the place where the file will be created
    is located at the root of the project folder (Python Projects).

    To create the text file in another location, specify the absolute path
    starting at [Python Projects]
'''
filePtr = open( "Prototype/Book1.txt", "w" )

filePtr.write( "Hello World" )

filePtr.close( )
import os
import sys

mydir = os.path.join( os.path.dirname( sys.argv[0]), "Resources" )
myFile = os.path.join( mydir, "test.txt" )

print( mydir )
print( myFile )

os.makedirs( "prototype/resources" )

f = open( "prototype/resources/test.cvs", "w" )
f.write( "Hey Ashley, hey Ivan :D" )
f.close( )
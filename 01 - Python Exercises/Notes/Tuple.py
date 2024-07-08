from typing import Tuple

tupleSample:Tuple[int, str] = ( 1, "Hello" )

def get_tuple( ) -> Tuple[ int, str ]:
    return ( 2, "world" )

numbers:Tuple[ int, ... ] = ( 1, 2, 3, 4, 5 )

tupleSample = ( {'name':"Frankie", 'lastName':"law"}, (), [] )

for x in tupleSample:
    print( type( x ) )

for x in range( len( tupleSample ) ):
    print( tupleSample[x] )

for index, element in enumerate( tupleSample ):
    print( index, element )



tupleSample2 = ( {}, [1, 2, 3, 4, 5, 6] )
print( f"List in Tuple: {tupleSample2[1][3]}" )



# Unpacking Sequences
student_tuple = ( 'Amanda', [98, 85, 87] )
first_name, grades = student_tuple
print( f"{first_name} | {grades}")


sampleString = "hi"
char1, char2 = sampleString
print( f"{char1} | {char2}" )


#swapping values
a = 10
b = 20

a, b = (b, a)
print( f"{a} | {b}")


# Enumerator
# Enumerator turns a list by create an index association to be iterate.
sampleList = [ "Frankie", "Law", "Cool" ]
for k, v in enumerate( sampleList ):
    print( f"{k} | {v}")



#Slice Sequence
x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print( x[:])            # print everything
print( x[2:6] )         # index 2 to 6
print( x[:6])           # Default starts at 0
print( x[6:])           # index 6 till the end
print( x[4:len(x)])     # index 4 till the end
print( x[::2])          # Iterate every other element
print( x[::-1])         # Iterate backwards

x[0:3] = [ 11, 12, 13 ]     # Reassign element 0 - 3 with a new list values
print( x ) 

x[0:3] = []                 # Deletes 3 elements
print( x )



print( "\n\nSample Integer2")
sampleInt2 = [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 ]
print( sampleInt2 )

# del sampleInt2[ 4 ]
# print( sampleInt2 )     # 10 is missing

# del sampleInt2[ 0:3 ]   # the first 3 element is gone
# print( sampleInt2 )

# del sampleInt2[-1]      # Delete last element
# print( sampleInt2 )

del sampleInt2[::2]     # Delete every other ones
print( sampleInt2 )

del sampleInt2[:]       # Delete all elements
print( sampleInt2 )

del sampleInt2          # Delete from memory
#print( sampleInt2 )    # This will cause an error



# Pass by Reference
print( "\n\nPass by Reference")
def modify_list( x ):
    x[0] = 100

a = 10
b = [10, 20, 30, 40]

print( b )
modify_list( b )
print( b )

#Initialize List from Range
print( "\n\nInit Range" )
sampleInit = list( range( 0, 15 ) )
print( sampleInit )

'''
    tuple is immutable
    1/ Concatenate tuples
    2/ Change to list and turn it back to tuple
'''

from typing import List


def listFactory( min:int, max:int ):
    result:List[int] = []
    for x in range( min, max + 1 ):
        result += [x]

    return result
        
    
myList:List[int] =  listFactory( 1, 15 )
print( myList )

del myList[0:4]
print( myList )

del myList[::2]
print( myList )


# List Object Methods
from datetime import datetime
import random

random.seed( datetime.now( ).timestamp( ) )

def scramble( unsortedList:List[int] ) -> None:
    for _ in range( 100 ):
        index1 = random.randrange( 0, len(unsortedList) )
        index2 = random.randrange( 0, len(unsortedList) )

        unsortedList[index1], unsortedList[index2] = (unsortedList[index2], unsortedList[index1])

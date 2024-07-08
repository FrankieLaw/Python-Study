# Self Check - 5.2 Q3
'''
    Create a function cube_list that cubes each element of a list.
    Call the function with the list numbers containing 1 through 10.
    Show numbers after the call.
'''
from typing import List

def cube_list( values:List[int] ):
    for x in range( len( values ) ):
        values[x] **= 3


# ==================================
#  MAIN
# ==================================
x:List[int] = [ 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ]
print( x )

cube_list( x )
print( x )
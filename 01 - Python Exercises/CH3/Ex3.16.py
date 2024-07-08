#Ex3.16.py
"""
    Find the largest of 2 numbers
"""


numbers:list = [ 23, 44, 1, 20, 84, 23, 56, 88, 32, 11, 34, 29, 50, 39, 13, 54, 98, 12, 34, 56, 55, 44 ]
largest_1:int  = numbers[0]
largest_2:int  = numbers[0]


for x in numbers:
    if( x > largest_1 ):
        largest_2 = largest_1
        largest_1 = x
        
print( f'First Largest: {largest_1:>}' )
print( f'Second Largest: {largest_2}' )

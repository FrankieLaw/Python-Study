'''
    Question 2.23
    
    (Largest and Smallest Integers) Write a program that reads in five integers and determines
    and prints the largest and the smallest integers in the group. Use only the programming techniques
    you learned in this chapter.
'''

a, b, c, d, e = input( "Enter 5 integers: " ).split( )

a = int( a )
b = int( b )
c = int( c )
d = int( d )
e = int( e )

largest = a
if( b > largest ):
    largest = b
if( c > largest ):
    largest = c
if( d > largest ):
    largest = d
if( e > largest ):
    largest = e

smallest = a
if( b < smallest ):
    smallest = b
if( c < smallest ):
    smallest = c
if( d < smallest ):
    smallest = d
if( e < smallest ):
    smallest = e

print( "Largest: %d" %( largest ) )
print( "Smallest: %d" %( smallest ) )

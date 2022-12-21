'''
    Question 2.25
    
    (Multiples) Write a program that reads in two integers and determines and prints if the first
    is a multiple of the second. [Hint: Use the modulus operator.]
'''

a, b = input( "Enter two integers: " ).split( )
a = int( a )
b = int( b )

if( a % b == 0 ):
    print( "%d is multiple of %d" %(a, b) )

if( a % b != 0 ):
    print( "%d is not multiple of %d" %(a, b) )

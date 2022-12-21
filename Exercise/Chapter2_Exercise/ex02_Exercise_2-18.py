'''
    Question 2.18
    
    (Comparing Integers) Write a program that asks the user to enter two integers, obtains the
    numbers from the user, then prints the larger number followed by the words "is larger." If the
    numbers are equal, print the message "These numbers are equal."
'''

a:int = 0
b:int = 0

a, b = input( "Enter two integer for comparison: " ).split( )

a = int(a)
b = int(b)

if( a > b ):
    print( "%d is larger than %d" %(a, b) )

if( b > a ):
    print( "%d is larger than %d" %(b, a) )

if( a == b ):
    print( "These numbers are equal" )
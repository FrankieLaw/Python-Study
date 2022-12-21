'''
    Question 2.16
    
    (Arithmetic) Write a program that asks the user to enter two numbers, obtains the two
    numbers from the user and prints the sum, product, difference, and quotient of the two numbers.
'''

a:int = 0
b:int = 0

a, b = input( "Enter two integers: " ).split( )

print( "Sum is %d" %( int(a) + int(b) ) )
print( "Difference is %d" %( int(a) - int(b) ) )
print( "Product is %d" %( int(a) * int(b) ) )

if( int(b) != 0 ):
    print( "Quotient is %d" %( int(a) / int(b) ) )

if( int(b) == 0 ):
    print( "Cannot Divide by Zero" )


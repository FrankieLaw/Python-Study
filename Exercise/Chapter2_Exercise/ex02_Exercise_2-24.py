'''
    Question 2.24
    
    (Odd or Even) Write a program that reads an integer and determines and prints whether
    it's odd or even. [Hint: Use the modulus operator. An even number is a multiple of two. Any multiple
    of two leaves a remainder of zero when divided by 2.]
'''

a = int( input( "Enter an integer:" ) )

if( a % 2 == 0 ):
    print( "Even" )
    
if( a % 2 != 0 ):
    print( "Odd" )

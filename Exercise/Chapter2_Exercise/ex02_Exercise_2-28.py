'''
    Question 2.28
    
    (Digits of an Integer) Write a program that inputs a five-digit integer, separates the integer
    into its digits and prints them separated by three spaces each. [Hint: Use the integer division and
    modulus operators.] For example, if the user types in 42339, the program should print: 4 2 3 3 9
'''

a:int = 0
b:int = 0
c:int = 0
d:int = 0
e:int = 0

a = int( input( "Enter a 5 digit number: " ) )

# 5th Digit
e = a % 10
a = a / 10

# 4th Digit
d = a % 10
a = a / 10

# 3th Digit
c = a % 10
a = a / 10

# 2th Digit
b = a % 10
a = a / 10

print( "%d   %d   %d   %d   %d" %(a, b, c, d, e) )
''' ====================================================================
    Question 2.4
    
    Write a statement (or comment) to accomplish each of the following (assume that using
    directives have been used for cin, cout and endl):
    
    a) State that a program calculates the product of three integers.
    b) Declare the variables x, y, z and result to be of type int (in separate statements).
    c) Prompt the user to enter three integers.
    d) Read three integers from the keyboard and store them in the variables x, y and z.
    e) Compute the product of the three integers contained in variables x, y and z, and assign
    the result to the variable result.
    f) Print "The product is " followed by the value of the variable result.
    g) Return a value from main indicating that the program terminated successfully.
==================================================================== '''

# This program calculates the product of three integers.
x:int = 0
y:int = 0
z:int = 0
result:int = 0

x, y, z = input( "Enter 3 integers: " ).split( )

result = int(x) * int(y) * int(z)

print( "The product is %d\n" %result )
'''
    Question 2.9

    Write a single statement or line that accomplishes each of the following:
        a) Print the message "Enter two numbers".
        b) Assign the product of variables b and c to variable a.
        c) State that a program performs a payroll calculation (i.e., use text that helps to document
        a program).
        d) Input three integer values from the keyboard into integer variables a, b and c.
'''

print( "Enter two numbers: " )

a:int = 0
b:int = 0
c:int = 0
a = b * c

#This program performs a payroll calculation

a, b, c = input( "Enter three numbers: " ).split( )
print( a, b, c )

# Fig. 2.13: fig02_13.cpp
# Comparing integers using if statements, relational operators
# and equality operators.


number1:int     # first integer to compare
number2:int     # second integer to compare

# ===========================================================
#  WHY THIS WORKS
# ===========================================================
#  The input prompts the user for two integers.
#
#  When the user enters the value, they are a string "2 3"
#
#  A string of "2 3" cannot be assigned to number1 and
#  number2 because the variables is declared using 
#  Parallel Assignment.
#
#  Since the input is a string "2 3", we can use string
#  object function to parse the information so that it can be
#  unpack and inserted into the Parallel Assignment.
#
#  The split function splits the string 2 3 using the space
#  delimiter, turning the string 2 3 to a list ["2", "3"]
#
#  Python will then automatically unpack the list into their
#  respective variable location.
number1, number2 = input( "Enter two integers to compare: " ).split( )

if number1 == number2:
    print( "%s == %s" %(number1, number2) )

if number1 != number2:
    print( "%s != %s" %(number1, number2) )

if number1 < number2:
    print( "%s < %s" %(number1, number2) )

if number1 > number2:
    print( "%s > %s" %(number1, number2) )

if number1 <= number2:
    print( "%s <= %s" %(number1, number2) )

if number1 >= number2:
    print( "%s >= %s" %(number1, number2) )
# Fig. 2.5: fig02_05.cpp
# Addition program that displays the sum of two integers.

# MAIN ==================================
# function main begins program execution
# =======================================

# variable declarations
number1:int;                # first integer to add
number2:int;                # second integer to add
sum:int;                    # sum of number1 and number2

number1 = input( "Enter first integer: " )      # prompt user for data
                                                # read first integer from user into number1

number2 = input( "Enter second integer: " )     # prompt user for data
                                                # read second integer from user into number2

sum = int(number1) + int(number2)               # add the numbers; store result in sum


print( "Sum is %d\n" %sum )                     # display sum
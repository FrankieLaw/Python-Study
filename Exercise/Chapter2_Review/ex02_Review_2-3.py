# ex02_Review.cpp
# Chapter 2 review coding questions

# Write a single C++ statement to accomplish each of the following (assume that using directives
# have not been used):
#   a) Declare the variables c, thisIsAVariable, q76354 and number to be of type int.
#   b) Prompt the user to enter an integer. End your prompting message with a colon (:) followed
#       by a space and leave the cursor positioned after the space.
#   c) Read an integer from the user at the keyboard and store it in integer variable age.
#   d) If the variable number is not equal to 7, print "The variable number is not equal to 7".
#   e) Print the message "This is a C++ program" on one line.
#   f) Print the message "This is a C++ program" on two lines. End the first line with C++.
#   g) Print the message "This is a C++ program" with each word on a separate line.
#   h) Print the message "This is a C++ program". Separate each word from the next by a tab.

c:int = 0
thisIsAVariable:int = 0
q76354:int = 0
number:int = 0

number = input( "Enter an integer: " )

if int(number) != 7:
    print( "The variable number is not equal to 7\n" )

print( "This is a C++ Program" )

print( "This is a C++\nProgram" )

print( "This\nis\na\nC++\nProgram" )

print( "This\tis\ta\tC++\tProgram" )


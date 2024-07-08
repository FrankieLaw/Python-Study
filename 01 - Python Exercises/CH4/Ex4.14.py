# Ex4.14.py
# (Computer Assisted Instruction)

"""
    Write a script to help an elementary school student learn multiplication.
    Create a function that randomly generates and returns a tuple of two positive integers.
    Use that function's result in your script to prompt the user with a question, such as
        How much is 6 times 7?

    For a correct answer, display the message "Very good!" and ask another multiplication question.
    For an incorrect answer, display the message "No.  Please try again." and let the student
    try the same question repeatedly until the student finally gets it right.
"""

import random
from datetime import datetime

random.seed( datetime.now( ).timestamp( ) )

def generateQuestion( ):
    return ( random.randrange( 1, 9 ), random.randrange( 1, 9 ) )


# ==========================================
#  Main
# ==========================================
while True:
    randNum = generateQuestion( )
    result  = randNum[0] * randNum[1]
    resultflag = False

    
    print( "\n================================" )
    print( " Multiplication Exercies" )
    print( "================================" )
    print( f"How much is {randNum[0]} times {randNum[1]}? " )
    
    while resultflag == False:
        answer = int( input( ">> " ) )

        if( answer == result ):
            print( "Very good!\n" )
            resultflag = True
        else:
            print( "Try again!\n" )

    print( )
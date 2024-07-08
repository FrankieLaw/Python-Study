# Ex4.15.py
# (Computer Assisted Instruction: Reducing Student Fatigue)
# Modify Ex4.14 to display various comments
# For correct answers - Possibly say
#   "Very Good!"
#   "Nice Work!"
#   "Keep up the good work!"
# For incorrect answers - Possibly say
#   "No. Please try again"
#   "Wrong. Try once more"
#   "No. Keey trying"

import random
from typing import List
from datetime import datetime

random.seed( datetime.now( ).timestamp( ) )

def generateQuestion( ):
    return ( random.randrange( 1, 9 ), random.randrange( 1, 9 ) )


# ==========================================
#  Main
# ==========================================
while True:
    randNum:tuple = generateQuestion( )
    result  = randNum[0] * randNum[1]
    resultflag = False

    correctResponse:List[str] = [ "Very Good!", "Nice Work!", "Keep up the good work!" ]
    wrongResponse:List[str] = [ "No. Please Try Again", "Wrong. Try Once More", "No. Keey Trying" ]

    
    print( "\n================================" )
    print( " Multiplication Exercies" )
    print( "================================" )
    print( f"How much is {randNum[0]} times {randNum[1]}? " )
    
    while resultflag == False:
        answer = int( input( ">> " ) )
        n = random.randrange( 0, 3 )

        if( answer == result ):
            print( correctResponse[n] )
            resultflag = True
        else:
            print( wrongResponse[n] )
            print( "Try again!\n" )

    print( )
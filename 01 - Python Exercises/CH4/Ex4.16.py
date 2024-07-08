# Ex4.16.py
# (Computer-Assisted Instruction: Difficultyu Levels)
'''
    Modify the previous exercise to allow the user to enter a difficulty level. 
    At a difficulty level of 1, the program should use only single-digit numbers 
    in the problems and at a difficulty level 2, numbers as large as two digits.
'''

import random
import os
from typing import List
from datetime import datetime

random.seed( datetime.now( ).timestamp( ) )

def level1Qestion( ):
    return ( random.randrange( 1, 9 ), random.randrange( 1, 9 ) )

def level2Question( ):
    return ( random.randrange( 10, 100 ), random.randrange( 10, 100 ) )


def clear_screen( ):   
    if os.name == 'nt':      # For Windows
        os.system('cls')
    else:                    # For Unix/Linux/Mac
        os.system('clear')


# ==========================================
#  Main
# ==========================================
userChoice:str = ""
correctResponse:List[str] = [ "Very Good!", "Nice Work!", "Keep up the good work!" ]
wrongResponse:List[str] = [ "No. Please Try Again", "Wrong. Try Once More", "No. Keey Trying" ]

while not( userChoice in ( "1", "2" ) ):
    os.system( 'cls' )
    print( "==================================" )
    print( " Math Quest Tutor " )
    print( "==================================\n" )

    print( "Please select a difficulty" )
    print( "1 - Level 1" )
    print( "2 - Level 2\n" )

    print( ">> " , end="" )
    userChoice = input( )

    if( not( userChoice in ( "1", "2" ) ) ):
        print( "Invalid Choice, please choose either 1 or 2 - Press Any Key to Continue..." )
        input( )



stats_Questions = 0

while True:
    os.system( 'cls' )    

    if( userChoice == "1" ):
        randNum:tuple = level1Qestion( )
    elif( userChoice == "2" ):
        randNum:tuple = level2Question( )

    result  = randNum[0] * randNum[1]
    resultflag = False

    
    print( "===================================" )
    print( f" Level {userChoice} - Multiplication Exercise " )
    print( "===================================" )
    print( f"Question {stats_Questions + 1}: How much is {randNum[0]} times {randNum[1]}? " )
    
    while resultflag == False:
        answer = int( input( ">> " ) )
        n = random.randrange( 0, 3 )

        if( answer == result ):
            print( correctResponse[n] )
            stats_Questions += 1
            resultflag = True
        else:
            print( wrongResponse[n] )
        print( )

    if( stats_Questions == 10 ):
        print( "Amazing! This is the end of the program, see ya!\n\n" )
        break
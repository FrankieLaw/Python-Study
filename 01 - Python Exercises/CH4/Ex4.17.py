# Ex4.17.py
# (Computer-Assisted Instruction: Varying the Types of Problems)
'''
    Modify the previous exercise to allow the user to pick a type of arithmetic problem to study
    1 - Addition Only
    2 - Subtraction Only
    3 - Multiplication Only
    4 - Division Only
    5 - Random Mix
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
userPracticeChoice:str = ""

correctResponse:List[str] = [ "Very Good!", "Nice Work!", "Keep up the good work!" ]
wrongResponse:List[str]   = [ "No. Please Try Again", "Wrong. Try Once More", "No. Keey Trying" ]
topicList:List[str]       = [ "Addition", "Subtraction", "Multiplication", "Division", "Mixed" ]


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


while not( userPracticeChoice in ( "1", "2", "3", "4", "5" ) ):
    os.system( 'cls' )
    print( "==================================" )
    print( " Arithmetic Practice Menu " )
    print( "==================================\n" )

    print( "Select a Topic" )
    print( "1 - Addition" )
    print( "2 - Subtraction" )
    print( "3 - Multiplication" )
    print( "4 - Division" )
    print( "5 - All of the Above" )

    print( ">> " , end="" )
    userPracticeChoice = input( )

    if( not( userPracticeChoice in ( "1", "2", "3", "4", "5" ) ) ):
        print( "Invalid Choice, please choose either 1 to 5 - Press Any Key to Continue..." )
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
    print( f" Level {userChoice} - {topicList[ int(userPracticeChoice) - 1 ]} Exercise " )
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


    '''
    Addition            Level 1     Level 2
    Subtraction         Level 1     Level 2
    Multiplication      Level 1     Level 2
    Division            Level 1     Level 2
    Mix                 Level 1     Level 2
    '''
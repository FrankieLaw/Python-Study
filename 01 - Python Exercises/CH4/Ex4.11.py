# Ex4.11.py
# (Guess-the-Number Modification)
'''
    Modify the previous exercise to count the number of guesses the player makes.
    If the number is 10 or fewer, display "Either you know the secret or you got lulcky!"
    If the player makes more then 10 guesses, display "You should be able to do better!"
    Why should it take no more than 10 guesses?
'''

import random
from datetime import datetime

# Seed only accepts None, int, float, str, bytes, and bytearray
random.seed( datetime.now( ).timestamp( ) )

victoryFlag = False
again       = "yes"
guesses     = 0

while( again == "yes" ):
    # ====================================
    # Reset Game State
    # ====================================
    victoryFlag = False
    guesses = 0
    secretNum = random.randrange( 1, 1001 )


    # ====================================
    # Run game until player wins
    # ====================================
    while( not victoryFlag ):
        x = input( "Guess my number between 1 to 1000: ")

        if( int(x) < secretNum ):
            print( "Higher")
            guesses += 1

        elif( int(x) > secretNum ):
            print( "Lower" )
            guesses += 1

        elif( int(x) == secretNum ):
            victoryFlag = True
            print( "\nNumber of attempts: ", guesses )

            if( guesses <= 10 ):    
                print( "Either you know the secret or you got lucky!\n" )
            elif( guesses > 10 ):
                print( "You should be able to do better!\n" )

    # ====================================
    # Player wins, prompt to play again
    # ====================================
    while True:
        again = input( "Do you want to play again? (yes/no): " )
    
        if( again == "yes" or again == "no" ):
            break
        else:
            print( "You need to say (Yes or No)" )


# ====================================
#  Player choose No
# ====================================
print( "Have a nice day" )
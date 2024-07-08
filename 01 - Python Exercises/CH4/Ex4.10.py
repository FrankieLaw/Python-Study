# Ex4.10.py
# (Guess the Number)
#
# Write a script that plays "guess the number." Choose the number to be guessed
# by selecting a random integer int he range 1 to 1000.  Do not reveal this
# number to the user.  Display the prompt "Guess my number between 1 to 1000 
# with the fewest guesses:".  The player inputs a first guess.  If the guess
# is incorrect, display "Too high. Try again." or "Too low. Try again." as
# appropriate to help the player "zero in" on the correct answer, then
# prompt the user for the next guess. When the user enters the correct answer,
# display "Congratulations. You guessed the number!", and allow the user to
# choose whether to play again.

# randomly choose a number, 1 to 1000
# Prompt Guess my number between 1 to 1000
# if the guess number is lower than Choosen number, say higher
# if the guess number is higher than Choosen number, say lower
# if the guess number = Choosen number, say "Congratulation"
# Prompt user if they want to play again.

import random
from datetime import datetime

# Seed only accepts None, int, float, str, bytes, and bytearray
random.seed( datetime.now( ).timestamp( ) )

victoryFlag = False
again = "yes"

while( again == "yes" ):
    # ====================================
    # Reset Game State
    # ====================================
    victoryFlag = False
    secretNum = random.randrange( 1, 1001 )


    # ====================================
    # Run game until player wins
    # ====================================
    while( not victoryFlag ):
        x = input( "Guess my number between 1 to 1000: ")

        if( int(x) < secretNum ):
            print( "Higher")
        elif( int(x) > secretNum ):
            print( "Lower" )
        elif( int(x) == secretNum ):
            print( "Congratulation" )
            victoryFlag = True

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
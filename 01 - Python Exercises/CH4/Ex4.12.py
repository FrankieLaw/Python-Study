# Ex4.12.py
# (Simulation: The Tortoise and the Hare)

'''
    In this problem, you'll re-create the classic race of the tortoise and the hare.  You'll use random-number
    generator to develop a simulation of this memorable event.

    Our contenders begin the race at square 1 of 70 squares.  Each square represents a position along the race course.
    The finish line is at square 70.  The first contender to reach or pass quare 70 is rewarded with a pail of fresh
    carrots and lattuce.  The course weaves in way up the side of a slippery mountain, so ocassionally the contenders
    lose ground.

    A click ticks one per second.  With each tick of the clock, your application should adjust the position of the
    animals according to the rules in the table below. Use variables to keep track of the positions of the animals.
    (I.e., position numbers are 1 - 70).  Start each animal at position 1 (the "starting gate").  If an animals slip
    left before square 1, move it back to square 1.

    Animal      Move Type       Percentage of the time          Actual Move
    Tortoise    Fast Plod       50%                             3 squares to the right
                Slip            20%                             6 squares to the left
                Slow Plod       30%                             1 square to the right

    Hare        Sleep           20%                             No move at all
                Big hop         20%                             9 squares to the right
                Big slip        10%                             12 squares to the left
                Small hop       30%                             1 square to the right
                Small slip      20%                             2 squares to the left
    
    Create two functions that generate the percentages in the table for the tortoise and the hare, 
    respectively, by producing a random integer 7 in the range 1 <= i <= 10. In the function for the 
    tortoise, perform a “fast plod” when 1 <= i <= 5, a “slip” when 6 <= i <= 7 or a "slow plod” 
    when 8 <= i <= 10, Use a similar technique in the function for the hare.
    
    Begin the race by displaying 
        BANG !!!!
        AND THEY'RE OFF !!!!

    Then, for each tick of the clock (i.e., each iteration of a loop), display a 70-position 
    line showing the letter "T" in the position of the tortoise and the letter "H" in the position of the hare. 
    
    Occasionally, the contenders will land on the same square. In this case, the tor-toise bites the hare, 
    and your application should display "OUCH!!!" at that position. All Positions other than the "T", the "H" 
    or the "OUCH!!!" (in case of a tie) should be blank. 
    
    After each line is displayed, test for whether either animal has reached or passed square 70, If so, 
    display the winner and terminate the simulation, If the tortoise wins, dis-play TORTOISE WINS!!! YAY!!! 
    If the hare wins, display Hare wins. Yuch. If both animals win on the same tick of the clock, you may 
    want to favor the tortoise (the “underdog”), or you may want to display "It's a tie". 
    
    If neither animal wins, perform the loop again to simulate the next tick of the clock. 
    When you're ready to run your application, assemble a group of fans to watch the race.

    You'll be amazed at how involved your audience gets!
'''

import random
import time
from datetime import datetime


# Seed only accepts None, int, float, str, bytes, and bytearray
random.seed( datetime.now( ).timestamp( ) )



# ===========================================
#  Global Variables
# ===========================================
tPos = 1                # Tortorise Position
hPos = 1                # Hare Position

raceline = 70           # Total Race Line


# ===========================================
#  Function Definition
# ===========================================
def showContenderPosition( whosePos:int, symbol:str ) -> None:
    result = ""
    for x in range( 1, raceline + 1 ):
        if( x < whosePos ):
            result += "*"

        elif( x == whosePos ):
            result += symbol
            
        else:
            result += " " 
        
    print( result )


# ===========================================
#  Function Definition - tortoiseMove
# ===========================================
def tortoiseMove( ) -> int:
    """
        Tortoise    Fast Plod       50%     3 squares to the right
                    Slip            20%     6 squares to the left
                    Slow Plod       30%     1 square to the right
    """
    result = random.randrange( 1, 11 )

    if( result >= 1 and result <= 5 ):
        return 3
    
    if( result >= 6 and result <= 7 ):
        return -6
    
    if( result >= 8 and result <= 10 ):
        return 1


# ===========================================
#  Function Definition - hareMove
# ===========================================
def hareMove( ) -> int:
    """
        Hare        Sleep           20%         No move at all
                    Big hop         20%         9 squares to the right
                    Big slip        10%         12 squares to the left
                    Small hop       30%         1 square to the right
                    Small slip      20%         2 squares to the left
    """
    result = random.randrange( 1, 11 )

    if( result >= 1 and result <= 2 ):
        return 0
    
    if( result >= 3 and result <= 4 ):
        return 9
    
    if( result == 5 ):
        return -12
    
    if( result >= 5 and result <= 8 ):
        return 1
    
    if( result >= 9 and result <= 10 ):
        return -2
    


print( "\n\n============================")
print( " BANG !!!!" )
print( " AND THEY'RE OFF !!!!" )
print( "============================\n\n")

while True:
    # Print Race Status for Tortorise
    showContenderPosition( tPos, "T" )
    showContenderPosition( hPos, "H" )
    print( "\n" )

    startTime = time.time( )

    # Random Generate Result for Tortoise
    tPos += tortoiseMove( )
    if( tPos < 1 ): tPos = 1
    if( tPos > 70 ): tPos = 70

    # Random Generate Result for Hare
    hPos += hareMove( )
    if( hPos < 1 ): hPos = 1
    if( hPos > 70 ): hPos = 70


    endTime = time.time( )
    waitTime = 1000 - ( endTime - startTime ) * 1000 
    time.sleep( 1 )

    if( not( tPos >= raceline or hPos >= raceline ) ):
        print( "The race continues!!" )
    else:
        print( "And the race is over!!" )

        if( tPos >= 70 ):
            print( "The winner is Tortoise!!" )
        elif( hPos >= 70 ):
            print( "The winner is the Hare!!" )
        elif( tPos >= 70 and hPos >= 70 ):
            print( "It is a tie!! But people like the Tortoise more!" )

        break
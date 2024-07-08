# MOM, NOON, racecaracecar, 123454321  WORK
# 98465454, frankie, law, correlation one

# Commonalities
# It must read forward and backwards
# Even number characters, or Odd number of characters.
#       MOM = 3             M == M      O
#       NOON = 4            N == N      O == O
#       MOM I need to test the character once     M
#       NOON I need to test the characters twice  N O

# MOM               ( 3 - 1 ) / 2  = 2 / 2 =         1
# NOON              ( 4 - 0 ) / 2  =                 2
# racecaracecar     ( 13 - 1 ) / 2 = 12 / 2          6
# 123454321         ( 9 - 1 ) / 2  =                 4

# 0 1 2 3 
# N O O N

# print( f"{word[front]} == {word[back]}")
# print( "Match")


# =========================================
# Variables
# =========================================
word = "999999999999999"
isMiddle = len( word ) % 2      # Give me 1 or 0
numberOfTest = ( len( word ) - isMiddle ) / 2

front = 0
back = len( word ) - 1
resultFlag = True

# =========================================
# MAIN
# =========================================
print( "\n\n" )
for _ in range( int( numberOfTest ) ):
    if( word[front] == word[back] ):
        front = front + 1
        back  = back - 1
    else:
        resultFlag = False
        break

if resultFlag == True:
    print( f"The word {word} Is a palindrome" )
else:
    print( f"The word {word} Is not a palindrome" )



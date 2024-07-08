# Ex3.12.py
"""
    Palindromes
"""

print('\n\n')

# ====================================
#  Program Variables
# ====================================
userInput: int = int( input( "Enter any digit number: " ) )      # unaltered User Input
copyInput = userInput;                                          # working copy of User Input

digits:int = len( str( userInput ) )                            # Determine how many digits the input have
lExt:int   = 10 ** ( digits - 1 )                               # Maximum Digit Extraction Value

palindromeFlag:bool = True;                                     # Signal Flag if left & right digit don't match



# ====================================
#  Find how many Repetition it needs
#  Regardless of Odd or Even input
# ====================================
repetition:int = 0;
if( digits % 2 == 0 ):
    repetition = digits // 2 
else:
    repetition = ( digits - 1 ) // 2


# ====================================
#  Find the first non equal digit
# ====================================
for _ in range( repetition ):
    lSide = copyInput // lExt       # Extract left side
    rSide = copyInput % 10          # Extract right side

    if( lSide != rSide ):           # Decide early if it is palindrome
        palindromeFlag = False;
        break;

    copyInput %= lExt
    copyInput //= 10

    lExt = int( lExt / 100 )        # Lower extraction value by 100


# ====================================
#  Display final results
# ====================================
print( f'The number {userInput} is {"" if palindromeFlag else "not"} a palindrome' )
print( '\n\n' );
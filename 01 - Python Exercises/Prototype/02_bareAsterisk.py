'''
Parameter is the definition listed on the function.
Argument is the real value listed when the function is called.

The Bare Asterisk paramater that preceeds another parameter enforces coders
to provide a "named" argument.

For more explanation:
    https://stackoverflow.com/questions/2965271/forced-naming-of-parameters-in-python/14298976#14298976
'''

# The 1st parameter enforces the 2nd parameter.
def cool( *, a:int ):
    print( a )


# The Bare Asterisk enforces the coder to provided
# a named variable and value.
cool( a=10 )

# I cannot simply type 10 as a parameter, it will generate an error
# TypeError: cool() takes 0 positional arguments but 1 was given
# cool( 10 )
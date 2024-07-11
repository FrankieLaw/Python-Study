# ==============================================
#  How Mapping Works
# ==============================================
def double( x ):
    return x * 2

numbers = [ 1, 2, 3, 4, 5 ]
doubled_numbers = map( double, numbers )

print( list( doubled_numbers ) )
# Ex4.13.py
# (Arbitrary Argument List)

"""
    Calculate the product of a series of integers that are passed to the function product,
    which receives an arbitrary argument list. Test your function with several calls, each
    with a different number of arguments.
"""

def product( *args:int ) -> int:
    result:int = 1

    for x in args:
        result *= x

    return result


def division( **kwargs ) -> float:
    return kwargs['num'] / kwargs['dem']

print( division( num=10, dem=10 ) )
print( product( 1, 2, 3, 4, 5.15, 18.2 ) )

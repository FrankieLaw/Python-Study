# Ex3.21.py
"""
    Break down dollar to coins
"""

from decimal import Decimal

print( "\n\n" )
amount:Decimal = Decimal( input( 'Enter a floating amount: ' ) )

denom:dict = {
    "quarter" : Decimal( '0.25' ),
    "dime"    : Decimal( '0.10' ),
    "nickel"  : Decimal( '0.05' ),
    "penny"   : Decimal( '0.01' )
}

changes:dict = {}

for key, value in denom.items( ):
    _count:float = amount // value

    amount -= _count * value

    changes[ key ] = _count


for _c, _v in changes.items( ):
    print( f'{_c:>10} : {_v:>7}' )
# Ex3.14.py
"""
    Approximating the Mathmetical constant Pie

    pie = 4 - 4/3 + 4/5
"""

flag:bool = False       # False use subtraction, True use addition
d:int     = 1           # The denominator use for division

pie:float = 0           # Pie constant


for x in range( 50000 ):
    if( flag ):
        pie -= ( 4 / d )
    else:
        pie += ( 4 / d )

    print( f'{pie} {"-" if flag else "+"}= 4 / {d}' )
    flag = not flag
    d   += 2
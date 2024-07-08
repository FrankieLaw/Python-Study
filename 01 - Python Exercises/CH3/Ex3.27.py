# Ex3.27.py
""" World Population Growth Calculator
"""

import math

rate:float      = 0.059           # 5.9%
population:int  = 7888000000      # 7.888 Billion
originalPop:int = population

# Question #1: Growth over the next 100 years
# Question #2: When will it double
# Question #3: When will it quaduple

# Column 1 - Year
# Column 2 - Population End-Of-Year
# Column 3 - Changes

thisYear:int = 2023

print( '--------------------------------------------------' )
print( f'|{"YEAR":^6}|{"Population EoY":^22}|{"Changes":^18}|')
print( '--------------------------------------------------' )

for x in range( 1, 101 ):
    changes = population * rate
    population *= 1 + rate
    
    fchanges    = '{:,.0f}'.format( changes )
    fPopulation = '{:,.0f}'.format( population )

    print( f'|{thisYear + x:^6}|{fPopulation:^22}|{fchanges:^18}|' )


double:float = math.log10( 2 ) / math.log10( 1 + rate )
quad:float   = math.log10( 4 ) / math.log10( 1 + rate )

print( '\n' )
print( f'The world population will double in {double:.2f} years')
print( f'{"Original Population: ":>25}{"{:,.0f}".format( originalPop ):<20}')
print( f'{"New Population: ":>25}{"{:,.0f}".format( originalPop * ( 1 + rate ) ** double ):<20}')
print( '\n' )

print( f'The world population will double in {quad:.2f} years')
print( f'{"Original Population: ":>25}{"{:,.0f}".format( originalPop ):<20}')
print( f'{"New Population: ":>25}{"{:,.0f}".format( originalPop * ( 1 + rate ) ** quad ):<20}')
print( '\n' )
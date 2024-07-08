# Ex4.7.py
# Using DateTime Module

import datetime


# print( datetime.MAXYEAR )
# print( datetime.MINYEAR )
# print( datetime.UTC )
# print( datetime.__package__ )
# print( datetime.__name__ )
# print( datetime.date )
# print( datetime.sys )
# print( datetime.time )
# print( datetime.timezone )

# Magic Method, Special Method or Dunder Method (Double Underscore Method)
# The double underscore identifier __name__ is built-in variable

def classify( name, obj ):
    print( f'{name:<25}{str( type( obj ) ):<60}{callable( obj )}' )


def date_and_time( ):
    print( datetime.datetime.today( ) )


# =========================================
#  Main
# =========================================
date_and_time( )

print( "\n\n" )
for x in dir( datetime ):
    print( x )

print( "\n\n" )
print( f'{"Member Name":<25}{"Type":<60}{"Callable"}' )
for x in dir( datetime ):
    classify( x, getattr( datetime, x ) )
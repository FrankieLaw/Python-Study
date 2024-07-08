# Ex3.28.py
""" Calculate Mean, Median, Mode
"""

import statistics

value:list = [ 9, 11, 22, 34, 17, 22, 34, 22, 40 ]

print( "\n" )
print( f'Mean:\t{statistics.mean( value ):.2f}')
print( f'Median:\t{statistics.median( value ):.2f}')
print( f'Mode:\t{statistics.mode( value ):.2f}')
print( "\n" )

# Issues with have another value 34 in the list
# It would create a bimodal with 2 values with the same frequency


newList:list [ 1, 1, 1, 2, 2, 2 ]
# Issue #1: Suppose all the values in a list are whole number.
#           Given a list with oven number of elements within a list would create issue
#           of Median value being rounded, because of average taken in the middle value



sampleList:list [ 1, 1, 1, 2, 2, 2, 23 ]
# Which one of the measurement of central tendency would be most affected by outliers
# Mean - The average caused by the outlier would significantly skew in favor of the larger number
#        Mean would be most affected because the average itself appear to be an outlier on its own.

# Median - The middle number is significantly out of range than the outlier
#          This isn't being affected much since all the value are to be sorted and picked the middle number out.
#          Even if the outlier exist, it would only shift the Median value by a small margin

# Mode - It doesn't affect mode as much, since most frequency is taken into consideration
#        Mode is the least affected considering the frequency of outlier would significantly lower than legitimate response.

# CH2-Ex2.14.py
"""
    Target Heart-Rate Calculator
    Maximum Heart Rate = Beats / Minute = 220 - Age
    Target heart rate = 50-85% of maximum heart rate
"""

print( '\n\n' )

# prompt for age
age:int = int( input( 'Enter your age: ' ) )

# Maximum Heart Rate
mhr:int = 220 - age

# Target Heart Rate
print( f'Your Target Heart Rate is { mhr * 0.50 } to { mhr * 0.85 }' )

print( '\n\n' )
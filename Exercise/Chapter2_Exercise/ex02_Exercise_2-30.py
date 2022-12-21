'''
    Question 2.30
    
    Create a BMI calculator application that reads the user's weight in pounds and height in inches
    (or, if you prefer, the user's weight in kilograms and height in meters), then calculates and displays
    the user's body mass index. Also, the application should display the following information from
    the Department of Health and Human Services/National Institutes of Health so the user can evaluate
    his/her BMI:

    BMI VALUES
    Underweight: less than 18.5
    Normal: between 18.5 and 24.9
    Overweight: between 25 and 29.9
    Obese: 30 or greater
'''
weight:int = 0
height:int = 0
index:int = 0

print( "This program calculates your BMI Value\n" )

print( "BMI VALUES" )
print( "Underweight: less than 18.5" )
print( "Normal: between 18.5 and 24.9" )
print( "Overweight: between 25 and 29.9" )
print( "Obese: 30 or greater" )
print( "\n" )

weight, height = input( "Enter your weight(lbs) and height(inches): " ).split( )
weight = int( weight )
height = int( height )

index = (weight * 703) / (height * height)

if( index < 18.5 ):
    print("You are underweight" )

if( index >= 18.5 ):
    if( index <= 24.9 ):
        print("You are Normal" )

if( index >= 25 ):
    if( index <= 29.9 ) :
        print("You are Overweight" )

if( index >= 30 ):
    print("You are Obses" )
'''
    Question 2.31

    (Car-Pool Savings Calculator) Research several car-pooling websites. Create an application
    that calculates your daily driving cost, so that you can estimate how much money could be saved by
    car pooling, which also has other advantages such as reducing carbon emissions and reducing traffic
    congestion. The application should input the following information and display the user’s cost per
    day of driving to work:

        a) Total miles driven per day.
        b) Cost per gallon of gasoline.
        c) Average miles per gallon.
        d) Parking fees per day.
        e) Tolls per day.
'''

milesPerDay:int = 0
gasCostPerGallon:int = 0
averageMPG:int = 0
parkingFee:int = 0
tolls:int = 0

'''
    The input requires bullet proof checking to dynamically detect the types of input is provided.

    1 - get input first
    2 - determine what type of input it is
    3 - If it is not the correct input
            set a default value of 0
            or generate an error
            or repeat prompt with input hints
    4 - Package this algorithm into personal library
'''
milesPerDay = int( input( "Enter miles drive per day: " ) )
gasCostPerGallon = int( input( "Enter Cost Per Gallon: " ) )

averageMPG = gasCostPerGallon / milesPerDay;

parkingFee = int( input( "Parking Fees?: " ) )
tolls = int( input( "Tolls Paid: " ) )

print("Your Total Saving if you were to car pool: $%d" %( averageMPG + parkingFee + tolls ) )
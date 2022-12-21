'''
    Question 2.19
    
    (Arithmetic, Smallest and Largest) Write a program that inputs three integers from the keyboard
    and prints the sum, average, product, smallest and largest of these numbers.
'''

# get 3 inputs
a:int = 0
b:int = 0
c:int = 0
largest:int = 0
smallest:int = 0

a, b, c = input( "Enter three integers: " ).split( )

a = int(a)
b = int(b)
c = int(c)

print( "Sum: %d" %( a + b + c ) )
print( "Average: %d" %( (a + b + c) / 3 ) )
print( "Product: %d" %( a * b * c ) )


largest = a
if( b > largest ):
    largest = b

    if( c > largest ):
        largest = c

smallest = a
if( b < smallest ):
    smallest = b
    if( c < smallest ):
        smallest = c

print( "Largest: %d" %(largest) )
print( "Smallest: %d" %(smallest) )
'''
About the "self" in Python Object.

It is common knowledge that in Object Oriented Programming
that a CLASS is a blueprint to an object.  As a CLASS, it
is self contain with all of its encapsulated variables
inside of its blueprint.

For a CLASS to function, the CLASS itself needs to be aware
of itself so that information can encapsulate inside and
hides it from the outside world.

In other programming languages there are keywords to reference
itself making a clear distingish from one object to another.
In C/C++, JavaScript, Java all use the keyword "this" in
their self referential code.

In Python, the concept of self is different from other
languages.  It uses a "variable self" rather than a keyword.
Self is a conventional variable used by Python programming
for an object to refer to itself.

Since there are no keyword for self referential referencing.
The "self" variable can be written as any acceptable variable
for instance, this. 
'''

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

cat1 = Cat( "Frankie", 15 )

# THE 2 FUNCTION CALL BELOW IS THE SAME THING
Cat.make_sound( cat1 )
cat1.make_sound( )

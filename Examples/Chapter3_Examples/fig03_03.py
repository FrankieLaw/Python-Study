# Fig. 3.3: fig03_03.py
# Define class GradeBook with a member function that takes a parameter,
# create a GradeBook object and call its displayMessage function.

class GradeBook:
    def displayMessage( self, courseName ):
        print( "Welcome to the grade book for \n" + courseName + "!\n" )

nameOfCourse:str = ""
myGradeBook:GradeBook = GradeBook( )

print( "Please enter the course name: " )
nameOfCourse = input( )
print( )

myGradeBook.displayMessage( nameOfCourse )
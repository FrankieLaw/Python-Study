# Fig. 3.5: fig03_05.cpp
# Define class GradeBook that contains a courseName data member
# and member functions to set and get its value;
# Create and manipulate a GradeBook object with these functions.

class GradeBook:
    def setCourseName( self, name:str ) -> None:
        self.name = name

    def getCourseName( self ) -> str:
        return self.name
    
    def displayMessage( self ) -> None:
        print( "Welcome to the grade book for \n" + self.name + "!\n" )


nameOfCourse:str = ""
myGradeBook = GradeBook( )

print( "Enter a course name: " )
nameOfCourse = input( )
print( )

myGradeBook.setCourseName( nameOfCourse )
myGradeBook.displayMessage( )
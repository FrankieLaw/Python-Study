# Fig. 3.7: fig03_07.cpp
# Instantiating multiple objects of GradeBook class and using
# the GradeBook constructor to specify the course name
# when each GradeBook object is created.

class GradeBook:
    def __init__(self, courseName:str ):
        self.setCourseName( courseName )

    def setCourseName( self, courseName:str ) -> None:
        self.courseName = courseName

    def getCourseName( self ) -> str:
        return self.courseName

    def displayMessage( self ) -> None:
        print( "Welcome to the grade book for \n" + self.getCourseName( ) + "!\n" )


gradeBook1:GradeBook = GradeBook( "Hello World Volumn 1" )
gradeBook2:GradeBook = GradeBook( "Data Analyst for Everything" )

print( "gradeBook1 created for coures: " + gradeBook1.getCourseName( ) )
print( "gradeBook2 created for coures: " + gradeBook2.getCourseName( ) )
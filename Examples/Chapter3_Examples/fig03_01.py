# Fig. 3.1: fig03_01.py
# Define class GradeBook with a member function displayMessage,
# create a GradeBook object, and call its displayMessage function.


# ==========================================
#  GradeBook class definition
# ==========================================
class GradeBook:

    # ==============================================================
    #  This is a member function that is responsible for the
    #  functionality of the class.
    #
    #  Noticed that this member function has "self" as its 
    #  first parameter.
    #
    #  This is there to show Python that this is a member function
    # ==============================================================
    def displayMessage(self):
        print( "Welcome to the Grade Book!" )


# ==========================================
#  funtion main begins program execution
# ==========================================
myBook:GradeBook = GradeBook( )
myBook.displayMessage( )


# Fig. 3.1: fig03_01.py
# Define class GradeBook with a member function displayMessage,
# create a GradeBook object, and call its displayMessage function.


# ==========================================
#  GradeBook class definition
# ==========================================
class GradeBook:

    # ==============================================================
    #  The declaration of variable is not essential
    # ==============================================================
    age:int


    # ==============================================================
    #  This function is python's version of a constructor
    #  Upon creation, this function will be called first.
    #
    #  The 'self' parameter is self referential and is essential
    #  to be listed as the first parameter.
    #
    #  Any subsequent parameter listed is considered additional
    #  information to initialize the starting state of the object.
    #
    #  To set the initialize the variable age.
    #  'self' referential needs to be the object followed by the
    #  variable name that you want to initialize.
    # ==============================================================
    def __init__(self, age):
        self.age = age


    # ==============================================================
    #  This is a member function that is responsible in sharing
    #  private information from the object.
    # ==============================================================
    def displayMessage(self):
        print( "Welcome to the Grade Book! " + str( self.age ) )


# ==========================================
#  funtion main begins program execution
# ==========================================
myBook = GradeBook( 25 )
myBook.displayMessage( )


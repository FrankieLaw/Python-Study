"""
This comment appears when the file is being referenced.

import Chef as myChef
    When I type myChef, the IntelliSense show the comment above.
"""
class Chef:
    def make_chicken(self):
        print( "Made Chicken" )
    
    def make_salad(self):
        print( "Made Salad" )

    def make_special(self):
        print( "Special Dish is here!" )


class HeadChef( ):
    """
    HeadChef, a Chef that cooks head.  Totally yummy.
    """

    def make_tofu(self):
        """
        make_tofu will make you tofu.  So call me.
        """
        print( "Made Tofu" )
'''
    The following line of code declares a variabled 'a' with annotation of [ int | None ]
    This means that variable 'a' accepts Int or None data type.
    
    The assignment operator that comes after is initialization.
    Which means, None value is assigned to variable a.
'''
a:int | None = None
print( type( a ) ) 

# RESULTS ========
#   --> None
# ================
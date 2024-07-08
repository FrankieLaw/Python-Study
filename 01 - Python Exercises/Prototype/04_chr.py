# Refer to OneNote - Career Development ->
#  Python ->
#  API | Built-in Functions
'''
    chr is a built-in function that takes an ascii number and return its character
    equivilent.  ASCII to CHAR
'''
minByte = 13312
maxByte = minByte + 1024

while minByte < maxByte:
    term1 = str(minByte)
    term2 = str(minByte+1)
    term3 = str(minByte+2)
    
    print( "%3s: %1s\t%3s: %1s\t%3s: %1s" %(term1, chr(minByte), term2, chr(minByte+1), term3, chr(minByte+2) ) )

    minByte += 3
setA = { 1, 2, 3, 4, 5 }
setB = { 1, 2, 3, 4 }


print( setA - setB ) # Difference, Element in SetB missing from SetA
print( setA & setB ) # Intersect, Only Elements that are Common
print( setA | setB ) # Union, Everything Unique
print( setA ^ setB ) # Symmetrical Difference, everything that is not common
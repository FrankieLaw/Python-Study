# ==============================================
#  Mapping (List Comprehension)
# ==============================================
test = [ (x, x * 0.0254) for x in [69, 77, 54]]
test2 = list( map( lambda x: ( x, x * 0.0254 ), [69, 77, 54 ] ) )
print( test )
print( test2 )
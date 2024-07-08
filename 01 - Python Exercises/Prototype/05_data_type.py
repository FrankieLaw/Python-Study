a1 = "Hello World"
b1 = 20
c1 = 20.5
d1 = 1j
e1 = [ "apple", "banana", "cherry" ]
f1 = ( "apple", "banana", "cherry" )
g1 = range(0, 6)
h1 = { "name" : "John", "age" : 36 }
i1 = { "apple", "banana", "cherry" }
j1 = frozenset( { "apple", "banana", "cherry" } )
k1 = True
l1 = b"Hello"
m1 = bytearray(5)
n1 = memoryview( bytes(5) )
o1 = None


a = str("Hello World")
b = int( 20 )
c = float( 20.5 )
d = complex( 1j )
e = list( ("apple", "banana", "cherry" ) )  # Mutable
f = tuple( ("apple", "banana", "cherry" ) ) # Immutable
g = range( 6 )
h = dict( name="John", age=36 )
i = set( ("apple", "banana", "cherry" ) )
j = frozenset( ("apple", "banana", "cherry" ) )
k = bool( )
l = bytes( 1 )
m = bytearray( 5 )
n = memoryview( bytes(5) )

print( n )
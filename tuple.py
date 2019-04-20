# tuple is another data type available in python. elements of tuple are always enclosed with in (),
# tuple is immutable, once created elements can not be added or removed

# creating  tuple
demo_tuple = (1,3,"Hello","my_tuple")
print("Contents of tuple")
print(demo_tuple)

# Creating a nested tuple
tuple_nested = ("Apple","Orange",("Apple Juice","Orange Juice"))
print("Contents of nested tuple")
print(tuple_nested)

# a tuple can also be created without () parenthesis this concept is call tuple packing
pack_tuple = "pack","tuple",34,55
print("Contents of tuple created using packing")
print(pack_tuple)

# unpacking tuple
a,b,c,d = pack_tuple
print(a)
print(b)
print(c)
print(d)



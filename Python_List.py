# Python program demonstrating List Data Structure and it's method
# List - A list in python is a ordered collection of heterogeneous elements enclosed within square brackets [].
# Element's in list are in ordered sequence and always indexed with the Zero being the first index.

# Creating a heterogeneous list named "demo"
demo = ['python', 'java', 1, 5, 'system']
# displaying contents of list
print('Printing Initial List')
print(demo)

# Append - add new elements to list.value will be added to end of list always
demo.append(2)
demo.append('Pycharm')
print('List after appending two elements')
print(demo)

# insert - this will also add elements to list. However we cam specify where to add element (i,e index)
demo.insert(0, 'First insert')
print('list after inserting element at 0 index')
print(demo)
demo.insert(4, 'second insert')
print('list after inserting element at 4 index')
print(demo)

# Remove - remove an element form list
demo.remove(5)
print('list after removing 5')
print(demo)

# pop - removes an element based on given index position. If index position is not provided pop works on concepts of
# LIFO.it will remove the last element.

demo.pop(4)
print('list after removing element at index 4')
print(demo)
demo.pop()
print("pop method without index position - removed last element in list 'Pycharm'")
print(demo)

# sort - sorts the values of list in ascending order
demo.remove(2)
demo.remove(1)
demo.sort()
print('Sorted list')
print(demo)

# reverse - reverse the order of the list
demo.reverse()
print('Revered list')
print(demo)

# index - this methods returns the index value of an element present in list
print('Index value of "Java"')
demo.index('java')

# extend - this method add the elements of another list to end of specified list
print('Creating list "demo2"')
demo2 = ['GGN','HYD']
print(demo2)
print('list "demo" after extending it with "demo2"')
demo.extend(demo2)
print(demo)

# copy - this method creates a copy of list
print('copying the values of list demo to variable x')
x = demo.copy()
print(x)

# count - this method will count the number of occurrence
print('Lets count number of "java" in our list "demo"')
y = demo.count('java')
print('Count for "java" is list is ' + str(y))

# clear - this method will make the list empty
demo.clear()
print('List after applying clear method')
print(demo)


"""This is very basic operations in Python using Data Structures and Algorithms(DSA). It includes the operations like Accessing, Inserting, Deleting, Searching and Updating."""

from array import *
array1 = array('i', [10, 20, 30, 40, 50])
for x in array1:
    print(x)

# Accessing Array element
from array import *
array1 = array('i', [10, 20, 30, 40, 50])
print(array1[0])
print(array1[4])

# Insertion Operation
from array import *
array1 = array('i', [10, 20, 30, 40, 50])
array1.insert(2, 25)
for x in array1:
    print(x)

# Deletion Operation
from array import *
array1 = array('i', [10, 20, 30, 40, 50])
array1.remove(30)
for x in array1:
    print(x)

# Search Operation
from array import *
array1 = array('i', [10, 20, 30, 40, 50])
print(array1.index(50))

# Update Operation
from array import *
array1 = array('i', [10, 20, 30, 40, 50])
array1[2] = 25
for x in array1:
    print(x)

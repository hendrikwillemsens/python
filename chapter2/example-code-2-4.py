#!/usr/bin/python3
################################################################################
# LISTS (example-code-2-4.py)
################################################################################
# Strings are immutable, another object created = different id
age = 40
print("Age 1: {} ".format(id(age)))
age = 41
print("Age 2: {} ".format(id(age)))
# Lists are mutable, can be modified
a = [1, 2, 3, 4, 5, 6, 7, 8]
print("a = {}".format(a))
################################################################################
# Lists are sequences like strings thus support sequence operations
print("Length of a = {}".format(len(a)))
print("Third item of a = {}".format(a[2]))
a[1] = 0
print("a[1] = {}".format(a[1]))
print("a = {}".format(a))
a = a + [9, 10]
print("After concatination: a = {}".format(a))
################################################################################
# Slicing a list returns a new list
a[1:4]
print("Items 1 to 3: {}".format(a[1:4]))
################################################################################
# Although lists have no fixed size
# not possible to assign off the end of a list
#a[99]
#a[99] = 99
################################################################################
# Type specific operations
# Append method expands list and inserts item at end
print("a = {}".format(a))
a.append("20")
a.append(30)
print("Now a is {}".format(a))
print("Item 10 of a = {} (type: {})".format(a[10],type(a[10])))
print("Item 11 of a = {} (type: {})".format(a[11],type(a[11])))
# Delete item (at given offset)
a.pop(10)
print("Now a is {}".format(a))
# Insert item, 2 parameters: index, object
a.insert(1,100)
print("Now a is {}".format(a))
################################################################################
# Sort list ascending with sort()
print("\nNow we sort:")
a.sort()
print("Now a is {}".format(a))
print("Items 1 to 3: {}".format(a[1:4]))
# Sort list descending with reverse()
a.reverse()
print("Now a is {}".format(a))
print("Items 1 to 3: {}".format(a[1:4]))
################################################################################
# Nesting e.g. 3x3 matrix as a list containing 3 other lists 
m = [[11, 12, 13],
     [21, 22, 23,],
     [31, 32, 33]]
print("Matrix looks like {}".format(m))
# To get a row
print("Row 2: {}".format(m[1]))
# To get an item within a row
print("Row 2 item 3: {}".format(m[1][2]))
################################################################################
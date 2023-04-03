#!/usr/bin/python3
################################################################################
# OPERATORS (example-code-2-8.py)
################################################################################
# ARITHMETIC OPERATORS
x = 15
y = 4
# Addition: x + y = 19
print("x + y = ", x+y)
# Substraction: x - y = 11
print("x - y = ", x-y)
# Multiplication: x * y = 60
print("x * y = ", x*y)
# Division: x / y = 3.75
print("x / y =", x/y)
# Floor division: x // y = 3
print("x // y =", x//y)
# Exponential: x ** y = 50625
print("x ** y =", x**y)
################################################################################
# COMPARISON OPERATORS
x = 10
y = 12
# Greater than: x > y is False
print("x > y is", x>y)
# Less than: x < y is True
print("x < y is", x<y)
# Equal to: x == y is False
print("x == y is", x==y)
# Not equal to: x != y is True
print("x != y is", x!=y)
# Greater than or equal to: x >= y is False
print("x >= y is", x>=y)
# Less than or equal to: x <= y is True
print("x <= y is", x<=y)
################################################################################
# LOGICAL OPERATORS
x = True
y = False
# Both operands true: x and y is False
print("x and y is", x and y)
# Either operands true: x or y is True
print("x or y is", x or y)
# Operand false: not x is False
print("not x is", not x)
################################################################################
# IDENTITY OPERATORS
# i1 and i2 are integers of same values
# so they are equal as well as identical
i1 = 5
i2 = 5
print(i1 is not i2) # Output: False
# Same case with s1 and s1 (strings)
s1 = 'Hello'
s2 = 'Hello'
print(s1 is s2) # Output: True
# But l1 and l2 are list, they are equal but not identical
l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2) # Output: False
################################################################################
# MEMBERSHIP OPERATORS
# H is in x but hi is not in x (Python case sensitive)
x = 'Hi Howest'
y = {1:'a',2:'b'}
print('H' in x) # Output: True
print('hi' not in x) # Output: True
# 1 is key and a is value in y
print(1 in y) # Output: True
print('a' in y) # Output: False
################################################################################
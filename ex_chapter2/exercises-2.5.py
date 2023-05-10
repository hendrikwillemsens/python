#!/usr/bin/python3
################################################################################
# 2.5 Operators
################################################################################
# Python program to find the area of triangle
a = 18
b = 12
c = 10

# Calculate semi-perimeter s
s = (a + b + c) / 2
print("Semi-perimeter s = {}".format(s))

# Calculate area A
A = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area of triangle A = {}".format(A))

# Show only two decimals
print('='*40)
print("Semi-perimeter s = {0:10.2f}".format(s))
print("Area triangle A = {0:.2f}".format(A))
print('='*40)
print('Area of triangle A is %0.2f' %A)

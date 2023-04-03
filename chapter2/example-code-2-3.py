#!/usr/bin/python3
################################################################################
# STRINGS (example-code-2-3.py)
################################################################################
# Select line(s) of code and press Shift+Enter to run
str1 = "bioinformatics"
len1 = len(str1)
print("Length of {} is {}".format(str1,len1))
# Indexes are coded as offsets from front and start from 0 
str1[0]
print("First char: " + str1[0])
print("Third char: " + str1[2])
# Last and second-to-last item from str1
str1[-1]
print("Last char is {1} and second last char is {0}".format(str1[-2],str1[-1]))
################################################################################
# Slicing is a way of extracting a section (slice) in one step:
# give me everything in str1 from offset 3 up to but not including offset 6
strslice1 = str1[3:6]
print(strslice1)
str1[6:]
str1[:6]
str1[:-1]
# Concatenation
print(str1 + str1[:3])
# Repetition
print(str1[:3] * 3)
################################################################################
print("\nSTRING METHODS:")
# Find offset of substring
print(str1)
print(str1.find("info"))
print(str1)
# Replace occurences of string with another
str1.replace("bio","structural bio")
# Upper (and lower) case conversions
str1.upper()
# Split on delimiter into list of substrings
str1.split("i")
################################################################################
print("\nMore string methods:")
# More string methods
print(str1.lstrip("bio")) # 'nformatics'
print(str1.lstrip("ibo")) # 'nformatics'
# Note: all combinations of characters in argument are removed
# from left of string until first mismatch!
print(str1.index("i"))    # 1
print(str1.rindex("i"))   # 11
str2 = "ABC123"
print(str2.zfill(10))     # '0000ABC123'
print(str2.rjust(10))     # '    ABC123'
str3 = "ABC1223123"
# split() method 2 parameters: separator and maxsplit
print(str3.rsplit("2",2)) # ['ABC12', '31', '3']
################################################################################
# Formatting strings
print("First char of str1: " + str1[0])
print("First {} and second {} string".format(str1,str2))
print("%s first and %s second" % (str1,str2))
################################################################################
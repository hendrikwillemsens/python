#!/usr/bin/python3
################################################################################
# ZIP FUNCTION (example-code-4-zip.py)
################################################################################
# Single argument returns tuples holding single values
for i in zip([1,2,3]):
    print(i)
################################################################################
# Multiple arguments of the same lengths
# zips elements together from each list
for i in zip([1,2,3],['a','b','c'],['#','*','$']):
    print(i)
################################################################################
# Multiple arguments of different lengths
# stops at shortest one unless using zip_longest() from itertools
numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')
for i in zip(numbersList, strList, numbersTuple):
    print(i)
################################################################################
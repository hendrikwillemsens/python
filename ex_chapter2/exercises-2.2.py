#!/usr/bin/python3
################################################################################
# 2.2 Slice operations with third number
################################################################################
seq = "MNKMDLVADVAEKTDLSKAKATEVIDAVFA"
print("Sequence: {}\nwith length: {}".format(seq,len(seq)))

# 1a = MMV
slice1 = seq[0:9:3]
print(slice1) 
# third number indicates number of characters to skip
# also known as step
# example takes first, fourth and seventh char

# 1b = SKDD
slice2 = seq[16:0:-4]
print(slice2)
# when step is negative, slice takes char in reverse
# to get result start must be greater than stop
# char of stop never included

# 1c = AFVA
slice3 = seq[:25:-1]
print(slice3) 
# ommiting first index when step is negative
# means start from end of string

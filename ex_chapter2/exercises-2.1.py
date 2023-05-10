#!/usr/bin/python3
################################################################################
# 2.1 String methods
################################################################################

# a) Ask for input and print in upper and lowercase
str_in = input("Enter a word or sentence: ")
print("In UPPERCASE: {}\n"
      "In lowercase: {}"
      .format(str_in.upper(),str_in.lower()))
# [Run script to ask for input]$ python3 exercises-01.py
# Use triple ' at beginning and end of code to toggle block comment



'''

# b) Sequence and motif input, show position of motif in sequence
seq = input("Enter a sequence: ")
motif = input("Enter a motif to search for: ")
find_pos = seq.find(motif)+1
print("[FIND] Motif found at position: {}".format(find_pos))
index_pos = seq.index(motif)
print("[INDEX] Motif found at index: {}".format(index_pos))



# c) Sequence and site input, split sequence in fragments by site
seq = input("Enter a sequence: ")
split = input("Cleave (split) sequence: ")
result = seq.split(split)
print("Sequence fragments: {}".format(result))

'''
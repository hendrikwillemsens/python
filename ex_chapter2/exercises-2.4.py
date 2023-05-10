#!/usr/bin/python3
################################################################################
# 2.4 Sets
################################################################################
# a)
#mySet = {1, 2, [3, 4]}
# Causes an error: TypeError: unhashable type: 'list'
# Sets cannot have mutable items but [3, 4] is a mutable list

# b)
Sprot = {}
print(type(Sprot))
# does NOT create an empty set but object of type dict
Sprot = set()
print(type(Sprot))
# initialize with set() to get empty set
Sprot.add("NP_001304113")
Sprot.add("NP_001304114")
print("RefSeq identifiers in the protein set:\n{}".format(Sprot))

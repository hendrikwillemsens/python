#!/usr/bin/python3
################################################################################
# COMPREHENSIONS (example-code-3-1.py)
################################################################################
# Create a 3 × 3 matrix as nested lists
# Code can span lines if bracketed
M = [[1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]]
print(M)
print("Row 2 of matrix M: {}".format(M[1]))
print("Item 1 in row 2 of M: {}".format(M[1][0]))
# Simple list comprehension
col2 = [row[1] for row in M]
print("Collected items in column 2: {}".format(col2))

# Add 1 to each item in column 2
col2plus1 = [row[1] + 1 for row in M]
print("col2 {} versus col2plus1 {}".format(col2,col2plus1))
# Filter out odd items
col2sel = [row[1] for row in M if row[1] % 2 == 0] 
print("Filtered odd items in column 2: {}".format(col2sel))
# Collect a diagonal from matrix
diag = [M[i][i] for i in [0, 1, 2]]
print("Diagonal from M: {}".format(diag))

# Expressions can also be used to collect multiple values
list6 = list(range(-6, 7, 2))
print("\nlist6: {}".format(list6))
multiples = [[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]
print("multiples: {}".format(multiples))

# Dictionary comprehension
peptides = ['MATGCY','GPSALVIMWAIL','RKGDPALEKG','SMALLY']
# create dict with aaseq as keys and length as values 
peplen = {pept:len(pept) for pept in peptides}
print("\npeptides = {}\nresult = {}".format(peptides,peplen))

# Using dict comprehension to reverse key:value pair in a dictionary
revdict = {v:k for k,v in peplen.items()}
print("\nrevdict = {}".format(revdict))

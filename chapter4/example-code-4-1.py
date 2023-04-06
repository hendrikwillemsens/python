#!/usr/bin/python3
################################################################################
# FUNCTIONS (example-code-4-1.py)
################################################################################
# Function definition
def times(x, y):
	return x * y
# Function call
times(2, 4)
# Save result object
x = times(2.5, 3)
print(x)
# Functions are typeless: multiply number, repeat string
y = times("Typeless", 3)
print(y)
################################################################################
# Function for a general intersection utility
def intersect(seq1, seq2):
	result = [] 				# Empty result
	for x in seq1: 				# Scan seq1
		if x in seq2: 			# Common item in seq2?
			result.append(x) 	# Add to result
	return result
# Calling the intersect function
s1 = "SPAM"
s2 = "SCAM"
print("\nIntersection of {} and {}:".format(s1,s2))
print(intersect(s1,s2))
# Using the intersection function on gene lists
print("\nIntersection of gene lists")
list1 = ["CDH1","CDH3","CDH5","CASP1","CASP3","CASP7"]
list2 = ["CDH1","CDH2","CDH5","CASP3","CASP7","CASP9"]
print("LIST1: {}\nLIST2: {}".format(list1,list2))
print("Common genes: {}".format(intersect(list1,list2)))
################################################################################
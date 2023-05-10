#!/usr/bin/python3
################################################################################
# 3.5 Combined control statements
################################################################################
# a) Find the largest value in a list
largest = None
print("\nBefore: {}".format(largest))
print("-"*20)
for itervar in [2,28,11,7,40,15]:
    if largest is None or itervar > largest :
        largest = itervar
    print("Loop:\t{}\t{}".format(itervar,largest))
print("-"*20)
print("Largest: {}".format(largest))
################################################################################
# b) Calculate sum and average
print("\nEnter integers to calculate sum and average.\nInput 0 to exit.\n")
count = 0
sum = 0.0
number = 1
while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1
print("Calculating sum and average for the above numbers:")
average = sum / (count-1)
print("sum = {}\ncount = {}\naverage = {}".format(sum,count-1,average))
################################################################################	
# c) Count number of strings length 2 or more and
#    first and last character are same
c = 0
words = ['abc', 'xyz', 'aba', '1221']
print("\nInput words: {}".format(words))
result = []
for word in words:
    if len(word) > 1 and word[0] == word[-1]:
        c += 1
        result.append(word)
print("Number of strings: {}".format(c))
print("List of these words: {}".format(result))
print("\n")
################################################################################
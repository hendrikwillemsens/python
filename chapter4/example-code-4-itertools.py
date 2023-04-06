#!/usr/bin/python3
################################################################################
# ITERTOOLS MODULE (example-code-4-itertools.py)
################################################################################
import itertools as it
# Infinite iterator count
# Generate 10 even integers starting with 0
def evens():
    n = 0
    while True:
        yield n
        n += 2
evens = evens()
evenlist = list(next(evens) for _ in range(10))
print("The long way (7 lines): ", evenlist)
# With itertools count function
# Similar to range but returns an infinite sequence
counter = it.count(start=0,step=2)
evenlist = list(next(counter) for _ in range(10))
print("The short way (2 lines): ", evenlist)
# Count also accepts non-integer arguments
count_with_floats = it.count(start=0.5, step=0.75)
floats = list(next(count_with_floats) for _ in range(10))
print("Count with floats: ", floats)
# Negative count using for loop and break out
print("Negative count:")
for i in it.count(start=-1, step=-1):
    if i < -50:
        break
    print(i)
# Infinite iterator over input values with cycle
# Cycle over 1 and -1 
# until we break out of loop when counter c > 10
print("\nCycle 1 and -1 example:")
c = 1
for i in it.cycle([1, -1]):
    if c > 10:
        break
    print("[{}] {}".format(c,i))
    c+=1
################################################################################
# Iterators that terminate
# accumulate(iterable[, func])
list1 = list(it.accumulate(range(10)))
print("\nList accumulated sums: ", list1)
print("0, 0+1=1, 1+2=3, 3+3=6, 6+4=10, etc.")
import operator
list2 = list(it.accumulate(range(1, 5), operator.mul))
print("\nArgument multiplied: ", list2)
print("1×1=1, 1×2=2, 2×3=6, 6x4=24")
# groupby(iterable, key=None)
families = [('cadherin', 'CDH1'), ('caspase', 'CASP3'),
            ('caspase', 'CASP7'), ('cadherin', 'CDHR1'),
            ('caspase', 'CASP9'), ('cadherin', 'CDH15')]
sorted_families = sorted(families)
print(sorted_families)
for key, group in it.groupby(sorted_families, lambda make: make[0]):
    print("*** KEY = {}, GROUP = {}".format(key,group))
    for family, gene in group:
        print('{gene} from {family} gene family'.format(gene=gene,
                                                  family=family))
    print ("*** END OF FAMILY ***\n")
################################################################################
# Example combinations banknotes
banknotes = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 5, 5]
# Combinations of three banknotes
combi3 = list(it.combinations(banknotes, 3))
print(combi3)
print("\nCombinations of 3 banknotes? {}".format(len(combi3)))
# To solve problem:
# loop over banknotes
# check which combinations add up to 100
makes100 = []
for n in range(1, len(banknotes) + 1):
    for combination in it.combinations(banknotes, n):
        if sum(combination) == 100:
            makes100.append(combination)
print("\nAll combinations making100:")
print(makes100)
print("\nTotal combinations making 100? {}".format(len(makes100)))
makes100set = set(makes100)
print("\nAll unique combinations:")
print(makes100set)
print("\nTotal after removing duplicates? {}".format(len(makes100set)))
################################################################################
#!/usr/bin/python3
################################################################################
# ITERATIONS with FOR statement (example-code-3-4.py)
################################################################################
# Simple iteration
listGenes = ["BRCA1","CASP1","CDH1","TNF","TP53"]
for gene in listGenes:
    print("GENE = {}".format(gene))
################################################################################
# Counting and summing loop
print("\nCounting and summing loop:")
print("-"*26)
count = 0
total = 0
for itervar in [2,28,11,7,40,15]:
    count = count + 1
    total = total + itervar
    print(count, "\t", total)
print("\nTotal count = {}\nTotal sum = {}".format(count,total))
################################################################################
# Iteration through a dictionary
d = {'BRCA1': 14, 'CDH1': 212, 'TP53': 38}
print("\nDictionary keys:")
for k in d:
    print(k)
print("\nDictionary values:")
for v in d.values():
    print(v)
print("\nBoth keys and values:")
for k, v in d.items():
    print("key = {}\tvalue = {}".format(k,v))
################################################################################
# Enumerate function
months = ['Jan', 'Feb', 'Mar', 'Apr']
print(list(enumerate(months)))
for n, v in enumerate(months):
    print(n, v, sep="\t")
################################################################################
# Range function
x = range(20)
for n in x:
    print(n)
print("\nIncrement by 3:")
print(list(range(5, 20, 3)))
print("\nIncrement by 1 from -5 to +5:")
print(list(range(-5, 5)))
print("\nDecrement by 2:")
print(list(range(10, -10, -2)))
################################################################################
# break and continue
d = {'BRCA1': 14, 'CDH1': 212, 'TP53': 38}
print("\nBREAK:")
for k, v in d.items():
    print("Key={}".format(k))
    if v<100:
        break
    print("\tvalue={}".format(v))
print("\nCONTINUE:")
for k, v in d.items():
    print("Key={}".format(k))
    if v<100:
        continue
    print("\tvalue={}".format(v))
################################################################################
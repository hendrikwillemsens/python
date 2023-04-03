#!/usr/bin/python3
################################################################################
# CONDITIONALS (example-code-3-2.py)
################################################################################
# Simple condition
print("\nSimple condition x < y:")
x = 5
y = 10
if x < y:
  print("{} < {}".format(x,y))
################################################################################
# One-alternative conditional statement
# Ask for a gene symbol and check if it is in the list
listGenes = ["BRCA1","CASP1","CDH1","TNF","TP53"]
inputGene = input("\nEnter a gene symbol: ")
if inputGene in listGenes:
    print("{} is in the list of genes:\n{}".format(inputGene,listGenes))
else:
    print("{} was NOT FOUND in the list of genes".format(inputGene))
print("Done!")
################################################################################
# Third form of conditional statement with more than one test
# Ask for a nucleotide letter and show the full name
code = input("\nEnter a nucleotide letter: ")
if code == 'A':
  print("A is Adenine")
elif code == 'C':
  print("C is Cytosine")
elif code == 'G':
  print("G is Guanine")
elif code == 'T':
  print("T is Thymine")
elif code == 'U':
  print("U is Uracil")
else:
  print("Invalid! {} is not a nucleotide.".format(code))
################################################################################
#!/usr/bin/python3
################################################################################
# SETS (example-code-2-7.py)
################################################################################
# Make a set out of a sequence
S = set('TCAGTTAT')
print("Set S: {}".format(S))
# Set S: set(['A', 'C', 'T', 'G'])
################################################################################
# Make a set with set literals
T = {'2BE7','1IF1','1BBB'}
print("Set T: {}".format(T))
# Set T: set(['2BE7', '1IF1', '1BBB'])
################################################################################
# Example using two genesets
gs1 = {'CDH1','CDH5','CASP7','TP53','BRCA1','CDH5'}
print(gs1)
gs2 = {'BRCA2','CDH11','CDH2','CASP3','CDH5'}
# Intersection: gs1 & gs2
print("Intersection: {}".format(gs1 & gs2))
# Union: gs1 | gs2
print("Union: {}".format(gs1 | gs2))
# Differences: gs1 - gs2
print("Difference: {}".format(gs1 - gs2))
print("Difference: {}".format(gs2 - gs1))
################################################################################
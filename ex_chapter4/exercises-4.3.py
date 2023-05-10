#!/usr/bin/python3
################################################################################
# 4.3 Functions: base counts and frequencies of DNA 
################################################################################
dna_seq = input("\nEnter DNA sequence: ")

# a) Function to calculate base counts
def get_base_counts(dna):
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for base in dna:
        counts[base] += 1
    return counts
print("\nCalculate base counts: ")
print(get_base_counts(dna_seq))


# b) Function to calculate base frequencies
def get_base_frequencies(dna):
    counts = get_base_counts(dna)
    return {base: count*1.0/len(dna) for base, count in counts.items()}
print("\nCalculate base frequencies: ")
print(get_base_frequencies(dna_seq))
################################################################################
#!/usr/bin/python3
################################################################################
# RANDOM MODULE (example-code-4-random.py)
################################################################################
import random
# Generate random floating point number 0-1
random_number1 = random.random()
print("Random number 1 = {}".format(random_number1))
# Generate random floating point number 0-100
random_number2 = random.random()*100
print("Random number 2 = {}".format(random_number2))
# Generate random integer from 1 to 5
random_number3 = random.randint(1,5)
print("Random number 3 = {}".format(random_number3))
################################################################################
# Random number from choice: 1 to 10
myrange = range(1,11)
for i in myrange:
    print("i={} ".format(i), end="")
chosen_number = random.choice(myrange)
print("\nA number from 1 to 10: {}".format(chosen_number))
################################################################################
# Generate random nucleotide sequence length=10
myrange = range(1,51)
ntseq = ""
for i in myrange:
    nt = random.choice(["A","C","T","G"])
    ntseq = ntseq + nt
    print("\nNew nt = {}\nntseq = {}".format(nt,ntseq))
print("Random nt seq: {}".format(ntseq))
################################################################################
# Shuffle a list in random order
import random
game = ["rock","paper","scissors"]
print ("Original list: ", game)
random.shuffle(game)
print ("List after shuffle 1: ", game)
random.shuffle(game)
print ("List after shuffle 2: ", game)
################################################################################
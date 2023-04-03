#!/usr/bin/python3
################################################################################
# NUMBERS (example-code-2-2.py)
################################################################################
print("\nNumbers:")
# INT and addition
myNumber1 = 123 + 456
print(myNumber1, type(myNumber1))
# FLOAT and multiplication
myNumber2 = 1.6 * 5
print(myNumber2, type(myNumber2))
# (LONG) INT and exponentiation
myNumber3 = 2 ** 100
print(myNumber3, type(myNumber3))
# Scientific
sci = -87.7e4
print(sci, type(sci))
sci2 = 2.3e-3
print(sci2, type(sci2))

# Useful numeric modules in Python
import math
print("\nFrom math: ")
print(math.pi)
print(math.sqrt(85))

import random
randomNumber = random.random()
print("\nRandom number: ",randomNumber)
chosen = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\nA number chosen between 0 and 10: ", chosen)
chosen2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\nA 2nd number chosen between 0 and 10: ", chosen2)
#!/usr/bin/python3
################################################################################
# 3.1 COMPREHENSIONS
################################################################################
# a) List of even values for a given list
givenlist = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("\nGiven list: {}".format(givenlist))
evenlist = [number for number in givenlist if number % 2 == 0] 
print("Even list: {}".format(evenlist))
################################################################################
# b) List of ages for a given list of years of birth
birthyears = [1990, 1995, 1990, 1991, 1992, 1991]
print("\nYears of birth: {}".format(birthyears))
ages = [2020 - year for year in birthyears]
print("Ages: {}".format(ages))
################################################################################
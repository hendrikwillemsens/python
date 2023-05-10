#!/usr/bin/python3
################################################################################
# 3.3 WHILE LOOP
################################################################################
# a) Fibonacci series between 0 to 50
# First terms: x = 0 and y = 1
x,y = 0,1
while x < 50:
	r = x + y
	print("{} ({}+{}={})".format(x,x,y,r))
	# update values
	x = y
	y = r
################################################################################
# b) Guess a number between 1 to 9
# random.randint(a, b) returns random integer N such that a <= N <= b
import random
target_num = random.randint(1, 9)
guess_num = 0
while target_num != guess_num:
    guess_num = int(input("\nGuess a number between 1 and 9: "))
print("\nYES! {} that's the number!".format(target_num))
################################################################################
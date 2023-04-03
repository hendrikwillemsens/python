#!/usr/bin/python3
################################################################################
# WHILE LOOPS (example-code-3-3.py)
################################################################################
# Simple while loop
i = 1
while i <= 5:
    print(i)
    i += 1
################################################################################
# Interactive loop 1
print("\nInteractive loop 1")
while True:
    response = input("\nEnter text: ")
    if response == "stop": break
    print("\nResponse is {}".format(response.upper()))
################################################################################
# Interactive loop 2
print("\nInteractive loop 2")
while True:
    response = input("\nEnter text: ")
    if response == "stop" \
    or response == "Stop" \
    or response == "STOP" : break
print("\nResponse is {}".format(response.upper()))
################################################################################
# Black Jack like example:
# reads numbers and sums them until total >= 21
# input of 0 will stop script even if sum < 21
total_sum = 0
number = int(input("Integer? "))
while number != 0:
    total_sum += number
    if total_sum >= 21:
        print("LOSE --> {} >= 21".format(total_sum))
        break
    number = int(input("Next integer? "))
else:
    print("WIN --> {} < 21".format(total_sum))
################################################################################
#!/usr/bin/python3
################################################################################
# 4.1 Function: reverse string
################################################################################
def string_reverse(str1):
    rstr1 = ""
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print("Reverse of live desserts = ", end="")
print(string_reverse('live desserts'))
################################################################################
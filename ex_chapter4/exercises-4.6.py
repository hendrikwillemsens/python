#!/usr/bin/python3
################################################################################
# 4.6 Modules: validity of password input 
################################################################################
import re
pw = input("\nGive a valid password: ")
x = True
while x:  
    if (len(pw)<6 or len(pw)>12):
        break
    elif not re.search("[a-z]",pw):
        break
    elif not re.search("[0-9]",pw):
        break
    elif not re.search("[A-Z]",pw):
        break
    elif not re.search("[$#@]",pw):
        break
    else:
        print("Valid password\n")
        x = False
        break
if x:
    print("NOT a valid password\n")
################################################################################
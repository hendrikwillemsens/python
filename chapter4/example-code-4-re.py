#!/usr/bin/python3
################################################################################
# Module for regular expressions (example-code-4-re.py)
################################################################################
import re
text = "A big black bug bit a big black dog on his big black nose."
################################################################################
# Compile RE pattern into pattern object and use method
check_text = re.compile('bi.', re.IGNORECASE)
print(check_text.findall(text))
# ['big','bit','big','big']
################################################################################
# Find all substrings where RE ".i." matches and return as list
result = re.findall(".i.", text)
print("\nFind all .i. : {}".format(result))
# ['big','bit','big','his','big']
################################################################################
# Search for three-letter words first = b, last = g
result = re.findall("b.g", text)
print("\nFind all b.g : {}".format(result))
# ['big','bug','big','big']
################################################################################
# Search for three-letter words enclosed by whitespace
result = re.findall("\\s\\w\\w\\w\\s", text)
print("\nFind all \\s\\w\\w\\w\\s : {}".format(result))
# Will return all *non-overlapping* matches
# Third-party regex module (not re) supports overlapping matches
# Changed in version 3.7: 
#  Only characters that can have special meaning in regular expression are escaped
#  --> '!', '"', '%', "'", ',', '/', ':', ';', '<', '=', '>', '@', and "`" 
#  are no longer escaped.
################################################################################
# Substitution: replace "bi" by "bo"
result = re.sub("bi", "bo", text)
print("\nReplace \"bi\" by \"bo\" : {}".format(result))
################################################################################
# Search for first occurence of RE within string
result = re.search("b.g", text)
if result:
    print("Found: {}".format(result.group()))
    print("Start: {}".format(result.start()))
    print("End: {}".format(result.end()))
else:
    print("Not found")
################################################################################
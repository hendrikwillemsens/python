#!/usr/bin/python3
################################################################################
# 4.2 Function: string separate by char, sort and join again by char
################################################################################
def split_sort_join(str_sep,split_char):
    str2split = str(str_sep)
    # print("str2split={}".format(str2split))
    items = [n for n in str2split.split(split_char)]
    # print("items={}".format(items))
    items.sort()
    # print("items after sort={}".format(items))
    print(split_char.join(items))
split_char = input("\nType a character to separate a sequence of words:\n")
str_sep = input("\nType a character separated sequence of words to sort and join again:\n")
split_sort_join(str_sep,split_char)
################################################################################
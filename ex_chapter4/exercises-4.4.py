#!/usr/bin/python3
################################################################################
# 4.4 Module time 
################################################################################
import time
# a) Month of year
print("\nMonth of year: ", time.strftime("%B"))
# b) Week number of year
print("Week number of year: ", time.strftime("%W"))
# c) Day of year
print("Day of year: ", time.strftime("%j"))
# d) Day of month
print("Day of month : ", time.strftime("%d"))
# e) Day of week
print("Day of week: ", time.strftime("%A"))

import locale
locale.setlocale(locale.LC_ALL, 'nl_NL')
print("\nMaand van jaar: ", time.strftime("%B"))
print("Dag van week: ", time.strftime("%A"))
################################################################################
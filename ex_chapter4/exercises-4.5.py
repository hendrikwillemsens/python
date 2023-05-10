#!/usr/bin/python3
################################################################################
# 4.5 Module datetime 
################################################################################
from datetime import date, timedelta
date_nextweek = date.today() + timedelta(days = 7)
date_min5 = date.today() - timedelta(5)
print('\nCurrent date :', date.today())
print('Date next week :', date_nextweek)
print('Five days before :', date_min5)
################################################################################
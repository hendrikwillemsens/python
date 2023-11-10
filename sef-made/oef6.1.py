#!/usr/bin/python3

import MySQLdb as my
import re
import humanfriendly
import os
# Reading data from UCSC
print("\nREADING DATA FROM UCSC DATABASE")
db = my.connect(host="genome-mysql.soe.ucsc.edu",
#db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg19")
c = db.cursor()
no_rows = c.execute("""SELECT * FROM ncbiRefSeq""")

result = c.fetchall()
c = 0
for row in result:
    resultaat = re.search("NM", row[1])
    if resultaat:
        c = c+1

print("de hoeveelheid is {}" . format(c))
db.close()

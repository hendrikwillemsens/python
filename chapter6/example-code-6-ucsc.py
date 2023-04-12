#!/usr/bin/python3
################################################################################
# MySQL (example-code-6-ucsc.py)
################################################################################
import MySQLdb as my
# Reading data from UCSC
print("\nREADING DATA FROM UCSC DATABASE")
db = my.connect(host="genome-mysql.soe.ucsc.edu",
#db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg19")
c = db.cursor()
no_rows = c.execute("""SELECT * FROM ensGene""")
# Fetch one row (ENST + ENSG)
print(c.fetchone())
print("Total rows ensGene: {}".format(no_rows))
################################################################################
# UCSC Table Browser: https://genome.ucsc.edu/cgi-bin/hgTables
# Number of rows in track NCBI RefSeq (table ncbiRefSeq)
no_rows2 = c.execute("""SELECT * FROM ncbiRefSeq""")
# Fetch all results
result = c.fetchall()
# Iterate over result
c = 1
for row in result:
   print("RefSeq {} on {} => {}".format(row[1],row[2],row[12]))
   c = c + 1
print("Total rows ncbiRefSeq: {}".format(no_rows2))
# Close database
db.close()
################################################################################
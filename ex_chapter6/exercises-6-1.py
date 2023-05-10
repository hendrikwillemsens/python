#!/usr/bin/python3
################################################################################
# 6.1 ncbiRefSeq: mRNA (NM_) transcripts only
################################################################################
import MySQLdb as my

# A) Number of mRNA transcripts in ncbiRefSeq hg19
# Connect with UCSC MySQL database hg19
print("\nReading data from hg19:")
db19 = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg19")
c = db19.cursor()
mRNA_hg19 = c.execute("""SELECT * FROM ncbiRefSeq WHERE name LIKE 'NM_%'""")

# Fetch one result
print(c.fetchone())

# Total NM_ transcripts
print("Total mRNA transcripts ncbiRefSeq: {}".format(mRNA_hg19))
# Total NM_ transcripts ncbiRefSeq: 47132 (of 61177 in February 2019)

# Close database
db19.close()


# B) Number of mRNA transcripts in ncbiRefSeq hg38
# Connect with UCSC MySQL database hg38
print("\nReading data from hg38:")
db38 = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg38")
c = db38.cursor()
# Number of rows in track NCBI RefSeq (table ncbiRefSeq)
# where name like NM_
mRNA_hg38 = c.execute("""SELECT * FROM ncbiRefSeq WHERE name LIKE 'NM_%'""")

# Fetch one result
print(c.fetchone())

# Total NM_ transcripts
print("Total NM_ transcripts ncbiRefSeq: {}".format(mRNA_hg38))
# Total NM_ transcripts ncbiRefSeq: 47461 (of 61177 in February 2019)

# Close database
db38.close()

# Difference between hg19 and hg38
diff = mRNA_hg38 - mRNA_hg19
print("\nRefSeq mRNA more in hg38 vs hg19: {}".format(diff))
# Difference: 329 (in February 2019)

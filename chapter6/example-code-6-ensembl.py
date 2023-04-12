#!/usr/bin/python3
################################################################################
# MySQL (example-code-6-ensembl.py)
################################################################################
import MySQLdb as my
# Reading data from Ensembl
print("\nREADING DATA FROM ENSEMBL DATABASE")
# Core databases: <genus_species>_core_<version>_<assembly_version>
# Ensembl Release 104 (May 2021)
db = my.connect(host="ensembldb.ensembl.org", user="anonymous", passwd="",
                db="homo_sapiens_core_104_38")
c = db.cursor()
no_rows3 = c.execute("""SELECT * FROM gene""")
# Fetch all results
print(c.fetchone())
# Iterate over result
result = c.fetchall()
c = 1
for row in result:
   if(c<5):
      print("Ensembl gene: {}\n\t{}\n\t{}".format(row[1],row[9],row[12]))
      c = c + 1
print("Ensembl hg38 gene table: {} ENSG records".format(no_rows3))
################################################################################
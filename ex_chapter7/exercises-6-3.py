#!/usr/bin/python3
################################################################################
# 6.3 Combine RefSeq and Ensembl data into a refgenes database
################################################################################
# Import required modules
import MySQLdb as my
import sqlite3


################################################################################
# Create database connection object
conn_lite = sqlite3.connect('refgenes.db')
# Create cursor object and call its execute() method to perform SQL
clite = conn_lite.cursor()

# Connect with UCSC database
db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg38")
cursor = db.cursor()


################################################################################
# A) Look for genes who have RefSeq transcripts and save in sqlite
################################################################################
# UCSC Table Browser: https://genome.ucsc.edu/cgi-bin/hgTables
# Get RefSeq data from ncbiRefSeq table
# Uncomment next line to rerun script
try:
    clite.execute('''DROP TABLE ncbiRefSeq''')
except sqlite3.OperationalError:
    print("\nNo ncbiRefSeq table to delete")


# Create table if not exists
clite.execute('''CREATE TABLE IF NOT EXISTS ncbiRefSeq (refseq_id INTEGER PRIMARY KEY, name VARCHAR, name2 VARCHAR, chrom VARCHAR)''')
# name = NM_nnnnn = refseq_accession_number
# name2 = gene_symbol

# Reading data from UCSC
print("\nREADING DATA FROM TABLE: ncbiRefSeq")
no_rows = cursor.execute("""SELECT * FROM ncbiRefSeq LIMIT 30000""")
#no_rows = cursor.execute("""SELECT * FROM ncbiRefSeq""")
# Fetch all results
result = cursor.fetchall()
# Iterate over result
c = 1
for row in result:
    name = row[1]
    chrom = row[2]
    name2 = row[12]
    # print("RefSeq {} on {} => {}".format(name,chrom,name2))
    if(c%1000==0): print("[{}] RefSeq {} on {} => {}".format(c,name,chrom,name2))
    # Save in database
    clite.execute('''INSERT INTO ncbiRefSeq VALUES(?,?,?,?)''',(c,name,name2,chrom))
    c = c + 1
conn_lite.commit()
print("\nTotal rows ncbiRefSeq: {}".format(no_rows))

# Check first row of sqlite ncbiRefSeq table
query = clite.execute('SELECT * FROM ncbiRefSeq')
print("\nExample result: ")
print(clite.fetchone())


################################################################################
# A) Look for genes who have Ensembl transcripts and save in sqlite
################################################################################
# UCSC Table Browser: https://genome.ucsc.edu/cgi-bin/hgTables
# Get data from kgXref table
# Uncomment next line to rerun script
try:
    clite.execute('''DROP TABLE kgXref''')
except sqlite3.OperationalError:
    print("\nNo kgXref table to delete")

# Create table if not exists
clite.execute('''CREATE TABLE IF NOT EXISTS kgXref (ens_id INTEGER PRIMARY KEY, enst VARCHAR, genesymbol VARCHAR, refseq VARCHAR, description VARCHAR)''')
# Reading data from UCSC
print("\nREADING DATA FROM TABLE: kgXref")
no_rows = cursor.execute('SELECT * FROM kgXref LIMIT 30000')
#no_rows = cursor.execute('SELECT * FROM kgXref')
# Fetch all results
result = cursor.fetchall()
# Iterate over result
c = 1
for row in result:
    kgID = row[0]
    genesymbol = row[4]
    refseq = row[5]
    description = row[7]
    # print(type(description))
    # print(description.decode("utf-8"))
    # description is longblob = b'Homo sapiens microRNA...'
    # decode type bytes to string using utf-8
    str_desc = description.decode("utf-8")
    # print("{} => {}\nDescription: {}".format(kgID,refseq,str_desc))
    if(c%1000==0): print("[{}] {} => {}\n\tGene: {}\n\tDescription: {}".format(c,kgID,refseq,genesymbol,str_desc))
    # Save in database
    clite.execute('''INSERT INTO kgXref VALUES(?,?,?,?,?)''',(c,kgID,genesymbol,refseq,str_desc))
    c = c + 1
conn_lite.commit()
print("\nTotal rows kgXref: {}".format(no_rows))

# Check first row of sqlite kgXref table
query = clite.execute('SELECT * FROM kgXref')
print("\nExample result: ")
print(clite.fetchone())

# Close UCSC database connection
db.close()


################################################################################
# B) Search for RefSeq and Ensembl transcripts for each gene
#    and save transcripts (comma-separated)
################################################################################
# Uncomment next line to rerun script
try:
    clite.execute('''DROP TABLE hg38_genes''')
except sqlite3.OperationalError:
    print("\nNo hg38_genes table to delete")

# Create table with refgenes 
clite.execute('''CREATE TABLE IF NOT EXISTS hg38_genes
    (gene_id INTEGER PRIMARY KEY, gene VARCHAR, refseq VARCHAR, ensembl VARCHAR)''')

# First loop over ncbiRefSeq genes
c_gene = 0
for row in clite.execute('''SELECT name2 FROM ncbiRefSeq GROUP BY name2'''):
    c_gene = c_gene + 1
    # Save as new gene
    if(c_gene%1000==0): print("ncbiRefSeq gene {} symbol {}".format(c_gene,row[0]))
    gene = row[0]
    refseq = ""
    ensembl = ""
    cursor2 = conn_lite.cursor()
    cursor2.execute('''INSERT INTO hg38_genes VALUES (?,?,?,?)''',(c_gene,gene,refseq,ensembl))

conn_lite.commit()
print("\nTotal hg38_genes based on ncbiRefSeq: {}".format(c_gene))
clite.execute('SELECT * FROM hg38_genes')
print("\nExample from hg38_genes: ", clite.fetchone())

# Next loop over kgXref and either update by adding ensembl transcripts to existing gene
# or add new gene record if no refseq exists
# c_gene --> keep using previous counter
c_exist = 0
c_new = 0
kgXref_query = clite.execute('''SELECT geneSymbol FROM kgXref GROUP BY genesymbol''')
kgXref_results = clite.fetchall()
print("\nNow check {} kgXref records for existing and new results".format(len(kgXref_results)))
for row in kgXref_results:
    c_gene = c_gene + 1
    if(c_gene%1000==0): print("kgXref gene {} symbol {}".format(c_gene,row[0]))
    genesymbol = row[0]
    query = "SELECT * FROM hg38_genes WHERE gene = '" + genesymbol + "'"
    cursor2 = conn_lite.cursor()
    cursor2.execute(query)
    results = cursor2.fetchall()
    if(len(results)==0):
        # Add if gene does not exist
        c_new = c_new + 1
        refseq = ""
        ensembl = ""
        cursor2 = conn_lite.cursor()
        cursor2.execute('''INSERT INTO hg38_genes VALUES (?,?,?,?)''',(c_gene,genesymbol,refseq,ensembl))
    else: 
        c_exist = c_exist + 1

conn_lite.commit()
print("\nMatching existing hg38_genes: {}".format(c_exist))
print("\nTotal new hg38_genes based on kgXref: {}".format(c_new))


# Define functions to get RefSeq transcripts
def getRefSeqTranscripts(gene):
    transcripts_refseq = ""
    query = "SELECT * FROM ncbiRefSeq WHERE name2 = '" + gene + "'"
    cursor = conn_lite.cursor()
    for row in cursor.execute(query):
        transcript = row[1]
        transcripts_refseq = transcripts_refseq + transcript + ","
    # Remove last , before returning
    transcripts_refseq = transcripts_refseq[:-1]
    return transcripts_refseq

# Define functions to get Ensembl transcripts
def getEnsemblTranscripts(gene):
    transcripts_ensembl = ""
    query = "SELECT * FROM kgXref WHERE genesymbol = '" + gene + "'"
    cursor = conn_lite.cursor()
    for row in cursor.execute(query):
        transcript = row[1]
        transcripts_ensembl = transcripts_ensembl + transcript + ","
    # Remove last , before returning
    transcripts_ensembl = transcripts_ensembl[:-1]
    return transcripts_ensembl

# Now we can get the transcripts for each gene
c_gene = 0
for row in clite.execute('''SELECT * FROM hg38_genes'''):
    c_gene = c_gene + 1
    gene_id = row[0]
    gene = row[1]
    if(c_gene%1000==0): print("\n[{}] Gene: {}".format(c_gene,gene))
    cursor2 = conn_lite.cursor()
    # Get RefSeq transcripts
    transcripts_refseq = getRefSeqTranscripts(gene)
    if(c_gene%1000==0): print("\n[{}] Refseq: {}".format(c_gene,transcripts_refseq))
    # Update record with RefSeq transcripts
    cursor2.execute('''UPDATE hg38_genes SET refseq = ? WHERE gene_id = ? ''', \
        (transcripts_refseq, gene_id))
    # Get Ensembl transcripts
    transcripts_ensembl = getEnsemblTranscripts(gene)
    if(c_gene%1000==0): print("\n[{}] Ensembl: {}".format(c_gene,transcripts_ensembl))
    # Update record with Ensembl transcripts
    cursor2.execute('''UPDATE hg38_genes SET ensembl = ? WHERE gene_id = ? ''', \
        (transcripts_ensembl, gene_id))

conn_lite.commit()
print("\nTotal hg38_genes genes: {}".format(c_gene))


################################################################################
# C) Query for genes
# HAVING BOTH REFSEQ AND ENSEMBL TRANSCRIPTS (26040)
query = "SELECT * FROM hg38_genes WHERE refseq != '' AND ensembl != ''"
clite.execute(query)
results = clite.fetchall()
print("\nHAVING BOTH REFSEQ AND ENSEMBL TRANSCRIPTS:\n{}".format(len(results)))
print("\nExample: ", results[0])

# HAVING ONLY REFSEQ TRANSCRIPTS (12683)
query = "SELECT * FROM hg38_genes WHERE refseq != '' AND ensembl == ''"
clite.execute(query)
results = clite.fetchall()
print("\nHAVING ONLY REFSEQ TRANSCRIPTS:\n{}".format(len(results)))
print("\nExample: ", results[0])

# HAVING ONLY ENSEMBL TRANSCRIPTS (32643)
query = "SELECT * FROM hg38_genes WHERE refseq == '' AND ensembl != ''"
clite.execute(query)
results = clite.fetchall()
print("\nHAVING ONLY ENSEMBL TRANSCRIPTS:\n{}".format(len(results)))
print("\nExample: ", results[0])

################################################################################
# D) Save results in Excel table
from openpyxl import Workbook
# Initialize Workbook
wb = Workbook()
# Active worksheet
ws = wb.active
# Append header row
ws.append(["gene_id","gene","refseq","ensembl"])
# Set worksheet name
ws.title = "BOTH"
# Get data and write to xlsx
query = "SELECT * FROM hg38_genes WHERE refseq != '' AND ensembl != ''"
clite.execute(query)
results = clite.fetchall()
for row in results:
    ws.append([row[0],row[1],row[2],row[3]]) 
# Save file
wb.save("hg38_genes.xlsx")

################################################################################
# Close sqlite connection
conn_lite.close()
################################################################################

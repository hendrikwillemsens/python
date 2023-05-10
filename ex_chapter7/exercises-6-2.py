#!/usr/bin/python3
################################################################################
# 6.1 Ensembl transcript data
################################################################################
import MySQLdb as my
import time
import sqlite3

def getTime():
    timetuple = time.localtime(time.time())
    return str(timetuple.tm_hour) + "h" + str(timetuple.tm_min)

'''
################################################################################
# Version 1: few records, without saving in sqlite database
################################################################################
# Reading data from Ensembl
print("\nReading Ensembl transcript data...")
start_time = getTime()

# Core databases: <genus_species>_core_<eg_version>_<ensembl_version>_<assembly_version>
# Ensembl release 95 - January 2019
db = my.connect(host="ensembldb.ensembl.org",
   user="anonymous",
   passwd="",
   db="homo_sapiens_core_95_38")
c = db.cursor()
query = "SELECT transcript.transcript_id, transcript.gene_id, \
         transcript.stable_id, gene.description, gene.stable_id \
         FROM transcript \
         LEFT JOIN gene ON transcript.gene_id = gene.gene_id"
         #LIMIT 100"
enst_rows = c.execute(query)
# 0 = transcript.transcript_id | 1 = transcript.gene_id
# 2 = transcript.stable_id | 3 = gene.description | 4 = gene.stable_id

# Iterate over some result
print("\nExample records:")
result = c.fetchall()
c = 1
for row in result:
   if(c<6):
      print("{} --> {} = {}".format(row[2],row[4],row[3]))
      c = c + 1

# Close database
db.close()

# Total transcripts
print("\nEnsembl hg38 transcript table: {} ENST records".format(enst_rows))

# Show start and end time
stop_time = getTime()
print("\nStarted at {}\nReady at {}".format(start_time, stop_time))
'''

################################################################################
# Version 2: all transcript records inserted in sqlite database
################################################################################
# Create database connection object
conn_lite = sqlite3.connect('ensembl.db')
# Create cursor object and call its execute() method to perform SQL
clite = conn_lite.cursor()
# Next line uncommented to rerun script
#clite.execute('''DROP TABLE enst''')
# Create table
clite.execute("""CREATE TABLE IF NOT EXISTS enst 
(enst_id INTEGER PRIMARY KEY, enst VARCHAR, ensg VARCHAR, description VARCHAR)""")

# Reading data from Ensembl
print("\nReading Ensembl transcript data...")
start_time = getTime()
conn_ens = my.connect(host="ensembldb.ensembl.org", user="anonymous", passwd="", db="homo_sapiens_core_95_38")
c = conn_ens.cursor()
query = "SELECT transcript.transcript_id, transcript.gene_id, \
         transcript.stable_id, gene.description, gene.stable_id \
         FROM transcript \
         LEFT JOIN gene ON transcript.gene_id = gene.gene_id \
         LIMIT 25000"
# Remove the limit to get all ENST transcripts (>200000)
enst_rows = c.execute(query)
# 0 = transcript.transcript_id | 1 = transcript.gene_id
# 2 = transcript.stable_id | 3 = gene.description | 4 = gene.stable_id

# Iterate over some result
print("\nExample records:")
result = c.fetchall()
c = 1
for row in result:
    if(c % 10000 == 0):
        print("[{}] {} --> {} = {}".format(c,row[2],row[4],row[3]))
    # Save in sqlite ensembl.db and commit
    clite.execute('''INSERT INTO enst VALUES(?,?,?,?)''',(c,row[2],row[4],row[3]))
    c = c + 1
"""    try:
           clite.execute('''INSERT INTO enst VALUES(?,?,?,?)''',(c,row[2],row[4],row[3]))
           conn_lite.commit()
       except sqlite3.IntegrityError:
           # If record would already exist
           print("\nIntegrityError! Maybe record already exists?")
"""
# Commit the changes to save in your database else table will be empty!
conn_lite.commit()

# Total transcripts
print("\nEnsembl hg38 transcript table: {} ENST records".format(enst_rows))

# Query sqlite
print("\nOne search query sqlite on ensembl.db:")
# e.g. ENSG00000143420
ensg_input = input("What Ensembl gene do you want to search for? ")
keyword = (ensg_input,)
# keyword = ('ENSG00000143420',)
ensembl_enst = clite.execute('SELECT * FROM enst WHERE ensg=?', keyword)
print("Result: ")
print(clite.fetchone())

# Total rows in enst table
clite.execute('SELECT COUNT(*) as rowcount FROM enst')
enst_rows = clite.fetchone()
print("Total rows in enst table of ensembl.db: {}".format(enst_rows[0]))

# Close database connections
conn_ens.close()
conn_lite.close()

# Show start and end time
stop_time = getTime()
print("\nStarted at {}\nReady at {}".format(start_time, stop_time))

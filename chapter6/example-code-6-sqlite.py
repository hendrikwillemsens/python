#!/usr/bin/python3
################################################################################
# SQLite3 (example-code-6-sqlite.py)
################################################################################
import sqlite3
# First step: create database connection object
conn = sqlite3.connect('taxonomy.db')
# Next create cursor object
# and call its execute() method to perform SQL query
c = conn.cursor()
# Create table
try:
    c.execute('''CREATE TABLE organisms \
            (org_id, latin_name, common_name, tax_id, kingdom, phylum, ordr)''')
except sqlite3.OperationalError:
    print("\nTable organisms already exists\n")
# To delete: c.execute('''DROP TABLE organisms''')
################################################################################
# Insert rows of data
c.execute("INSERT INTO organisms \
           VALUES (1,'Homo sapiens','human', \
           9606,'Metazoa','Chordata','Primates')")
c.execute("INSERT INTO organisms \
           VALUES (2,'Danio rerio','zebrafish', \
           7955,'Metazoa','Chordata','Cypriniformes')")
c.execute("INSERT INTO organisms \
           VALUES (3,'Monosiga brevicollis','choanoflagellate', \
           81824,'','','Choanoflagellida')")
# Recommended to use the "?" placeholder
c.execute('''INSERT INTO organisms \
             VALUES(?,?,?,?,?,?,?)''', \
            (4,'Gallus gallus','chicken', 9031,'Metazoa','Chordata','Galliformes'))
# Last insert id
insert_id = c.lastrowid
print('Last row insert id: {}'.format(insert_id))
################################################################################
# Larger example that inserts many records at a time
species = [(5,'Anopheles gambiae','malaria mosquito', 7165,'Metazoa','Arthropoda','Diptera'),
           (6,'Tribolium castaneum','red flour beetle', 7070,'Metazoa','Arthropoda','Coleoptera')
          ]
c.executemany('INSERT INTO organisms VALUES (?,?,?,?,?,?,?)', species)

# Update record
c.execute('''UPDATE organisms SET common_name = ? WHERE tax_id = ? ''', \
         ('African malaria mosquito', 7165))
################################################################################
# Save (commit) changes
conn.commit()
# Close connection when done with it
conn.close()
################################################################################
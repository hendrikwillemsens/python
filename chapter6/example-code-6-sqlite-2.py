#!/usr/bin/python3
################################################################################
# SQLite3 (example-code-6-sqlite-2.py)
################################################################################
import sqlite3
# Reconnect again and query
print("\nReconnect again with taxonomy.db and run queries:")
conn2 = sqlite3.connect('taxonomy.db')
c2 = conn2.cursor()
# First query using fetchone
print("\nFirst query using fetchone:")
keyword = ('Chordata',)
c2.execute('SELECT * FROM organisms WHERE phylum=?', keyword)
print(c2.fetchone())
print(c2.fetchone())
# Second query using fetchall
print("\nSecond query using fetchall:")
keyword = ('Arthropoda',)
c2.execute('SELECT * FROM organisms WHERE phylum=?', keyword)
print(c2.fetchall())
################################################################################
# Query using iterator
print("\nQuery using iterator:")
# keyword = "Metazoa"
for row in c2.execute('SELECT * FROM organisms'):
    print(row)
# Delete table
#c2.execute('DROP TABLE organisms')
conn2.close()
################################################################################
# Reconnect and executescript
print("\nReconnect and executescript:")
conn3 = sqlite3.connect('taxonomy.db')
c3 = conn3.cursor()
try:
    c3.executescript(''' 
CREATE TABLE organisms (org_id, latin_name, common_name, tax_id, kingdom, phylum, ordr);
INSERT INTO organisms VALUES (1,'Homo sapiens','human', 9606,'Metazoa','Chordata','Primates');
    ''')
    conn3.commit() # commit changes
    print("TABLE organisms committed")
except sqlite3.OperationalError:
    print("Table organisms already exists")
conn3.close()
################################################################################
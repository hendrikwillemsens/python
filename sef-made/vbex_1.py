#!/usr/bin/python3
import MySQLdb as my
from openpyxl import Workbook
# Initialize Workbook
wb = Workbook()
# Active worksheet
ws = wb.active


your_list=[]
while True:
    accesion = input("Enter an exesionnumber")
    your_list.append(accesion)
    
    if accesion == "0": break
print(your_list)


print("\nREADING DATA FROM UCSC DATABASE")
db = my.connect(host="genome-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg38")
c = db.cursor()

count = 0
for i in your_list:
    no_rows = c.execute("""SELECT chromStart, chromEnd, name FROM snp151CodingDbSnp WHERE transcript = '{}'""".format(your_list[count]))
    print("Total SNP's found for {}: {}".format(your_list[count], no_rows))
    count = count + 1


# Fetch all results

# Iterate over result



db.close()





wb.save('cbex_0.xlsx')
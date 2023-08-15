#!/usr/bin/python3
import csv
from openpyxl import Workbook
wb = Workbook()
ws = wb.active

with open('NCBI_Genome_result_Legionella.txt', "r") as f:
    lines = f.read()
    print(lines)


# Reading csv file line by line
with open('lpsn_export.csv') as csv_file:
     print("Reading LPSN file and searching for leg nomenclature")
     line_count = 0
     csv_reader = csv.reader(csv_file, delimiter=',')
     
     for row in csv_reader:
        opsomming = row[0]+ row[1]
        while row[0] == 'Legionella':
            print(row[0], row[1])
            reference = row[3]
            print(reference)
            status = row[4]
            print(status)
            addres= row[6]
            print(addres)
    
csv_file.close()  

wb.save('Legionalla.xlsx')
    

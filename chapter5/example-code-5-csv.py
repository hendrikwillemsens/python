#!/usr/bin/python3
################################################################################
# Comma- and tab-separated files (example-code-5-csv.py)
################################################################################
import csv
# Reading csv file line by line
with open('urine.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print column names
            print("Column names are:")
            print("{0:5s} | {1:5s} | {2:10s}".format(row[0],row[1],row[2]))
            line_count += 1
        elif(line_count<=20):
            # print first 5 lines of data
            print("{0:5s} | {1:5s} | {2:10s}".format(row[0],row[1],row[2]))
            line_count += 1
    print("Processed {} lines.".format(line_count))
csv_file.close()
################################################################################
# Reading csv file into a dictionary
# First line of CSV file is assumed to contain keys
print("\nReading into dictionary...")
with open('urine.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 1
    for row in csv_reader:
        if(line_count<=5):
            # print first 5 lines of data
            print("{0:5s} | {1:5s} | {2:10s}".format(row[""],row["r"],row["gravity"]))
            line_count += 1
    print("Processed {} lines.".format(line_count))
csv_file.close()
################################################################################
# Writing csv file
with open('pers.csv', mode='w') as pers_file:
    pers_writer = csv.writer(pers_file, 
    delimiter=';', 
    quotechar='"', 
    quoting=csv.QUOTE_MINIMAL)
    pers_writer.writerow(['John Snow', '1,73', '32'])
    pers_writer.writerow(['Arya Stark', '1,55', '21'])
    pers_writer.writerow(['Daenerys Targaryen', '1,57', '32'])
pers_file.close()
################################################################################
#!/usr/bin/python3
################################################################################
# 5.1 Parse vcf file (line by line)
################################################################################
import csv
import re
################################################################################
'''
# V1
# First try to only read the comments
fileObj = open("129P2_OlaHsd.mgp.v5.indels.dbSNP142.normed.vcf", "r")
c = 1
for line in fileObj.readlines():
    result = re.search("^#", line)
    if result:
        # line containing # comment
        print("{}: {}".format(c,line))
    # Increase line counter
    c = c + 1
fileObj.close()

################################################################################

# V2
# Now for first 100 lines try to parse the indel lines
# and print chr:pos
fileObj = open("129P2_OlaHsd.mgp.v5.indels.dbSNP142.normed.vcf", "r")
c = 1
for line in fileObj.readlines():
    result = re.search("^#", line)
    if result:
        # line containing # comment
        print("{}: {}".format(c,line))
    elif(c<100):
        # split tab-delimited line in list (0=CHROM, 1=POS)
        indel_list = line.split('\t')
        print("chr{}:{}".format(indel_list[0],indel_list[1]))
    # Increase line counter
    c = c + 1
fileObj.close()

################################################################################

# V3
# Now can we find stop_gained and frameshift indels in first 100000 lines
fileObj = open("129P2_OlaHsd.mgp.v5.indels.dbSNP142.normed.vcf", "r")
c = 1
for line in fileObj.readlines():
    result = re.search("^#", line)
    if result:
        # line containing # comment
        print("{}: {}".format(c,line))
    elif(c<100000):
        # split tab-delimited line in list
        indel_list = line.split('\t')
        # Fields: 0=CHROM, 1=POS, 2=ID, 3=REF, 4=ALT, 
        #         5=QUAL, 6=FILTER, 7=INFO, 8=FORMAT, 9=STRAIN 
        result_stop = re.search("stop_gained|frameshift", indel_list[7])
        if result_stop:
            print("chr{}:{}".format(indel_list[0],indel_list[1]))
            print("\tref: ", indel_list[3])
            print("\talt: ", indel_list[4])
            print("\tinfo: ", indel_list[7])
            print("\tformat: ", indel_list[8])
            print("\tstrain: ", indel_list[9])
    # Increase line counter
    c = c + 1
fileObj.close()
'''
################################################################################

# V4
# Writing csv file
with open('results.csv', mode='w') as result_file:
    result_writer = csv.writer(result_file,delimiter=';')
    # header row for csv
    result_writer.writerow(["chromosome","position","reference","alternative","consequence"])
    # Now also save info filtered indels to csv file (parsing all lines)
    fileObj = open("129P2_OlaHsd.mgp.v5.indels.dbSNP142.normed.vcf", "r")
    c = 1
    for line in fileObj.readlines():
        result = re.search("^#", line)
        if result:
            # line containing # comment
            print("{}: {}".format(c,line))
        else:
            # split tab-delimited line in list
            # Fields: 0=CHROM, 1=POS, 2=ID, 3=REF, 4=ALT, 
            #         5=QUAL, 6=FILTER, 7=INFO, 8=FORMAT, 9=STRAIN 
            indel_list = line.split('\t')
            csq = ""
            result_match = re.search("stop_gained|frameshift", indel_list[7])
            if result_match:
                print("chr{}:{}".format(indel_list[0],indel_list[1]))
                stop_match = re.search("stop_gained", indel_list[7])
                if stop_match: csq = csq + "stop_gained "
                frameshift_match = re.search("frameshift", indel_list[7])
                if frameshift_match: csq = csq + "frameshift"
                result_writer.writerow([indel_list[0],indel_list[1],indel_list[3],indel_list[4],csq])
        # Increase line counter
        c = c + 1
    fileObj.close()
# Close csv file
result_file.close()
#!/usr/bin/python3
################################################################################
# Beautiful Soup (example-code-7-bs4-3.py)
################################################################################
import urllib.request
from bs4 import BeautifulSoup
# Get content data using urllib and create soup object
url = "http://www.cazy.org/GH100_all.html"
response = urllib.request.urlopen(url)
content = response.read()
soup = BeautifulSoup(content, 'html.parser')

# Tag contents
table_tag = soup.table
print("\nContents of table:\n{}".format(table_tag.contents))
table_content1 = table_tag.contents[0]
print("\nContent 1 in head: {}".format(table_content1))
table_content2 = table_tag.contents[1]
print("\nContent 2 in head: {}".format(table_content2))
print("Content of table tag: {}".format(table_content2.contents))

# Iterate over table tag
print("\nCHILDREN OF TABLE:"
      "\n==================")
for child in table_tag.children:
    print("\nNEW CHILD:\n{}".format(child))
# Iterate recursively
print("\nDESCENDENTS OF TABLE:" 
      "\n=====================")
for child in table_tag.descendants:
    print("NEW CHILD:\n{}".format(child))
# Text nodes incl. line breaks ('\n'") --> also iterated

################################################################################
# Look for a specific tag and attribute
table_listing = soup.find("table", {"class":"listing"})
print("\nTABLE LISTING: {}".format(table_listing))
print(soup.find("table", class_="listing"))
# Look for all td with id=separateur2 and get string value
print("\nTABLE DATA:"
      "\n===========")
td_separateur2 = soup.find_all("td", {"id":"separateur2"})
c = 1
for td in td_separateur2:
    print("[{}] {}".format(c,td))
    print("--> Name = {} | string = {}".format(td.name,td.string))
    c = c+1
################################################################################
'''
# Sleep for 3 sec
import time
print("\nSleeping...\n")
time.sleep(3.0)
################################################################################
# Now repeat and try to identify each value and save in Excel document
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "GH100"
cazy_list = ['Protein name','Organism','Genbank']
ws.append(cazy_list)
c = 1 
cazy_list = []
for td in td_separateur2:
    # Check column number using counter c
    if(c<7):
        if(c==1):
            print("\nProtein name: {}".format(td.string))
            protein_string = td.string
            protein_string = protein_string.replace('\xa0','')
            cazy_list.append(str(protein_string))
            # OR: td.string.encode('utf-8')
            c = c + 1
        elif(c==2):
            # print("EC#: {}".format(td))
            c = c + 1
        elif(c==3):
            print("Organism: {}".format(td.a.string))
            cazy_list.append(str(td.a.string))
            c = c + 1
        elif(c==4):
            print("GenBank: {}".format(td.a.string))
            cazy_list.append(str(td.a.string))
            c = c + 1
        elif(c==5):
            # print("Uniprot: {}".format(td))
            c = c + 1
        elif(c==6):
            # print("PDB: {}".format(td))
            c = c + 1
    else:
        # Save list as row in Excel document
        print(cazy_list)
        ws.append(cazy_list)
        # Reinitilize list
        cazy_list = []
        # Reset column counter
        c = 1
# Save file
wb.save("GH100_all.xlsx")
'''
################################################################################
## First try on smaller table: 
#  http://www.cazy.org/GH156_all.html
## When there are more pages for one family:
#  http://www.cazy.org/GH1_all.html?debut_PRINC=1000#pagination_PRINC
#  http://www.cazy.org/GH1_all.html?debut_PRINC=2000#pagination_PRINC
################################################################################
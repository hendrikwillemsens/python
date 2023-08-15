#!/usr/bin/python3
################################################################################
# Accessing the internet
################################################################################
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

### 7.1a #######################################################################
# Data from Human Cell Atlas
# https://data.humancellatlas.org/apis
################################################################################
print("\nSearch on human cell atlas REST web service:")
url = 'https://service.azul.data.humancellatlas.org/index/catalogs'
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    #response_data = response.read()
    response_data = response.read().decode('utf-8')
    # print(response_data)
    soup = BeautifulSoup(response_data, 'html.parser')
    print(soup.prettify())
    save_file = open('urllib_hca_api.json','w')
    save_file.write(str(response_data))
    save_file.close()
except Exception as e:
    print(str(e))
### 7.1b #######################################################################
# Data from Pfam
# http://pfam.xfam.org/
################################################################################
print("\nSearch on Pfam:")
url = 'http://pfam.xfam.org/search/keyword?query=caspase'
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    #response_data = response.read()
    response_data = response.read().decode('utf-8')
    # print(response_data)
    soup = BeautifulSoup(response_data, 'html.parser')
    print(soup.prettify())
    save_file = open('urllib_pfam.html','w')
    save_file.write(str(response_data))
    save_file.close()
except Exception as e:
    print(str(e))

### 7.1c #######################################################################
# Spots from SRX sample 
# https://www.ncbi.nlm.nih.gov/sra/SRX4179991[accn]
################################################################################
print("\nSearch on NCBI SRA:")
print("===================")
srx = input("Give the SRX number to get #spots (e.g. SRX4179991)? ")
url = 'https://www.ncbi.nlm.nih.gov/sra/'+ srx + '[accn]'
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    #response_data = response.read()
    response_data = response.read().decode('utf-8')
    # print(response_data)
    soup = BeautifulSoup(response_data, 'html.parser')
    # print(soup.prettify())
    save_file = open('urllib_srx.html','w')
    save_file.write(str(response_data))
    save_file.close()
    # Iterate over td in each tr in tbody tag
    table_tag = soup.table
    #print("\nTable body rows (tr):")
    r = 1
    for tr_tag in table_tag.children:
        #print("\nRow {}".format(r))
        c = 1
        tds= tr_tag.find_all("td")
        for td_tag in tds:
            #print("Column {}: {}".format(c, td_tag))
            if c==2:
                print("# of Spots: {}".format(td_tag.string))
            c = c + 1
        r = r + 1
except Exception as e:
    print(str(e))
################################################################################

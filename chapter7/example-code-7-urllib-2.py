#!/usr/bin/python3
################################################################################
# Accessing the internet with urllib (example-code-7-urllib-2.py)
################################################################################
import urllib.request
import urllib.parse
# Google search
print("\nSearch Google:")
# Prepare request 
values = {'q' : 'bachelor bioinformatics'}
params = urllib.parse.urlencode(values)
params = params.encode('utf-8') # data should be bytes
url = 'https://www.google.com/search'
request = urllib.request.Request(url, params)
# Get response and read data
#response = urllib.request.urlopen(request)
#response_data = response.read()
#print(response_data)
# Google returns HTTP Error 405: Method Not Allowed
# Same but with catching the error (requires commenting lines 16-18)
try:
    response = urllib.request.urlopen(request)
    response_data = response.read()
    print(response_data)
except Exception as e:
    print(str(e))
################################################################################
# Let the script take a break :-)
import time
time.sleep(2)
# Modify user-agent in headers
print("\nGoogle search with modified user-agent:")
url = 'https://www.google.com/search?q=bachelor+bioinformatics'
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    print(response_data)
    save_file = open('google-search-with-headers.txt','w')
    save_file.write(str(response_data))
    save_file.close()
except Exception as e:
    print(str(e))
################################################################################
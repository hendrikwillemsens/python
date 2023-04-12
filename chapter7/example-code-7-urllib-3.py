#!/usr/bin/python3
################################################################################
# Accessing the internet with urllib (example-code-7-urllib-3.py)
################################################################################
import urllib.request
import urllib.parse
# POSTing data to a server
print("\nPOSTing data to a server:")
print("=========================\n")
url = 'https://tryphp.w3schools.com/demo/demo_form_validation_complete.php'
params = {
    'name': 'Test 2022-2023', 
    'email': 'test@gmail.com', 
    'website': 'www.howest.be', 
    'comment': 'nothing', 
    'gender': 'other'}
query = urllib.parse.urlencode(params)   
data = query.encode("utf-8")
try:
    response = urllib.request.urlopen(url,data)
    # response_data = response.read()
    response_data = response.read().decode('utf-8')
    print(response_data)
    save_file = open('w3schools-post-data.txt','w')
    save_file.write(str(response_data))
    save_file.close()
except Exception as e:
    print(str(e))
################################################################################
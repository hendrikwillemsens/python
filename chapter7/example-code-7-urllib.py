#!/usr/bin/python3
################################################################################
# Accessing the internet with urllib (example-code-7-urllib.py)
################################################################################
import urllib.request
import urllib.parse
# Data from GitHub url
url = "https://api.github.com/users?since=100"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
data_content = response.read()
print(data_content)
# Result is a mess but we did read source code 
################################################################################
# Shorter version repeated for CaZy Database
print("\nNow CaZy:")
response = urllib.request.urlopen('http://www.cazy.org/')
print(response.read())
################################################################################
# GET values in url hardcoded
print("\nCaZy search 1: \n============== ")
url = "http://www.cazy.org/search?page=recherche&lang=en&recherche=xylanase&tag=3"
response = urllib.request.urlopen(url)
print(response.read())
################################################################################
# GET values in url using urllib.parse.urlencode
print("\nCaZy search 2: \n============== ")
params = urllib.parse.urlencode({'page': 'recherche', 'lang': 'en', 'recherche': 'xylanase', 'tag': '3'})
url = "http://www.cazy.org/search?%s" % params
response = urllib.request.urlopen(url)
print(response.read().decode('utf-8'))
################################################################################
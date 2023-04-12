#!/usr/bin/python3
################################################################################
# Beautiful Soup (example-code-7-bs4.py)
################################################################################
import urllib.request
from bs4 import BeautifulSoup
# Get content data using urllib and create soup object
url = "http://www.cazy.org/GH100_all.html"
response = urllib.request.urlopen(url)
content = response.read()
soup = BeautifulSoup(content, 'html.parser')
# Print parse tree in better format
print(soup.prettify())
################################################################################
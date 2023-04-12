#!/usr/bin/python3
################################################################################
# Beautiful Soup (example-code-7-bs4-4.py)
################################################################################
import urllib.request
from bs4 import BeautifulSoup
# Get content data using urllib and create soup object
url = "http://www.cazy.org/GH100_all.html"
response = urllib.request.urlopen(url)
content = response.read()
soup = BeautifulSoup(content, 'html.parser')
################################################################################
# Parents of an element
print("\nParents:")
soup_table = soup.find("table", class_="listing")
for parent in soup_table.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
# Sideways navigating using sibling
option_tag = soup.find("option")
print("Current entryID element [1 in list]: {}".format(option_tag))
print("Next sibling: {}".format(option_tag.next_sibling))
print("Previous sibling: {}\n".format(repr(option_tag.previous_sibling)))
# repr() function returns printable representation of object
for options in option_tag.find_next_siblings():
    print("Next option sibling: {}".format(options))
# find_next_siblings() alternative to get next sibling elements without newlines 
################################################################################
# Finding an element with the select() method
# All elements named <title>
title = soup.select('title')
print("\nTitle: {}".format(title))
# Element with id attribute 
actif = soup.select('#actif')
print("\nElement with id='actif': {}".format(actif))
# All elements with class attribute 
result_thsum = soup.select('.thsum')
print("\nResult class='thsum': {}".format(result_thsum))
# All elements names <span> within elements <tr><td>
tr_td_span = soup.select('tr td span')
print("\ntr td span:\n{}".format(tr_td_span))
# All elements named <select> directly within element <input>
# with no other element in between
input_select = soup.select('input > select')
print("\ninput select:\n{}".format(input_select))
################################################################################
#!/usr/bin/python3
################################################################################
# PPRINT MODULE (example-code-4-pprint.py)
################################################################################
import pprint
# Proper dictionary printing
person_dict = {'Name': 'Paco', 'Class': '1999', 
     'Address': {'Street':'Somestreet', 'No': 681, 'City': 'Oostende'}}
print("\nPerson dictionary:")
print(person_dict)
print("\nWith PrettyPrinter:")
pprint.pprint(person_dict)
# Default output width formatted text is 80 columns
# To adjust width use width argument to pprint()
print("\nWith PrettyPrinter width=20:")
pprint.pprint(person_dict, width=20)
# When width is too small to accommodate formatted data
# lines are not truncated or wrapped
################################################################################
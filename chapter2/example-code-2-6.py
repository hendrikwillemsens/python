#!/usr/bin/python3
################################################################################
# DICTIONARIES (example-code-2-6.py)
################################################################################
# Example 1: dict of nucleotides as key:value pairs
Dnt = {'A':'adenine', 'C':'cytosine', 'G':'guanine', 'T':'thymine'}
print("dict Dnt = {}".format(Dnt))
print("Key 'A' has value '{}'".format(Dnt['A']))
# Example 2: create keys by assignment
Daa = {}
Daa['A'] = 'Ala'
Daa['C'] = 'Cys'
Daa['D'] = 'Asp' 
print("dict Daa = {}".format(Daa))
# Example 3: make dictionary by passing to dict type name
# either keyword arguments using special name=value syntax
pers1 = dict(name='Paco', job='scientist', age=40)
# or zipping together sequences of keys and values
pers2 = dict(zip(['name','job','age'],['Flore','student',16]))
print("Pers1 = {}\nPers2 = {}".format(pers1,pers2))
################################################################################
# Nested dictionary: values more complex
pers1 = {'name': {'first': 'Paco', 'last': 'Hulpiau'},
         'jobs': ['lecturer', 'researcher'],
         'age': 40.5}
print("Pers1 = {}".format(pers1))
#print("Pers1 = {}".format(pers1['name']['first']))
pers1['name']['first'] = 'PACO'
pers1['name']['last'] = 'HULPIAU'
pers1['jobs'] = ['SCIENTIST','LECTURER']
print("Pers1 = {}".format(pers1))
################################################################################
# Keys and values
Ks = list(pers1.keys())
print("Keys of pers1: {}".format(Ks))
Vs = list(pers1.values())
print("Values of pers1: {}\n{}".format(Vs,type(Vs)))
print("Value {} has {}".format(Vs[1],type(Vs[1])))
print("Value {} has {}".format(Vs[2],type(Vs[2])))
################################################################################
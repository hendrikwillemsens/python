#!/usr/bin/python3
################################################################################
# 3.4 FOR iteration
################################################################################
# a) Iterate a dictionary of countries and capitals
countriesCapitals = { 
    'Belgium' : 'Brussels', 
	'England' : 'London',
    'France' : 'Paris', 
    'Spain' : 'Madrid'
}
print("\nList of capitals:")
print("="*17)
for capital in countriesCapitals.values():
	print(capital) 
################################################################################
# b) A pattern with a nested for loop
n = 5
for i in range(n):
	#print("i={}".format(i))
	for j in range(i):
		print ('* ', end="")
	print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
################################################################################
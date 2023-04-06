#!/usr/bin/python3
################################################################################
# MODULES (example-code-4-2.py)
################################################################################
# Import greeting from mymodule
import mymodule
#input
mymodule.greeting("Paco")
################################################################################
print("Gene 1:")
g1s = mymodule.gene1["symbol"]
g1n = mymodule.gene1["name"]
g1o = mymodule.gene1["organism"]
print("symbol={}\nname={}\norganism={}".format(g1s,g1n,g1o))
# Re-naming a module by creating alias with as keyword
import mymodule as mm
print("\nAliases of gene 1: {}".format(mm.gene1["aliases"]))
# Variant import statement
from mymodule import greeting
greeting("World")
################################################################################
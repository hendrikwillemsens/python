#!/usr/bin/python3
import re
import os
import humanfriendly


location = "/media/sf_SF/python/ex_chapter5/"
os.chdir(location)
print(os.getcwd())

fastqc_dir = location + "fastqc/"
fastqc_list = os.listdir(fastqc_dir)

for file in fastqc_list:
    pathfile = fastqc_dir + file
    if(os.path.isdir(pathfile)):
        
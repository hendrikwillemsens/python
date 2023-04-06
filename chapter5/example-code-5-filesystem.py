#!/usr/bin/python3
################################################################################
# FILESYSTEM (example-code-5-filesystem.py)
################################################################################
import os
# Some envirnoment variables
# print(os.environ) to see all
hostname = os.environ['HOSTNAME']
print("HOSTNAME: ", hostname)
print("USERNAME: ", os.environ['USERNAME'])
print("HOME DIR: ", os.environ['HOME'])
print("LANGUAGE: ", os.environ['LANG'])
print("PATH VAR: ", os.environ['PATH'])
################################################################################
# Print current working directory
print("\nCurrent working directory: ", os.getcwd())
# Change directory to location and print again
print("Changing directory to HTA folder...")
# location = "/home/pacoh/Dropbox/howest/PYTHON/HTA/"
location = "/media/sf_VMshare/Python-scripts/HTA/"
os.chdir(location)
print("\nCurrent working directory: ", os.getcwd())
################################################################################
# Create a new folder
# newdir = "/home/pacoh/Dropbox/howest/PYTHON/HTA/newdir/"
newdir = "/media/sf_VMshare/Python-scripts/HTA/newdir/"
os.mkdir(newdir)
# Using location containing trailing "/" !
newdir2 = location + "newdir2"
os.mkdir(newdir2)
# Remove first directory again
os.rmdir(newdir)
################################################################################
# Iterate the list of filenames and directories
# on the fastqc folder downloaded from Leho
fastqc_dir = location + "fastqc/"
fastqc_list = os.listdir(fastqc_dir)
print("Files and folders in {} :".format(fastqc_dir))
for file in fastqc_list:
    print(file)
################################################################################
# Package humanfriendly to get human readable file sizes
# sudo dnf install python3-humanfriendly OR pip3 install --user humanfriendly
import humanfriendly
# Split path
print("Files and folders in {} :".format(fastqc_dir))
for file in fastqc_list:
    path_file = fastqc_dir + file
    print(os.path.split(path_file))
    if(os.path.isfile(path_file)):
        print("{} is file".format(file))
        size_bytes = os.path.getsize(path_file)
        print("file size is {}".format(size_bytes))
        hsize = humanfriendly.format_size(size_bytes, binary=True)
        print("file size is {}".format(hsize))
    elif(os.path.isdir(path_file)):
        print("{} IS DIRECTORY".format(file))
################################################################################
# fnmatch module
import fnmatch
print("\nHTML files in {} :".format(fastqc_dir))
for root, dirs, files in os.walk(fastqc_dir):
    for filename in fnmatch.filter(files,'*.html'):
        print("Found {} in {}".format(filename, root))
################################################################################
# glob module
import glob
# look for each *.html file in current directory
# location = "/home/pacoh/Dropbox/howest/PYTHON/HTA/fastqc/"
location = "/media/sf_VMshare/Python-scripts/HTA/fastqc/"
os.chdir(location)
print("\nLook for .html files in {}:".format(location))
for filename in glob.iglob('*.html'):
    print(filename)
# look for each *.Rmd file in a specified directory
print("\nLook for each .Rmd file (recursively):")
iternames = glob.iglob("/media/sf_VMshare/Python-scripts/**/*.py",recursive=True)
#iternames = glob.iglob("/media/sf_VMshare/BIT04-R/**/*.Rmd",recursive=True)
for filename in iternames:
    print(filename)
################################################################################
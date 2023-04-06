#!/usr/bin/python3
################################################################################
# ARGPARSE MODULE (example-code-4-argparse.py) 
################################################################################
import argparse
parser = argparse.ArgumentParser(description='Plot data')
parser.add_argument('indir', type=str, help='Input dir with raw data')
parser.add_argument('outdir', type=str, help='Output dir for processed data')
parser.add_argument('--t', type=str, help='Number of threads to use')
args = parser.parse_args()
print("First argument input dir: {}".format(args.indir))
print("Second argument output dir: {}".format(args.outdir))
print("Argument t for threads: {}".format(args.t))
################################################################################
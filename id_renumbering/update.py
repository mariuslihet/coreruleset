#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import argparse
import os
import sys

idTranslationFile = os.path.join(sys.path[0], "IdNumbering.csv")

if(not os.path.isfile(idTranslationFile)):
	sys.stderr.write("We were unable to locate the ID translation CSV (idNumbering.csv) please place this is the same directory as this script\n")
	sys.exit(1)
parser = argparse.ArgumentParser(description="A program that takes in an exceptions file and renumbers all the ID to match OWASP CRS 3.0-rc1 numbers. Output will be directed to STDOUT and can be used to overwrite the file using '>'")
parser.add_argument("-f","--file",required=True,action="store",dest="fname",help="the file to be renumbered")
args = parser.parse_args()
if(not os.path.isfile((args.fname).encode('utf8'))):
	sys.stderr.write("We were unable to find the file you were trying to upate the ID numbers in, please check your path\n")
	sys.exit(1)
fcontent = ""
try:
    	f = open((args.fname).encode('utf-8'), "r")
    	try:
    		fcontent = f.read()
	finally:
        	f.close()
except IOError:
    sys.stderr.write("There was an error opening the file you were trying to update")

if(fcontent != ""):
	# CSV File
	f = open(idTranslationFile, 'rt')
	try:
	    	reader = csv.reader(f)
	    	for row in reader:
	        	fcontent.replace(row[0],row[1])
	finally:
		f.close()

print fcontent

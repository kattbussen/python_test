#!/usr/bin/env python

import sys
import os


#printFromFile()
#addToFile()
#printFromFile()


def addToFile():
	f = open('dictionary.txt', 'r+')
	f.write("second line\n")
	f.close()


def removeFromFile():
	f = open('dictionary.txt', 'w')
	for line in lines:
		if "second line\n" not in line:
			f.write(line)
	f.close()

def printFromFile():
	f = open('dictionary.txt', 'r')
	print(f.read())
	f.close()


printFromFile()
addToFile()
printFromFile()


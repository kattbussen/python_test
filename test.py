#!/usr/bin/env python

import sys
import os
from tempfile import NamedTemporaryFile

def addToFile(fileName="dictionary.txt", indata="second line\n"):
	f = open(fileName, 'a')
	f.write(indata)
	f.close()

def removeFromFile(fileName="dictionary.txt", removeLine="second line\n"):
	dirpath = os.path.dirname(fileName)
	with open(fileName) as file, NamedTemporaryFile("w", dir=dirpath) as outfile:
		for line in file:
			if removeLine not in line:
				outfile.write(line)
		outfile.delete = False
	os.remove(fileName)
	os.rename(outfile.name, fileName)

def printFromFile(fileName="dictionary.txt"):
	f = open(fileName, 'r')
	print(f.read())
	f.close()


printFromFile()
addToFile()
printFromFile()
removeFromFile()
printFromFile()

#print("Enter input into file:\n")
#addString = input()

#print("You entered: "+addString)


def readAndCompare(file="dictionary.txt"):
	f = open(file, 'r')
	#for line

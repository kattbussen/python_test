#!/usr/bin/env python

import sys
import os
from tempfile import NamedTemporaryFile

##############################################
#
##############################################
def addToFile(fileName="dictionary.txt", indata="second line\n"):
	f = open(fileName, 'a')
	f.write(indata)
	f.close()

##############################################
#
##############################################
def removeFromFile(fileName="dictionary.txt", removeLine="second line\n"):
	dirpath = os.path.dirname(fileName)
	with open(fileName) as file, NamedTemporaryFile("w", dir=dirpath) as outfile:
		for line in file:
			if removeLine not in line:
				outfile.write(line)
		outfile.delete = False
	os.remove(fileName)
	os.rename(outfile.name, fileName)

##############################################
#
##############################################
def printFromFile(fileName="dictionary.txt"):
	f = open(fileName, 'r')
	print(f.read())
	f.close()

##############################################
#
##############################################
def printResult():
	global correctAnswers
	global wrongAnswers
	print("\nYou got "+str(correctAnswers)+" of "+str(correctAnswers+wrongAnswers)+" answers correct.\n")

##############################################
#
##############################################
def readAndCompare(fileName="dictionary.txt"):
	
	global correctAnswers
	global wrongAnswers
	
	with open(fileName) as file:
		for line in file:
			qna = line.split(' / ')
			print("Translate "+qna[0]+":")
			answer = input()

			corr_answer = qna[1].replace("\n", "")
			
			if answer == corr_answer:
				print("correct!")
				correctAnswers+=1
			else:
				print("wrong!")
				wrongAnswers+=1

##############################################
# main
##############################################
def main():
	global correctAnswers
	global wrongAnswers
	correctAnswers = 0
	wrongAnswers = 0

	#readAndCompare()
	#printResult()

	if(len(sys.argv) == 1):
		print("passed one argument \n")
	elif(len(sys.argv) == 2):
		try:
			int(sys.argv[1])
		except ValueError:
			print("wrong type of parameter\n")
		else:
			print("skickade in ett argument; "+str(int(sys.argv[1]))+"\n")
	else:
		print("\n\n############################################################################")
		print("This script can be used two ways:\n")
		print("	'python test.py' to quiz you on all words in dictionary.txt\n")
		print("	'python test.py <int>' to quiz you on <int> words from dictionary.txt\n")
		print("During the quiz, answer 'please exit' to stop the quiz.\n")
		print("############################################################################\n\n")

if __name__ == '__main__':
	main()



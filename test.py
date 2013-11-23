#!/usr/bin/env python

import sys
import os
import random
import linecache
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
	global mode
	
	if(mode != "japToEng"):
		changeKeyboardLayout("swedish")

	print("\nYou got "+str(correctAnswers)+" of "+str(correctAnswers+wrongAnswers)+" answers correct.\n")

##############################################
#
##############################################
def readAndCompare(fileName="dictionary.txt"):
	
	global correctAnswers
	global wrongAnswers
	global numberOfWords
	global maxNumberOfWords
	global mode	

	random.seed()

	#We need the range to go from 1 - words+1 because getline(1) returns the first line
	listOfLinesToRead = random.sample(range(1, maxNumberOfWords+1), numberOfWords) 

	for line in listOfLinesToRead:	
		qnaRaw = linecache.getline(fileName, line)
		qnaSplit = qnaRaw.partition(" / ")

		if mode == "engToJap":
			qna = (qnaSplit[2].replace("\n",""), qnaSplit[1], qnaSplit[0])
		else:
			qna = (qnaSplit[0], qnaSplit[1], qnaSplit[2].replace("\n",""))

		print("Translate '"+qna[0]+"':")
		answer = input()

		#corr_answer = qna[2].replace("\n", "")
		corr_answer = qna[2]
	
		if answer == corr_answer:
			print("correct!")
			correctAnswers+=1
		elif answer == "please exit":	
				printResult()
				sys.exit() 
		else:
			print("wrong!")
			print("The correct answer is "+corr_answer+"\n")
			wrongAnswers+=1

##############################################
#
##############################################
def countWords(fileName="dictionary.txt"):
	with open(fileName) as file:
		return len(file.readlines())		

##############################################
#
##############################################
def changeKeyboardLayout(language):
	if(language == "japanese"):
		cmd = """osascript change_input_to_hiragana.scpt"""
	elif(language == "swedish"):
		cmd = """osascript change_input_to_swedish.scpt"""
	else:
		print("ERROR: use of unknown language.\n")
		sys.exit()

	os.system(cmd)


##############################################
#
##############################################
def printHelpAndExit():
	print("\n\n############################################################################")
	print("This script can be used the following ways:\n")
	print("	'python test.py' to quiz you on all words in dictionary.txt using japToEng\n")
	print("	'python test.py <int>' to quiz you on <int> words from dictionary.txt using japToEng\n")
	print(" 'python test.py <mode> to quiz you on all words from dictionary.txt using <mode>")
	print("		mode can be 'japToEng', 'engToJap' or 'mixed'\n")
	print("	'python test.py <int> <mode> to quiz you on <int> words from dictionary.txt using <mode>")
	print("		mode can be 'japToEng', 'engToJap' or 'mixed'\n")
	print("During the quiz, answer 'please exit' to stop the quiz.\n")
	print("############################################################################\n\n")
	sys.exit()

##############################################
# main
##############################################
def main():
	#initiation of variables
	global correctAnswers
	global wrongAnswers
	global numberOfWords
	global maxNumberOfWords
	global modes
	global mode
	correctAnswers = 0
	wrongAnswers = 0
	numberOfWords = countWords()
	maxNumberOfWords = numberOfWords
	modes = ["japToEng", "engToJap", "mixed"]
	mode = "japToEng"

	#evaluation of input parameters	
	if(len(sys.argv) == 2):
		try:
			int(sys.argv[1])
		except ValueError:
			if sys.argv[1] in modes:
				mode = sys.argv[1]
			else:
				printHelpAndExit()
		else:
			if int(sys.argv[1]) < numberOfWords:
				numberOfWords = int(sys.argv[1])
	elif(len(sys.argv) == 3):
		try:
			int(sys.argv[1])
		except ValueError:
			printHelpAndExit()
		else:
			if sys.argv[2] in modes:
				mode = sys.argv[2]
			else:
				printHelpAndExit()
			if int(sys.argv[1]) < numberOfWords:
				numberOfWords = int(sys.argv[1])
	else:
		printHelpAndExit()

	#Parameters evaluted correctly
	if mode == "engToJap":
		changeKeyboardLayout("japanese")

	readAndCompare()
	printResult()

if __name__ == '__main__':
	main()



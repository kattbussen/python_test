#!/usr/bin/env python

import sys
import os
import random
import linecache
from tempfile import NamedTemporaryFile

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
def switchMode(prevMode):
	if prevMode == "engToJap":
		changeKeyboardLayout("swedish")
		return "japToEng"
	else:
		changeKeyboardLayout("japanese")
		return "engToJap" 	

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

	tmpMode = mode		
	randomNumber = random.randint(1,2)
	prevRandomNumber = random.randint(1,2)

	#We need the range to go from 1 - words+1 because getline(1) returns the first line
	listOfLinesToRead = random.sample(range(1, maxNumberOfWords+1), numberOfWords) 

	#if we are running in 'mixed' we need to initiate the modes
	if mode == "mixed":
		tmpMode = "japToEng"

	for line in listOfLinesToRead:	
		fullLine = linecache.getline(fileName, line)
		splitLine = fullLine.partition(" / ")

		prevRandomNumber = randomNumber
		randomNumber = random.randint(1,2)	

		if mode == "mixed" and prevRandomNumber != randomNumber:
			tmpMode = switchMode(tmpMode)			

		if tmpMode == "engToJap":
			qna = (splitLine[2].replace("\n",""), splitLine[1], splitLine[0])
		else:
			qna = (splitLine[0], splitLine[1], splitLine[2].replace("\n",""))

		print("Translate '"+qna[0]+"':")
		answer = input().lower()

		if answer == qna[2]:
			print("correct!")
			correctAnswers+=1
		elif answer == "please exit":	
				printResult()
				sys.exit() 
		else:
			print("wrong!")
			print("The correct answer is "+qna[2]+"\n")
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



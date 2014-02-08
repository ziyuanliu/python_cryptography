#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ziyuanliu
# @Date:   2014-02-07 18:12:47
# @Last Modified by:   ziyuanliu
# @Last Modified time: 2014-02-07 21:23:50

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n' 

def loadDictionary():
	dictionaryFile = open('dictionary.txt')
	englishWords = {}
	for word in dictionaryFile.read().split('\n'):
		englishWords[word]=None
	dictionaryFile.close()
	return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
	message = message.upper()
	message = removeNonLetters(message)
	possibleWords = message.split()

	if possibleWords == []:
		return 0.0

	matches = 0
	for word in possibleWords:
		if word in ENGLISH_WORDS:
			matches += 1
	return float(matches)/len(possibleWords)

def removeNonLetters(message):
	lettersOnly = []
	for char in message:
		if char in LETTERS_AND_SPACE:
			lettersOnly.append(char)
	return ''.join(lettersOnly)

def isEnglish(message, wordPercentage = 20, letterPer = 85):
	wordsMatch = getEnglishCount(message)*100 >= wordPercentage
	numLetters = len(removeNonLetters(message))
	msgLetterPercentage = float(numLetters)/len(message)*100
	lettersMatch = msgLetterPercentage >= letterPer
	return wordsMatch and lettersMatch





#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ziyuanliu
# @Date:   2014-02-07 15:13:12
# @Last Modified by:   ziyuanliu
# @Last Modified time: 2014-02-07 21:20:45

import math, random, sys
from detectEnglish import isEnglish

def encrypt_transposition(msg,key):
	ciphertext = ['']*key
	for col in range(key):
		pointer = col

		while pointer < len(msg):
			ciphertext[col]+=msg[pointer]
			pointer += key
	return ''.join(ciphertext)

def decrypt_transposition(message, key):
	numOfColumns = int(math.ceil(len(message)*1.0 / key))
	# The number of "rows" in our grid will need: 
	numOfRows = int(key) 
	# The number of "shaded boxes" in the last "column" of the grid: 
	numOfShadedBoxes = int((numOfColumns * numOfRows) - len(message) )

	plaintext = [''] * numOfColumns 
	
	col = 0 
	row = 0 

	for symbol in message: 
		plaintext[col] += symbol 
		col += 1 # point to next column 
		# print plaintext, col, row, numOfColumns, len(message)
		if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes): 
			col = 0 
			row += 1 
	
	return ''.join(plaintext) 



def test_transposition():
	random.seed(42)

	for i in range(20):
		message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40) 
		message = list(message)

		random.shuffle(message)
		message = ''.join(message)
		print 'Test #%s: "%s..."'%(i+1,message[:50])

		for key in range(1, len(message)):
			encrypted = encrypt_transposition(message, key)
			decrypted = decrypt_transposition(encrypted, key)

			if message!=decrypted:
				print "Mismatch key %s and message %s."%(key,message)

				print "decrypted",decrypted
				sys.exit()
	print 'Transposition cipher test passed'


def transposition_brute_force(message):
	for key in range(1, len(message)):
		print 'Trying key #%s...'%(key)
		decryptedText = decrypt_transposition(message,key)

		if isEnglish(decryptedText):
			print ''
			print 'Possible Encryption hack:'
			print 'Key %s: %s' % (key,decryptedText[:100])
			print ''
			resp = raw_input('Enter D for done, or just press Enter to continue: ')
			if resp.strip().upper().startswith('D'):
				return decryptedText
	return None





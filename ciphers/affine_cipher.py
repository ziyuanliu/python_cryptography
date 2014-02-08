#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ziyuanliu
# @Date:   2014-02-07 22:10:08
# @Last Modified by:   ziyuanliu
# @Last Modified time: 2014-02-07 23:45:20

from utils import *
import sys, random

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" 

def getKeyParts(key):
	keyA = key // len(SYMBOLS)
	keyB = key % len(SYMBOLS)
	return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
	if keyA == 1 and mode == 'encrypt':
		sys.exit('The affine cipher becomes incredible weak when key A is set to 1. Choose a different key.')

	if keyB == 0 and mode == 'encrypt':
		sys.exit('The affine cipher becomes incredible weak when key A is set to 0. Choose a different key.')

	if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
		sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))

	if gcd(keyA, len(SYMBOLS)) != 1:
		sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS))) 

def encrypt_affine(key, message):
	keyA, keyB = getKeyParts(key)
	checkKeys(keyA, keyB, 'encrypt')
	ciphertext = ''
	for char in message:
		if char in SYMBOLS:
			symIndex = SYMBOLS.find(char)
			ciphertext += SYMBOLS[(symIndex*keyA+keyB)%len(SYMBOLS)]
		else:
			ciphertext += symbol
	return ciphertext

def decrypt_affine(key, message):
	keyA, keyB = getKeyParts(key)
	checkKeys(keyA, keyB, 'decrypt')
	plaintext = ''
	modInverseOfKeyA = findModInverse(keyA, len(SYMBOLS))

	for char in message:
		if char in SYMBOLS:
			symIndex = SYMBOLS.find(char)
			plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
		else:
			plaintext += char
	return plaintext

def getRandomKey():
	while True:
		keyA = random.randint(2, len(SYMBOLS))
		keyB = random.randint(2, len(SYMBOLS))
		if gcd(keyA, len(SYMBOLS)) == 1:
			return keyA * len(SYMBOLS) + keyB

def affine_brute_force(message):
	for key in range(1, len(message)):
		print 'Trying key #%s...'%(key)
		decryptedText = decrypt_affine(key, message)

		if isEnglish(decryptedText):
			print ''
			print 'Possible Encryption hack:'
			print 'Key %s: %s' % (key,decryptedText[:100])
			print ''
			resp = raw_input('Enter D for done, or just press Enter to continue: ')
			if resp.strip().upper().startswith('D'):
				return decryptedText
	return None

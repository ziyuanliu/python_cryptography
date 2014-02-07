#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ziyuanliu
# @Date:   2014-02-07 14:43:24
# @Last Modified by:   ziyuanliu
# @Last Modified time: 2014-02-07 15:15:21


LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~' 
MAX_KEY_SIZE = len(LETTERS)
def getMode():
	while True:
		mode = raw_input("encrypt or decrypt? ").lower()
		if mode in 'encrypt e decrypt d':
			return mode
		
def getMsg():
	return raw_input("enter your message: ")

def getKey():
	key = 0
	while True:
		key = int(raw_input("Enter the key number 1 - %s: "%(MAX_KEY_SIZE)))
		if key>0 and key <= MAX_KEY_SIZE:
			return key

def translate_caesar(mode, msg, key):
	if mode[0]=='d':
		key = -key
	translated = ''
	letter_len = len(LETTERS)
	for char in msg:
		num = ord(char)
		num += key

		if num>ord('~'):
			num-=letter_len
		elif num < ord(' '):
			num+=letter_len
		translated+=chr(num)
	return translated

def brute_force(encrypted):
	for key in range(len(LETTERS)):
		translated = ''
		for char in encrypted:
			if char in LETTERS:
				num = LETTERS.find(char) 
				num = num - key

				if num<0:
					num = num + len(LETTERS)

				translated = translated + LETTERS[num]

			else:
				translated = translated + char

		print 'Key #%s: %s' % (key, translated)



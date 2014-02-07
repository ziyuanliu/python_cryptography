#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ziyuanliu
# @Date:   2014-02-07 15:13:12
# @Last Modified by:   ziyuanliu
# @Last Modified time: 2014-02-07 16:27:17

import math

def encrypt_transposition(msg,key):
	ciphertext = ['']*key
	for col in range(key):
		pointer = col

		while pointer < len(msg):
			ciphertext[col]+=msg[pointer]
			pointer+=key
	return ''.join(ciphertext)

def decrypt_transposition(msg, key):
	numOfColumns = int(math.ceil(len(msg)/key))
	numOfRows = key
	unused = (numOfColumns*numOfRows)-len(msg)

	plaintext = ['']*numOfColumns

	col = 0
	row = 0

	for char in msg:
		plaintext[col]+=char
		col += 1

		if (col==numOfColumns) or (col == numOfColumns-1 and row >= numOfRows - unused):
			col = 0
			row += 1
	return ''.join(plaintext)


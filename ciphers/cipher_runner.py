#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ziyuanliu
# @Date:   2014-02-07 14:37:51
# @Last Modified by:   ziyuanliu
# @Last Modified time: 2014-02-07 23:45:53

from caesar_cipher import *
from transposition_cipher import *
from transpositionFileCipher import *
from affine_cipher import *

def get_raw_key():
	return int(raw_input("input key: "))

def run_caesar():
	mode = getMode()
	msg = getMsg()
	key = getKey()
	m = translate_caesar(mode,msg,key)
	caesar_brute_force(m)

def run_transposition():
	msg = getMsg()
	key = getKey()
	encrypted = encrypt_transposition(msg,key)
	decrypted = decrypt_transposition(encrypted,key)
	print "encrypted",encrypted
	print "decrypted",decrypted
	# test_transposition()
	transposition_brute_force(decrypted)


def run_transposition_over_file(filename):
	mode = getMode()
	key = getKey()
	transposition_file(filename,key,mode)

def run_affine():
	msg = getMsg()
	key = get_raw_key()
	mode = getMode()
	translated = ''
	if mode == 'encrypt': 
		translated = encrypt_affine(key, msg) 
	elif mode == 'decrypt': 
		translated = decrypt_affine(key, msg) 
		affine_brute_force(msg)
		return
	print('Key: %s' % (key)) 
	print('%sed text:' % (mode.title())) 
	print(translated) 


if __name__ == '__main__':
	run_affine()


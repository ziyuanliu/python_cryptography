#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ziyuanliu
# @Date:   2014-02-07 14:37:51
# @Last Modified by:   ziyuanliu
# @Last Modified time: 2014-02-07 21:16:49

from caesar_cipher import *
from transposition_cipher import *
from transpositionFileCipher import *
from detectEnglish import *
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



if __name__ == '__main__':
	# run_transposition_over_file('devilsdictionary.txt.encrypted')
	run_transposition()


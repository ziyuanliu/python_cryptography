#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ziyuanliu
# @Date:   2014-02-07 17:44:40
# @Last Modified by:   ziyuanliu
# @Last Modified time: 2014-02-07 18:04:18

import time, os, sys
from transposition_cipher import *

def transposition_file(filename, myKey, myMode):
	outputFilename = filename+'.encrypted'

	if not os.path.exists(filename):
		print "%s does not exist" % filename
		sys.exit()

	if os.path.exists(outputFilename):
		response = raw_input("output file %s already exists. (C)ontinue or (Q)uit?"%(outputFilename))
		if not response.lower().startswith('c'):
			sys.exit()

	fileObj = open(filename)
	content = fileObj.read()
	fileObj.close()

	print '%sing...'%myMode.title()

	startTime = time.time()
	translated=''

	if myMode == 'encrypt':
		translated = encrypt_transposition(content,myKey)	
	elif myMode == 'decrypt': 
		outputFilename = filename+'.decrypt'
		translated = decrypt_transposition(content,myKey)	

	totalTime = round(time.time()-startTime,2)
	print '%sion time: %s seconds' % (myMode.title(), totalTime)

	outputFileObj = open(outputFilename,'w')
	outputFileObj.write(translated)
	outputFileObj.close()

	print 'Done %sing %s (%s characters).'%(myMode, filename, len(content))
	print '%sed file is %s.'%(myMode.title(), outputFilename)




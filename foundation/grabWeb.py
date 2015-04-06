#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Filename : grabWeb.py

from urllib import urlretrieve

def firstNonBlank(lines):
	for eachLine in lines:
		if not eachLine.strip():
			continue
		else:
			return eachLine

def firstLast(webpage):
	f = open(webpage)
	lines = f.readlines()
	f.close()
	print firstNonBlank(lines),
	lines.reverse()
	print firstNonBlank(lines),

def download(url = 'http://www.jianshu.com/p/b87413a9307e',
			process = firstLast):
	try:
		retval = urlretrieve(url)[0]
	except IOError:
		retval = None
	if retval:
		process(retval)

if __name__ == '__main__':
	download()
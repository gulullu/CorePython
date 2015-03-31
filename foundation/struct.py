# !/usr/bin/env python

"this is a test module"

import sys
import os

debug = True

class FooClass(object):
	"""docstring for FooClass"""
	def __init__(self, arg):
		super(FooClass, self).__init__()
		self.arg = arg

def test():
	"test function"
	foo = FooClass()

if __name__ == '__main__':
	test()
		

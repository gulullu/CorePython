# !/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : easyMath.py

from operator import add, sub
from random import randint, choice

ops = {'+': add. '-': sub}
MAXTRIES = 2

def doprob():
	op = choice('+-')
	nums = [ randint(1,10) for i in range(2) ]
	nums.sort(reverse = True)
# !/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : anyIter.py


class AnyIter(object):
    """docstring for ClassName"""
    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def next(self, howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval

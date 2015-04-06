#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Filename : descr.py

import os
import pickle


class FileDescr(object):
    """docstring for FileDescr"""
    saved = []

    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, typ=None):
        if self.name not in FileDescr.saved:
            raise AttributeError('{} used before assignment'.format(self.name))
        try:
            f = open(self.name, 'r')
            val = pickle.load(f)
            f.close()
            return val
        except (
                pickle.UnpicklingError, IOError, EOFError, AttributeError,
                ImportError, IndexError
                ), e:
            raise AttributeError('could not read {}'.format(self.name,))

    def __set__(self, obj, val):
        try:
            try:
                f = open(self.name, 'w')
                pickle.dump(val, f)
                FileDescr.saved.append(self.name)
            except (IOError, TypeError, pickle.UnpicklingError), e:
                raise ArithmeticError('could not pickle {}'.format(self.name))
        finally:
            f.close()

    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError), e:
            pass


class MyFileVarClass(object):
    """docstring for MyFileVarClass"""
    foo = FileDescr('foo')
    bar = FileDescr('bar')


fvc = MyFileVarClass()
fvc.foo = 42
fvc.bar = 'leanna'

del fvc.foo
print fvc.foo, fvc.bar

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Filename : test.py

from operator import add, mul
from functools import partial
from randSeq import RandSeq


def dictVarArgs(arg1, arg2='defaultB', **theRest):
    'display 2 regular args and keyword variable args'
    print 'formal arg1:', arg1
    print 'formal arg2:', arg2
    for eachXtrArg in theRest.keys():
        print 'Xtra arg %s: %s' % \
            (eachXtrArg, str(theRest[eachXtrArg]))

dictVarArgs(1220, 740.0, c='grail')
dictVarArgs(arg2='tales', c=123, d='poe', arg1='mystery')
dictVarArgs('one', d=10, e='zoo', men=('freud', 'gaudi'))


def newfoo(arg1, arg2, *nkw, **kw):
    'display regular args and all variable args'
    print 'arg1 is:', arg1
    print 'arg2 is:', arg2
    for eachNKW in nkw:
        print 'additional non-keyword arg:', eachNKW

    for eachKW in kw.keys():
        print "additional keyword arg '%s': %s" % \
            (eachKW, kw[eachKW])

newfoo('wolf', 3, 'projects', freud=90, gamble=96)

print '总和是', reduce((lambda x, y: x+y), range(5))
add1 = partial(add, 1)
mul100 = partial(mul, 100)  # mul100(x) == mul(100, x)

print add1(10)
print mul100(500)


def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]
    return incr

count = counter(5)

for i in range(3):
    if i < 4:
        print count()


def simpleGen():
    yield 1
    yield '2 ---> punch!'
simpleGen.version = 0.2
simpleGen.father = 'Allen'

myGen = simpleGen()
print myGen.next()
print myGen.next()


# from random import randint


# def  randGen(aList):
#   while len(aList) > 0:
#       yield aList.pop(randint(0, len(aList)))

# for item in randGen(['rock', 'paper', 'scissors']):
#   print item

a = [1, 2, 3, 4]
c = 'abcdef'
print a[::-1]
print c[::-1]

print 'Hello %(name)s!' % {'name': 'Tom'}


class AddrBookEntry(object):  # 类定义
    """address book entry class"""
    def __init__(self, nm, ph):  # 定义构造器
        self.name = nm  # 设置 name
        self.phone = ph  # 设置 phone
        print 'Created instance for: ', self.name

    def updatePhone(self, newph):  # 定义方法
        self.phone = newph
        print 'Updated phone# for:', self.name

john = AddrBookEntry('John Doe', '08-555-1212')
jane = AddrBookEntry('Jane', '650-555-1212')

print john
print john.name
john.updatePhone('415-455-1212')
print john.phone


class EmplAddrBookEntry(AddrBookEntry):
    """Employee Address Book Entry class"""  # 员工地址本类
    def __init__(self, nm, ph, id, em):
        self.empid = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print 'Updated e-mail address for:', self.name

john = EmplAddrBookEntry('John Doe', '408-555-1212', 42, 'john@spam.doe')
print john

stype = type('What is your quest?')
print stype
print stype.__name__

# for eachItem in RandSeq(('rock', 'paper', 'scissors')):
#     print eachItem


class DevNu111(object):
    """docstring for DevNu111"""
    def __get__(self, obj, typ=None):
        pass

    def __set__(self, obj, val):
        pass


class DevNu112(object):
    """docstring for DevNu111"""
    def __get__(self, obj, typ=None):
        print 'Accessing attribute... ignoring'

    def __set__(self, obj, val):
        print 'Attempt to assign %r... ignoring' % (val)


class C1(object):
    """docstring for C1"""
    foo = DevNu111()


class C2(object):
    """docstring for C2"""
    foo = DevNu112()

c1 = C1()
c1.foo = 'bar'
print 'c1.foo contains:', c1.foo

c2 = C2()
c2.foo = 'bar'
x = c2.foo
print 'c2.foo contains:', c2.foo

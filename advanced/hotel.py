#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Filename : test.py


class HotelRoomCalc(object):
    """Hotel room rate calculator"""
    def __init__(self, rt, sales=0.085, rm=0.1):
        '''HotelRoomCalc default arguments:
        6sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        'Calculate total; default to daily rate'
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily


class TestStaticMethod(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        self.arg = arg

    @staticmethod
    def foo():
        print 'calling static method foo()'

    @classmethod
    def fool(cls):
        print 'calling class method foo()'
        print 'foo() is part of class:', cls.__name__


class P1(object):  # parent class 1 父类 1
    """docstring for P1"""
    def foo(self):
        print 'called P1-foo()'


class P2(object):  # parent class 2 父类 2
    """docstring for P2"""
    def foo(self):
        print 'called P2-foo()'

    def bar(self):
        print 'called P2-bar()'


class C1(P1, P2):  # child 1 der. from P1, P2 #子类 1,从 P1,P2 派生
    """docstring for C1"""
    pass


class C2(P1, P2):  # child 2 der. from P1, P2 #子类 2,从 P1,P2 派生
    """docstring for C2"""
    def bar(self):
        print 'called C2-bar()'


class GC(C1, C2):  # define grandchild class #定义子孙类
    """docstring for GC"""  # derived from C1 and C2 #从 C1,C2 派生
    pass

gc = GC()
gc.foo()
gc.bar()
print GC.__mro__


class Time60(object):
    """docstring for Time60"""
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def __str__(self):
        return '%(hr)s:%(min)s' % {'hr': self.hr, 'min': self.min}

    __repr__ = __str__

    def __add__(self, other):
        return self.__class__(self.hr + other.hr, self.min + other.min)

    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self

mon = Time60(10, 30)
tue = Time60(11, 15)
mon += tue
print mon
print tue
print mon + tue

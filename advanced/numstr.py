# !/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : numstr.py


class NumStr(object):
    """docstring for NumStr"""
    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self):
        return '[{} :: {}]'.format(self.__num, self.__string)
    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(
                self.__num + other.__num,
                self.__string + other.__string
                )
        else:
            raise TypeError('Illegal argument type for built-in operation')

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.__num * num, self.__string * num)
        else:
            raise TypeError('Illegal argument type for built-in operation')

    def __nonzero__(self):
        return self.__num or len(self.__string)

    def __norm_cval(self, cmpres):
        return cmp(cmpres, 0)

    def __cmp__(self, other):
        return self.__norm_cval(cmp(self.__num, other.num)) + \
            self.__norm_cval(cmp(self.__string, other.__string))

a = NumStr(10, 'long')
b = NumStr(3, 'zhang')
c = a + b
print c

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Filename : randSeq.py

from random import choice


class RandSeq(object):
    """docstring for RandSeq"""
    def __init__(self, seq):
        super(RandSeq, self).__init__()
        self.data = seq

    def __iter__(self):
        return self

    def next(self):
        return choice(self.data)

# !/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : queue.py

queue = []


def enQ():
    queue.append(raw_input('Enter new string: ').strip())


def deQ():
    if len(queue) == 0:
        print 'Cannot pop from empty queue!'
    else:
        print 'Removed [' queue.pop(0), ']'


def viewQ():
    print str(queue)


def showmenu():
    prompt = """
(E)nqueue
(D)equeue
(V)iew
(Q)uit

Enter choice: """
    done = 0

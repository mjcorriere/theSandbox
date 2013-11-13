# -*- coding: utf-8 -*-
"""
Created on Mon Nov 04 11:25:00 2013

@author: NotMark
"""

def mygen(n):
    i = 0
    while i < n:
        yield i
        i += 1
        
        
for test in mygen(5):
    print test
    
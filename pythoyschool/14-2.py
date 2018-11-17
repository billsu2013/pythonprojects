# -*- coding: utf-8 -*-
"""
Created on Thu May  3 18:25:46 2018

@author: dell
"""

def diff(a, b): 
    if a.imag==0:
        return a+b
    else:
        return abs(a)+b

c=diff(-3+2j, 4)
print (c)
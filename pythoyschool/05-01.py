# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:01:53 2018

@author: dell
"""

def addNumbers(num):
    total = 0
    i = 1
    while i <=num:
        total = total +i
        i+=1
    return total

abc= addNumbers(1000)
print (abc)
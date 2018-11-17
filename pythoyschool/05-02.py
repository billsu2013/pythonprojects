# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:53:00 2018

@author: dell
"""

def addNumbers(start, end):
    total = 0
    i=start
    while start <= i <= end:
        total = total + i
        i +=1
    return total

a= addNumbers(5,10)
print (a)
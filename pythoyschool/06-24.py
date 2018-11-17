# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:50:01 2018

@author: dell
"""

def getSumOfFirstDigit(num): 
    a=0
    b=[]
    for i in range(len(num)):
        b=int(str(num[i])[0])
        a=a+b
    return a
num=[12, 23, 34, 45, 56]
c=getSumOfFirstDigit(num)
print (c)

        
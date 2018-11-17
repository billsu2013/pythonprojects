# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:38:48 2018

@author: dell
"""


def addNumbers(start,end): 
    a=0
    for i in range (start,end+1):
        a=a+i

    return a

    
    
b=addNumbers(5,6)
print (b)

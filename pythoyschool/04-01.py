# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 12:02:21 2018

@author: dell
"""

def generateNumber(num): 
    gen=[]
    for i in range(num+1):
        
        gen.append(i)
    return gen

a=generateNumber(6)
print (a)
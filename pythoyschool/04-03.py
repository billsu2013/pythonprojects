# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 12:33:01 2018

@author: dell
"""

def generateNumber(start,end,step): 
    gen=[]
    if step<0:
       
        for i in range(start,end-1,step):
            gen.append(i)
        return gen


    if step>0:
        for i in range(start,end+1,step):
            gen.append(i)
        return gen

a=generateNumber(20, 0, -3)
print (a)
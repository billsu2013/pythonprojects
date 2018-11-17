# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:27:07 2018

@author: dell
"""

def shiftByTwo(*args) :
    sh=[]
    if len(args)==1:
        sh.append(args[1])
    if len(args)>=2:
 
        sh.append(args[-2])
        sh.append(args[-1])
        for i in range(len(args)-2):
            sh.append(args[i])
    tsh=tuple(sh)
    return tsh
    
    
    
    
    
a=shiftByTwo(1,2,3,4,5,6)
print (a)
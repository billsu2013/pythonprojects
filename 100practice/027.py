# -*- coding: utf-8 -*-
"""
Created on Thu May 10 16:53:38 2018

@author: dell
"""

def palin(n):
    next=0
    if n<=1:
        next=input('str1 =')
#        print
        print (next)
    else:
        next=input('str2   = ')
        palin(n-1)
        print (next)
        
i=5
a=palin(i)
print (a)
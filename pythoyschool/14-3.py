# -*- coding: utf-8 -*-
"""
Created on Thu May  3 18:36:04 2018

@author: dell
"""

def toString(alist): 
    s=''
    for i in range(len(alist)):
        
        s=s+chr(alist[i])
    return s

a=toString([112, 121, 115, 99, 104, 111, 111, 108, 115])
print (a)
        
        
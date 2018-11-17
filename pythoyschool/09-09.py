# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:41:22 2018

@author: dell
"""

def sortByIndex(list):
    nsl=sorted(list,key=lambda x:x[0])
    nvl=[]
    for i in range(len(list)):
        nvl.append(nsl[i][1])
    return tuple(nvl)
        
    
a=sortByIndex([(4,'Python'), (1, 'Welcome'), (3, 'Begin'), (2, 'To')])
print (a)
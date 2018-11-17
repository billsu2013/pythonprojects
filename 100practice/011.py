# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:20:35 2018

@author: dell
"""


l=[]


for i in range(30):
    l.append([i])
    if i==0:
        l[i]=1
        print ('month %d is %d'%(i,l[i]))
    elif i==1:
        l[i]=1
        print ('month %d is %d'%(i,l[i]))
    else:
        l[i]=l[i-1]+l[i-2]
        print ('month %d is %d'%(i,l[i]))
        
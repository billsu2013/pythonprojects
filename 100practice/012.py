# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:38:53 2018

@author: dell
"""
s=[]
for i in range(101,200):
    for j in range(2,i):
        if i%j==0:
            break
    else:s.append(i)
    
print(s)
            
            
        
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:23:44 2018

@author: dell
"""
d1=['a','b','c']
d2=['x','y','z']

for i in d1:
    for j in d2:
        if (i=='a' and j=='x') or (i=='c' and  (j=='x' or j=='z')):
#            print (i,j)
            continue
        else:
            print ('better is ',i,j)
            
            
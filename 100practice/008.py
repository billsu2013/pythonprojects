# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:21:23 2018

@author: dell
"""

for i in range(1,10):
    for j in range(1,i+1):
        print ('%dX%d = %-3d'%(i,j,i*j),end="") 
    print ('')
    
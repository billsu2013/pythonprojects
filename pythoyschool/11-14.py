# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:08:09 2018

@author: dell
"""

def pascal(row, col): 
    if row==0 and col==0:
        return 1
    if col==0 or row==col:
#        c=1
        return 1
    else:
        return pascal(row-1,col-1)+pascal(row-1,col)
    
a=pascal(6,3)
print (a)
    
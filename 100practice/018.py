# -*- coding: utf-8 -*-
"""
Created on Wed May  9 23:30:36 2018

@author: dell
"""

c=int(input('input a number:\n'))
b=int(input('input a digit:\n'))
total=0
for i in range(b):

    total=total+c
    c=c*10+c    
print (total)
    


# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:29:04 2018

@author: dell
"""
import sys
sys.stdout.write(chr(1))
sys.stdout.write(chr(1))
for i in range(15):
    for j in range(15):
        print (u'\u2588',end="")
        if i==j:
            print(u'\u2588')
            print(u'\u2588',end='')
            break
            
#for i in range(15):
#    for j in range(1,i):
#        print (u'\u2588')

            

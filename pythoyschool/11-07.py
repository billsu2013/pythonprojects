# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 22:21:14 2018

@author: dell
"""

def countX(s):
    if len(s) < 1:
        return 0
    else:
        count = 0
        if s[0] == 'X':
                count = 1
               
        return countX(s[1:len(s)])+count 
    
a=countX('XcvXn')
print (a)
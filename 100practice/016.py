# -*- coding: utf-8 -*-
"""
Created on Wed May  9 23:20:43 2018

@author: dell
"""

letter=0
digit=0
space=0
other=0

s=input('raw string:\n')
for i in s:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
    else:
        other+=1
        
        
print ('letter is %d,digit is %d,space is %d,other is %d'%(letter,digit,space,other))
        

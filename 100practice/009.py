# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:41:19 2018

@author: dell
"""

for i in range (8):
    for j in range (8):
        if (i+j)%2!=0:
#            sys.stdout.write(chr(219))
#            sys.stdout.write(chr(219))
            print(u'\u2588',end="")
            print(u'\u2588',end="")
        else:
            print('  ',end="")
    print ('')
            
        
        
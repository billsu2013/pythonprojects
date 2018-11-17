# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 17:10:10 2018

@author: dell
"""

def matrixDimensions(m): 

    c=len(m[0])
    r=len(m)
    for i in range(len(m)):
        if len(m[i])!=c:
            return 'This is not a valid matrix.'
            break
    
    return 'This is a '+ '%d'%c +'x' +'%d'%r+ ' matrix.'  
   
m=[ [1, 3], [-5, 6, 0] ]
a=matrixDimensions(m)
print (a)   
    
    
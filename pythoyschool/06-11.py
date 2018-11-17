# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:10:33 2018

@author: dell
"""

def MatrixProduct(a, b): 
    c=[]
    
    for i in range(len(a)):
        d=[]
        for m in range(len(b[0])):
            ma=0
        
            for j in range(len(a[0])):

                for n in range(len(b)):
                    if j==n:
                        ma=ma+a[i][j]*b[n][m]
            d.append(ma)
        c.append(d)
                    
    return c

a = [ [1, 3], [-5, 6], [2, 4]]
b= [ [1, 4], [8, 7]]

p=MatrixProduct(a,b)

print (p)                
            
            
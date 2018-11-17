# -*- coding: utf-8 -*-
"""
Created on Thu May  3 18:02:05 2018

@author: dell
"""

def createLists(num): 
    x=[]
    z=[]
    y=[]
	
    for j in range(1,num+1):
        x.append(j)
    x1=sorted(x,reverse=True)
    y.append(x)
    y.append(x1)
    for m in range((-1)*num,0):
        z.append(m)
    z1=sorted(z,reverse=True)
    y.append(z)
    y.append(z1) 
    w=tuple(y)           
            
   
    return w

a=createLists(9)
print (a)

            
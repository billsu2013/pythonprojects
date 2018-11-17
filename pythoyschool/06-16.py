# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 23:34:23 2018

@author: dell
"""

la =range(10, 2, -2)
lb= range(1, 10, 3)
print (la)
print (lb)

a=[]
lenght1=len(la)
length2=len(lb)
for i in range(lenght1):    
    a.append(la[i])
for j in range(length2):    
    a.append(lb[j])
b=sorted(a,reverse=False)



print (b)


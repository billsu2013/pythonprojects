# -*- coding: utf-8 -*-
"""
Created on Thu May 10 16:17:06 2018

@author: dell
"""
a=[]
b=[]
a.append(2.0)

b.append(1.0)

total=a[0]/b[0]
for i in range(1,20):
    a.append(a[i-1]+b[i-1])
    b.append(a[i-1])
    total=total+a[i]/b[i]
    
print (total)    
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 23:49:22 2018

@author: dell
"""

#for i in range(1,6):
#    print (i,'=',end='')
#    t=0
list=[]


for i in range(2,10000):
    s=1
    a=i
   
    
    for j in range(2,a):
        if a%j==0:
            s=s+j
            
    if s==i:
        list.append(i)  
print (list)
       

        
    
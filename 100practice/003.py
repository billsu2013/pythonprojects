# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:32:03 2018

@author: dell
"""

#num=100000
#AA=[]
#bb=[]
#for i in range(1,num):
#    for j in range (1,1000):
#        if i+100==j*j:
#            AA.append(i)
#            bb.append(j)
#            
##print (AA)
##print (bb)            
#for n in range(len(AA)):
#    for m in range(1,1000):
#        if AA[n]+268==m*m:                
#             print (AA[n])
#             print (m)
#             break
#         
            
#            
#num=10000
#AA=[]
#bb=[]
#f=0
#for i in range(1,num):
#    for j in range (1,100):
#        if i+100==j*j:
#            AA.append(i)
#            bb.append(j)
#            
##print (AA)
##print (bb)            
#for n in range(len(AA)):
#    for m in range(1,100):
#        if AA[n]+268==m*m:                
#             print (AA[n])
#             f=1             
#             break
#    if f==1:
#         break
     
import math
for i in range (100000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if (x*x==i+100) and (y*y==i+268):
        print (i)
        
                     
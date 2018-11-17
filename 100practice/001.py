# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:41:08 2018

@author: dell
"""

#001
i=0
for k in range(1,5):
     for l in range(1,5):
         for m in range(1,5):
             if (k!=l) and (l!=m) and (k!=m):
                 print(k,l,m)
                 i+=1
print(i)                

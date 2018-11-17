# -*- coding: utf-8 -*-
"""
Created on Thu May 10 12:33:34 2018

@author: dell
"""

def bump(meter,n):
    s=0
    h=meter
    for i in range(n):
      
        s=s+h+h*0.5
        h=h*0.5
        
    return round(s,2),round(h,2)

a=bump(100,10)
print (a)
        
    
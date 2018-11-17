# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:36:21 2018

@author: dell
"""
import math
for m in range(100,999):
#    for j in range(3)
    a= (m//100)
    b=(m//10%10)
    c=(m%100%10)
    if (a*100+b*10+c)==math.pow(a,3)+math.pow(b,3)+math.pow(c,3):
        print (m)
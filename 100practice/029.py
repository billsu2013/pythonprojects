# -*- coding: utf-8 -*-
"""
Created on Sat May 12 09:56:51 2018

@author: dell
"""

x=int(input('row number is   ')) 
a=x//10000
b=x%10000//1000
c=x%1000//100
d=x%100//10
e=x%10
if 0<a<10:
    print (e,d,c,b,a)
elif 0<b<10:
    print (e,d,c,b)
elif 0<c<10:
    print (e,d,c)
elif 0<d<10:
    print (e,d)
elif 0<x<10:
    print (e)    
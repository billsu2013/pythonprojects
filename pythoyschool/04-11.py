# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:51:35 2018

@author: dell
"""

def sum(nums):
#    length=len(nums)
    ch=str(nums)
    sum=0
    for x in ch:
        sum=sum+int(x)
    return sum

a=sum(1234)
print (a)
        
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 19:26:52 2018

@author: dell
"""

def pac(age,n):
    if n==1:
        return age
    else:
        return pac(age,n-1)+2

print (pac(13,5))
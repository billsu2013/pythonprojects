# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:53:04 2018

@author: dell
"""

def countPages(num):
    total = 0
    i = 1
    while i <=num:
         page_no = str(i)
         total += page_no.count('1')
         i+=1
    return total 


a=countPages(200)
print (a)
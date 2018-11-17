# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 22:24:48 2018

@author: dell
"""

def piApprox(num):
    i=1
    pi=0

    while i <=num:                # set 'while' termination condition
                                    
            pi += 4/(2*i-1)*pow( (-1) ,i+1)                  # compute the ith term of the series  
            i+=1                       # update i
    return pi

a=piApprox(500)
print (a)
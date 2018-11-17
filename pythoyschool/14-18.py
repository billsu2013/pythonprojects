# -*- coding: utf-8 -*-
"""
Created on Fri May  4 20:05:56 2018

@author: dell
"""

def exponent(num, base):
    exp = 0
    
    while divmod(num, base )[0]>0:  # loop while the quotient is non-zero
    	num=divmod(num,base)[0]
    	exp+=1 	
    	
    	


    return exp

a=exponent(8, 2)
print (a)
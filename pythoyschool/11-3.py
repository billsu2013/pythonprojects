# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:28:12 2018

@author: dell
"""

def fibonacci(number):
	if number==0:
		return 0
	if number==1:
		return 1
	else:
		return fibonacci(number-1)+fibonacci(number-2)
number=3    
a=fibonacci(number)
print (a)
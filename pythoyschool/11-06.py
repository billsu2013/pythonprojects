# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 17:27:30 2018

@author: dell
"""

def sumOfDigits(num):
	
	unit = num % 10
	if num<10:
		return unit
	else:
		return unit+ sumOfDigits(num//10)
    
    

a=sumOfDigits(1234)
print (a)
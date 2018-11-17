# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 23:00:27 2018

@author: dell
"""

def reverseLookup(dictionary, value):
	dl=[]
	for i in dictionary.keys():
		if dictionary[i]==value:
			dl.append(i)
	return dl

a=reverseLookup({'a':1, 'b':2, 'c':2}, 2)
print (a)
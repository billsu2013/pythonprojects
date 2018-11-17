# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:27:54 2018

@author: dell
"""

def removeCommonElements(t1,t2):

	ta1=sorted(t1)
	ta2=sorted(t2)
		
	for i  in t1:
		if i in t2:
			ta1.remove(i)
			ta2.remove(i)
			

	R=ta1+ta2
	return tuple(R)
a=removeCommonElements(('b','a','d','c'), ('a','b'))
print (a)
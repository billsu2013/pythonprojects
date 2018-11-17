# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:25:10 2018

@author: dell
"""

def convertDictionary(dictionary):
	s=[]
	m=max(dictionary.keys())
	for j in range(m+1):
		s.append(0)
	for i in dictionary.keys():
		s[i]=dictionary[i]
	return s



dictionary={0: 1, 3: 2, 7: 3, 12: 4}
c=convertDictionary(dictionary)
print (c)
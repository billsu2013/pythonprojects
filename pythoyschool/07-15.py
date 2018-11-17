# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 22:23:12 2018

@author: dell
"""

def getCommonLetters(word1, word2):
    a=[]
    for i in range(len(word1)):
        if word1[i] in word2:
            a.append(word1[i])
    b=list(set(a))
    if b==[]:
        return ''
    else:
        return ''.join(b)

c=getCommonLetters('microsoft','apple')
print (c)
            
            
            
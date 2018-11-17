# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 18:54:46 2018

@author: dell
"""

def countLetters(word):
    newlist=[]
    
    for i in word:
        a=[]
        a.append(i)
        a.append(word.count(i))
        b=tuple(a)
        newlist.append(b)
        R=list(set(newlist))
        S=sorted(R,key=lambda x: x[0],reverse=False)
        
    return S

word='google'
c=countLetters(word)
print (c)
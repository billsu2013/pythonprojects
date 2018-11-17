# -*- coding: utf-8 -*-
"""
Created on Thu May  3 23:02:37 2018

@author: dell
"""

def capitalize(phrase):
#    newp=[]
#    for i in range(len(phrase)):
#        ch=chr(ord(phrase[i][0])-32)
#        print (phrase[i])
#        v=list(phrase[i])
#        for j in range(len(v)):
#            if j==0:
#               v[j]=ch 
#            newstr=''.join(v[j])
#    
#        newp.append(newstr)
    str=phrase.title()
    return str 
a=capitalize('how are you?')
print (a)
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:08:57 2018

@author: dell
"""

def isTripleDouble(word):
    c=0
    first=0
    end=0
    for  i in range(len(word)):

        if word.count(word[i]*2)==1:
            c=c+1
            if c==1:
                first=word.index(word[i]*2)

            end=word.index(word[i]*2)
            if c==6 and end-first==4:             
                return True
               

    if c<6 or end-first!=4:
           return False

a=isTripleDouble('appllee')
print (a)
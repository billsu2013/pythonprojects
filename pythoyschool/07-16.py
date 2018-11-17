# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 23:03:42 2018

@author: dell
"""

def isAllLettersUsed(word, required):
    for c in required:
        if c not in word:
            return False
    else:
        return True
    
a=isAllLettersUsed('apple', 'google')

print (a)
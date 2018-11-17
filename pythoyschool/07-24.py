# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:50:49 2018

@author: dell
"""

def isAnagram(w1, w2):
    Sw1=sorted(w1.lower(),reverse=False)
    Sw2=sorted(w2.lower(),reverse=False)

    if Sw1==Sw2:
        return True
    else:
        return False
    
a=isAnagram('google', 'gogole')  
print (a)          
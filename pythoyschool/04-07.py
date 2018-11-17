# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:51:17 2018

@author: dell
"""

def skipVowels(word):
    novowels = ''
    for ch in word:
        if ch.lower() in 'aeiou':
             continue
             novowels=novowels+ch.lower()
        novowels+=ch
    return novowels

a=skipVowels('grieeel')
print (a)

#novowels = ''
#for ch in 'grieeel':
#   if ch.lower() in 'aeiou':
#       continue
#       novowels=novowels+ch.lower()
#   novowels+=ch
#   
#print (novowels)
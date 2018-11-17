# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 17:34:20 2018

@author: dell
"""

def baseComposition(dna_seq): 
    dic={}
    for i in dna_seq:
        D1={i:dna_seq.count(i)}
        dic.update(D1)
    b=list(dic.keys()) 
    c=''.join(b)
    print(c)
    return dic

        
a=baseComposition("CTATCGGCACCCTTTCAGCA")
print (a)


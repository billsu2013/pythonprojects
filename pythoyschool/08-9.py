# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 23:02:57 2018

@author: dell
"""

def invertDictionary(d):
    newd={}
    keys=list(d.keys())
    
    for i in range(len(keys)):
        newl=[]
        newl.append(keys[i])
        
        for j in range(i+1,len(keys)):
            if d[keys[i]]==d[keys[j]]:
                
                newl.append(keys[j])
            
        newd.setdefault(d[keys[i]],newl)


    return newd        


            

    
    
    
    
    
A=invertDictionary({'a':1, 'b':2, 'c':3, 'd':2})
print (A)
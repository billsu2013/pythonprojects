# -*- coding: utf-8 -*-
"""
Created on Thu May 10 16:32:58 2018

@author: dell
"""
#total=0
#
#for i in range(1,5):
#    a=1
#    for j in range(1,i+1):
#        a=a*j
#    total=total+a
#    
#print (total)

def fact(num):
        if num==0:
            return 1

        else:
            return num*fact(num-1)
        
total=0
for i in range(1,21):
    total=total+fact(i)
print (total)
    
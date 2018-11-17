# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 23:24:48 2018

@author: dell
"""

#def getNumbers(num): 
#    Ge=[]
#    for i in range(num,0,-2):
#            a=i*i
#            Ge.append(a)        
#    for j in range(0,num+2,2):
#            a=j*j
#            Ge.append(a)
#    return Ge
#
#b=getNumbers(0)
#print (b)
#        

num=9
ge=[a*a for a in range(num,0,-2)]

Rge=sorted(ge,reverse=False)
if num%2==0:
    ge.append(0)
c=ge+Rge

print(c)            





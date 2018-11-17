# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 19:59:24 2018

@author: dell
"""

def estimatePi(num):
#    import math
    pi=1
    wi=0
    k=0
       
    def factorial(m):
        if m==0:
            return 1
        else:
            n=1
            fac=1
            while n <=m:
                 fac=n * fac
                              
                 n=n+1
            return fac


    while k<=num:
        
        coni=2*pow(2,0.5)/9801*(factorial(4*k))*(1103+26390*k)/factorial(k)/pow(396,4*k)
        k=k+1
        wi=wi+coni
        pi=1/wi
    return pi


        
a=estimatePi(1)  
print (a)      
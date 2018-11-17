# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:33:17 2018

@author: dell
"""

def primeFactorization(pnum): 

    num=pnum
    def primefact(num):
        prim=[]
        if num==0:
            return prim
        j=2
        while j<=num:
            n=2
            if j==2:
                prim.append(2)
            while n<j:
                if j%n==0:
                    break                   
                else:
                    n=n+1
                    if n==j:
                        prim.append(j)
            j=j+1
        return prim

    prim=primefact(num)
    dv=[]
    i=0
    dint=pnum
    length=len(prim)
    while i <=length:  

         if dint%prim[i]!=0:
             i=i+1
         if dint%prim[i]==0:
             dv.append(prim[i])
             dint=dint/prim[i]
             i=0
         if dint==1:
             break
    return dv

a=primeFactorization(1050)
print (a)
         
             

        
                

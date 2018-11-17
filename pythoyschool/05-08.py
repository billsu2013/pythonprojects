# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:49:43 2018

@author: dell
"""

#def primeNumbers(num):
#    i=2
#    j=2
#    prime1=[]
#
#    if num==1:
#        prime1=[]
#          
#    while j <= num:
##            if j==2:
##                
##                prime1.append(j)
##                j+=1
#            for i in range(2,j):        
#                if j%i==0:
#                    break
#            else:
#                prime1.append(j)
#                j=j+1
#    return prime1
#
#a=primeNumbers(10)
#print (a)   


# -------correct
#def primeNumbers(num):
#    prime=[]
#    if num==1:
#        return prime
#    for j in range(2,10):
#        for i in range(2,j):        
#            if j%i==0:
#    #            print ("不是质数")
#                break
#        else:
#    #       print ('质数')
#           prime.append(j)
#    return prime
#  
#a=primeNumbers(1)
#print (a)    

def primeNumbers(num):
    prime=[]
    
    if num==1:
        return prime
    j=2
    
    while j <=num:
        i=2
        if j==2:
            prime.append(2)
        while i<j:        
            if j%i==0:
    #            print ("不是质数")
                break
            else:
                i=i+1
                if i==j:
                    prime.append(j)
        j=j+1
           
    return prime
  
a=primeNumbers(60)
print (a)         
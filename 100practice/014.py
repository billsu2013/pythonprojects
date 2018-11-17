# -*- coding: utf-8 -*-
"""
Created on Wed May  9 20:57:05 2018

@author: dell
"""
num=10000
#
p=[]
def pac(num):
    s=[]        
    for i in range(2,num):
        for j in range (2,i):
            if i%j==0:
                break
        else:
    
                s.append(i)
    return s

a=pac(num)

while num>a[0]:            
    for n in range(len(a)):
            if num%a[n]==0:
                num=int(num/a[n])
                
                p.append(a[n])
                break
            
            
print (p)


           


#def com(num):
#                 
#    for n in range(2,num+1):
#            if num%n==0:
#                
#                 return n
##                break
#p=[]
#while num>2:
#    b=com(num)
#    num=int(num/b)
#    p.append(b)
    
            
            
#print (p)            
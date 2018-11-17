# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:04:03 2018

@author: dell
"""
#import math
def sqApprox(num):
    i = 0
    minsq = int(pow(num,0.5))                        # set lower bound
    maxsq = int(pow(num,0.5))+1                        # set upper bound

    while i<=maxsq :                       # set 'while' termination condition
          if i*i==num:
             minsq=i
             return(minsq,minsq)
#             break

          if i*i<=num and i >=minsq:  # complete inequality condition  
             minsq = i
          if i*i>=num and i <=maxsq:  # complete inequality condition
             maxsq = i

          i+=1                         # update i so that 'while' will terminate
    return (minsq, maxsq) 

a=sqApprox(4)
print (a)
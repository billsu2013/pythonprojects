# -*- coding: utf-8 -*-
import numpy as np

n=3

a = np.array([[4,3,1],
       [6,5,2],
       [9,7,3]])

v1 = a[0][0]
v2 = a[0][1]
v3 = a[1][0]
print(v1)
print(v2)
print(v3)
b= np.arange(9).reshape(3, 3)
print(b)

if(v1 < v2 and v1 > v3):
    print("turn left")
    for i in range(3):
        for l in range(3):
            b[i][l]=a[2-i][2-l]
        
elif(v1 > v2 and v1 < v3):
    print("turn right")
    for i in range(3):
        for l in range(3): 
#            m=abs(i-2)
#            n=abs(l)
##            print("m is:"+ str(m) + "n is:"+ str(n))
            b[l][i]=a[i][l]


print(b)
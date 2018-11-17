# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 23:34:30 2018

@author: dell
"""

def transpose(matrix): 
    col=len(matrix[0])
    row=len(matrix)
    newmatrix=[]
    for i in range(col):
        newlist=[]
        for j in range (row):
            newlist.append(matrix[j][i])
            j=j+1
        newmatrix.append(newlist)
    return newmatrix


#    b=[[c[i] for c in matrix ] for i in range(col)]
# 
##    b=[ [col[row] for col in matrix ] for row in range(col)]
#    return b

matrix = [[1,2,3], [4,5,6]]
a=transpose(matrix)
print (a)
            
            
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 22:47:03 2018

@author: dell
"""
#x=input('输入数字1   :')
#y=input('输入数字2   :')
#z=input('输入数字3   :')
#w=input('输入数字4   :')

numlist =[]
while True:
    line = input()
    if numlist.index < 4:
        numlist.append(line)
    else:
        break    

if (numlist[0]=='8' or numlist[0]=='9') and (numlist[3]=='8' or numlist[3]=='9') and (numlist[1]==numlist[2]):    
    print ('ok')
else:
    print('input again')
    
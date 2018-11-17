# -*- coding: utf-8 -*-
"""
Created on Sun May  6 10:41:25 2018

@author: dell
"""


year=int(input('year:\n'))
month=int(input('month:\n'))
day=int(input('day:\n'))
dayth=0
monthd=[31,28,31,30,31,30,31,30,31,30,31,30]

for i in range(len(monthd)):
    if ((year%400==0) or (year%4==0 and year%100!=0)) and month>2:
        dayth=dayth+monthd[i]+1
    else:
        dayth=dayth+monthd[i]
dayth=dayth+day

print(dayth)
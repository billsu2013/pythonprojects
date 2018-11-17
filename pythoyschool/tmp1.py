# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:23:47 2018

@author: dell

"""
records = []
records.append({'x':1, 'y':2, 'z':3})
records.append({'z':6, 'y':5, 'x':4})
import csv
with open('records.txt', 'w', newline='') as f:
    w=csv.writer(f)

#    for i in range(len(records)):
        
         
    w.writerow(records)

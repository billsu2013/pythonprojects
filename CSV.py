# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:46:13 2018

@author: dell
"""

import csv
import sys
filename = 'j:\\pythonprojects\supplier_data.csv'
data = []
 
try:
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        data = [row for row in reader]
except csv.Error as e:
    sys.exit(-1)
 
for datarow in data:
    print( datarow)
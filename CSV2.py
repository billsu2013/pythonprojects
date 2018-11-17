# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:52:23 2018

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:46:13 2018

@author: dell
"""

import csv
filename =open( 'j:\\pythonprojects\supplier_data.csv',"r")
data = []
 
reader = csv.reader(filename, delimiter=',')
data = [row for row in reader]
 
for datarow in data:
    print( datarow)
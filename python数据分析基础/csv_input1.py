# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

#for panda
#import sys
#
#import pandas as pd
#
#
#data_frame = pd.read_csv('j:\pythonprojects\supplier_data.csv')
#
#print(data_frame)
#
#data_frame.to_csv('j:\pythonprojects\input1.csv', index=False)
#


#for python
#!/usr/bin/env python3

import csv

import sys



with open('j:\pythonprojects\supplier_data.csv', 'r', newline='') as csv_in_file:

	with open('j:\pythonprojects\input2.csv', 'w', newline='') as csv_out_file:

		filereader = csv.reader(csv_in_file, delimiter=',')
        
		filewriter = csv.writer(csv_out_file, delimiter=',')

		for row_list in filereader: 
            
            filewriter.writerow(row_list)
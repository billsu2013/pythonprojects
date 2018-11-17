# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:21:24 2018

@author: dell
"""

#!/usr/bin/env python3
import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
row_counter = 0
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header_list = ['供应商e', '发票','零件', '成本', '时间']
        filewriter.writerow(header_list)
        for row in filereader:
            if row_counter >= 3 and row_counter <= 15:
                filewriter.writerow(row)
            row_counter += 1
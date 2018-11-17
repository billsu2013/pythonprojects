# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:18:19 2018

@author: dell
"""

import xlrd
import os
import sys
path = 'J:\\pythonprojects\\'
file = path + 'out2_sales.xls'
wb = xlrd.open_workbook(filename=file)
ws = wb.sheet_by_name('Sheet1')   #指定工作表
dataset =  []
print (ws)
for  r in range(ws.nrows):
    col = []
    for c in range(ws.ncols):
        col.append(ws.cell(r,c).value)  #某行某列数值
    dataset.append(col)
 
print(dataset)
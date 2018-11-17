# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:01:55 2018

@author: dell
"""

# =============================================================================
# 1 #!/usr/bin/env python3
# 2 import sys
# 3 from xlrd import open_workbook
# 4 input_file = sys.argv[1]
# 5 workbook = open_workbook(input_file)
# 6 print('Number of worksheets:', workbook.nsheets)
# 7 for worksheet in workbook.sheets():
# 8 print("Worksheet name:", worksheet.name, "\tRows:",\
# 9 worksheet.nrows, "\tColumns:", worksheet.ncols)
# =============================================================================
import xlrd
#import sys
#from xlrd import open_workbook
input_file='J:\\pythonprojects\\out2_sales.xls'
#workbook= open_workbook(input_file)
#print('Number of worksheets:', workbook.nsheets)
#for worksheet in workbook.sheets():
#    print("Worksheet name:", worksheet.name,"\tRows:",worksheet.nrows,"\tcolums:",
#          worksheet.ncols)
    
wb = xlrd.open_workbook(filename=input_file)
ws = wb.sheet_by_name('jan_2013_output')   #指定工作表
print(wb)
dataset =  []
print (ws)
for  r in range(ws.nrows):
    col = []
    for c in range(ws.ncols):
        col.append(ws.cell(r,c).value)  #某行某列数值
    dataset.append(col)
 
print(dataset)    
    
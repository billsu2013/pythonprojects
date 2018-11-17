# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:16:12 2018

@author: dell
"""



# =============================================================================
# 
# import sys
# from datetime import date
# from xlrd import open_workbook, xldate_as_tuple
# from xlwt import Workbook
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# output_workbook = Workbook()
# output_worksheet = output_workbook.add_sheet('jan_2013_output')
# #输出文件时XLS
# with open_workbook(input_file) as workbook:
#     worksheet = workbook.sheet_by_name('january_2013')
#     for row_index in range(worksheet.nrows):
#         row_list_output = []
#         for col_index in range(worksheet.ncols):
#             if worksheet.cell_type(row_index,col_index) == 3:
#                 date_cell = xldate_as_tuple(worksheet.cell_value(row_index,col_index),workbook.datemode)
#                 print(date_cell)
#                 date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                 print(date_cell)
#                 row_list_output.append(date_cell)   
#                 output_worksheet.write(row_index,col_index,date_cell)
#             else:
#                 non_date_cell = worksheet.cell_value(row_index,col_index)
#                 row_list_output.append(non_date_cell)
#                 print(non_date_cell)
#                 output_worksheet.write(row_index,col_index,non_date_cell)
#                 output_workbook.save(output_file)
#             
# =============================================================================
            
            
            
     #!/usr/bin/env python3
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file, sheetname='january_2013')
writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()       
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
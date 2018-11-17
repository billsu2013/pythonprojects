# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# import urllib3
#  
# response = urllib3.urlopen("http://www.baidu.com")
# print ( response.read())
# =============================================================================
 #!/usr/bin/env python3

# =============================================================================
# import sys
# input_file=sys.argv[1]
# output_file = sys.argv[2]
# 
# with open(input_file, 'r', newline = '' ) as filereader:
#     with open(output_file, 'w', newline ='') as filewrite:
#         header = filereader.readline()
#         header_list = header.split(',')
#         print(header_list)
#         filewrite.write(','.join(map(str,header_list))+'\n')
#         for row in filereader:
#             row = row.strip()
#             row_list = row.split(',')
#             print(row_list)
#             filewrite.write(','.join(map(str,row_list))+'\n')
# =============================================================================
            
 
 #!/usr/bin/env python3

# =============================================================================
# import sys
# import pandas as pd
# input_file = sys.argv[1]
# print(input_file)
# output_file = sys.argv[2]
# print(output_file)
# data_frame= pd.read_csv(input_file)
# print(data_frame)
# data_frame.to_csv(output_file,index=False)
# 
# 
# =============================================================================

#!/usr/bin/env python3
# =============================================================================
# 1 #!/usr/bin/env python3
# 2 import csv
# 3 import sys
# 4 input_file = sys.argv[1]
# 5 output_file = sys.argv[2]
# 6 with open(input_file, 'r', newline='') as csv_in_file:
# 7 with open(output_file, 'w', newline='') as csv_out_file:
# 8 filereader = csv.reader(csv_in_file, delimiter=',')
# 9 filewriter = csv.writer(csv_out_file, delimiter=',')
# 10 for row_list in filereader:
# 11 print(row_list)
# 12 filewriter.writerow(row_list)
# 你可以看到，上面大部分代码与前一个脚本中的代码非
# =============================================================================

# =============================================================================
# import csv
# import sys
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# 
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         filereader = csv.reader(csv_in_file)
#         filewriter = csv.writer(csv_out_file)
#         # read first line into header
#         header = next(filereader)
#         filewriter.writerow(header)
#         
#         #processing start from line 2
#         for row_list in filereader:            
#             supplier = str(row_list[0]).strip()
#             cost = str(row_list[3]).strip('$').replace(',', '')
#             print(cost)
#             if supplier == 'Supplier Z' or float(cost) > 600.0:
#                 filewriter.writerow(row_list)
#                 
# =============================================================================
# =============================================================================
#          行中的值属于某个集合       
# =============================================================================
import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
important_dates = ['1/20/14', '1/30/14'] 
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        # read first line into header
        header = next(filereader)
        filewriter.writerow(header)
        
        #processing start from line 2
        for row_list in filereader:
            a_date = row_list[4]
            if a_date in important_dates:
                filewriter.writerow(row_list)
 
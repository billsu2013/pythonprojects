# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:46:32 2018

@author: dell
"""

# =============================================================================
# #!/usr/bin/env python3
# import pandas as pd
# import sys
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# 
# data_frame = pd.read_csv(input_file)
# data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
# data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
# .str.contains('Z')) | (data_frame['Cost'] > 600.0), :]
# data_frame_value_meets_condition.to_csv(output_file, index=False)
# =============================================================================


#!/usr/bin/env python3
# =============================================================================
# import pandas as pd
# import sys
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# data_frame = pd.read_csv(input_file)
# important_dates = ['1/20/14', '1/30/14']
# data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].\
# isin(important_dates), :]
# data_frame_value_in_set.to_csv(output_file, index=False)
# =============================================================================


# =============================================================================
# 1 #!/usr/bin/env python3
# 2 import csv
# 3 import sys
# 4 input_file = sys.argv[1]
# 5 output_file = sys.argv[2]
# 6 my_columns = [0, 3]
# 7 with open(input_file, 'r', newline='') as csv_in_file:
# 8 with open(output_file, 'w', newline='') as csv_out_file:
# 9 filereader = csv.reader(csv_in_file)
# 10 filewriter = csv.writer(csv_out_file)
# 11 for row_list in filereader:
# 12 row_list_output = [ ]
# 13 for index_value in my_columns:
# 14 row_list_output.append(row_list[index_value])
# 15 filewriter.writerow(row_list_output)
# =============================================================================


# =============================================================================
# #输入软件包
# import csv
# import sys
# #定义文件参数
# input_file = sys.argv[1]
# output_file = sys.argv[2]
# #选择列
# my_columns = [0,3]
# #打开文件
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         #定义读取文件名
#         filereader = csv.reader(csv_in_file)
#         #定义写入文件名
#         filewriter = csv.writer(csv_out_file)
#         #逐行读取文件
#         for row_list in filereader:
#             #定义list名
#             row_list_output=[]
#              #选取列
#             for index_value in my_columns:
#                  #添加到list?
#                 row_list_output.append(row_list[index_value])
#                 print(row_list_output)
#                 #写入到filewriter?
#                 filewriter.writerow(row_list_output)
# =============================================================================
                
            
        
        
#!/usr/bin/env python3
import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
#read file
data_frame = pd.read_csv(input_file)
#read selected column
data_frame_column_by_name = data_frame.loc[:, ['Supplier Name', 'Purchase Date']]
#write to file
data_frame_column_by_name.to_csv(output_file, index=False)







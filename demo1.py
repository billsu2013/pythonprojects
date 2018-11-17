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
1 #!/usr/bin/env python3
2 import sys
3
4 input_file = sys.argv[1]
5 output_file = sys.argv[2]
6
7 with open(input_file, 'r', newline='') as filereader:
8 with open(output_file, 'w', newline='') as filewriter:
9 header = filereader.readline()
10 header = header.strip()
11 header_list = header.split(',')
12 print(header_list)
13 filewriter.write(','.join(map(str,header_list))+'\n')
14 for row in filereader:
15 row = row.strip()
16 row_list = row.split(',')
17 print(row_list)
18 filewriter.write(','.join(map(str,row_list))+'\n')
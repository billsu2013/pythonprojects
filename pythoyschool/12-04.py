# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:40:53 2018

@author: dell
"""

import re
regex_1 = re.findall('c{4}', 'abbccccd')    #  match exactly 4 characters
regex_2 = re.findall('.{0,}', 'abbccccd')    #  match 0 or more characters
regex_3 =  re.findall('.{,1}', 'abbccccd')  #  match 0 or 1 character 
regex_4 =  re.findall('.{1,}', 'abbccccd')  #  match 1 or more character 

print (regex_1)
print (regex_2)
print (regex_3)
print (regex_4)
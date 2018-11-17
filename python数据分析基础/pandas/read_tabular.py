# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:19:02 2018

@author: dell
"""

import pandas as pd
#orders=pd.read_table('http://bit.ly/chiporders')
#orders.head()
##print(orders.head())
#user_cols=['user_id','age','gender','occupation','zip_code']
#orders2=pd.read_table('http://bit.ly/movieusers',sep='|',header=None,names=user_cols)
#print(orders2.head())

#read excel

#excel1=pd.read_excel('j:\pythonprojects\sales_2013.xlsx')
#print(excel1)
#


ufo=pd.read_csv('http://bit.ly/uforeports')

type(ufo)
print(ufo)
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 00:02:11 2018

@author: dell
"""

def csvReader(filename):
    records = []
    c=[]
    for line in open(filename):
        line = line.rstrip('\n')  # strip '\n'
        if line=='':
           continue           # ignore empty line
        
        
    
        line=line.split('"')
        c=list(line)
        c.remove('')
        c[1]=str(c[1]).replace(',','')
        print (c)        
        records.append(c)

        

        


    
    return records 

a=csvReader('dob.csv')
print (a)
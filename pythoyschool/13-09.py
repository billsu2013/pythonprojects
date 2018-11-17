# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:23:47 2018

@author: dell

"""
records = []
records.append({'x':1, 'y':2, 'z':3})
records.append({'z':6, 'y':5, 'x':5})

def csvWriter(filename, records):
    import csv
    with open(filename, 'w', newline='') as f:
        w=csv.writer(f)
        
        
        w.writerow(records[0].keys())
        for i in range(len(records)):
            v=[]
            l=sorted(records[i].items(),key=lambda x:x[0],reverse=False) 
    #        m=list(y for y in l(n)[1] (for n in range(len(l)))
            
            for j in range(len(l)):
                v.append(str(l[j][1]))
            w.writerow(v)
    return w
#        w.writerow(v+'\n')
csvWriter('wwwww.txt', records)  
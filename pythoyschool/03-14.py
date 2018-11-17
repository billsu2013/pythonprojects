# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:15:44 2018

@author: dell
"""

#    >>> time12hr('1619')
#    '4:19 p.m.'
#    >>> time12hr('1200')
#    '12:00 p.m.'
#    >>> time12hr('1020')
#    '10:20 a.m.'
    
def time12hr(time):
    if int(time[0:2])>12:
        a=int(time[0:2])-12
        
        return str(a) +':' +time[2:4] +' p.m.'
        
    if int(time[0:2])==12:
        return time[0:2] +':' +time[2:4] +' p.m.'
    if int(time[0:2])<12:
        return time[0:2]+':' +time[2:4] +' a.m.'
    
b=time12hr('1020')
print (b)


#time='1619'
#print (time[2:4])
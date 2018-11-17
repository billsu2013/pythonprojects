# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:25:41 2018

@author: dell
"""

def sortByLength (T,s):
    Vl=[]
    Tl=[]
    if s=='asc':
        r=False
    if s=='des':
        r=True
    for i in range(len(T)):
        Vl.append(len(T[i]))
        Tl.append(T[i])
    d=zip(Vl,Tl)
    sd=sorted(d,key=lambda x:x[0],reverse=r)
    st=[]
    for n in range(len(sd)):
        st.append(sd[n][1])
        
    wt=tuple(st)
    return wt
        
        
        
        
        
        
a= sortByLength(('iOS', 'iPhone', 'iPad'), 'asc') 
print(a)       
        
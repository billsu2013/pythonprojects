# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 23:25:57 2018

@author: dell
"""
#str1  = 'abcefghxyzThis,is,the,target,string  xyzlkdjf'
#idx1 = str1.find('xyz')
#print(idx1)                    # get the position of 'xyz'
#idx2 = str1.find('xyz', idx1+1)            # get the next 'xyz'
#print(idx2)
#str1 = str1[idx1+3:idx2].replace(',','|')    # replace ',' with '|'
#print(str1)
#str1 = str1.strip() 
#print(str1)

#002-06
#def BMI(weight, height): 
#    BMI=float(weight/(height*height))
#    return '%0.1f'%BMI
#
#a=BMI(110,2)
#print (a)

#002-07
#def percent (x,y):
#    return int((x/y)*100)
#
#a=percent(63,12)
#print (a)


#def getSumOfLastDigits(numList): 
#	 
#    a0=numList[0]
#    a1=numList[1]
#    a2=numList[2]
##    b=int(str(a0)[-1])+int(str(a1)[-1])+int(str(a2)[-1])
##    return b
#    b=a0%10+a1%10+a2%10
#    return b
#c=getSumOfLastDigits([12, 13, 14])
#
#print (c)

#numList = [12, 23, 54]
#a0=numList[0]
#a1=numList[1]
#a2=numList[2]
#print (numList[0][-1])
#str_a1=str(a1)
#print(str(a1)[-1])


#def addFirstAndLast(x):
#	if len(x)>1:  
#	   Sum = x[0] + x[-1]
#	   return Sum
#	if len(x) == 1:
#	   Sum = x[0]
#	   return Sum
#	else:
#	   return 0
#x=[2]



#def addOne(x):
#        return x**2
#        
#def useFunction(addOne,num): 
#    return addOne(num) 
#
#w=useFunction(1,4)
#print (w)



def time24hr(tstr): 
    if tstr[-2:]=='am':
       if tstr[:2]=='12':
          return str('00'+tstr[3:5]+'hr')
       else:
          return str(tstr[:1]+tstr[3:5]+'hr')
    if tstr[-2:]=='pm':
       if tstr[:2]=='12':
          return str('12'+tstr[3:5]+'hr')
       else:
          y=int(tstr[:2])+12
          return str(str(y)+tstr[3:5]+'hr')

z = time24hr('01:34pm')
print (z)
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 20:16:08 2018

@author: dell
"""

def genSet(nums): 

    nums.sort()
    lastnums=nums[-1]
    length=len(nums)
    for i in range(length-2,-1,-1):
#        currentnum=nums[i]
        if nums[i]==lastnums:
             nums.remove(nums[i])
        else:
             lastnums=nums[i]
    return nums
a=genSet([5,4,8,4,9,8])
print (a)         


#def genSet(nums): 
#
#    nums.sort()
#    firstnums=nums[0]
#    length=len(nums)
#    for i in range(-length+1,0,1):
#        currentnum=nums[i]
#        if currentnum==firstnums:
#             nums.remove(currentnum)
#        else:
#             firstnums=currentnum
#    return nums
#a=genSet([3,-2,-1,-1,3,-2,0])
#print (a)         

#def genSet(nums):
#    nums.sort()
#    list=[]
#    length=len(nums)
#    list.append(nums[0])
#    currentnum=list[0]
#    for i in range(length):
#        if nums[i]!=currentnum:
#           list.append(nums[i])
#           currentnum=nums[i]
#    return list
#a=genSet([3,-2,-1,-1,3,-2,0])
#print (a) 
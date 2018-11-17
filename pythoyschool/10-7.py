# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 22:41:12 2018

@author: dell
"""


class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
   def __sub__(self,other):
      return Vector(self.a - other.a, self.b -other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)

print (v1-v2)
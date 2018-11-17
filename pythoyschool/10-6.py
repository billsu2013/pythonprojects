# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 22:23:45 2018

@author: dell
"""

class Point:
       x = 0
       y = 0
       def __init__(self, x, y):
            Point.x = x
            Point.y = y
            self.x = x
            self.y = y

p1 = Point(1,2)
p2 = Point(3,4)
p2.x = 2


print (Point.x)
#print (p1.x)
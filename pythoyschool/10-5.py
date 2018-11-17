# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 11:40:50 2018

@author: dell
"""

class Point:

      def __init__(self, x,y  ):
          
                self.x=x
                self.y=y

      def __str__(self):
              print    ('(%d,%d)'%(self.x,self.y))
              return  "A class implementation of a %d -dimensional point."%self.x 

#      def str(self):
##          self.__str__()
#          return '(%d,%d)'%(self.x,self.y)
#              
              
p1=Point(2,4)
#print (p1.__str__())
#print (str(p1))
#print (str(p1))
print (p1)


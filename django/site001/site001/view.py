# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:46:35 2018

@author: dell
"""

from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! you are faourite. Today is happy day ")


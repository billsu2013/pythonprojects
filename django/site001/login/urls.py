# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:55:26 2018

@author: dell
"""

from django.conf.urls import url
from login import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/',views.index),
    url(r'^login/',views.login),

    url(r'^register/',views.register),
    url(r'^logout/',views.logout),
    ]
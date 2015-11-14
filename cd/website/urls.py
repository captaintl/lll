# -*- coding: utf-8 -*-
"""
Created on Fri Dec 06 16:54:36 2013

@author: Zengliangwei
"""
from django.conf.urls import patterns, url
from addr_book.views import *

urlpatterns = patterns('',
    (r'^site_media/(?P<path>.*)','django.views.static.serve',{'document_root':'./addr_book/'}), 
    url(r'^$',main_page),
    url(r'^addpeople/',add_people),
    url(r'^check/',check),
    url(r'^delete',delete),
    url(r'^update',update)
)
#lalala

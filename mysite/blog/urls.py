# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^posts/(?P<slug>[a-zA-Z0-9_]+)/$', 'view_post', name='post'),
     url(r'^posts/(?P<year>\d+)/(?P<month>\d+)/$', 'view_month', name='month'),
     url(r'^category/(?P<slug>[a-zA-Z0-9_]+)/$', 'view_category', name='category'),
     url(r'^citations/$', 'view_citations', name='citation'),
)
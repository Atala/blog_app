# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    # Examples:
     url(r'^posts/(?P<slug>[a-zA-Z0-9_-]+)/$', 'view_post', name='post'),
     url(r'^posts/(?P<year>\d+)/(?P<month>\d+)/$', 'view_month', name='month'),
     url(r'^category/(?P<slug>[a-zA-Z0-9_]+)/$', 'view_category', name='category'),
     url(r'^citations/$', 'view_citations', name='citation'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

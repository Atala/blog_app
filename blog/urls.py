# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from views import PostDetail, PostList, MonthView
from models import Entry, Category, Citation 


urlpatterns = patterns('blog.views',
    # Examples:
   url(r'^$', PostList.as_view(model=Entry) , name='home'),
   url(r'^posts/(?P<slug>[a-zA-Z0-9_-]+)/$', PostDetail.as_view(model=Entry), name='post'),
   url(r'^posts/(?P<year>\d+)/(?P<month>\d+)/$', MonthView.as_view(model=Entry), name='month'),
   url(r'^category/(?P<slug>[a-zA-Z0-9_]+)/$', PostList.as_view(model=Category), name='category'),
   url(r'^citations/$', PostList.as_view(model=Citation), name='citation'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
)

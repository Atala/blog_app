# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = urlpatterns = patterns('blog.views',
    url(r'^$', 'home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('blog.views',
    url(r'^', include('blog.urls', namespace="blog")),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)



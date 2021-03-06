# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView
from views import PostDetail, PostList, MonthView, CitationList, ContactView
from models import Entry, Category, Citation 


urlpatterns = patterns('blog.views',
    # Examples:
    url(r'^$', PostList.as_view() , name='home'),
    url(r'^posts/(?P<slug>[a-zA-Z0-9_-]+)/$', PostDetail.as_view(model=Entry), name='post'),
    url(r'^posts/(?P<year>\d+)/(?P<month>\d+)/$', MonthView.as_view(model=Entry), name='month'),
    url(r'^category/(?P<slug>[a-zA-Z0-9_]+)/$', PostList.as_view(), name='category'),
    url(r'^citations/$', CitationList.as_view(), name='citation'),
    url(r'^contact/$', ContactView.as_view(), name = 'contact'),
    url(r'^email_successful$', TemplateView.as_view(template_name='contact_success.html'), name = 'contact_success'),    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG :    
    urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve',
	    {'document_root': settings.MEDIA_ROOT}),)

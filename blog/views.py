# Create your views here.
# -*- coding: utf-8 -*-

from models import Entry, Category, Citation 
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import list_detail, date_based 
import calendar


def home(request):
   return list_detail.object_list(request, queryset = Entry.objects.all(), 
				  template_name = 'home.html', 
				  template_object_name = 'posts', 
				  extra_context =   {'dates' : get_base_content}) 

def view_post(request, slug_given):
   return list_detail.object_detail(request, queryset = Entry.objects.filter(slug = slug_given),
				    slug = slug_given, slug_field = 'slug', 
				    template_name = 'view_post.html', 
				    template_object_name = 'post')

def view_category(request, category):
    return list_detail.object_detail(request, queryset = Entry.objects.filter(category__title = category), 
				     slug = category, 
				     template_name = 'view_category.html',
				     template_object_name = 'posts')

def view_month(request, year, month):
    return date_based.archive_month(queryset=Entry.objects.filter(posted__year=year,posted__month=month),
				    year=year,
				    month=month,
				    template_object_name = 'post',
				    date_field=u'Publié le') 

def view_citations(request):
   return list_detail.object_list(request, queryset = Citation.objects.all(), 
				  template_name = 'view_citation.html', 
				  template_object_name = 'posts', 
				  extra_context =   {'dates' : get_base_content}) 


def get_base_content():
    monthDict={1:'Janvier', 2:'Février', 3:'Mars', 4:'Avril', 5:'Mai', 6:'Juin', 7:'Juillet', 8:'Août', 9:'Septembre', 10:'Octobre', 11:'Novembre', \
    12:'Décembre'}

    dates = []
    for entry in Entry.objects.all():
        sthg = (entry.posted.year, monthDict[entry.posted.month], entry.posted.month)
        if sthg not in dates:
            dates.append(sthg)

    return dates           


# Create your views here.
# -*- coding: utf-8 -*-

from models import Entry, Category, Citation 
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView, MonthArchiveView
import calendar


class PostList(ListView):
    context_object_name = 'posts_list'
    
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['dates'] = get_base_content()
        return context
         

class PostDetail(DetailView):
    context_object_name = 'post'  
    
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['dates'] = get_base_content()
        return context
   
class MonthView(MonthArchiveView):
    date_field, context_object_name, month_format  = 'posted' , 'posts', '%m' 

    def get_context_data(self, **kwargs):
        context = super(MonthView, self).get_context_data(**kwargs)
        context['dates'] = get_base_content()
        return context
 
def get_base_content():
    monthDict={1:'Janvier', 2:'Février', 3:'Mars', 4:'Avril', 5:'Mai', 6:'Juin', 7:'Juillet', 8:'Août', 9:'Septembre', 10:'Octobre', 11:'Novembre', \
    12:'Décembre'}

    dates = []
    for entry in Entry.objects.all():
        sthg = (entry.posted.year, monthDict[entry.posted.month], entry.posted.month)
        if sthg not in dates:
            dates.append(sthg)

    return dates           


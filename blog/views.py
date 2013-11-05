# Create your views here.
# -*- coding: utf-8 -*-

from models import Entry, Category, Citation 
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView, MonthArchiveView
import calendar
 

class PostList(ListView):
    model, context_object_name, slug_kwarg, template_name  = Entry, 'posts_list', 'slug', 'entry_list.html'
    
    def get_queryset(self, **kwargs):
	slug = self.kwargs.get('slug', None)
	if slug:
	    queryset = Entry.objects.filter(category__slug=slug)
	else:
	    queryset = Entry.objects.all()    
	return queryset 


class PostDetail(DetailView):
    context_object_name, template_name = 'post'  , 'entry_detail.html'
    

  
class MonthView(MonthArchiveView):
    date_field, context_object_name, month_format, template_name  = 'posted' , 'posts', '%m', 'entry_archive_month.html' 


class CitationList(ListView):
    model = Citation
    context_object_name = 'quotes'
    template_name = 'citation_list.html'

    


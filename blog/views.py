# Create your views here.
# -*- coding: utf-8 -*-

from models import Entry, Category, Citation 
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView, MonthArchiveView
import calendar
 

class PostList(ListView):
    model, context_object_name, slug_kwarg = Entry, 'posts_list', 'slug'
    
    def get_queryset(self, **kwargs):
	slug = self.kwargs.get('slug', None)
	if slug:
	    queryset = Entry.objects.filter(category__slug=slug)
	else:
	    queryset = Entry.objects.all()    
	return queryset 


class PostDetail(DetailView):
    context_object_name = 'post'  
    

  
class MonthView(MonthArchiveView):
    date_field, context_object_name, month_format  = 'posted' , 'posts', '%m' 

 


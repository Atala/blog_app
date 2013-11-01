# Create your views here.
# -*- coding: utf-8 -*-

from models import Entry, Category, Citation 
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import list_detail 
import calendar


def home(request):
   return list_detail.object_list(request, queryset = Entry.objects.all(), template_name = 'home.html', template_object_name = "posts")

def view_post(request, slug):
   return render_to_response('view_post.html',{'post': get_object_or_404(Entry, slug=slug)})

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    return render_to_response('view_category.html', {'category': category, 'posts': Entry.objects.filter(category=category)[:5]})

def view_month(request, year, month):
    monthDict={1:'Janvier', 2:'Février', 3:'Mars', 4:'Avril', 5:'Mai', 6:'Juin', 7:'Juillet', 8:'Août', 9:'Septembre', 10:'Octobre', 11:'Novembre', \
    12:'Décembre'}
    
    entry = Entry.objects.filter(posted__year=year,posted__month=month)
    month_display = monthDict[int(month)]

    return render_to_response('view_month.html', {'posts': entry, 'month' : month_display, 'year' : year, })

def view_citations(request):  
    result = get_base_content()
    quotes = Citation.objects.all()[:5]

    return render_to_response('view_citation.html', {'quotes': quotes, 'posts': result['entries'][:5], 'dates' : result['dates'], })

def get_base_content():
    monthDict={1:'Janvier', 2:'Février', 3:'Mars', 4:'Avril', 5:'Mai', 6:'Juin', 7:'Juillet', 8:'Août', 9:'Septembre', 10:'Octobre', 11:'Novembre', \
    12:'Décembre'}
    monthDictSansAcc={1:'janvier', 2:'fevrier', 3:'mars', 4:'avril', 5:'mai', 6:'juin', 7:'juillet', 8:'aout', 9:'septembre', 10:'octobre',  \
    11:'novembre', 12:'decembre'}
    dates = []
        
    entries = Entry.objects.all()
   

    for entry in Entry.objects.all():
         sthg = (entry.posted.year, monthDict[entry.posted.month],entry.posted.month)
         if not sthg in dates:
             dates.append(sthg)

    return {'dates':dates, 'entries':entries[:5]}           



# -*- coding: utf-8 -*-
from models import Entry

def get_base_content(request):
    monthDict={1:u'Janvier', 2:u'Février', 3:u'Mars', 4:u'Avril', 5:u'Mai', 6:u'Juin', 7:u'Juillet', 8:u'Août', 9:u'Septembre', 10:u'Octobre', \
	11:u'Novembre', 12:u'Décembre'}
    dates_feed = []
    for entry in Entry.objects.all():
        sthg = (entry.posted.year, monthDict[entry.posted.month], entry.posted.month)
        if sthg not in dates_feed:
            dates_feed.append(sthg)

    return {'dates_feed' : dates_feed }           


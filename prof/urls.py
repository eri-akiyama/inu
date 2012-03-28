# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *


# http://localhost:8000/prof/

#
urlpatterns = patterns( 'inu2.prof.views',
    # トップ
    # URL /prof/ は view の index で 名前は prof_index
    url(r'$', 'index', name="prof_index"),
)

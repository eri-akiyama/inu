# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *


# http://localhost:8000/top/

#
urlpatterns = patterns('inu2.top.views',
    # トップ
    url(r'$', 'index', name="top_index"),
)

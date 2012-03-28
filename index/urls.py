# -*- coding: utf-8 -*-

# polls/urls.py
from django.conf.urls.defaults import *


# http://localhost:8000/index/
urlpatterns = patterns( 'inu2.index.views',
    # トップ
    (r'$', 'index'),
)

## -*- coding: utf-8 -*-

#--------- import ---------
from django.conf.urls.defaults import *

#--------- URL ---------
urlpatterns = patterns('',
    # 汎用ビュー
    ('login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'} ),
    #
    ('logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logout.html'} ),

    #
    # account : http://127.0.0.1:8000/account/
    ( 'newac/$', ('inu2.accounts.views.newac') ),
    ( '$', ('inu2.top.views.index') ),

)

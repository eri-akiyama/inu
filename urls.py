# -*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inu.views.home', name='home'),
    # url(r'^inu/', include('inu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^top/', include('inu2.accounts.urls')),
    url(r'^accounts/', include('inu2.accounts.urls')),
#    url(r'^top/', include('inu2.accounts.urls')),
    # top : http://127.0.0.1:8000/top/
    ( r'^top/', include('top.urls') ),
)

# -*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # 管理画面
    url(r'^admin/', include(admin.site.urls)),
    # 認証画面
    url(r'^top/', include('inu2.accounts.urls')),
    url(r'^accounts/', include('inu2.accounts.urls')),
    # トップページ : http://127.0.0.1:8000/top/
    url(r'^top/', include('top.urls')),
    # プロフ管理ページ : http://127.0.0.1:8000/prof/
    url(r'^prof/', include('prof.urls')),
    # インデックスページ : http://127.0.0.1:8000/index/
    url(r'^index/', include('index.urls')),
)

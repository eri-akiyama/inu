# -*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('inu2.views.root',
    # プログ公開ページ
    url(r'^(?P<prof_id>\d+)/$', 'prof_index', nama='prof_index'),
)

urlpatterns += patterns('inu2.views.prof',
    # プロフ管理ページ
    url(r'prof/admin/$', 'prof_admin', name="prof_admin"),
)

# Django が 既にviewを用意してくれてるぞ！======================================

urlpatterns += patterns('django.contrib.auth.views',
    # ログイン
    ('accounts/login/$', 'login', {'template_name': 'accounts/login.html'} ),
    # ログアウト
    ('accounts/logout/$', 'logout', {'template_name': 'accounts/logout.html'} ),
)

urlpatterns += patterns('',
    # Django Admin 
    url(r'^admin/', include(admin.site.urls)),
)

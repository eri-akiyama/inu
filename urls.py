# -*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

# プロフ公開ページ
urlpatterns = patterns('inu2.views.root',
    # プログ公開ページ
    # url(r'^(?P<prof_id>\d+)/$', 'prof_index', nama='prof_index'),
)

# プロフ管理ページ
urlpatterns += patterns('inu2.views.prof',
    # プロフ管理ページ
    url(r'prof/admin/$', 'prof_admin', name="prof_admin"),
    # プロフ編集ページ
    url(r'prof/index/$', 'prof_edit', name="prof_edit"),
    # プロフ編集確認ページ
    url(r'prof/prof_results/(?P<user_id>\d+)/$', 'prof_results', name="prof_results"),
)

# 新規ユーザ登録
urlpatterns += patterns('inu2.views.accounts',
    # 新規ユーザ登録ページ
    url(r'accounts/new/$', 'new_account_form', name="new_account_form"),

    # 新規ユーザ確認ページ
    url(r'accounts/new_account/$', 'new_account', name="new_account"),
)
# Django が 既にviewを用意してくれてるぞ！======================================

urlpatterns += patterns('django.contrib.auth.views',
    # ログイン
    ('$', 'login', {'template_name': 'accounts/login.html'} ),
    ('accounts/login/$', 'login', {'template_name': 'accounts/login.html'} ),
    # ログアウト
    ('accounts/logout/$', 'logout', {'template_name': 'accounts/logout.html'} ),
)

urlpatterns += patterns('',
    # Django Admin 
    url(r'^admin/', include(admin.site.urls)),
)

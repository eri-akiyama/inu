# -*- encoding: utf-8 -*-

#=====================================================
# @file  : views.py
# @breaf : プロフ管理ページ view定義
#=====================================================

#--------- import ---------
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from inu2.prof.models import Prof_data

#------------------------------------------------
# @breaf : プロフ管理ページ呼び出し
#------------------------------------------------
def index(request):
    # ログインしていないのに直接 http://localhost:8000/prof/をたたいた時
    if not request.user.is_authenticated():
        return render_to_response('accounts/index_error.html')

    # ログインしている状態の時
    latest_prof_list = Prof_data.objects.all()
    return render_to_response('prof/index.html', {"latest_prof_list":latest_prof_list},context_instance = RequestContext(request))

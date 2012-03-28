# -*- encoding: utf-8 -*-

#=====================================================
# @file  : views.py
# @breaf : プロフ管理ページ view定義
#=====================================================

#--------- import ---------
from django.shortcuts import render_to_response


#------------------------------------------------
# @breaf : プロフ管理ページ呼び出し
#------------------------------------------------
def index(request):
    return render_to_response('prof/index.html', {"request":request})

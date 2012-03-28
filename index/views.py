# -*- encoding: utf-8 -*-

#=====================================================
# @file  : views.py
# @breaf : 一番最初のインデックスページ view定義
#=====================================================

#--------- import ---------
from django.shortcuts import render_to_response


#------------------------------------------------
# @breaf : インデックスページ呼び出し
#------------------------------------------------
def index(request):
    return render_to_response('index/index.html', {"request":request})
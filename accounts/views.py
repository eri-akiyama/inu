
# -*- encoding: utf-8 -*-

#=====================================================
# @file  : views.py
# @breaf : 認証ページ view定義
#=====================================================

#--------- import ---------
from django.shortcuts import render_to_response


#------------------------------------------------
# @breaf : 認証ページ呼び出し
#------------------------------------------------
def index(request):
    if request.user.is_authenticated():
    # Do something for authenticated users.
    return render_to_response('top/index.html', {"request":request})

    else:
    # Do something for anonymous users.
    return render_to_response('top/index.html', {"request":request})

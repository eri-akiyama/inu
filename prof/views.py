# -*- encoding: utf-8 -*-

#=====================================================
# @file  : views.py
# @breaf : プロフ管理ページ view定義
#=====================================================

#--------- import ---------
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.db.models.base import Model
from inu2.prof.models import Prof_data2
from django import forms

#------------------------------------------------
# @breaf : プロフ管理ページ呼び出し
#------------------------------------------------



# ログイン後のページ（プロフィール管理画面）
def index(request):
    # ログインしていないのに直接 http://localhost:8000/prof/をたたいた時
    if not request.user.is_authenticated():
        return render_to_response('accounts/index_error.html')

    ## ログインしている状態の時

    # ログインしているID取得
    user_id = request.user.id
    # ログインしている名前取得
    user_name = request.user.username

#    use_data = Prof_data2.objects.filter(name=user_id)

    data_all = Prof_data2.objects.get(auth_id=user_id)

    print "ログインしたID：",user_id
    print "ログインした名前：",user_name
#    print "ログインした名前でフィルターかけたデータ：",use_data
    print "ログインしたデータ：",data_all.hobby

    return render_to_response('prof/index.html',{"data_all":data_all},context_instance = RequestContext(request))


#　登録処理
def register(request):
    if request.POST:
        form = InputForm(request.POST)
        if form.is_valid():
            #　ここで受け取った値を処理する。
            return HttpResponseRedirect('/inputinfo/updated/')
    else:
        form = InputForm()
    return render_to_response('input_form.html', dict(form=form))


#　更新処理(登録完了ビュー)
def updated(request):
    message = "Your id and e-mail address are registered."
    return HttpResponse(message)

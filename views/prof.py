# -*- coding:utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required
from inu2.prof.models import Prof_data2
from django.db import IntegrityError


#　ログインしているかチェック
@login_required()

#　ログインしていたらする処理
def prof_admin(request):
    # ログインしているID取得
    user_id = request.user.id
    # ログインしているidでデータを取得
    data = Prof_data2.objects.get(auth_id=user_id)
    # ※チェック用※
    # 後で消す
    print data.name
    print user_id

    # 取得したデータを表示するように、コンテキストで格納する

    ctxt = RequestContext(request, {
#        'hoge': u"ほげ",
        'l_id':data.id,
        'l_name':data.name,
        'l_birthday':data.birthday,
        'l_blood_type':data.blood_type,
        'l_hobby':data.hobby,
        'l_favorite_food':data.favorite_food,
    })
    print request
    return render_to_response('prof/index.html', ctxt)

#　新規登録された情報表示
def prof_results(context_instance):


    return render_to_response('prof/prof_results.html', context_instance)


#　プロフ編集情報をフォームから登録
def prof_edit(request):

    # ユーザー情報
    l_id = request.POST.get('l_id')
    l_name = request.POST.get('l_name')
    l_birthday = request.POST.get('l_birthday')
    l_blood_type = request.POST.get('l_blood_type')
    l_hobby = request.POST.get('l_hobby')
    l_favorite_food = request.POST.get('l_favorite_food')
    print l_name


    prof_data = Prof_data2(l_id, l_name, l_birthday, l_hobby, l_blood_type, l_favorite_food)
    #　セーブする
#    prof_data.save()

    context_instance = RequestContext(request, {
        'l_id':l_id,
        'l_name':l_name,
        'l_birthday':l_birthday,
        'l_hobby':l_hobby,
        'l_blood_type':l_blood_type,
        'l_favorite_food':l_favorite_food
    } )
    print request

    return prof_results(context_instance)




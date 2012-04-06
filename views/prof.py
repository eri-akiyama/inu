# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required
from inu2.prof.models import Prof_data2

# TODO 使ってないからとりあえずコメントアウト
# from django.db import IntegrityError

"""
ログインしないと閲覧出来ないページには
@login_required()デコレータを利用しよう！！
"""

@login_required()
def prof_admin(request):
    # 認証されたユーザーのIDを取得する。
    user_id = request.user.id

    # ユーザーIDからprof_dataを取得する。
    #
    # SQL文はこんな感じ。
    # SELECT * FROM prof_prof_data2 WHERE auth_id = user_id;
    data = Prof_data2.get_prof_data(user_id)

    # prof_dataがなかったら表示する。
    if data is None:
         return HttpResponse(u"DoseNotExist at ProfData user_id:%s" % user_id)

    # 取得したデータを表示するように、コンテキストで格納する
    # ctxt = RequestContext(request, { "key1": value1, "key2": value2, })
    ctxt = RequestContext(request, {
        "user_id": user_id,
        "data": data,
    })
    return render_to_response('prof/index.html', ctxt)


#　新規登録された情報表示
# TODO このページはログインしていなくても閲覧できるページかな？
def prof_results(context_instance):
    return render_to_response('prof/prof_results.html', context_instance)


#　プロフ編集情報をフォームから登録
def prof_edit(request):

    # リクエストメソッドがPOSTじゃないときは処理させない
    if not request.method == "POST":
        return HttpResponse(u"POSTしないとだめよ!!")

    # ポストされてきたユーザー情報
    l_id = request.POST.get('l_id')
    l_name = request.POST.get('l_name')
    l_birthday = request.POST.get('l_birthday')
    l_blood_type = request.POST.get('l_blood_type')
    l_hobby = request.POST.get('l_hobby')
    l_favorite_food = request.POST.get('l_favorite_food')

    # TODO 修正すべきprof_dataを取得する。

    # TODO prof_dataに受け取ったユーザー情報を入れていく。

    # TODO 修正が終わったらprof_dataセーブする
    # prof_data.save()

    context_instance = RequestContext(request, {
        'l_id':l_id,
        'l_name':l_name,
        'l_birthday':l_birthday,
        'l_hobby':l_hobby,
        'l_blood_type':l_blood_type,
        'l_favorite_food':l_favorite_food
    })

    # TODO Redirectという処理でこの処理に戻らないようにする
    return prof_results(context_instance)

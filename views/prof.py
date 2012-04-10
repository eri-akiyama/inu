# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required
from inu2.prof.models import Prof_data2
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import time
import datetime



# TODO 使ってないからとりあえずコメントアウト
# from django.db import IntegrityError

"""
ログインしないと閲覧出来ないページには
@login_required()デコレータを利用しよう！！
"""

@login_required()
def prof_admin(request):
    # 認証されたユーザーのIDを取得する。
    # user_idはauth_userテーブルのid
    # prof_prof_dataテーブルのauth_id
    user_id = request.user.id

    # ユーザーIDからprof_dataを取得する。
    #
    # SQL文はこんな感じ。
    # SELECT * FROM prof_prof_data2 WHERE auth_id = user_id;
    data = Prof_data2.get_prof_data(user_id)

    # prof_dataがなかったらからのフォームを表示する。
    if data is None:
        user_name = request.user.username
        ctxt = RequestContext(request, {
            "user_id": user_id,
            "user_name":user_name,
            "data": data,
            })
        return render_to_response('prof/index.html', ctxt)

#         return HttpResponse(u"DoseNotExist at ProfData user_id:%s" % user_id)

    # 取得したデータを表示するように、コンテキストで格納する
    # ctxt = RequestContext(request, { "key1": value1, "key2": value2, })
    ctxt = RequestContext(request, {
        "user_id": user_id,
        "data": data,
#        "birthday":data.birthday,
    })
    return render_to_response('prof/index.html', ctxt)


#　プロフ編集情報をフォームから登録
@login_required()
def prof_edit(request):
    print "prof_edit haittayo"
    # リクエストメソッドがPOSTじゃないときは処理させない
    if not request.method == "POST":
        return HttpResponse(u"POSTしないとだめよ!!")

    # ポストされてきたユーザー情報
    l_id = request.POST.get('l_id')
    user_id = request.POST.get('user_id')
    l_name = request.POST.get('l_name')
    l_birthday = request.POST.get('l_birthday')
    l_blood_type = request.POST.get('l_blood_type')
    l_hobby = request.POST.get('l_hobby')
    l_favorite_food = request.POST.get('l_favorite_food')

    print "l_birthday dayo"
    print l_birthday
    print type(l_birthday)
    _date = time.strptime(l_birthday, '%Y%m%d')
    day = datetime.date(_date[0], _date[1], _date[2]) #=> 2009年3月18日
    print day
    # TODO 修正すべきprof_dataを取得する。
    # 新規の時はdbに追加して、すでにあるデータは編集できるようにする。
    prof_data, created = Prof_data2.get_or_create_prof_date(user_id)
    print created
    #prof_data = Prof_data2.get_prof_data(user_id)


    # TODO prof_dataに受け取ったユーザー情報を入れていく。
    # datetime処理をする！
    prof_data.birthday = day  #'1999-1-1'
    print "(prof_data.birthday)"
    print type(prof_data.birthday)
    print prof_data.birthday
    prof_data.blood_type = l_blood_type
    prof_data.hobby = l_hobby
    prof_data.favorite_food = l_favorite_food

    # TODO 修正が終わったらprof_dataセーブする
    prof_data.save()
    # TODO Redirectという処理でこの処理に戻らないようにする
    return HttpResponseRedirect(reverse('prof_results', args=[user_id],))


#　プロフ編集された情報表示
# TODO このページはログインしていなくても閲覧できるページかな？
#@login_required()
def prof_results(context_instance,user_id):

    print "kokoha results"
    print user_id
    # 表示するprof_dataを取得する。
    prof_data = Prof_data2.get_prof_data(user_id)
    context_instance = RequestContext(context_instance, {
        'prof_data':prof_data,
    })

    return render_to_response('prof/prof_results.html', context_instance = context_instance)

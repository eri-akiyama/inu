# -*- coding:utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required()
def prof_admin(request):
    ctxt = RequestContext(request, {
        'hoge': u"ほげ",
    })
    return render_to_response('prof/index.html', ctxt)


def new_account(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    user.save()

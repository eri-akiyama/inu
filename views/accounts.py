# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def new_account_form(request):

    return render_to_response('accounts/new_account_form.html')

#
def results(context_instance):


    return render_to_response('accounts/new_account.html', context_instance)


#
def new_account(request):

    # ユーザー情報
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    user.save()

    context_instance = RequestContext(request, {'username':username, 'email':email, 'password':password } )

    return results(context_instance)

#    return render_to_response('accounts/new_account.html', context_instance)
#    return HttpResponseRedirect(reverse('results'))

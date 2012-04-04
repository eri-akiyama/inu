# -*- encoding: utf-8 -*-

#=====================================================
# @file  : views.py
# @breaf : 認証ページ view定義
#=====================================================

#--------- import ---------
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from forms import UserRegistrationForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from inu2.prof.models import Prof_data2



#------------------------------------------------
# @breaf : 新規登録ページ
#------------------------------------------------
def newac(request):
    if request.user.is_authenticated():
        pass

#    if request.method == 'POST':
##        data = request.POST.copy()
##        form = UserRegistrationForm( data )
##        if form.is_valid() :
##            username = data[ 'username' ]
##            email = data[ 'email' ]
##            password = data[ 'password' ]
##            user = User.objects.create_user( username, email, password )
##            user.save()
#            return HttpResponseRedirect( 'prof/index.html' )
#        else :
#            return render_to_response( 'prof/index.html',
#                    { 'form': form } )
    else :
        #
        form = UserRegistrationForm()
        return render_to_response( 'accounts/account.html',{ 'form': form } )
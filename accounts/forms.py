
# -*- encoding: utf-8 -*-
#from django import newforms as forms
from django import forms

class UserRegistrationForm( forms.Form ):
    """ユーザー登録用フォーム
    
    """

    username = forms.CharField(
        required = True,
        max_length = 30,
        label = 'UserName' )

    password = forms.CharField(
        required = True,
        max_length = 128,
        widget = forms.PasswordInput )

    email = forms.EmailField(
        required = True,
        label = 'email address' )

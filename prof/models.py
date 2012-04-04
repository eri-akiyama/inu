# -*- coding: utf-8 -*-

from django.db import models
from django import forms


#class Prof_data(models.Model):
#    name = models.CharField(max_length=50)
#    birthday = models.DateField('%Y/%m/%d')
#    blood_type = models.CharField(max_length=20)
#    hobby = models.CharField(max_length=200)
#    favorite_food = models.CharField(max_length=200,unique=True)

class Prof_data2(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField('%Y/%m/%d')
    blood_type = models.CharField(max_length=20)
    hobby = models.CharField(max_length=200)
    favorite_food = models.CharField(max_length=200,unique=True)
    auth_id = models.IntegerField(max_length=20,unique=True)

class InputForm(forms.Form):
    auth_id = forms.IntegerField(max_length=20, label="User's id")
    name = forms.CharField(max_length=50, label="User's name")
    birthday = forms.DateField('%Y/%m/%d', label="User's birthday")
    blood_type = forms.CharField(max_length=20, label="User's blood_type")
    hobby = forms.CharField(max_length=200, label="User's hobby")
    favorite_food = forms.CharField(max_length=200, label="User's favorite_food")

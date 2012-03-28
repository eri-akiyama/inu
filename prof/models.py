# -*- coding: utf-8 -*-

from django.db import models
#import datetime

class Prof_data(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField('%Y/%m/%d')
    blood_type = models.CharField(max_length=20)
    hobby = models.CharField(max_length=200)
    favorite_food = models.CharField(max_length=200,unique=True)

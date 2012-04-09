# -*- coding: utf-8 -*-

from django.db import models

class Prof_data2(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField('%Y/%m/%d')
    blood_type = models.CharField(max_length=20)
    hobby = models.CharField(max_length=200)
    favorite_food = models.CharField(max_length=200)
    auth_id = models.IntegerField(max_length=20,unique=True)

    @classmethod
    def get_prof_data(cls, user_id):
        if not user_id:
            return None

        try:
            prof_data = cls.objects.get(auth_id=user_id)
        except:
            return None

        return prof_data
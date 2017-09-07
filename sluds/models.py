# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import  post_save
from datetime import datetime
from django.utils import timezone
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Users(models.Model):
    UserID = models.IntegerField('用户编号',primary_key=True)
    NickName = models.CharField('用户昵称',max_length=128, default='')
    LevelID = models.IntegerField('用户级别',blank=True, default=1)
    AccountPic_URL = models.CharField('用户头像URL',max_length=255,blank=False, default='')
    SelfIntroduction = models.CharField('自我介绍',max_length=255,blank=False, default='')
    Gender = models.IntegerField('性别')
    LocationProvince = models.CharField('省份',max_length=50, blank=False, default='')
    LocationCity = models.CharField('城市',max_length=100, blank=False, default='')
    #CTime = models.DateTimeField('创建时间', default=datetime.now())
    #MTime = models.DateTimeField('更新时间', default=datetime.now())
    CTime = models.DateTimeField('创建时间', default=timezone.now)
    MTime = models.DateTimeField('更新时间', default=timezone.now)

    class Meta:
        db_table = 'Users'

    def __repr__(self):
        return u'<Users: %d, %s>' % (self.UserID, self.NickName)

class User_OpenAuth(models.Model):
    ID = models.IntegerField(primary_key=True)
    UserID = models.IntegerField(db_index=True)
    NickName = models.CharField(max_length=255, default='')
    OAuthType = models.IntegerField()
    OAuthID = models.CharField(max_length=255, default='')
    OAuth_Access_Token = models.CharField(max_length=255, default='')
    OAuth_Refresh_Access_Token = models.CharField(max_length=255, default='')
    OAuth_Expires = models.CharField(max_length=255, default='')
    Scope = models.CharField(max_length=255, default='')
    AccountPic_URL = models.CharField(max_length=255, default='')
    Gender = models.IntegerField(blank=True)
    Country = models.CharField(max_length=255, default='', blank=True)
    Province = models.CharField(max_length=255, default='', blank=True)
    City = models.CharField(max_length=255, default='', blank=True)
    # CTime = models.DateTimeField(default=datetime.now(), blank=False)
    # MTime = models.DateTimeField(default=datetime.now(), blank=False)
    CTime = models.DateTimeField('创建时间', default=timezone.now)
    MTime = models.DateTimeField('更新时间', default=timezone.now)

    class Meta:
        db_table = 'User_OpenAuth'

    def __repr__(self):
        return u'<User_OpenAuth: %d, %s>' % (self.UserID,self.NickName)

class User_LocalAuth(models.Model):
    ID = models.IntegerField(primary_key=True, blank=False)
    UserID = models.IntegerField(db_index=True)
    LAuthType = models.IntegerField(blank=False)
    UserName = models.CharField(max_length=255, unique=True, db_index=True, blank=False)
    Password = models.CharField(max_length=255, blank=False)
    # CTime = models.DateTimeField(default=datetime.now(), blank=False)
    # MTime = models.DateTimeField(default=datetime.now(), blank=False)
    IsActive = models.IntegerField(default=0)
    CTime = models.DateTimeField('创建时间', default=timezone.now)
    MTime = models.DateTimeField('更新时间', default=timezone.now)

    class Meta:
        db_table = 'User_LocalAuth'

    def __repr__(self):
        return u'<User_LocalAuth: %d, %s>' % (self.UserID, self.UserName)

# 为每个用户添加token值
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

'''
#sender指定实体
@receiver(post_save, sender=Users)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
'''
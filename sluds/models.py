# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class ReqBodyPrefix(models.Model):
    version = models.CharField(max_length=6)
    action = models.CharField(max_length=50)
    class Meta:
        abstract = True

class ResBodyPrefix(models.Model):
    version = models.CharField(max_length=6)
    request_id = models.CharField(max_length=50)
    code = models.CharField(max_length=4)
    class Meta:
        abstract = True

class Users(models.Model):
    UserID = models.IntegerField(primary_key=True)
    NickName = models.CharField(max_length=128, default='')
    LevelID = models.IntegerField()
    AccountPic_URL = models.CharField(max_length=255, default='')
    SelfIntroduction = models.CharField(max_length=255, default='')
    Gender = models.IntegerField()
    LocationProvince = models.CharField(max_length=50, default='')
    LocationCity = models.CharField(max_length=100, default='')
    CTime = models.DateTimeField(auto_now_add=True)
    MTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Users'

    def __repr__(self):
        return u'<Users: %d, %s>' % (self.UserID, self.NickName)

class User_OpenAuth(models.Model):
    ID = models.IntegerField(primary_key=True)
    UserID = models.IntegerField(db_index=True, blank=False)
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
    CTime = models.DateTimeField(auto_now_add=True, blank=False)
    MTime = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        db_table = 'User_OpenAuth'

    def __repr__(self):
        return u'<User_OpenAuth: %d, %s >' % (self.UserID,self.NickName)

class User_LocalAuth(models.Model):
    ID = models.IntegerField(primary_key=True, blank=False)
    UserID = models.IntegerField(db_index=True, blank=False)
    LAuthType = models.CharField(max_length=100, default='', blank=False)
    UserName = models.CharField(max_length=255, unique=True, db_index=True, blank=False)
    Password = models.CharField(max_length=255, blank=False)
    CTime = models.DateTimeField(auto_now_add=True, blank=False)
    MTime = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        db_table = 'User_LocalAuth'

    def __repr__(self):
        return u'<User_LocalAuth: %d, %s>' % (self.UserID, self.UserName)
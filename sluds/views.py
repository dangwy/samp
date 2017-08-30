# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Users, User_OpenAuth, User_LocalAuth
from rest_framework import viewsets
from serializers import UsersSerializer, User_OpenAuthSerializer, User_LocalAuthSerializer
from django.core import serializers
import json,simplejson
from rcode import returncodeDict
from django.db import connection
from datetime import datetime
from django.core.mail import send_mail,BadHeaderError
from django.utils import timezone

import logging
#logger = logging.getLogger(__name__)
logger = logging.getLogger('django')

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class User_OpenAuthViewSet(viewsets.ModelViewSet):
    queryset = User_OpenAuth.objects.all()
    serializer_class = User_OpenAuthSerializer

class User_LocalAuthViewSet(viewsets.ModelViewSet):
    queryset = User_LocalAuth.objects.all()
    serializer_class = User_LocalAuthSerializer

def resprefix(returncode):
    res = {}
    res['code'] = returncodeDict[returncode]['code']
    res['msg'] = returncodeDict[returncode]['msg']
    return  res

@api_view(['GET'])
def users_detail(request):
    logger.debug(request)
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        logger.debug(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    logger.error(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_user_info(request):
    """
    (13)用户信息查询接口
    """
    logger.info(request.body)
    try:
        if request.method == 'POST':
            req = JSONParser().parse(request)
            version = req['version']
            action = req['action']
            userid = req['params']['UserID']
        elif request.method == 'GET':
            version = request.GET.get('version')
            action = request.GET.get('action')
            userid = request.GET.get('UserID')
        if version != "1.0" or action != "get_user_info":
            logger.error(returncodeDict['RC990501'])
            return Response(returncodeDict['RC990501'])
    except:
        logger.error(returncodeDict['RC990501'])
        return Response(returncodeDict['RC990501'])
    else:
        try:
            users = Users.objects.get(pk = userid)
            serializer = UsersSerializer(users)
            resdata = serializer.data
            res = resprefix('RC8200')
            res['result'] = resdata
            logger.info(res)
            return Response(res)
        except:
            logger.error(returncodeDict['RC990506'])
            return Response(returncodeDict['RC990506'])

@api_view(['POST'])
def update_user_info(request):
    """
    (14)用户基本信息更新接口

    """
    logger.info(request.body)

    if request.method == 'POST':
        req = JSONParser().parse(request)
        version = req['version']
        action = req['action']
        UserID = req['params']['UserID']
        data = req['params']
        if version != "1.0" or action != "update_user_info":
            logger.error(returncodeDict['RC990501'])
            return Response(returncodeDict['RC990501'])
        # check usesr exist
        try:
            userid = Users.objects.get(pk = UserID)
        except Users.DoesNotExist:
            logger.error(returncodeDict['RC990506'])
            return Response(returncodeDict['RC990506'])

        # begin update Users table
        serializer = UsersSerializer(userid, data=data)
        if serializer.is_valid():
            serializer.save()
            #resdata = serializer.data
            res = resprefix('RC8200')
            #res['result'] = resdata
            logger.info(res)
            return Response(res)
        else:
            logger.error(returncodeDict['RC990506'])
            return Response(returncodeDict['RC990506'])

        # begin update User

@api_view(['POST'])
def update_user_accountpic(request):
    """
    (15)用户添加或更新头像
    """
@transaction.atomic
@api_view(['POST'])
def localregist_user_email(request):
    """
    (20)邮箱注册接口
    """
    logger.info(request.body)

    if request.method == 'POST':
        req = JSONParser().parse(request)
        version = req['version']
        action = req['action']
        data = req['params']
        username = req['params']['UserName']
        password = req['params']['Password']
        if version != "1.0" or action != "localregist_user_email":
            logger.error(returncodeDict['RC990501'])
            return Response(returncodeDict['RC990501'])

        with connection.cursor() as c:
            # check username in Users_LocalAuth exist, if not exist then insert
            c.execute("SELECT UserName FROM User_LocalAuth WHERE UserName = %s AND LAuthType = 3", [username])
            UserName = c.fetchone()
            if UserName is None:
                c.execute("INSERT INTO User_LocalAuth(LAuthType,UserName,Password,CTime,MTime) VALUES(3,%s,%s,%s,%s)",
                          [username,password,timezone.now(),timezone.now()])
            else:
                logger.info(returncodeDict['RC9012000'])
                return Response(returncodeDict['RC9012000'])
            # check username in NickName in Users,if not exist then insert,and get UserID
            c.execute("SELECT UserID FROM Users WHERE NickName = %s", [username])
            userid = c.fetchone()
            if userid is None:
                c.execute("INSERT INTO Users(NickName,CTime,MTime) VALUES(%s,%s,%s)",[username,timezone.now(),timezone.now()] )
            # update User_LocalAuth table.UserID
            c.execute("SELECT UserID from Users WHERE NickName = %s",[username])
            userid = c.fetchone()
            c.execute("UPDATE User_LocalAuth SET UserID = %s WHERE UserName = %s AND LAuthType = 3", [userid,username])

        # begin send email
        msgCode = u'您的注册授权码为: ' + str(userid[0]) + '584'
        try:
            send_mail('注册授权码邮件',msgCode, 'dangwenyun@163.com',[username],fail_silently=False)
        except BadHeaderError:
            logger.error(returncodeDict['RC9012001'])
            return Response(returncodeDict['RC9012001'])
        #return HttpResponseRedirect('/contact/thanks')
        logger.info(returncodeDict['RC8200'])
        return Response(returncodeDict['RC8200'])

@api_view(['POST'])
@transaction.atomic
def checkin_email(request):
    """
    (21)邮箱注册验证接口
    """
    logger.info(request.body)

    if request.method == 'POST':
        req = JSONParser().parse(request)
        version = req['version']
        action = req['action']
        data = req['params']
        username = req['params']['UserName']
        password = req['params']['Password']
        authcode = req['params']['authcode']
        if version != "1.0" or action != "checkin_email":
            logger.error(returncodeDict['RC990501'])
            return Response(returncodeDict['RC990501'])

        with connection.cursor() as c:
            c.execute("SELECT UserID FROM User_LocalAuth WHERE UserName = %s AND LAuthType = 3", [username])
            userid = c.fetchone()
            if userid is None:
                logger.error(returncodeDict['RC990506'])
                return Response(returncodeDict['RC990506'])

            authCode = str(userid[0]) + '584'
            if authcode == authCode:
                c.execute('UPDATE User_LocalAuth SET IsActive = 1 WHERE UserID = %s AND LAuthType = 3', [userid])
            else:
                logger.info(returncodeDict['RC9012002'])
                return Response(returncodeDict['RC9012002'])

        # gen token


        logger.info(returncodeDict['RC8200'])
        return Response(returncodeDict['RC8200'])

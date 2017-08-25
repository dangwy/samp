# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
    (30)用户信息查询接口
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
    (31)用户基本信息更新接口
    """
    logger.info(request.body)

    if request.method == 'POST':
        req = JSONParser().parse(request)
        version = req['version']
        action = req['action']
        userid = req['params']['UserID']
        if version != "1.0" or action != "update_user_info":
            logger.error(returncodeDict['RC990501'])
            return Response(returncodeDict['RC990501'])
        #try:
        users = Users.objects.get(pk = userid)
        serializer = UsersSerializer(Users, data=req['params'])

        if serializer.is_valid():
            print serializer.errors
            print serializer.error_messages
            print serializer.validated_data
            serializer.save()
        res = resprefix('RC8200')
        logger.info(res)
        return Response(res)
        # except Users.DoesNotExist:
        #     logger.error(returncodeDict['RC990506'])
        #     return Response(returncodeDict['RC990506'])



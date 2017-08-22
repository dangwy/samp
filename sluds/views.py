# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import  JSONParser
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Users, User_OpenAuth, User_LocalAuth, ReqBodyPrefix,ResBodyPrefix
from rest_framework import viewsets
from serializers import UsersSerializer, User_OpenAuthSerializer
from django.core import serializers

import logging
logger = logging.getLogger(__name__)
#logger = logging.getLogger('django')

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class User_OpenAuthSet(viewsets.ModelViewSet):
    queryset = User_OpenAuth.objects.all()
    serializer_class = User_OpenAuthSerializer

# @api_view(['GET'])
# def users_detail(request):
#     logger.debug(request)
#     if request.method == 'GET':
#         users = Users.objects.all()
#         serializer = UsersSerializer(users, many=True)
#         logger.debug(serializer.data)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = UsersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             logger.debug(serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     logger.error(serializer.errors)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_user_info(request):
    """
    用户信息查询接口
    :param request:
    :param pk:
    :return:
    """
    logger.info(request.body)
    #data = JSONParser().parse(request)
    #data = serializers.serialize("xml", SomeModel.objects.all())
    #serializer = UsersSerializer(data = data)
    # if request.POST.has_key('UserID'):
    #     userid = request.POST['UserID']
    # try:
    #     users = Users.objects.get(pk=userid)
    #     serializer = UsersSerializer(users)
    #     return Response(serializer.data)
    # except Users.DoesNotExist:
    #     logger.error(status=status.HTTP_404_NOT_FOUND)
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
    #     serializer = UsersSerializer(users)
    #     logger.debug(serializer.data)
    #     return Response(serializer.data)
    #
    # elif request.method == 'PUT':
    #     serializer = UsersSerializer(users, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         logger.debug(serializer.data)
    #         return Response(serializer.data)
    #     logger.error(serializer.errors)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'DELETE':
    #     users.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
#
# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse,self).__init__(content, **kwargs)
#
# @csrf_exempt
# def users_list(request):
#     if request.method == 'GET':
#         users = Users.objects.all()
#         serializer = UsersSerializer(users)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UsersSerializer(data = data)
#         if serializer.is_valid():
#             return JSONResponse(serializer.data, status= 201)
#         else:
#             return JSONResponse(serializer.errors, status= 400)
#
# @csrf_exempt
# def users_detail(request, pk):
#     try:
#         users = Users.objects.get(pk = pk)
#     except Users.DoesNotExist:
#         return HttpResponse(status= 404)
#     #question = get_object_or_404(Question, pk=question_id)
#     if request.method == 'GET':
#         serializer = UsersSerializer(users)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UsersSerializer(users, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         else:
#             return JSONResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         users.delete()
#         return HttpResponse(status=204)



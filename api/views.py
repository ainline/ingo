from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework.viewsets import ModelViewSet


class LoginView(APIView):
    """ 登录接口 """
    def post(self, request, *args, **kwargs):
        username = request._request.POST.get('username')
        password = request._request.POST.get('password')
        print(username, password)
        return JsonResponse('xxoo')
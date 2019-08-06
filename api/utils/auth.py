from api import models
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions


class Authtication(BaseAuthentication):
    """ 自定义token认证 """
    def authenticate(self, request):
        token = request._request.GET.get('token')
        if not token:
            raise exceptions.AuthenticationFailed('未获取到用户token，非法访问。')

        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败，请重新登录认证。')
        return (token_obj.user, token_obj) # (request.user,request.auth)
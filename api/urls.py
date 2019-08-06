from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from api import views
urlpatterns = [
    url(r'v1/login/$', views.LoginView.as_view()),
]
